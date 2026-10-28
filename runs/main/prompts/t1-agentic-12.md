You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- c5b959f2: Which HTTP method is suggested as the simplest way to fire a non-RESTful action such as a reload, and what must the response metadata avoid when that method is used to propagate a signal?
- 5d0fc096: In a SQL Server deadlock graph, an IX lock request is blocked by an SIU page lock after a SELECT with UPDLOCK. What turns the IU page lock into SIU?
- 0208225b: Why is the MAC address bb:bb:bb:bb:bb:bb treated as a non-unicast address?
- b014f05a: On SQL Server 2008 R2 or 2012, how can I quickly check whether my application relies on features slated for removal?
- a0422471: In a Jenkins scripted pipeline, how do I list the commit messages and authors of every build since the last successful one?
- e0c877d2: Which build task should be used in Azure DevOps for a .NET Core 3.0 app hosted on Ubuntu?
- e54940b7: Can a child process change its parent's environment variables, and if I must alter a running process's environment anyway, which debugger sequence is suggested?
- efc56c13: In my WPF app a base view model has one handler that picks the action from a string in the XAML. What problem arises if a child class must change just one action's behavior?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.