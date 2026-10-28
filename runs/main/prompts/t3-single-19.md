You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 59e6a44a: Which pipeline prints only the grand total disk usage of a set of *.sql files, and which one lists directories sorted by size, largest first, in human-readable units?
- 987da246: How do you configure per-IP bandwidth management on a SonicWall so each user gets guaranteed and maximum speeds?
- e40fecd1: To start a document database server in the background so it survives logout, what is the argument for using the server's own built-in backgrounding option over a shell wrapper that ignores hangups?
- e94afbb4: How can a developer deal with accumulating technical debt without asking a non-technical manager for a big-bang rewrite: what goes quietly into every estimate, and where should larger changes be made?
- b7f355b7: People tell me to code against abstractions, but making a separate abstract type for every class seems absurd. In what broader sense can that advice be applied beyond language keywords?
- b02b5a9e: Where can I find open scripts for hardening Enterprise Linux servers to a US Defense Department security guideline, including one that builds a pre-hardened installer image?
- 931c2c03: A MySQL query filters on a very lopsided col1 = 1, adds a date range and LIKE on col2, and orders by date DESC with a small LIMIT. What single composite index is suggested on InnoDB?
- 529816df: My container builds keep re-downloading external binaries and libraries from outside sources on every run. What kind of tool can I host to store those dependencies locally, and which two popular ones have free open source editions?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.