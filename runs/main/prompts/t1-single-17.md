You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- a15bf8d7: In bash, how do I pass a wget user-agent option containing spaces from a variable correctly, and what is a safer alternative to eval for filling variables into a stored template string later?
- 0f53e0e7: I applied IP-based packet filter rules to a switch port carrying several tagged VLANs and nothing is filtered. Why is that, and where do the rules belong?
- 607bbd4b: In a layered GUI/BLL/DAL project, why shouldn't CRUD methods be built into the User object, and how should data access classes get their IDatabaseService?
- 0a5fa462: What GitHub practices did one company adopt for ISO27001 certification, without moving to GitHub Enterprise?
- 9a29312d: I'm new to automating manual operations work. What basic starter toolchain is suggested for spinning up developer VMs, managing server configuration, running the build and deploy pipeline, and containerizing apps?
- 984a7998: When sending a for loop to a remote host over ssh, why do the loop variables come out empty if the command is in double quotes, and what can you do when the remote login shell is tcsh?
- 054d9779: I'm drawing a modelling diagram for a codebase that mixes classes with free-standing helper routines doing I/O. How could I show those routines without cluttering the picture?
- 3b0a5724: SSH to my VPS fails with "Server refused to allocate pty". What commands re-create the pty devices, and which command regenerates the Ubuntu initramfs where devpts gets mounted?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.