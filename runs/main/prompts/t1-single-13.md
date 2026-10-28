You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 3eacf8ca: Why do many hardware controllers, such as wireless adapters or GPUs, need their firmware supplied again at every power-on, and which host component does that loading?
- ad57e5bf: I forward web traffic through a router to an internal server, but once I apply an outbound filter on the router interface, external clients' HTTPS requests get no response. Why?
- b632cca9: What workaround is suggested when a new RDS MySQL 8.0.16 instance has an empty ST_SPATIAL_REFERENCE_SYSTEMS table?
- 8e8d6efe: In a SQL Server availability group, how can I stop reporting-only accounts from ever logging into the current writable node even when their connection strings lack read-only intent?
- f691f6e4: A host answers telnet fine, but an openssl TLS connection to it fails with "No route to host". The name has both A and AAAA records. What is the likely cause?
- 3ec5a41c: People tell me to code against abstractions, but making a separate abstract type for every class seems absurd. In what broader sense can that advice be applied beyond language keywords?
- 620b523b: Why did creating a Truecrypt hidden partition delete the original data on the drive?
- be3a7408: I want agents' Cisco phones to auto-dial a customer list. What is this feature called, and which Cisco product is the cheaper, simpler option for it?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.