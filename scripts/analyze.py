"""Combine runs, judge labels, transcripts and latency estimates into the comparison report.

    python -I scripts/latency.py && python -I scripts/analyze.py
    # writes runs/main/report.md and runs/main/summary.json

Definitions (fixed before results were read):
- answerable types: correct = judge "correct"; unsupported = "incorrect" or "partial";
  missed = NOT_FOUND (including an exhausted search budget)
- unanswerable: correct refusal = NOT_FOUND; unsupported = any answer
- per question and pipeline, a trial-majority label is used for paired McNemar tests
- latency: Qdrant per call (exact, server-side); per-question latency = model time + Qdrant time
  rebuilt from transcripts (scripts/latency.py), because batch sub-agents worked on several
  questions at once and their wall clock overlaps
- tokens per question: each batch sub-agent's total tokens divided by its questions (inflated by
  batching), and the retrieved text each run put in front of the model (per question, exact)
Added after the runs, as descriptive extras: evidence retrieval (were the reference chunks shown),
cited-support rate, judge agreement (kappa), trial consistency, and two sensitivity checks.
"""
import collections
import glob
import json
import pathlib
import re
import statistics as st
from math import comb

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN, D = ROOT / "runs" / "main", ROOT / "data"
SUB = pathlib.Path("C:/Users/Home Laptop/.claude/projects/C--Users-Home-Laptop/cdca6ab0-f36b-482f-ad74-c7003f8734ab/subagents")
TYPES = ["straightforward", "semantic", "multi", "unanswerable"]
PIPES = ("single", "agentic")
ACCIDENT = {"010e9458"}  # recorded "NOT_FINAL" by mistake (runs/main/NOTES.md)

qs = {q["qid"]: q for q in json.load(open(D / "questions.json", encoding="utf-8"))}
rows = {r["run"]: r for r in map(json.loads, open(RUN / "results.jsonl", encoding="utf-8"))}
key = json.load(open(RUN / "judge_key.json"))
lat = json.load(open(RUN / "latency.json"))


def labels(pattern):
    out = {}
    for f in glob.glob(str(D / "judge" / "out" / pattern)):
        for line in open(f, encoding="utf-8"):
            if line.strip():
                j = json.loads(line)
                out[key.get(j["jid"], j["jid"])] = j
    return out


main_l, second_l = labels("j_*.jsonl"), labels("k_*.jsonl")
qtype = lambda r: qs[r["qid"]]["type"]


def label(r, judge=None):
    return "not_found" if r["final"] != "answer" else (judge or main_l).get(r["run"], {}).get("label", "unjudged")


def outcome(r, judge=None):
    lab = label(r, judge)
    if qtype(r) == "unanswerable":
        return "correct_refusal" if lab == "not_found" else "unsupported"
    return {"correct": "correct", "partial": "unsupported", "incorrect": "unsupported",
            "not_found": "missed"}.get(lab, lab)


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(p / 100 * (len(xs) - 1))))] if xs else float("nan")


