You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d6c73b65: What must a VoIP customer and provider maintain so that E911 emergency calls carry more than just a street address?
- e9ba7a01: How can I check the free memory of a Jenkins build executor?
- c1e75c2b: How do I concatenate many files without exceeding the command line length limit, and what constraint applies to files when using device mapper to build a virtual concatenated file?
- 540ac648: In an Ansible playbook run against localhost, how can I print the directory ansible-playbook was invoked from on the control host?
- 30f21208: In the fish shell, how do I find and rerun an old command when I only remember part of it?
- 54375fcd: After renaming my Windows server, the Oracle listener won't start. How do I find the file to edit and what do I change?
- cc7b238e: Which gcc options produce annotated assembly to read when learning how code maps to machine instructions, and why are CPU opcode values not chosen arbitrarily?
- 6fcfdb52: How do you configure per-IP bandwidth management on a SonicWall so each user gets guaranteed and maximum speeds?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.