You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 4b8b5f08: Back in the 0.19 days of a popular Lucene-based search server, which codec compressed stored data by default, and which one was planned to come later?
- 61da8f49: After upgrading my Linux desktop environment, opening a link from another app no longer switches me to the workspace where my browser window lives. Which window behavior setting restores that?
- a50f0bc9: Which escape sequence request makes a terminal type back its Primary Device Attributes string, and which status-report query makes it reply with a sequence that bash can bind to inject text?
- 80dc9352: When I poll a router with a command-line walk tool on Ubuntu, I only see long dotted numeric identifiers instead of readable names. How do I fix that?
- ab89343a: In a code review dispute over assigning a comparison result to a boolean field like obj.NeedsChange, what small readability tweak was suggested as a compromise?
- 2967f8cb: On a Windows web server, if I shut down a site while a page request is still running, does that in-flight request run to completion first?
- 689fcb4f: Two distros share one swap partition. What must be done to the swap space at boot for sharing to work, and why is hibernating one install and then booting the other dangerous?
- b12fdc0f: On a pair of Cisco Nexus switches sharing a multi-chassis port channel, must the trunk's allowed list of Layer 2 segments match on both switches to avoid the channel being suspended?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.