# Run notes (kept as recorded; nothing in results.jsonl is edited)

- 010e9458 (t3-agentic-03): the sub-agent recorded the literal answer "NOT_FINAL" (citing chunk
  721784) by accident while testing a command, and reported it. Kept as recorded: the judge grades
  it like any other answer. The report states it and gives the agentic numbers with and without it.
- Budget closures: an agentic run that makes a 7th search/open call is closed by the server as
  "budget" and scored as NOT_FOUND (pre-registered). Several sub-agents reported reaching the cap
  with an answer in hand because they miscounted their calls.
