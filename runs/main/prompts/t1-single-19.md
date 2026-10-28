You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- e9506c7c: I want to see which of my SQL Server databases are busiest right now. Which built-in view could I query, and what session id threshold excludes internal sessions?
- 6871d523: What is the next-best way to give RRAS VPN clients on a Windows server DHCP addresses from their own scope, since an Amazon VPC's DHCP options cannot be overridden?
- 3147f681: Why do many web API designers still put the release number in the endpoint path despite purists' objections?
- 1af3bdce: In Postgres, a partial index is ignored when the query has a big IN list. Which release removes this limitation, and what element limit applied before?
- cefe17d1: How can a developer deal with accumulating technical debt without asking a non-technical manager for a big-bang rewrite: what goes quietly into every estimate, and where should larger changes be made?
- 764fa2a2: My web server log shows GET requests mentioning cmd.exe and System.Net.WebClient that returned 404. What do they indicate, and why do people send requests for pages that don't exist?
- fecdfa3e: Why might a Unix system deliberately leave /usr/local out of root's PATH?
- e748c534: In PostgreSQL versions before 9.3, how can I pick 10 random rows with replacement from a table?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.