def mcnemar(b, c):
    n = b + c
    return 1.0 if n == 0 else min(1.0, 2 * sum(comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = collections.Counter(a for a, _ in pairs), collections.Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in ca) / n ** 2
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def sel(pipe, t=None, trial=None, runs=None):
    return [r for r in (runs or rows.values()) if r["pipeline"] == pipe and (t is None or qtype(r) == t
            or (t == "answerable" and qtype(r) != "unanswerable")) and (trial is None or r["trial"] == trial)]


# tokens per question from the run sub-agents' transcripts; each batch sub-agent was told to
# read runs/main/prompts/<batch>.md, so that path names its batch
tok = collections.defaultdict(list)
batch_runs = collections.defaultdict(set)
for r in rows.values():
    batch_runs[r["batch"]].add(r["run"])
tok_batches = collections.Counter()
for f in SUB.glob("*.jsonl"):
    txt = open(f, encoding="utf-8").read()
    names = set(re.findall(r"runs/main/prompts/(t\d-(?:single|agentic)-\d\d)\.md", txt))
    match = [b for b in names if batch_runs.get(b)]
    if len(match) != 1:
        continue
    tok_batches[match[0]] += 1
    seen, inp, out = set(), 0, 0
    for line in txt.splitlines():
        d = json.loads(line)
        m = d.get("message") or {}
        u = m.get("usage")
        if u and m.get("id") not in seen:
            seen.add(m.get("id"))
            inp += u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
            out += u.get("output_tokens", 0)
    pipe = rows[next(iter(batch_runs[match[0]]))]["pipeline"]
    n = len(batch_runs[match[0]])
    tok[pipe].append((inp / n, out / n))

# retrieved text per run (what each pipeline put in front of the model), from the server's event
# log; batch transcripts carry earlier questions' context, so this is the per-question measure
ev_ids, need = collections.defaultdict(list), set()
for e in map(json.loads, open(RUN / "events.jsonl", encoding="utf-8")):
    if e.get("run") in rows and "ids" in e:
        ev_ids[e["run"]] += e["ids"]
        need.update(e["ids"])
clen = {}
for c in map(json.loads, open(D / "chunks.jsonl", encoding="utf-8")):
    if c["id"] in need:
        clen[c["id"]] = len(c["text"])
ret_tok = {run: sum(clen.get(i, 0) for i in ids) / 4 for run, ids in ev_ids.items()}  # ~4 chars per token


def ev_shown(r):  # reference evidence chunks the run was shown: "all", "some" or "none"
    ev, shown = {int(i) for i in qs[r["qid"]].get("evidence", [])}, set(r["shown"])
    return "all" if ev <= shown else ("some" if ev & shown else "none")


S = {"definitions": __doc__, "pipelines": {}}
L = ["# Single-pass vs agentic RAG on Qdrant: results", "",
     f"{len(qs)} questions x 2 pipelines x 3 trials = {len(rows)} runs; "
     f"judge labels {len(main_l)}, second-judge labels {len(second_l)}.", ""]

# 1. outcomes per type: mean over trials, with the per-trial range
L += ["## 1. Outcomes by question type (mean of 3 trials, per-trial range in brackets)", "",
      "| type | pipeline | correct | unsupported (partial / incorrect) | missed (NOT_FOUND) |",
      "|---|---|---|---|---|"]
for t in TYPES:
    for pipe in PIPES:
        per = []
        for tr in (1, 2, 3):
            rs = sel(pipe, t, tr)
            c = collections.Counter(outcome(r) for r in rs)
            lc = collections.Counter(label(r) for r in rs)
            per.append((len(rs), c, lc))
        n = sum(x[0] for x in per)
        tot = sum((x[1] for x in per), collections.Counter())
        ltot = sum((x[2] for x in per), collections.Counter())
        rate = lambda k: [x[1][k] / x[0] for x in per]
        fmt = lambda k: f"{100 * tot[k] / n:.1f}% [{100 * min(rate(k)):.0f}-{100 * max(rate(k)):.0f}]"
        S["pipelines"].setdefault(pipe, {})[t] = {"runs": n, **{k: tot[k] for k in tot}, **{"label_" + k: ltot[k] for k in ltot},
                                                  "per_trial": [dict(x[1]) for x in per]}
        if t == "unanswerable":
            L.append(f"| {t} | {pipe} | correct refusal {fmt('correct_refusal')} | answered anyway {fmt('unsupported')} | - |")
        else:
            L.append(f"| {t} | {pipe} | {fmt('correct')} | {fmt('unsupported')} ({ltot['partial']} / {ltot['incorrect']}) | {fmt('missed')} |")
for pipe in PIPES:
    rs = sel(pipe, "answerable")
    c = collections.Counter(outcome(r) for r in rs)
    S["pipelines"][pipe]["answerable"] = dict(c)
    L.append(f"| all answerable | {pipe} | {100 * c['correct'] / len(rs):.1f}% | {100 * c['unsupported'] / len(rs):.1f}% | {100 * c['missed'] / len(rs):.1f}% |")
L.append("")

# 2. paired comparison on trial-majority outcomes
maj = {}
byq = collections.defaultdict(list)
for r in rows.values():
    byq[(r["qid"], r["pipeline"])].append(outcome(r))
for k, v in byq.items():
    maj[k] = collections.Counter(v).most_common(1)[0][0]
L += ["## 2. Paired comparison per question (trial-majority outcome, exact McNemar)", "",
      "| type | single right | agentic right | only single | only agentic | p |", "|---|---|---|---|---|---|"]
S["paired"] = {}
for t in TYPES + ["answerable"]:
    target = "correct_refusal" if t == "unanswerable" else "correct"
    ids = [q for q in qs if (qs[q]["type"] == t or (t == "answerable" and qs[q]["type"] != "unanswerable"))]
    a = sum(maj[(q, "single")] == target for q in ids)
    g = sum(maj[(q, "agentic")] == target for q in ids)
    b = sum(maj[(q, "single")] == target and maj[(q, "agentic")] != target for q in ids)
    c = sum(maj[(q, "agentic")] == target and maj[(q, "single")] != target for q in ids)
    S["paired"][t] = {"n": len(ids), "single": a, "agentic": g, "only_single": b, "only_agentic": c, "p": mcnemar(b, c)}
    L.append(f"| {t} | {a}/{len(ids)} | {g}/{len(ids)} | {b} | {c} | {mcnemar(b, c):.2g} |")
L.append("")

# 3. retrieval: were the reference evidence chunks shown, and what happened when they were not
L += ["## 3. Retrieval: did the run see the reference evidence?", "",
      "Share of runs whose retrieved text included all / some / none of the reference evidence chunks "
      "(the chunks the question was written from; another chunk can also hold the answer).", "",
      "| type | pipeline | all | some | none | correct when all shown | correct when none shown |", "|---|---|---|---|---|---|---|"]
S["evidence"] = {}
for t in ["straightforward", "semantic", "multi"]:
    for pipe in PIPES:
        rs = sel(pipe, t)
        c = collections.Counter(ev_shown(r) for r in rs)
        acc = {k: (sum(outcome(r) == "correct" for r in rs if ev_shown(r) == k), c[k]) for k in ("all", "none")}
        S["evidence"][f"{t}/{pipe}"] = {"shown": dict(c), "correct_given": {k: list(v) for k, v in acc.items()}}
        f = lambda k: f"{acc[k][0]}/{acc[k][1]}" if acc[k][1] else "-"
        L.append(f"| {t} | {pipe} | {100 * c['all'] / len(rs):.0f}% | {100 * c['some'] / len(rs):.0f}% | "
                 f"{100 * c['none'] / len(rs):.0f}% | {f('all')} | {f('none')} |")
L += ["", "Where iterative retrieval changed the outcome (answerable questions, per run pair: same question, same trial):", ""]
pair = collections.Counter()
for r in sel("single", "answerable"):
    g = next(x for x in rows.values() if x["pipeline"] == "agentic" and x["qid"] == r["qid"] and x["trial"] == r["trial"])
    pair[(ev_shown(r) != "none", outcome(r), outcome(g))] += 1
S["pairs_by_single_evidence"] = {f"{'hit' if h else 'miss'}|{a}|{b}": n for (h, a, b), n in pair.items()}
for h in (True, False):
    n = sum(v for (hh, _, _), v in pair.items() if hh == h)
    s_ok = sum(v for (hh, a, _), v in pair.items() if hh == h and a == "correct")
    g_ok = sum(v for (hh, _, b), v in pair.items() if hh == h and b == "correct")
    lost = sum(v for (hh, a, b), v in pair.items() if hh == h and a == "correct" and b != "correct")
    won = sum(v for (hh, a, b), v in pair.items() if hh == h and a != "correct" and b == "correct")
    L.append(f"- single-pass top 10 {'held' if h else 'missed'} the evidence ({n} run pairs): single correct {s_ok}, "
             f"agentic correct {g_ok}; agentic fixed {won}, agentic lost {lost}")
L.append("")

# 4. cost
L += ["## 4. Cost: retrieval calls, tokens, latency", "", "| | single | agentic |", "|---|---|---|"]
cost = {}
for pipe in PIPES:
    rs = sel(pipe)
    lr = [lat[r["run"]] for r in rs if r["run"] in lat]
    qms = [m for r in rs for m in r["qdrant_ms"] if m > 0]
    cost[pipe] = {
        "retrieval calls per question (mean)": st.mean(r["calls"] for r in rs),
        "retrieval calls per question (p95)": pct([r["calls"] for r in rs], 95),
        "searches / opens per question (mean)": (st.mean(r["searches"] for r in rs), st.mean(r["opens"] for r in rs)),
        "runs closed by the 6-call budget": sum(r["final"] == "budget" for r in rs),
        "sequential model rounds per question (mean / p95)": (st.mean(x["rounds"] for x in lr), pct([x["rounds"] for x in lr], 95)),
        "retrieved context tokens per question (mean / p95)": (st.mean(ret_tok.get(r["run"], 0) for r in rs),
                                                                pct([ret_tok.get(r["run"], 0) for r in rs], 95)),
        "sub-agent tokens per question, in / out (batched, inflated)": (st.mean(x for x, _ in tok[pipe]), st.mean(y for _, y in tok[pipe])),
        "Qdrant ms per query (p50 / p95)": (pct(qms, 50), pct(qms, 95)),
        "Qdrant ms per question (p50 / p95)": (pct([1000 * x["qdrant_s"] for x in lr], 50), pct([1000 * x["qdrant_s"] for x in lr], 95)),
        "latency s, model + Qdrant, shared-turn split (p50 / p95)": (pct([x["modeled_split_s"] for x in lr], 50), pct([x["modeled_split_s"] for x in lr], 95)),
        "latency s, model + Qdrant, full-turn charge (p50 / p95)": (pct([x["modeled_full_s"] for x in lr], 50), pct([x["modeled_full_s"] for x in lr], 95)),
        "wall clock s incl. Claude Code tool overhead (p50 / p95)": (pct([x["latency_split_s"] for x in lr], 50), pct([x["latency_split_s"] for x in lr], 95)),
    }
S["cost"] = cost
fmt = lambda v: (f"{v[0]:.1f} / {v[1]:.1f}" if isinstance(v, tuple) else (f"{v:.2f}" if isinstance(v, float) else str(v)))
for k in cost["single"]:
    L.append(f"| {k} | {fmt(cost['single'][k])} | {fmt(cost['agentic'][k])} |")
L += ["", "Agentic cost by question type (mean calls; latency p50 / p95, model + Qdrant, split):", ""]
S["cost_by_type"] = {}
for t in TYPES:
    rs = sel("agentic", t)
    x = [lat[r["run"]]["modeled_split_s"] for r in rs]
    y = [lat[r["run"]]["modeled_split_s"] for r in sel("single", t)]
    S["cost_by_type"][t] = {"agentic_calls": st.mean(r["calls"] for r in rs), "agentic_lat": (pct(x, 50), pct(x, 95)),
                            "single_lat": (pct(y, 50), pct(y, 95)), "agentic_ret_tok": st.mean(ret_tok.get(r["run"], 0) for r in rs)}
    L.append(f"- {t}: {S['cost_by_type'][t]['agentic_calls']:.2f} calls; latency agentic {pct(x, 50):.1f} / {pct(x, 95):.1f} s "
             f"vs single {pct(y, 50):.1f} / {pct(y, 95):.1f} s; agentic retrieved tokens {S['cost_by_type'][t]['agentic_ret_tok']:.0f}")
L.append("")

# 5. reliability of the measurement
pairs = [(main_l[k]["label"], second_l[k]["label"]) for k in second_l if k in main_l]
bin_pairs = [(a == "correct", b == "correct") for a, b in pairs]
ans_pairs = [(a, b) for a, b in pairs if a != "not_found"]
S["judges"] = {"n": len(pairs), "exact": sum(a == b for a, b in pairs) / len(pairs), "kappa": kappa(pairs),
               "binary_correct_agreement": sum(a == b for a, b in bin_pairs) / len(bin_pairs),
               "answered_items": len(ans_pairs), "answered_exact": sum(a == b for a, b in ans_pairs) / len(ans_pairs),
               "answered_kappa": kappa(ans_pairs),
               "confusion": {f"{a}->{b}": n for (a, b), n in collections.Counter(pairs).items() if a != b}}
cons = {}
for pipe in PIPES:
    same = [len(set(outcome(r) for r in rows.values() if r["pipeline"] == pipe and r["qid"] == q)) == 1 for q in qs]
    cons[pipe] = sum(same) / len(same)
S["trial_consistency"] = cons
cs = {pipe: collections.Counter(main_l[r["run"]].get("cited_support") for r in sel(pipe) if r["final"] == "answer") for pipe in PIPES}
S["cited_support"] = {p: dict(c) for p, c in cs.items()}
L += ["## 5. Measurement checks", "",
      f"- Second judge on {len(pairs)} runs (20% sample): exact label agreement {100 * S['judges']['exact']:.1f}%, "
      f"Cohen's kappa {S['judges']['kappa']:.2f}; on answered items only {100 * S['judges']['answered_exact']:.1f}% "
      f"(kappa {S['judges']['answered_kappa']:.2f}); correct-vs-not agreement {100 * S['judges']['binary_correct_agreement']:.1f}%.",
      f"  Disagreements: {S['judges']['confusion']}",
      f"- Same outcome in all 3 trials: single {100 * cons['single']:.0f}% of questions, agentic {100 * cons['agentic']:.0f}%.",
      f"- Cited chunks do not support the answer (judge cited_support = no): single {cs['single']['no']}/{sum(cs['single'].values())}, "
      f"agentic {cs['agentic']['no']}/{sum(cs['agentic'].values())} answers.", ""]

# 6. sensitivity
L += ["## 6. Sensitivity", ""]
for name, keep in (("without the accidental 'NOT_FINAL' run", lambda r: r["run"] not in ACCIDENT),):
    for pipe in PIPES:
        rs = [r for r in sel(pipe, "answerable") if keep(r)]
        c = collections.Counter(outcome(r) for r in rs)
        L.append(f"- {name}, {pipe}: correct {100 * c['correct'] / len(rs):.1f}%, unsupported {100 * c['unsupported'] / len(rs):.1f}%")
for pipe in PIPES:
    rs = sel(pipe, "answerable")
    sc = sum({"correct": 1, "partial": 0.5}.get(label(r), 0) for r in rs) / len(rs)
    L.append(f"- partial counted as half credit, {pipe}: {100 * sc:.1f}%")
for pipe in PIPES:  # second judge's labels where available
    rs = [r for r in sel(pipe, "answerable") if r["run"] in second_l]
    c1 = sum(outcome(r) == "correct" for r in rs)
    c2 = sum(outcome(r, second_l) == "correct" for r in rs)
    L.append(f"- second-judge sample, {pipe} ({len(rs)} answerable runs): correct {c1} by judge 1, {c2} by judge 2")
L += ["", f"Batches with token counts: {len(tok_batches)}/{len(batch_runs)}; "
      f"batches matched by more than one transcript: {[b for b, n in tok_batches.items() if n > 1]}"]

(RUN / "report.md").write_text("\n".join(L), encoding="utf-8")
json.dump(S, open(RUN / "summary.json", "w"), indent=1, default=str)
print("\n".join(L))
