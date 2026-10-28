"""Write question-generation packets from data/sources.json.

    python -I scripts/make_qgen.py

Types and sources (fixed order from select_sources.py, seed 2028):
- straightforward : single[:80]   accepted-answer chunks, with chunk ids
- semantic        : single[80:160]
- multi           : pairs[:80]    accepted-answer chunks of both threads, with chunk ids
- unanswerable    : unanswerable[:80]  accepted-answer text of a held-out thread (not indexed)

Packets of 20 items go to data/qgen/<type>_<n>.md; generators write
data/qgen/out/<type>_<n>.jsonl.
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
QG = D / "qgen"
(QG / "out").mkdir(parents=True, exist_ok=True)
src = json.load(open(D / "sources.json"))
want = {tuple(k) for k in src["single"]} | {tuple(k) for p in src["pairs"] for k in p}
held = {tuple(k) for k in src["unanswerable"]}

indexed = collections.defaultdict(list)       # (site, thread) -> accepted chunks with ids
for line in open(D / "chunks.jsonl", encoding="utf-8"):
    r = json.loads(line)
    k = (r["site"], r["thread"])
    if k in want and r["accepted"]:
        indexed[k].append(r)
heldtext = collections.defaultdict(list)
for line in open(D / "chunks_all.jsonl", encoding="utf-8"):
    r = json.loads(line)
    k = (r["site"], r["thread"])
    if k in held and r["accepted"]:
        heldtext[k].append(r)


def block(k, with_ids=True):
    rows = sorted(indexed[k] if with_ids else heldtext[k], key=lambda r: r["chunk"])
    title = rows[0]["title"]
    body = "\n\n".join((f"[chunk {r['id']}] " if with_ids else "") + r["text"].split("\n", 1)[1] for r in rows)
    return f"Site: {k[0]} | Thread title: {title}\n{body}"


items = []
for i, k in enumerate(src["single"][:160]):
    k = tuple(k)
    items.append(("straightforward" if i < 80 else "semantic", f"T{k[0]}-{k[1]}", block(k)))
for a, b in src["pairs"][:80]:
    a, b = tuple(a), tuple(b)
    items.append(("multi", f"P{a[0]}-{a[1]}-{b[1]}", "THREAD A\n" + block(a) + "\n\nTHREAD B\n" + block(b)))
for k in src["unanswerable"][:80]:
    k = tuple(k)
    items.append(("unanswerable", f"U{k[0]}-{k[1]}", block(k, with_ids=False)))

by_type = collections.defaultdict(list)
for t, key, text in items:
    by_type[t].append((key, text))
for t, rows in by_type.items():
    for n in range(0, len(rows), 20):
        part = rows[n:n + 20]
        body = "\n\n".join(f"### item {key}\n{text}" for key, text in part)
        (QG / f"{t}_{n // 20}.md").write_text(body, encoding="utf-8")
print({t: len(v) for t, v in by_type.items()})
