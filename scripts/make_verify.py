"""Verification packets for the generated questions (Opus verifiers, fresh context).

    python -I scripts/make_verify.py                       # round 1: everything -> v_<n>.md
    python -I scripts/make_verify.py w multi unverified    # only unverified multi items -> w_<n>.md
    python -I scripts/make_verify.py r unanswerable dense  # unanswerable items still needing a dense
                                                           # check (unverified, recheck, or kept) -> r_<n>.md

Reads data/qgen/out/*.jsonl; attaches the evidence text (indexed chunks by id, or the
held-out source for unanswerable items); writes data/verify/<prefix>_<n>.md, 20 items each,
types mixed. Verifiers write data/verify/out/<prefix>_<n>.jsonl.
"""
import collections
import glob
import json
import pathlib
import random
import sys

PREFIX = sys.argv[1] if len(sys.argv) > 1 else "v"
TYPES = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
MODE = sys.argv[3] if len(sys.argv) > 3 else "all"

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
V = D / "verify"
(V / "out").mkdir(parents=True, exist_ok=True)

items = []
for f in sorted((D / "qgen" / "out").glob("*.jsonl")):
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        if "skip" in r or not r.get("question"):
            continue
        items.append(r)
verdict = {}
for f in sorted(glob.glob(str(V / "out" / "*.jsonl"))):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            v = json.loads(line)
            verdict[v["item"]] = v.get("verdict")
if TYPES:
    items = [r for r in items if r["type"] in TYPES]
if MODE == "unverified":
    items = [r for r in items if r["item"] not in verdict]
elif MODE == "dense":
    items = [r for r in items if verdict.get(r["item"]) in (None, "recheck", "keep")]
elif MODE == "round3":                     # only the round-3 unanswerable drafts
    r3 = {f"U{s}-{t}" for s, t in json.load(open(D / "unanswerable_extra3.json"))}
    items = [r for r in items if r["item"] in r3]
need = {int(i) for r in items for i in r.get("evidence", [])}
chunks = {}
for line in open(D / "chunks.jsonl", encoding="utf-8"):
    r = json.loads(line)
    if r["id"] in need:
        chunks[r["id"]] = r
held = collections.defaultdict(list)
heldkeys = {r["item"] for r in items if r["type"] == "unanswerable"}
for line in open(D / "chunks_all.jsonl", encoding="utf-8"):
    r = json.loads(line)
    key = f"U{r['site']}-{r['thread']}"
    if key in heldkeys and r["accepted"]:
        held[key].append(r)

bad = []
for r in items:
    if r["type"] != "unanswerable":
        missing = [i for i in r.get("evidence", []) if int(i) not in chunks]
        if missing or not r.get("evidence"):
            bad.append((r["item"], missing))
random.Random(7).shuffle(items)
blocks = []
for r in items:
    if r["type"] == "unanswerable":
        src = "\n".join(c["text"] for c in sorted(held[r["item"]], key=lambda c: c["chunk"]))
        ev = f"Source (NOT in the index):\n{src}"
    else:
        ev = "\n\n".join(f"[chunk {i}] (post {chunks[int(i)]['post']}, {chunks[int(i)]['site']})\n{chunks[int(i)]['text']}"
                         for i in r.get("evidence", []) if int(i) in chunks)
    blocks.append(f"### item {r['item']}\nType: {r['type']}\nQuestion: {r['question']}\n"
                  f"Reference answer: {r['answer']}\nEvidence chunk ids: {r.get('evidence', [])}\n{ev}\n")
for n in range(0, len(blocks), 20):
    (V / f"{PREFIX}_{n // 20}.md").write_text("\n".join(blocks[n:n + 20]), encoding="utf-8")
print(f"{len(items)} items -> {len(range(0, len(blocks), 20))} packets; by type {collections.Counter(r['type'] for r in items)}; "
      f"items with missing or empty evidence: {len(bad)} {bad[:5]}")
