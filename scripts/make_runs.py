"""Blind run assignment: 3 trials x 2 pipelines x every question in data/questions.json.

    python -I scripts/make_runs.py

Batches of 8 questions per sub-agent, one pipeline per batch (the prompt differs by
pipeline), question types mixed, and no two questions from the same source thread in a
batch. Run ids are random hex. Writes runs/main/assign.json, runs/main/batches.json and
runs/main/prompts.md (the exact prompts given to the sub-agents).
"""
import json
import pathlib
import random
import secrets

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "runs" / "main"
OUT.mkdir(parents=True, exist_ok=True)
assert not (OUT / "assign.json").exists(), "assignment exists; refusing to overwrite"
TOOL = "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py"
BATCH, TRIALS = 8, 3

RULE = ("Answer only from text the tool returned. Record a short answer (one or two sentences) "
        "together with the ids of the chunks that support it. If the retrieved text does not contain "
        "the answer, record not_found instead. Do not answer from your own knowledge.")
PROMPTS = {
    "single": (
        "You answer questions about Linux, servers, databases, networking, security and software "
        "engineering using a knowledge base of community answers. For each question below, run the "
        "context command once: it returns the passages a retrieval system found for that question. "
        "You cannot search again.\n\n" + RULE + "\n\n"
        "Commands (Bash):\n"
        f'python -I "{TOOL}" context <run>\n'
        f'python -I "{TOOL}" answer <run> <chunk ids, comma-separated> "<answer>"\n'
        f'python -I "{TOOL}" not_found <run>\n\n'
        "Rules: use only these commands. Do not read, list, grep or search any files or folders, and "
        "do not use any other tool. Record exactly one answer per question, then move on.\n\n"),
    "agentic": (
        "You answer questions about Linux, servers, databases, networking, security and software "
        "engineering using a knowledge base of community answers. For each question below, search the "
        "knowledge base: you may search several times with different wording, look at the next page of "
        "results, and open a post to read the whole answer. Each question allows at most 6 search/open "
        "calls.\n\n" + RULE + "\n\n"
        "Commands (Bash):\n"
        f'python -I "{TOOL}" search <run> "<query>" [page]\n'
        f'python -I "{TOOL}" open <run> <post number>\n'
        f'python -I "{TOOL}" answer <run> <chunk ids, comma-separated> "<answer>"\n'
        f'python -I "{TOOL}" not_found <run>\n\n'
        "Rules: use only these commands. Do not read, list, grep or search any files or folders, and "
        "do not use any other tool. Record exactly one answer per question, then move on.\n\n"),
}
TAIL = ("When every question has an answer recorded, reply with one line: how many you answered and how "
        "many you marked not_found.")

qs = json.load(open(ROOT / "data" / "questions.json", encoding="utf-8"))
rng = random.Random(4242)
assign, batches = {}, {}
for trial in range(1, TRIALS + 1):
    for pipeline in ("single", "agentic"):
        order = qs[:]
        rng.shuffle(order)
        for b in range(0, len(order), BATCH):
            part = order[b:b + BATCH]
            name = f"t{trial}-{pipeline}-{b // BATCH:02d}"
            lines = []
            for q in part:
                rid = secrets.token_hex(4)
                while rid in assign:
                    rid = secrets.token_hex(4)
                assign[rid] = {"qid": q["qid"], "pipeline": pipeline, "trial": trial, "batch": name}
                lines.append(f"- {rid}: {q['question']}")
            batches[name] = {"pipeline": pipeline, "prompt": PROMPTS[pipeline] + "Questions (run id: question):\n"
                             + "\n".join(lines) + "\n\n" + TAIL}
json.dump(assign, open(OUT / "assign.json", "w"), indent=0)
json.dump(batches, open(OUT / "batches.json", "w"), indent=0)
(OUT / "prompts.md").write_text("\n\n".join(f"## {k}\n{v}" for k, v in PROMPTS.items()), encoding="utf-8")
print(len(assign), "runs in", len(batches), "batches")
