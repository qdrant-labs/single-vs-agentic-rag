You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- b54193cc: In a layered GUI/BLL/DAL project, why shouldn't CRUD methods be built into the User object, and how should data access classes get their IDatabaseService?
- deef71ff: In a CircleCI 2.0 config, how do I make a private deploy key I uploaded in the dashboard usable inside a job?
- eb671727: How do I stop Outlook repeatedly prompting for credentials over RPC over HTTPS, given Remember my Password doesn't cover the front-end proxy server?
- 849a6e2e: How do I let a parameter choose between different multi-column sort orders in a SQL Server ORDER BY, and why does it fail with a conversion error when the sorted columns have different data types?
- 5dc20c61: To avoid programming by coincidence, how much new code should I add between test runs, according to the advice on shortening the edit/compile/test cycle?
- 792a9109: On SQL Server 2008 R2 or 2012, how can I quickly check whether my application relies on features slated for removal?
- f088cff6: In SQL Server, how can I write decimal multiplication and division so the result's precision and scale stay predictable, and what formula gives the result scale of a division before it is capped?
- 2c982161: My window manager doesn't see a timezone variable I exported in ~/.bashrc. Which file should I define it in instead, and which shells never read that file?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.