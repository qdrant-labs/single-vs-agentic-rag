You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 9aaaf3a3: Which ImageMagick option, together with which escape sequence, writes an image's own filename as text in a corner of the image?
- 2467e670: To get a newer GCC without upgrading the whole distribution, where does a self-built compiler install to avoid clashing with the distro's, and what pin priorities does the suggested apt preferences file for pulling gcc-4.7 from wheezy onto Debian Squeeze give squeeze and wheezy?
- caba4b07: What is the term for a really big source code commit or patch that is so large no one can review it?
- b7329144: A SELECT joining a big session table to a smaller latest-session table with ORDER BY and LIMIT 500 is slow when few rows match. What query rewrite was suggested?
- 08255158: Why must a load balancer rewrite the IP address in the node's response before forwarding it to the client?
- 6376439e: With Apache's mod_bw, how can I limit files over 1MB to 200kb/s?
- 4972148a: When sending a for loop to a remote host over ssh, why do the loop variables come out empty if the command is in double quotes, and what can you do when the remote login shell is tcsh?
- 2fd6df67: Is it safe to tell everyone which password hash my site uses if I publish its source code, and what alternative is suggested if the site owner is uneasy about public code?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.