You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 8cb52e43: In my WPF app a base view model has one handler that picks the action from a string in the XAML. What problem arises if a child class must change just one action's behavior?
- a1c22e66: What does the construct bash <<(curl -s http://xxx.com) actually do?
- 74b0f044: A tenant changed their apartment's network setup on a fiber line they had been told was capped at 100 down and 50 up. What speeds did they then measure?
- 33c1d6fb: Why must a load balancer rewrite the IP address in the node's response before forwarding it to the client?
- 24efc2ff: A MySQL query filters on a very lopsided col1 = 1, adds a date range and LIKE on col2, and orders by date DESC with a small LIMIT. What single composite index is suggested on InnoDB?
- 8b65d9e0: Why is the MAC address bb:bb:bb:bb:bb:bb treated as a non-unicast address?
- bf35b57e: How does Sonatype Nexus 3 Pro provide high availability for the artifact repository, and what are its mechanisms collectively called?
- 9e188473: After finding a reflected XSS hole on my site, where can I look for evidence that it was exploited, and what can a simple script do with a visitor's session?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.