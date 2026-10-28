You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 88c61d47: Why do many languages specify a fixed stack size for each thread?
- f0ef3613: kubectl says the server could not find the requested resource. What kubectl-to-cluster version rule should I check, and what are the fixes?
- d52239bd: After renaming my Windows server, the Oracle listener won't start. How do I find the file to edit and what do I change?
- b375bec0: Which weakness of SHA-2 is the reason PBKDF2 is often built on HMAC, and how far does repeated iteration shrink the hash space of a 256-bit hash?
- 648ea954: Why does Yubico not let users supply their own key material to an authenticator, in terms of what its attestation can promise?
- 323637dc: I have a prebuilt test executable with no source code and want to package it as a container. What goes in the build definition, and how long will the container live?
- 6634e38f: I accidentally posted the barcode I scanned to set up my phone's rotating six-digit login codes. Is it still safe to use, and how do I fix it?
- 23653c8a: Why is installing Proxmox on top of an existing Ubuntu server a bad idea?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.