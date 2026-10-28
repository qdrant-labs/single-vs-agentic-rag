You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 76a2f0c9: Burp Suite shows a garbled response body whose headers say Content-Encoding: br. What workaround is suggested?
- 6ae81c2d: Why is it unsafe to store the XSRF value inside an anonymous JavaScript function?
- 178cc80e: In bash, how do I pass a wget user-agent option containing spaces from a variable correctly, and what is a safer alternative to eval for filling variables into a stored template string later?
- 2edc9775: After renaming my Windows server, the Oracle listener won't start. How do I find the file to edit and what do I change?
- 9bc775ec: What must a VoIP customer and provider maintain so that E911 emergency calls carry more than just a street address?
- a12a1e09: What happens to transactional replication data if the distribution agent is stopped, and what risk does a long delay carry?
- 022464c7: I want to see which of my SQL Server databases are busiest right now. Which built-in view could I query, and what session id threshold excludes internal sessions?
- e61783a8: To avoid programming by coincidence, how much new code should I add between test runs, according to the advice on shortening the edit/compile/test cycle?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.