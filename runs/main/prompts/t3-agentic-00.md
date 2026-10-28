You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 1e0568aa: How can rsync keep deleted or overwritten files in a separate directory instead of discarding them, and how can I delete from one directory every file that exists at the same relative path in another?
- 6cf0f8a2: What does the construct bash <<(curl -s http://xxx.com) actually do?
- bd121a58: In an Ansible playbook run against localhost, how can I print the directory ansible-playbook was invoked from on the control host?
- 6d74d648: I administer Microsoft's database server from an Apple laptop, where the old GUI tracing tool doesn't run. Is there an open source script that finds the most resource-hungry queries from the plan cache without starting a trace?
- f3fa60d6: I have a prebuilt test executable with no source code and want to package it as a container. What goes in the build definition, and how long will the container live?
- 58df8b3c: How can an email recipient avoid open-tracking by services like Bananatag that insert a tracking pixel into messages?
- fc742c3a: How can I start a program automatically when CPU percent reaches a certain level on Windows?
- 8e24a14f: Which weakness of SHA-2 is the reason PBKDF2 is often built on HMAC, and how far does repeated iteration shrink the hash space of a 256-bit hash?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.