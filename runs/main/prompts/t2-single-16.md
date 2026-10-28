You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d1b9a03a: To decouple CI tooling data from servers with an immutable architecture, which tools are suggested for static analysis, artifact storage, base images and deployment?
- f1533433: Why do exported variables from a shell script vanish after I run it, and what file permission difference is there between running it directly and passing its path to an interpreter?
- c8d6269a: I want to see which of my SQL Server databases are busiest right now. Which built-in view could I query, and what session id threshold excludes internal sessions?
- bf498304: Why is it unsafe to store the XSRF value inside an anonymous JavaScript function?
- 51d80f71: Why does piping grep into xargs dirname inside find -exec print a usage message for files that don't match, and how can bash make a shell function available to find -exec?
- cc68f7e1: In my WPF app a base view model has one handler that picks the action from a string in the XAML. What problem arises if a child class must change just one action's behavior?
- 9f8236b2: Which build task should be used in Azure DevOps for a .NET Core 3.0 app hosted on Ubuntu?
- 44e8a9ea: How do I let a parameter choose between different multi-column sort orders in a SQL Server ORDER BY, and why does it fail with a conversion error when the sorted columns have different data types?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.