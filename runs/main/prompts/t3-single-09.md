You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 2250c893: Why do many hardware controllers, such as wireless adapters or GPUs, need their firmware supplied again at every power-on, and which host component does that loading?
- 19634af6: On a Junos switch, one access port faces a customer who sends tagged frames. How can I map the customer's VLANs 41-42 into one provider VLAN and 51-52 into another on that single port?
- 4e86b9f5: My PHP web service parses XML sent by browsers, and I'm worried the parser could be tricked into reading local files or probing internal hosts. Which PHP call mitigates this?
- 87920ec9: I want agents' Cisco phones to auto-dial a customer list. What is this feature called, and which Cisco product is the cheaper, simpler option for it?
- 3e9a9389: Which kernel release did a brand-new Radeon HD 6450 need for full resolution on Fedora, and if the boot then freezes after X was reconfigured, which file should be deleted and which log checked?
- c000ef26: What free toolset is recommended on Linux for collecting and reporting NetFlow data, and which free collector runs on Windows but needs recompiling because its supplied build is limited?
- c65fba25: In SQL Server, what permission benefit is lost by spreading related code across separate databases, and what kind of data requirement forces tables to share one database?
- aa5f8d58: In Packet Tracer with a serial DCE cable between two routers, which router becomes the DCE end and how can I identify it on the link?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.