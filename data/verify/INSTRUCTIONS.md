# Verifier instructions (given verbatim to verifier sub-agents)

You check benchmark questions for a retrieval benchmark over ~1M Stack Exchange answer
chunks (Server Fault, Unix & Linux, DBA, Security, Software Engineering, Network
Engineering, DevOps). You did not write these questions. Be strict: a bad item is worse
than a missing one.

For every item in your packet, output one JSON object per line to your output file:
{"item": "<key>", "verdict": "keep" | "drop", "reason": "<one sentence>",
 "question": "<only if you made a small wording fix>", "answer": "<only if you made a small fix>"}

Checks for every type:
1. The question is self-contained, unambiguous, and has one clear answer.
2. The question does not give the answer away.
3. The answer depends on specifics in the source, not on general knowledge alone.

Per type:
- straightforward: the listed evidence chunks state the reference answer.
- semantic: as straightforward, and the question avoids the distinctive terms of the source
  (command names, option names, error strings, product names) unless unavoidable.
- multi: the answer needs facts from both threads; each thread alone is not enough; the
  evidence includes at least one chunk from each thread and together they state the answer.
- unanswerable: the source shown is NOT in the index. Confirm the index does not contain
  the answer anyway. Run at least three different searches with each tool:
    RAG_BENCH_ENV_FILE="C:/Users/HOMELA~1/AppData/Local/Temp/claude/C--Users-Home-Laptop/cdca6ab0-f36b-482f-ad74-c7003f8734ab/scratchpad/qdrant.env" python -I "C:/Users/Home Laptop/rag-bench/scripts/dense_search.py" "<query>" 20
    python -I "C:/Users/Home Laptop/rag-bench/scripts/kw_index.py" search "<keywords>" 20
  Drop the item if any result states the answer (or an equivalent answer to the question).
  Keep it only if the question is still a reasonable thing to ask this knowledge base.

Small fixes (a clearer word, a tighter answer) are allowed and must be written out in
full. Anything bigger: drop.

## Amendment sent to all verifiers mid-run (2026-10-28)
While the HNSW index was still being built on the 1-vCPU cluster, dense searches took
minutes or timed out. Verifiers were told: do not wait on dense search; rely on at least
three keyword searches for unanswerable items; if a dense search fails, set
"verdict": "recheck" instead of keep. Recheck items get a second pass with dense search
after the index is green (outputs data/verify/out/x_*.jsonl, which sort after v_ and w_ and so override).
