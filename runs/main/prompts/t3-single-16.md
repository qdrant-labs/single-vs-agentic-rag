You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- c6d94ec5: In a SQL Server availability group, how can I stop reporting-only accounts from ever logging into the current writable node even when their connection strings lack read-only intent?
- 1327e4b5: Burp Suite shows a garbled response body whose headers say Content-Encoding: br. What workaround is suggested?
- 0228baee: With psql run with ON_ERROR_STOP on and --single-transaction, an error in an \include file stops the script but nothing is rolled back. What is the workaround?
- d0f14fac: In SQL Server, which tools help find where the performance problems lie among a set of 35 suspect stored procedures?
- eaaa9532: Why is it unsafe to store the XSRF value inside an anonymous JavaScript function?
- f45bab96: What workaround is suggested when a new RDS MySQL 8.0.16 instance has an empty ST_SPATIAL_REFERENCE_SYSTEMS table?
- 3e95ab36: Why does Python allow 1 + 1.0 but not 1 + "1" when it avoids implicit conversions?
- db12712c: Which HISTCONTROL values make bash skip commands that start with a space when saving history?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.