"""Gated pipeline: single pass by default, escalate to the agent when the retrieval looks weak.

    python -I scripts/gate_eval.py      # needs gate_signals.json, latency.json, judge labels
                                        # writes runs/main/gate_report.md and gate_summary.json

Method follows Predicting Weak Retrieval Without an LLM (Couzon, 2026):
- window = the single pass's top 10; a retrieval is weak when the window lacks any of the
  question's evidence chunks (unanswerable questions: always weak, there is nothing to find)
- cheap signals, oriented so lower means weaker: max_score (top-1 cosine), dense_variance
  (population variance of the top-10 cosines), dense_sparse_overlap (Jaccard of the dense and
  BM25 top 10, i.e. 1 - retriever_divergence)
- separation = max(AUC, 1 - AUC); floor = Youden point on a calibration split; final numbers
  on the held-out split. 500 random 50/50 question splits, stratified by type.
Each gated run takes the recorded outcome of the same question and trial: the single-pass run
when the gate passes it, the agentic run when it escalates. Cost of an escalated question = the
first search plus the whole agentic run (the gate reads scores, so no model call is spent on
the single pass). Nothing is rerun through a model.
"""
import collections
import glob
import json
import pathlib
import random
import statistics as st

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN, D = ROOT / "runs" / "main", ROOT / "data"
REPEATS, SEED = 500, 7

qs = {q["qid"]: q for q in json.load(open(D / "questions.json", encoding="utf-8"))}
rows = list(map(json.loads, open(RUN / "results.jsonl", encoding="utf-8")))
key = json.load(open(RUN / "judge_key.json"))
lat = json.load(open(RUN / "latency.json"))
sig_raw = json.load(open(RUN / "gate_signals.json"))
label = {}
for f in glob.glob(str(D / "judge" / "out" / "j_*.jsonl")):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            j = json.loads(line)
            label[key[j["jid"]]] = j["label"]


def outcome(r):
    lab = "not_found" if r["final"] != "answer" else label[r["run"]]
    if qs[r["qid"]]["type"] == "unanswerable":
        return "correct_refusal" if lab == "not_found" else "unsupported"
    return {"correct": "correct", "partial": "unsupported", "incorrect": "unsupported", "not_found": "missed"}[lab]


# retrieved tokens per run (same measure as analyze.py)
ev_ids, need = collections.defaultdict(list), set()
for e in map(json.loads, open(RUN / "events.jsonl", encoding="utf-8")):
    if e.get("run") and "ids" in e:
        ev_ids[e["run"]] += e["ids"]
        need.update(e["ids"])
clen = {}
for c in map(json.loads, open(D / "chunks.jsonl", encoding="utf-8")):
    if c["id"] in need:
        clen[c["id"]] = len(c["text"])
ret_tok = {run: sum(clen.get(i, 0) for i in ids) / 4 for run, ids in ev_ids.items()}

# one record per (question, trial): what each pipeline did
cell = collections.defaultdict(dict)
for r in rows:
    cell[(r["qid"], r["trial"])][r["pipeline"]] = {
        "outcome": outcome(r), "calls": r["calls"], "tok": ret_tok.get(r["run"], 0),
        "lat": lat[r["run"]]["modeled_split_s"], "qdrant": lat[r["run"]]["qdrant_s"]}

# signals and weak labels per question
sig, weak = {}, {}
for qid, s in sig_raw.items():
    scores = [x for _, x in s["dense"]]
    ids = [i for i, _ in s["dense"]]
    b = set(s["bm25"])
    sig[qid] = {"max_score": scores[0], "dense_variance": st.pvariance(scores),
                "dense_sparse_overlap": len(set(ids) & b) / len(set(ids) | b) if b else 0.0}
    ev = {int(i) for i in qs[qid].get("evidence", [])}
    weak[qid] = 1 if qs[qid]["type"] == "unanswerable" or not ev <= set(ids) else 0
SIGNALS = list(next(iter(sig.values())))


def auc(vals, labs):  # P(signal of a weak retrieval < signal of a good one); 0.5 = chance
    pos = [v for v, l in zip(vals, labs) if l]
    neg = [v for v, l in zip(vals, labs) if not l]
    if not pos or not neg:
        return float("nan")
    return sum((p < n) + 0.5 * (p == n) for p in pos for n in neg) / (len(pos) * len(neg))


