You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 3175fafe: Of the 4,096 possible values in the 12-bit tag field on Ethernet trunks, why can only 4,094 be used, and what are the two excluded values for?
- 5a8adc18: I want agents' Cisco phones to auto-dial a customer list. What is this feature called, and which Cisco product is the cheaper, simpler option for it?
- 8d037840: Does all of Chrome's telemetry use a unique ID to tie activity to an anonymised user?
- f398377f: Edits I make to the server's crontab keep getting overwritten every time we deploy our Rails app. What is overwriting them?
- de938a1e: On a Junos switch, one access port faces a customer who sends tagged frames. How can I map the customer's VLANs 41-42 into one provider VLAN and 51-52 into another on that single port?
- f34d4cca: What command clamps the MSS for TCP over IPv6 on Junos?
- 4d8370bc: I forward web traffic through a router to an internal server, but once I apply an outbound filter on the router interface, external clients' HTTPS requests get no response. Why?
- ced13ec3: How can I raise PostgreSQL's 32 TB maximum table size, and what limit do I get?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.