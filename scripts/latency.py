"""Per-question latency estimate from the run sub-agents' transcripts.

    python -I scripts/latency.py            # writes runs/main/latency.json

Why: a batch sub-agent often worked on several questions at once (parallel tool calls), so a
run's wall clock from first tool call to answer (e2e_s in results.jsonl) includes other
questions' work. This rebuilds each run's own critical path instead:

- model time: for each assistant message that issued bench_tool calls, the time from the
  previous user event (prompt or tool result) to the message's last line; shared evenly
  between the runs that message touched ("split"), or charged in full to each ("full")
- tool time: tool_use line to its tool_result, shared evenly between the runs in that command;
  this is mostly Claude Code's own Bash-tool overhead (Qdrant itself is qdrant_s)
- rounds: how many assistant messages touched the run (sequential model calls)

The reported latency is model time + Qdrant time ("modeled_*"): what a pipeline that calls the
model and Qdrant directly would spend. The true single-question figure sits between "split"
and "full". latency_*_s adds the harness tool time back, for reference.
"""
import collections
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN = ROOT / "runs" / "main"
SUB = pathlib.Path("C:/Users/Home Laptop/.claude/projects/C--Users-Home-Laptop/cdca6ab0-f36b-482f-ad74-c7003f8734ab/subagents")
CALL = re.compile(r"bench_tool\.py\"?\s+(?:context|search|open|answer|not_found)\s+([0-9a-f]{8})")
rows = {r["run"]: r for r in map(json.loads, open(RUN / "results.jsonl", encoding="utf-8"))}


def ts(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


est = collections.defaultdict(lambda: {"model_split": 0.0, "model_full": 0.0, "tool": 0.0, "rounds": 0})
for f in SUB.glob("*.jsonl"):
    txt = open(f, encoding="utf-8").read()
    if not re.search(r"runs/main/prompts/t\d-(?:single|agentic)-\d\d\.md", txt):
        continue
    last_user, msgs, order, tool_start, tool_runs = None, {}, [], {}, {}
    for line in txt.splitlines():
        d = json.loads(line)
        if d.get("type") == "user" and d.get("timestamp"):
            t = ts(d["timestamp"])
            for b in (d.get("message") or {}).get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_result" and b.get("tool_use_id") in tool_start:
                    runs = tool_runs[b["tool_use_id"]]
                    for r in runs:
                        est[r]["tool"] += (t - tool_start[b["tool_use_id"]]) / len(runs)
            last_user = t
        elif d.get("type") == "assistant" and d.get("timestamp"):
            m = d["message"]
            t = ts(d["timestamp"])
            if m["id"] not in msgs:
                msgs[m["id"]] = {"start": last_user, "end": t, "runs": set()}
                order.append(m["id"])
            msgs[m["id"]]["end"] = t
            for b in m.get("content") or []:
                if b.get("type") == "tool_use":
                    runs = [r for r in dict.fromkeys(CALL.findall(str(b.get("input", {}).get("command", "")))) if r in rows]
                    if runs:
                        tool_start[b["id"]], tool_runs[b["id"]] = t, runs
                        msgs[m["id"]]["runs"].update(runs)
    for mid in order:
        m = msgs[mid]
        if not m["runs"] or m["start"] is None:
            continue
        dur = m["end"] - m["start"]
        for r in m["runs"]:
            est[r]["model_split"] += dur / len(m["runs"])
            est[r]["model_full"] += dur
            est[r]["rounds"] += 1

out = {}
for run, e in est.items():
    qms = sum(rows[run]["qdrant_ms"]) / 1000
    out[run] = {**e, "qdrant_s": qms, "modeled_split_s": e["model_split"] + qms,
                "modeled_full_s": e["model_full"] + qms, "latency_split_s": e["model_split"] + e["tool"],
                "latency_full_s": e["model_full"] + e["tool"]}
json.dump(out, open(RUN / "latency.json", "w"), indent=0)
print(f"runs with an estimate: {len(out)}/{len(rows)}")
