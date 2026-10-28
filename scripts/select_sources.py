"""Choose question sources and the held-out set, then fix the indexed corpus.

    python -I scripts/select_sources.py

Runs once, before upload, with a fixed seed. Writes:
- data/heldout.json   threads excluded from the index (unanswerable sources and every thread
                      linked to them as duplicate or related)
- data/sources.json   candidate threads for straightforward/semantic questions, candidate
                      thread pairs for multi-document questions, and unanswerable candidates
- data/chunks.jsonl   the indexed corpus: chunks_all minus held-out threads, capped at
                      TARGET points by dropping whole non-source threads at random

Candidates are oversampled (about 2.5x the ~50 needed per type) because verification
drops items.
"""
import collections
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
TARGET, SEED = 1_000_000, 2028
N_SINGLE, N_PAIRS, N_HELDOUT = 160, 110, 110   # 80 straightforward + 80 semantic, ~80 each of the rest

rng = random.Random(SEED)
threads = collections.OrderedDict()          # (site, thread) -> info
for line in open(D / "chunks_all.jsonl", encoding="utf-8"):
    c = json.loads(line)
    k = (c["site"], c["thread"])
    t = threads.setdefault(k, {"chunks": 0, "accepted_chunks": 0, "accepted_len": 0, "answers": set()})
    t["chunks"] += 1
    t["answers"].add(c["post"])
    if c["accepted"]:
        t["accepted_chunks"] += 1
        t["accepted_len"] += len(c["text"])
total = sum(t["chunks"] for t in threads.values())
print(f"threads {len(threads)}, chunks {total}")

links = collections.defaultdict(set)         # (site, thread) -> linked threads, both directions
related = []
for site_dir in (D / "parsed").iterdir():
    s = site_dir.name
    for a, b, kind in json.load(open(site_dir / "links.json")):
        links[(s, a)].add((s, b))
        links[(s, b)].add((s, a))
        if kind == 1:
            related.append(((s, a), (s, b)))
meta = {}
for site_dir in (D / "parsed").iterdir():
    for tid, t in json.load(open(site_dir / "threads.json", encoding="utf-8")).items():
        meta[(site_dir.name, int(tid))] = t


def good(k, lo=200, hi=2500, min_score=3):
    t = threads.get(k)
    return bool(t) and t["accepted_chunks"] > 0 and lo <= t["accepted_len"] <= hi and meta.get(k, {}).get("score", 0) >= min_score


by_site = collections.defaultdict(list)
for k in threads:
    if good(k):
        by_site[k[0]].append(k)
for s in by_site:
    rng.shuffle(by_site[s])


def draw(n, taken):
    """Round-robin across sites so every site contributes."""
    out, sites = [], sorted(by_site)
    while len(out) < n:
        progressed = False
        for s in sites:
            while by_site[s] and by_site[s][-1] in taken:
                by_site[s].pop()
            if by_site[s] and len(out) < n:
                k = by_site[s].pop()
                out.append(k)
                taken.add(k)
                progressed = True
        if not progressed:
            break
    return out


taken = set()
unanswerable = draw(N_HELDOUT, taken)
heldout = set(unanswerable)
for k in unanswerable:
    heldout |= links.get(k, set())
taken |= heldout
single = [k for k in draw(N_SINGLE + len(heldout), taken) if k not in heldout][:N_SINGLE]

rng.shuffle(related)
pairs, used = [], set(taken)
for a, b in related:
    if len(pairs) >= N_PAIRS:
        break
    if a in used or b in used or a == b or not (good(a, min_score=2) and good(b, min_score=2)):
        continue
    if links.get(a, set()) & heldout or links.get(b, set()) & heldout:
        continue
    pairs.append((a, b))
    used |= {a, b}

protected = set(single) | {k for p in pairs for k in p}
keep = [k for k in threads if k not in heldout]
size = sum(threads[k]["chunks"] for k in keep)
if size > TARGET:
    droppable = [k for k in keep if k not in protected]
    rng.shuffle(droppable)
    drop = set()
    for k in droppable:
        if size <= TARGET:
            break
        drop.add(k)
        size -= threads[k]["chunks"]
    keep = [k for k in keep if k not in drop]
keep_set = set(keep)

n = 0
with open(D / "chunks.jsonl", "w", encoding="utf-8") as f:
    for line in open(D / "chunks_all.jsonl", encoding="utf-8"):
        c = json.loads(line)
        if (c["site"], c["thread"]) in keep_set:
            c["id"] = n
            f.write(json.dumps(c) + "\n")
            n += 1
json.dump(sorted([list(k) for k in heldout]), open(D / "heldout.json", "w"))
json.dump({"single": [list(k) for k in single], "pairs": [[list(a), list(b)] for a, b in pairs],
           "unanswerable": [list(k) for k in unanswerable], "seed": SEED, "target": TARGET},
          open(D / "sources.json", "w"), indent=0)
print(f"held out {len(heldout)} threads ({len(unanswerable)} unanswerable sources); "
      f"single sources {len(single)}; pairs {len(pairs)}; indexed chunks {n}; "
      f"per-site single: {collections.Counter(k[0] for k in single)}")
