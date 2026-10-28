You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- b0b3695c: Why is the MAC address bb:bb:bb:bb:bb:bb treated as a non-unicast address?
- bf62310d: My CloudWatch anomaly detection alarms fire false positives every time daylight saving time shifts. Would switching my timers to UTC make them less likely?
- 48e92052: Why is it considered a code smell to have a CompanyDao use an EmployeeDao internally?
- 50de0093: I'm considering enabling Google's experimental faster web transport protocol on my TLS site. Which known attack on compressed headers and cookies is the security concern?
- 57f130e6: I couldn't build a PHP opcode cache extension because the temp directory is mounted without execute permission and I can't remount it. What workaround did one person use?
- ab86397c: To get a newer GCC without upgrading the whole distribution, where does a self-built compiler install to avoid clashing with the distro's, and what pin priorities does the suggested apt preferences file for pulling gcc-4.7 from wheezy onto Debian Squeeze give squeeze and wheezy?
- 6ea8028b: In PostgreSQL versions before 9.3, how can I pick 10 random rows with replacement from a table?
- 36e0dcae: In SQL Server, which tools help find where the performance problems lie among a set of 35 suspect stored procedures?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.