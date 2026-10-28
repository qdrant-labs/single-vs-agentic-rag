"""Third round (unanswerable only, seed 47, 60 items, excludes round 2), after the first verification pass (2026-10-28).

    python -I scripts/make_qgen_extra.py

Why: verifiers dropped about 65% of first-round unanswerable items because another thread
in the 1M index already answered them, and multi-document items were projected just under
50. This adds:
- multi        : pairs[80:110] from sources.json (unused, already protected in the index)
- unanswerable : 120 threads that are NOT in the index (removed by the 1M cap), none of whose
                 linked threads are in the index, accepted answer 200-2500 chars, question
                 score >= 5, drawn round-robin across sites with seed 31
Packets continue the numbering: multi_4.., unanswerable_4..
"""
import collections
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
QG = D / "qgen"
src = json.load(open(D / "sources.json"))

indexed_threads, indexed_acc = set(), collections.defaultdict(list)
pairs = [(tuple(a), tuple(b)) for a, b in src["pairs"][80:110]]
want_pairs = {k for p in pairs for k in p}
for line in open(D / "chunks.jsonl", encoding="utf-8"):
    r = json.loads(line)
    k = (r["site"], r["thread"])
    indexed_threads.add(k)
    if k in want_pairs and r["accepted"]:
        indexed_acc[k].append(r)

links = collections.defaultdict(set)
for site_dir in (D / "parsed").iterdir():
    for a, b, _ in json.load(open(site_dir / "links.json")):
        links[(site_dir.name, a)].add((site_dir.name, b))
        links[(site_dir.name, b)].add((site_dir.name, a))
meta = {}
for site_dir in (D / "parsed").iterdir():
    for tid, t in json.load(open(site_dir / "threads.json", encoding="utf-8")).items():
        meta[(site_dir.name, int(tid))] = t
used = {tuple(k) for k in json.load(open(D / "heldout.json"))} | {tuple(k) for k in json.load(open(D / "unanswerable_extra.json"))}

acc = collections.defaultdict(list)
for line in open(D / "chunks_all.jsonl", encoding="utf-8"):
    r = json.loads(line)
    k = (r["site"], r["thread"])
    if k not in indexed_threads and k not in used and r["accepted"]:
        acc[k].append(r)
by_site = collections.defaultdict(list)
for k, rows in acc.items():
    n = sum(len(r["text"]) for r in rows)
    if 200 <= n <= 2500 and meta.get(k, {}).get("score", 0) >= 5 and not (links.get(k, set()) & indexed_threads):
        by_site[k[0]].append(k)
rng = random.Random(47)
for s in by_site:
    by_site[s].sort()
    rng.shuffle(by_site[s])
extra = []
while len(extra) < 60 and any(by_site.values()):
    for s in sorted(by_site):
        if by_site[s] and len(extra) < 60:
            extra.append(by_site[s].pop())


def block(rows_by_key, k, with_ids=True):
    rows = sorted(rows_by_key[k], key=lambda r: r["chunk"])
    body = "\n\n".join((f"[chunk {r['id']}] " if with_ids else "") + r["text"].split("\n", 1)[1] for r in rows)
    return f"Site: {k[0]} | Thread title: {rows[0]['title']}\n{body}"


multi = []  # round 3 adds unanswerable only
unans = [(f"U{k[0]}-{k[1]}", block(acc, k, with_ids=False)) for k in extra]
for name, rows, start in (("multi", multi, 4), ("unanswerable", unans, 10)):
    for n in range(0, len(rows), 20):
        part = rows[n:n + 20]
        (QG / f"{name}_{start + n // 20}.md").write_text("\n\n".join(f"### item {k}\n{t}" for k, t in part), encoding="utf-8")
json.dump([list(k) for k in extra], open(D / "unanswerable_extra3.json", "w"))
print(f"multi items {len(multi)}, extra unanswerable {len(unans)} "
      f"(per site {collections.Counter(k[0] for k in extra)}); candidates available {sum(len(v) for v in by_site.values())}")
