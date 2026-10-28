You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 6fe2c3cc: How can I check whether a running Linux kernel supports io_uring by looking at its symbol list, and what name prefix do system calls conventionally have in that list?
- 9564c9e8: How can an email recipient avoid open-tracking by services like Bananatag that insert a tracking pixel into messages?
- 7bbe18c6: What is the term for a really big source code commit or patch that is so large no one can review it?
- 51617a30: How can I start a program automatically when CPU percent reaches a certain level on Windows?
- d3ec2537: Processing an SSAS Tabular model attached to an Analysis Services instance fails on impersonation. Which ImpersonationMode value is not supported for such databases?
- 51bc0b0d: I keep contacts for a small church group in one wide table with a column per detail. Should I break out separate tables for things like addresses and churches?
- 1f48f45d: kubectl says the server could not find the requested resource. What kubectl-to-cluster version rule should I check, and what are the fixes?
- f240ea93: Why does Yubico not let users supply their own key material to an authenticator, in terms of what its attestation can promise?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.