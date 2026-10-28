"""Judge packets: every finished run, blind to pipeline and trial.

    python -I scripts/make_judge.py

Each item gets an opaque judge id; the key is runs/main/judge_key.json. Items are shuffled
across pipelines and trials into packets of 40 (data/judge/j_<n>.md). A seeded 20% sample
is also written as second-judge packets (data/judge/k_<n>.md) for agreement.
"""
import json
import pathlib
import random
import secrets

ROOT = pathlib.Path(__file__).resolve().parent.parent
D, RUN = ROOT / "data", ROOT / "runs" / "main"
J = D / "judge"
(J / "out").mkdir(parents=True, exist_ok=True)
qs = {q["qid"]: q for q in json.load(open(D / "questions.json", encoding="utf-8"))}
rows = [json.loads(l) for l in open(RUN / "results.jsonl", encoding="utf-8")]
need = {i for r in rows for i in r["cited"]} | {i for q in qs.values() for i in q["evidence"]}
text = {}
for line in open(D / "chunks.jsonl", encoding="utf-8"):
    c = json.loads(line)
    if c["id"] in need:
        text[c["id"]] = c["text"]

key, blocks = {}, []
for r in rows:
    q = qs[r["qid"]]
    jid = secrets.token_hex(4)
    key[jid] = r["run"]
    if q["type"] == "unanswerable":
        ref = "This question has NO answer in the knowledge base. The correct response is NOT_FOUND."
    else:
        ev = "\n".join(f"[chunk {i}] {text.get(i, '(missing)')}" for i in q["evidence"])
        ref = f"Reference answer: {q['answer']}\nReference evidence:\n{ev}"
    if r["final"] == "answer":
        cited = "\n".join(f"[chunk {i}] {text.get(i, '(not a valid chunk id)')}" for i in r["cited"]) or "(no chunks cited)"
        resp = f"System answer: {r['answer']}\nChunks the system cited:\n{cited}"
    else:
        resp = "System answer: NOT_FOUND"          # covers not_found and an exhausted search budget
    blocks.append((jid, f"### judge item {jid}\nQuestion: {q['question']}\n{ref}\n\n{resp}\n"))
rng = random.Random(5)
rng.shuffle(blocks)
for n in range(0, len(blocks), 40):
    (J / f"j_{n // 40:02d}.md").write_text("\n".join(b for _, b in blocks[n:n + 40]), encoding="utf-8")
sample = rng.sample(blocks, k=len(blocks) // 5)
for n in range(0, len(sample), 40):
    (J / f"k_{n // 40:02d}.md").write_text("\n".join(b for _, b in sample[n:n + 40]), encoding="utf-8")
json.dump(key, open(RUN / "judge_key.json", "w"), indent=0)
print(len(blocks), "items,", -(-len(blocks) // 40), "packets;", len(sample), "second-judge items")
