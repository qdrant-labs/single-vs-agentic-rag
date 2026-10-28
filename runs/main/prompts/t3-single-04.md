You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- a61b476f: Which weakness of SHA-2 is the reason PBKDF2 is often built on HMAC, and how far does repeated iteration shrink the hash space of a 256-bit hash?
- d86cd2dc: To decouple CI tooling data from servers with an immutable architecture, which tools are suggested for static analysis, artifact storage, base images and deployment?
- c962c64c: How can users change their password without re-encrypting all their data, and if the key comes from a passphrase via PBKDF2 for an encrypt-then-MAC scheme, how many bits are derived and how are they used?
- d9cc704d: What must a VoIP customer and provider maintain so that E911 emergency calls carry more than just a street address?
- 9126b948: A host answers telnet fine, but an openssl TLS connection to it fails with "No route to host". The name has both A and AAAA records. What is the likely cause?
- 8017bcb0: What does the construct bash <<(curl -s http://xxx.com) actually do?
- 8c66b4ca: What GitHub practices did one company adopt for ISO27001 certification, without moving to GitHub Enterprise?
- 9ffbb36e: In TCP as defined in RFC 793, what inequality must hold for an incoming ACK to count as an acceptable acknowledgment?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.