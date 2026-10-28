You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 5a2793d7: Which standard number was the LLDP-MED extension published under, and by which organization and when?
- c7180874: Which GNU screen commands switch on background colour erase for a window and for the default of all new screens, and when did tmux implement that capability?
- 55f769ba: Pulse Secure's client UI on Ubuntu 22.04 can't download its Chromium Embedded Framework. Which script and argument install it manually, and how do I verify it?
- b2fe6195: I keep contacts for a small church group in one wide table with a column per detail. Should I break out separate tables for things like addresses and churches?
- b12efaef: In SQL Server, which tools help find where the performance problems lie among a set of 35 suspect stored procedures?
- 2036738f: With psql run with ON_ERROR_STOP on and --single-transaction, an error in an \include file stops the script but nothing is rolled back. What is the workaround?
- 1ce4840b: kubectl says the server could not find the requested resource. What kubectl-to-cluster version rule should I check, and what are the fixes?
- dc8c9ff8: Why does Python allow 1 + 1.0 but not 1 + "1" when it avoids implicit conversions?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.