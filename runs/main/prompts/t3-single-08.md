You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d1d4be2e: Why do many web API designers still put the release number in the endpoint path despite purists' objections?
- 46387cf3: In my WPF app a base view model has one handler that picks the action from a string in the XAML. What problem arises if a child class must change just one action's behavior?
- c2c12860: Can a database attached to a newer SQL Server release be moved back to an older release if I keep the same compatibility level?
- f0b1b8cb: Is it supported to configure BFD on a virtual-template or dialer interface on Cisco IOS-XE 3S?
- 7caf2d03: Why does piping grep into xargs dirname inside find -exec print a usage message for files that don't match, and how can bash make a shell function available to find -exec?
- 620fe319: Which standard number was the LLDP-MED extension published under, and by which organization and when?
- 20fdfb56: Besides provider documentation, what general way works to find out the attributes of any Terraform object you can refer to in an expression?
- 54f4f247: Why is the MAC address bb:bb:bb:bb:bb:bb treated as a non-unicast address?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.