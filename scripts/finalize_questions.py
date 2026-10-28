"""Freeze the question set: verified items only, 50 per type, chosen with a fixed seed.

    python -I scripts/finalize_questions.py

Applies verifier fixes, keeps verdict == "keep", draws 50 per type in a seeded order,
writes data/questions.json and data/questions.sha256. Run before any benchmark run.
"""
import collections
import hashlib
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
PER_TYPE, SEED = 50, 99

gen = {}
for f in sorted((D / "qgen" / "out").glob("*.jsonl")):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            if "skip" not in r and r.get("question"):
                gen[r["item"]] = r
verdicts = {}
for f in sorted((D / "verify" / "out").glob("*.jsonl")):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            v = json.loads(line)
            verdicts[v["item"]] = v
kept = collections.defaultdict(list)
dropped = collections.Counter()
for key, r in gen.items():
    v = verdicts.get(key)
    if not v or v.get("verdict") != "keep":
        dropped[r["type"]] += 1
        continue
    r = dict(r, question=v.get("question") or r["question"], answer=v.get("answer") or r["answer"],
             verifier_reason=v.get("reason", ""))
    kept[r["type"]].append(r)
out = []
rng = random.Random(SEED)
for t in ("straightforward", "semantic", "multi", "unanswerable"):
    rows = sorted(kept[t], key=lambda r: r["item"])
    rng.shuffle(rows)
    if len(rows) < PER_TYPE:
        print(f"WARNING: only {len(rows)} verified {t} items")
    for r in rows[:PER_TYPE]:
        out.append({"qid": f"q{len(out) + 1:03d}", "type": t, "question": r["question"], "answer": r["answer"],
                    "evidence": [int(i) for i in r.get("evidence", [])], "item": r["item"],
                    "support": r.get("support", ""), "verifier_reason": r["verifier_reason"]})
blob = json.dumps(out, indent=1, ensure_ascii=False)
(D / "questions.json").write_text(blob, encoding="utf-8")
digest = hashlib.sha256(blob.encode("utf-8")).hexdigest()
(D / "questions.sha256").write_text(digest + "\n")
print(f"frozen {len(out)} questions; kept per type { {t: len(v) for t, v in kept.items()} }; "
      f"dropped {dict(dropped)}; sha256 {digest[:16]}")
