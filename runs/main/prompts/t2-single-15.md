You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 8f4e876e: In a Jenkins scripted pipeline, how do I list the commit messages and authors of every build since the last successful one?
- 007e759a: Besides provider documentation, what general way works to find out the attributes of any Terraform object you can refer to in an expression?
- c3d62436: When I poll a router with a command-line walk tool on Ubuntu, I only see long dotted numeric identifiers instead of readable names. How do I fix that?
- 726799db: Which ImageMagick option, together with which escape sequence, writes an image's own filename as text in a corner of the image?
- 9df172e0: Why is encapsulating translations in a separate normalized table better than adding a column for each language?
- 8d8254ac: I'm designing storage for a chat bot's access rights, where users can have rights per channel and also globally. How should I lay out the tables?
- a3bd82c7: What habits help design patterns emerge pragmatically instead of being forced onto code, and what is the main lasting benefit of knowing pattern names such as Strategy or Builder?
- ddd4d90a: How much in Azure credits could a startup qualify for through Microsoft's BizSpark programme to host an application?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.