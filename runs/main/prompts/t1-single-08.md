You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 334e59d0: On a Cisco chassis switch with removable line cards, what global configuration command turns one card fully off instead of just restarting it?
- baf75687: How much in Azure credits could a startup qualify for through Microsoft's BizSpark programme to host an application?
- 80d3dfe9: Which profiling tool did one answerer use as part of an application to profile SQL Azure?
- eeae4fd2: I granted a login the server-wide right to run bulk file loads, but it still can't load rows into my target database in SQL Server. What other permission does it need there?
- ce316550: If I can't use Let's Encrypt as my certificate authority, which ACME challenge types can Ansible's acme_certificate module handle?
- 4b263acd: In the fish shell, how do I find and rerun an old command when I only remember part of it?
- 4adb11e5: How can an email recipient avoid open-tracking by services like Bananatag that insert a tracking pixel into messages?
- 6f55e514: Besides encrypting traffic, what does a CA-signed web server certificate establish, and which certificate should an ordinary site that is not a bank buy?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.