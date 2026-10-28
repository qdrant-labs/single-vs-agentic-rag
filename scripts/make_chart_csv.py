"""Chart data for the article, written straight from the benchmark outputs (nothing typed by hand).

    python -I scripts/make_chart_csv.py <output csv>

Reads runs/main/summary.json (judged outcomes) and runs/main/results.jsonl (retrieval calls), and
writes one row per question type and pipeline: share answered correctly (for unanswerable
questions: share that said "not found"), runs, mean search-or-open calls, and the estimated median
latency from summary.json.
"""
import collections
import csv
import json
import pathlib
import statistics as st
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN = ROOT / "runs" / "main"
S = json.load(open(RUN / "summary.json"))
qs = {q["qid"]: q for q in json.load(open(ROOT / "data" / "questions.json", encoding="utf-8"))}
calls = collections.defaultdict(list)
for r in map(json.loads, open(RUN / "results.jsonl", encoding="utf-8")):
    calls[(qs[r["qid"]]["type"], r["pipeline"])].append(r["calls"])

TYPES = [("straightforward", "Straightforward"), ("semantic", "Reworded"),
         ("multi", "Multi-document"), ("unanswerable", "No answer")]
PIPES = [("single", "One search"), ("agentic", "Agent")]
LAT = {"single": "single_lat", "agentic": "agentic_lat"}

with open(sys.argv[1], "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["question_type", "pipeline", "correct_pct", "correct_runs", "runs", "calls_per_q", "median_latency_est_s"])
    for t, tname in TYPES:
        for p, pname in PIPES:
            cell = S["pipelines"][p][t]
            ok = cell.get("correct_refusal" if t == "unanswerable" else "correct", 0)
            w.writerow([tname, pname, f"{100 * ok / cell['runs']:.1f}", ok, cell["runs"],
                        f"{st.mean(calls[(t, p)]):.2f}", f"{S['cost_by_type'][t][LAT[p]][0]:.1f}"])
print(open(sys.argv[1], encoding="utf-8").read())
