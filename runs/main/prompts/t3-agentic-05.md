You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 6bf0ce01: In SQL Server, how can I write decimal multiplication and division so the result's precision and scale stay predictable, and what formula gives the result scale of a division before it is capped?
- b785ebae: In my WPF app a base view model has one handler that picks the action from a string in the XAML. What problem arises if a child class must change just one action's behavior?
- 0edb0518: Why is installing Proxmox on top of an existing Ubuntu server a bad idea?
- 4ac58ae1: After upgrading my Linux desktop environment, opening a link from another app no longer switches me to the workspace where my browser window lives. Which window behavior setting restores that?
- 0fd83618: Since which SQL Server version is the built-in Windows Administrators group not made sysadmin by default, and if no sysadmin login remains, does the Dedicated Administrator Connection let you recover one?
- bdb89d45: In a CircleCI 2.0 config, how do I make a private deploy key I uploaded in the dashboard usable inside a job?
- bb2c91fd: Is it safe to tell everyone which password hash my site uses if I publish its source code, and what alternative is suggested if the site owner is uneasy about public code?
- fc0e7371: A MySQL query filters on a very lopsided col1 = 1, adds a date range and LIKE on col2, and orders by date DESC with a small LIMIT. What single composite index is suggested on InnoDB?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.