def youden_floor(qids, s):  # floor maximizing catch rate minus false-alarm rate
    pairs = sorted((sig[q][s], weak[q]) for q in qids)
    P = sum(w for _, w in pairs) or 1
    N = (len(pairs) - sum(w for _, w in pairs)) or 1
    best, floor = -1, pairs[0][0]
    for i in range(len(pairs) + 1):          # escalate the i lowest
        tp = sum(w for _, w in pairs[:i])
        fp = i - tp
        j = tp / P - fp / N
        if j > best:
            best = j
            floor = pairs[i][0] if i < len(pairs) else float("inf")
    return floor


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(p / 100 * (len(xs) - 1))))]


def evaluate(qids, escalate, gated=True):
    """Metrics over all trials of qids; escalate(qid) -> bool. Without a gate (always agent)
    there is no first search to pay for."""
    first = 1 if gated else 0
    acc, ans, ref, una, calls, tok, lats, esc = 0, 0, 0, 0, [], [], [], 0
    for q in qids:
        for t in (1, 2, 3):
            c = cell[(q, t)]
            e = escalate(q)
            esc += e
            run = c["agentic"] if e else c["single"]
            if qs[q]["type"] == "unanswerable":
                una += 1
                ref += run["outcome"] == "correct_refusal"
            else:
                ans += 1
                acc += run["outcome"] == "correct"
            calls.append(first + c["agentic"]["calls"] if e else 1)
            tok.append(c["agentic"]["tok"] if e else c["single"]["tok"])
            lats.append(first * c["single"]["qdrant"] + c["agentic"]["lat"] if e else c["single"]["lat"])
    n = len(qids) * 3
    return {"escalated": esc / n, "answerable_acc": acc / ans if ans else None, "refusal": ref / una if una else None,
            "calls": st.mean(calls), "tok": st.mean(tok), "lat_p50": pct(lats, 50), "lat_p95": pct(lats, 95)}


def avg(ms):
    return {k: st.mean(m[k] for m in ms if m[k] is not None) for k in ms[0]}


ALL = sorted(qs)
by_type = collections.defaultdict(list)
for q in ALL:
    by_type[qs[q]["type"]].append(q)
S, L = {}, ["# Gated pipeline: one search, escalate to the agent when retrieval looks weak", ""]

# 1. which signals separate weak from good retrievals
L += ["## 1. Signal separation (AUC; 0.5 = chance; weak = window lacks the evidence)", "",
      "| signal | all 200 | answerable 150 | straightforward | semantic | multi |", "|---|---|---|---|---|---|"]
S["auc"] = {}
for s in SIGNALS:
    cols = [ALL, [q for q in ALL if qs[q]["type"] != "unanswerable"]] + [by_type[t] for t in ("straightforward", "semantic", "multi")]
    vals = [auc([sig[q][s] for q in c], [weak[q] for q in c]) for c in cols]
    S["auc"][s] = vals
    L.append(f"| {s} | " + " | ".join("-" if v != v else f"{v:.2f}" for v in vals) + " |")
weak_rate = {t: sum(weak[q] for q in by_type[t]) / len(by_type[t]) for t in by_type}
L += ["", f"Weak share by type: {', '.join(f'{t} {100 * v:.0f}%' for t, v in weak_rate.items())}", ""]

