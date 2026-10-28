You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 296f9893: Why does Python allow 1 + 1.0 but not 1 + "1" when it avoids implicit conversions?
- 6dd25fd3: When a class only supports a single observer registered after construction, how should that limit be handled so allowing multiple observers later changes only the implementation?
- 5ac7f601: When automating build, deploy-to-dev and deploy-to-prod on my CI server, what rule of thumb decides where to split the work into separate jobs?
- b0f8a7c1: To get a newer GCC without upgrading the whole distribution, where does a self-built compiler install to avoid clashing with the distro's, and what pin priorities does the suggested apt preferences file for pulling gcc-4.7 from wheezy onto Debian Squeeze give squeeze and wheezy?
- 8c725be7: In a SQL Server deadlock graph, an IX lock request is blocked by an SIU page lock after a SELECT with UPDLOCK. What turns the IU page lock into SIU?
- 24065a54: When building a writable snapshot overlay on a read-only loop device so LVM will activate it, how do you stop LVM complaining about duplicate PVs, and how can you check how full the overlay is?
- 14be42f1: Which escape sequence request makes a terminal type back its Primary Device Attributes string, and which status-report query makes it reply with a sequence that bash can bind to inject text?
- e8d3eb5d: In Packet Tracer with a serial DCE cable between two routers, which router becomes the DCE end and how can I identify it on the link?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.