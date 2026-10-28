You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- e1db4abd: Which profiling tool did one answerer use as part of an application to profile SQL Azure?
- 3e9a5c8a: Back in the 0.19 days of a popular Lucene-based search server, which codec compressed stored data by default, and which one was planned to come later?
- 356d2273: How can rsync keep deleted or overwritten files in a separate directory instead of discarding them, and how can I delete from one directory every file that exists at the same relative path in another?
- da294a5a: Besides avoiding rounding on every query, what index-related benefit comes from storing timestamps with lower precision in PostgreSQL?
- c360ce70: How can a developer deal with accumulating technical debt without asking a non-technical manager for a big-bang rewrite: what goes quietly into every estimate, and where should larger changes be made?
- 118f504d: Why must a load balancer rewrite the IP address in the node's response before forwarding it to the client?
- 246ee54b: For Merkle-Damgard hashes like SHA-1, why does revealing h(P+B) give an attacker no extra information beyond h(P)?
- a4803430: To script a login to criticker.com with curl and then fetch protected pages, which URL should the credentials be posted to?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.