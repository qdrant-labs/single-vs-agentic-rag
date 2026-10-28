You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- f5bfe921: With Apache's mod_bw, how can I limit files over 1MB to 200kb/s?
- 369af575: To avoid programming by coincidence, how much new code should I add between test runs, according to the advice on shortening the edit/compile/test cycle?
- d397a980: In SQL Server, how can I write decimal multiplication and division so the result's precision and scale stay predictable, and what formula gives the result scale of a division before it is capped?
- 58516057: A SELECT joining a big session table to a smaller latest-session table with ORDER BY and LIMIT 500 is slow when few rows match. What query rewrite was suggested?
- 89398066: How can I raise PostgreSQL's 32 TB maximum table size, and what limit do I get?
- 9bf6d46f: How many key-derivation iterations does a KeePass database use by default, and what extra step makes a cloud-stored copy of the database harder to breach?
- b2350846: How do I stop Outlook repeatedly prompting for credentials over RPC over HTTPS, given Remember my Password doesn't cover the front-end proxy server?
- 9800f276: Why do many languages specify a fixed stack size for each thread?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.