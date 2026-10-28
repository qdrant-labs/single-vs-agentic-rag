You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- c870bd00: Why is installing Proxmox on top of an existing Ubuntu server a bad idea?
- b443964d: In the one-line form if [ "a" == "a" ] ; then echo "true" ; fi, what are if and then technically in the shell, and which comparison operator is more portable than ==?
- 7e344be1: How can I raise PostgreSQL's 32 TB maximum table size, and what limit do I get?
- d2c6feb8: Can I run a graphical app in Docker on a headless server by mounting the X11 libraries from a separate container through a volume?
- 1d72ddc8: After finding a reflected XSS hole on my site, where can I look for evidence that it was exploited, and what can a simple script do with a visitor's session?
- 31ebc682: Of the 4,096 possible values in the 12-bit tag field on Ethernet trunks, why can only 4,094 be used, and what are the two excluded values for?
- e46e8661: I couldn't build a PHP opcode cache extension because the temp directory is mounted without execute permission and I can't remount it. What workaround did one person use?
- d6147b4e: Does the Cisco 2504 WLC support LAG, and what is required to enable it?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.