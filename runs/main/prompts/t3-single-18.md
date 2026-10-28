You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 49cff93c: How many key-derivation iterations does a KeePass database use by default, and what extra step makes a cloud-stored copy of the database harder to breach?
- afb56342: I accidentally posted the barcode I scanned to set up my phone's rotating six-digit login codes. Is it still safe to use, and how do I fix it?
- 370c0f90: How can I check whether a running Linux kernel supports io_uring by looking at its symbol list, and what name prefix do system calls conventionally have in that list?
- 050c0be8: My CloudWatch anomaly detection alarms fire false positives every time daylight saving time shifts. Would switching my timers to UTC make them less likely?
- f9e75396: When a class only supports a single observer registered after construction, how should that limit be handled so allowing multiple observers later changes only the implementation?
- e7f33506: Which profiling tool did one answerer use as part of an application to profile SQL Azure?
- 7ce466df: Which gcc options produce annotated assembly to read when learning how code maps to machine instructions, and why are CPU opcode values not chosen arbitrarily?
- 519e2ea1: Why does GNU tr mangle UTF-8 characters, and what must a Perl one-liner add so tr/// with fullwidth letters in its source code works, given that -C alone does not help?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.