# 2. held-out gate, repeated splits
rng = random.Random(SEED)
held = collections.defaultdict(list)
for _ in range(REPEATS):
    cal, test = [], []
    for t in by_type:
        g = by_type[t][:]
        rng.shuffle(g)
        cal += g[:len(g) // 2]
        test += g[len(g) // 2:]
    best = max(SIGNALS, key=lambda s: abs(auc([sig[q][s] for q in cal], [weak[q] for q in cal]) - 0.5))
    for s in SIGNALS + ["chosen on calibration"]:
        use = best if s == "chosen on calibration" else s
        fl = youden_floor(cal, use)
        held[s].append(evaluate(test, lambda q, use=use, fl=fl: sig[q][use] < fl))
    held["single pass"].append(evaluate(test, lambda q: False))
    held["always agent"].append(evaluate(test, lambda q: True, gated=False))
    held["oracle (escalate answerable misses only)"].append(evaluate(test, lambda q: weak[q] and qs[q]["type"] != "unanswerable"))
    r = held["chosen on calibration"][-1]["escalated"]
    pick = set(rng.sample(test, round(r * len(test))))
    held["random, same escalation rate"].append(evaluate(test, lambda q, pick=pick: q in pick))
S["held_out"] = {k: avg(v) for k, v in held.items()}
L += [f"## 2. Held-out results ({REPEATS} random 50/50 splits; floor = Youden point on the calibration half)", "",
      "| pipeline | escalated | answerable correct | unanswerable refused | calls / q | retrieved tokens / q | latency p50 / p95 s |",
      "|---|---|---|---|---|---|---|"]
for k in ["single pass", "always agent"] + SIGNALS + ["chosen on calibration", "random, same escalation rate", "oracle (escalate answerable misses only)"]:
    m = S["held_out"][k]
    L.append(f"| {k} | {100 * m['escalated']:.0f}% | {100 * m['answerable_acc']:.1f}% | {100 * m['refusal']:.1f}% | "
             f"{m['calls']:.2f} | {m['tok']:.0f} | {m['lat_p50']:.1f} / {m['lat_p95']:.1f} |")

# 3. per-type view of the chosen gate on all questions (floor from all 200, descriptive)
best_all = max(SIGNALS, key=lambda s: abs(auc([sig[q][s] for q in ALL], [weak[q] for q in ALL]) - 0.5))
fl_all = youden_floor(ALL, best_all)
S["full_fit"] = {"signal": best_all, "floor": fl_all}
L += ["", f"## 3. By question type ({best_all} < {fl_all:.4g}, floor fitted on all 200: descriptive, not held out)", "",
      "| type | escalated | single correct | gated correct | agent correct | calls / q gated vs agent | latency p50 s gated vs agent |",
      "|---|---|---|---|---|---|---|"]
S["by_type"] = {}
for t in ("straightforward", "semantic", "multi", "unanswerable"):
    g = evaluate(by_type[t], lambda q: sig[q][best_all] < fl_all)
    s1 = evaluate(by_type[t], lambda q: False)
    a1 = evaluate(by_type[t], lambda q: True, gated=False)
    k = "refusal" if t == "unanswerable" else "answerable_acc"
    S["by_type"][t] = {"gated": g, "single": s1, "agent": a1}
    L.append(f"| {t} | {100 * g['escalated']:.0f}% | {100 * s1[k]:.1f}% | {100 * g[k]:.1f}% | {100 * a1[k]:.1f}% | "
             f"{g['calls']:.2f} vs {a1['calls']:.2f} | {g['lat_p50']:.1f} vs {a1['lat_p50']:.1f} |")

# 4. trade-off curve: escalate the lowest x% by the chosen signal (in-sample)
L += ["", f"## 4. Trade-off curve: escalate the weakest x% by {best_all} (all 200, in-sample)", "",
      "| escalated | answerable correct | unanswerable refused | calls / q | retrieved tokens / q | latency p50 / p95 s |", "|---|---|---|---|---|---|"]
order = sorted(ALL, key=lambda q: sig[q][best_all])
S["curve"] = []
for x in range(0, 101, 10):
    esc = set(order[:round(x / 100 * len(order))])
    m = evaluate(ALL, lambda q: q in esc)
    S["curve"].append(m)
    L.append(f"| {x}% | {100 * m['answerable_acc']:.1f}% | {100 * m['refusal']:.1f}% | {m['calls']:.2f} | {m['tok']:.0f} | "
             f"{m['lat_p50']:.1f} / {m['lat_p95']:.1f} |")

# 5. side estimate: cap the agent's budget, from the logs. A run that used more calls than the
# cap is counted as NOT_FOUND (a lower bound for answerable questions: with fewer calls the agent
# might still have answered from what it had); its cost is the cap.
L += ["", "## 5. Side estimate: always agent with a smaller search budget (from the logs, conservative)", "",
      "| budget | answerable correct | unanswerable refused | calls / q | latency p50 / p95 s |", "|---|---|---|---|---|"]
S["budget"] = {}
for cap in (2, 3, 4, 6):
    acc = ans = ref = una = 0
    calls, lats = [], []
    for (q, t), c in cell.items():
        a = c["agentic"]
        over = a["calls"] > cap
        o = ("correct_refusal" if qs[q]["type"] == "unanswerable" else "missed") if over else a["outcome"]
        if qs[q]["type"] == "unanswerable":
            una += 1
            ref += o == "correct_refusal"
        else:
            ans += 1
            acc += o == "correct"
        calls.append(min(a["calls"], cap))
        lats.append(a["lat"] * min(1, cap / a["calls"]) if a["calls"] else a["lat"])  # time scales with calls made
    S["budget"][cap] = {"answerable_acc": acc / ans, "refusal": ref / una, "calls": st.mean(calls),
                        "lat_p50": pct(lats, 50), "lat_p95": pct(lats, 95)}
    m = S["budget"][cap]
    L.append(f"| {cap} | {100 * m['answerable_acc']:.1f}% | {100 * m['refusal']:.1f}% | {m['calls']:.2f} | {m['lat_p50']:.1f} / {m['lat_p95']:.1f} |")

(RUN / "gate_report.md").write_text("\n".join(L), encoding="utf-8")
json.dump(S, open(RUN / "gate_summary.json", "w"), indent=1)
print("\n".join(L))
