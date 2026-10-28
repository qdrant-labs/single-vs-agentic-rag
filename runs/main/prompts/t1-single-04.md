You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- eaf28271: To decouple CI tooling data from servers with an immutable architecture, which tools are suggested for static analysis, artifact storage, base images and deployment?
- 1899b211: I have an executable script written in the classic Unix pattern-scanning language, and flags like -h are swallowed by the interpreter. With GNU coreutils 8.30 or newer, what shebang passes them through to the script?
- 2bb22c07: Why would adding a random per-user value before hashing not have stopped a big social network's leaked password hashes from being cracked, and what should they have used?
- c2c6834c: How can I fill a named volume with generated static files before starting my web server with docker-compose, without leaving an idle generator container behind afterwards?
- e5f8ca42: Besides avoiding rounding on every query, what index-related benefit comes from storing timestamps with lower precision in PostgreSQL?
- 16949c75: In PostgreSQL, how does the efficiency of the GIN and GiST indexes used on jsonb columns compare with a plain b-tree index on an ordinary column?
- d4830e80: My Linux resolv.conf shows an unfamiliar DNS server, 46.161.40.29. How can I tell whether my router is the compromised device without logging into the router?
- 363ee60b: How can I start a program automatically when CPU percent reaches a certain level on Windows?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.