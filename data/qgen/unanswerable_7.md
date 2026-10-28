### item Userverfault-846478
Site: serverfault | Thread title: Why does Ubuntu want to reboot so often after installing updates?
Ubuntu will suggest a restart after the update if it can't restart the affected components in a meaningful way.
In a nutshell:
Things like editors or command line tools don't need any kind of restart, they just get replaced.
Services like a web server might need to be restarted by itself.

Other things like the kernel or the core libc that affect everything will require a reboot, as they can't be easily replaced in a running system (NB: Things like ksplice exist that allows to patch some things in a running kernel).

But even with kernel updates without ksplice you don't strictly need to restart the system in every case - you have to carefully read the update notes to check if you are affected by the fixed bug(s) - if not, it's often safe to ignore this until the next update or regular maintenance cycle.

### item Usoftwareengineering-328812
Site: softwareengineering | Thread title: Can't grasp programming design patterns
Software Design patterns are well-known solutions to well-known problems. The way you understand them is by learning the patterns, understanding how they work, and knowing when it is appropriate to apply each one to your software design.
The way you learn software design patterns is by studying them, one at a time. It's a continuous education process. If you want to reduce the learning footprint, study those patterns that relate directly to the technologies that you are currently using.

Some important things to know about design patterns:
Some design patterns are architectural in nature. MVC and MVVM are examples of such patterns. You use such patterns when you need the organizational and structural benefits that they provide.

Some design patterns are workarounds for deficiencies in programming languages. You won't need these patterns if you use a more expressive programming language, but often you don't get to make this choice. A majority of the GoF patterns are in this category.
Use a software pattern only when you're trying to solve the problem that the pattern is specifically designed to solve. If you're writing an application by stitching together software patterns, you're doing it wrong.

There isn't an existing software pattern for every computing problem in existence. Were that the case, programming would merely be a pattern-matching exercise.
Some patterns are actually anti-patterns. The additional complexity that these patterns introduce outweighs the benefits that they provide. You'll have to decide for yourself, on a pattern-by-pattern basis, which of these patterns you'll avoid.

### item Uunix-357847
Site: unix | Thread title: readline: does non-incremental search offer anything that incremental search doesn't?
I actually found a really nice feature of non-incremental search. By default, Readline binds:
M-n to non-incremental-forward-search-history
M-p to non-incremental-reverse-search-history
These kinda suck, IMHO. But Readline also has another pair of non-incremental search functions, with no default bindings:
history-search-forward
history-search-backward
Search forward/backward through the history for the string of characters between the start of the current line and the point.

These are actually pretty useful. I've bound them to M-n and M-p, replacing the default non-incremental functions.
If I've started typing a command and decide to search for a matching history entry, I can tap Escape p (since I don't actually have a Meta key).
Repeated taps cycle farther back and Escape n cycles forward again.

### item Udba-20117
Site: dba | Thread title: Oracle: How do I query a Hierarchical table?
FrusteratedWithFormsDesigner has the right direction(+1). Here is what I think you are looking for specifically.
CREATE OR REPLACE VIEW BuildingSubs AS
 SELECT connect_by_root location "Building", location "SubLocation"
 FROM some_table l
 START WITH l.Location IN 
 (
 SELECT location FROM
 (
 SELECT level MyLevel, location FROM some_table 
 START WITH parent IS NULL 
 CONNECT BY PRIOR location=parent
 )
 WHERE MyLevel=3 
 )
 CONNECT BY PRIOR l.location = l.parent;
select * from BuildingSubs;

Building SubLocation 
-------------------- --------------------
BLDG-01 BLDG-01 
BLDG-01 Basement 
BLDG-01 Room B-002 
BLDG-01 Floor-01 
BLDG-01 Room 1-001 
BLDG-02 BLDG-02 
BLDG-03 BLDG-03 
Grounds Grounds
The view accomplishes all three goals. You can query it for a building to find everything it contains and you can query it for a sub-location to find what building it is in.
drop table some_table;
create table some_table (Location Varchar2(20), Parent Varchar2(20));

insert into some_table values ('Org.
Name',NULL);
insert into some_table values ('MAINCAMPUS','Org.

Name');
insert into some_table values ('BLDG-01','MAINCAMPUS');
insert into some_table values ('BLDG-02','MAINCAMPUS');
insert into some_table values ('BLDG-03','MAINCAMPUS');
insert into some_table values ('Grounds','MAINCAMPUS');
insert into some_table values ('Floor-01','BLDG-01');
insert into some_table values ('Basement','BLDG-01');
insert into some_table values ('Room B-002','Basement');
insert into some_table values ('Room 1-001','Floor-01');

If you don't want to count the building itself as one of the sub-locations you can wrap the existing query in one the eliminates entries in which the building and sublocation are the same.

### item Udevops-1992
Site: devops | Thread title: Re-using Python virtual environments on a build server
It's generally a best practice to make your builds idempotent.
Leaving artifacts behind only opens up opportunities for dependency management issues- and resolving those in a resilient way is exactly why you're using a build server.
I suggest you take a look at WHY your Python builds are running so slow- if you discover this is because of an overabundance of packages in each project, this might be optimizable.

If you discover this is because of server performance issues, those are easily fixable with more resources.
If you find you are blocked by network throughput, consider using an artifact repository to cache packages locally.
But building persistent virtualenvs seems like a recipe for problems that could be unpredictable when moving to another server, and extremely frustrating to troubleshoot.

### item Unetworkengineering-1962
Site: networkengineering | Thread title: Delay or Offset-List for EIGRP tuning?
Any metric manipulation I've ever seen has been via offset-lists. This allows very fine-grained control over the metric, and removes the need to calculate metric differences based on different interface delays.
Note that offset-lists have the added benefit of being applied (optionally) per-interface. So you can essentially do everything that a delay change does with an offset-list.

In the 'wild', the only thing my org uses offset-lists for is to force traffic to take a particular backup WAN link when the primary is having issues that don't actually take it down. That is -- I've seen very little EIGRP metric manipulation in production networks. I'm sure someone else will almost immediately disagree. =)

### item Usecurity-22727
Site: security | Thread title: How can I use nmap to distinguish between a normal linux machine and an android device?
I've used nmap extensively and while I've found it's in general pretty good at discovering the OS on server and desktop/laptop hardware it's pretty poor at detecting embedded and handheld kernels.
This is because quite frequently these systems are not listening on any ports, and it's the responses to TCP handshake process that gives the most OS detection information.
Without an open port all nmap has to work on is the response to closed ports and ICMP echo replies.

### item Userverfault-313287
Site: serverfault | Thread title: Best way to self destruct all data on a linux server?
I endorse all the other recommendations for DBAN, but if you really can't do this, I've had a lot of success with shutting down as many services as I can (esp. the windowing system), then doing
dd if=/dev/urandom of=/dev/sda bs=1000k
from a root shell prompt, sitting back, and waiting. This basically writes pseudorandom bytes, a megabyte at a time, all over /dev/sda (you may need to use /dev/hda or other device as appropriate to your setup).

Because the kernel and the tool are in-core, the system will stay up for a surprising amount of time while this is running, and it leaves an utterly unbootable and mostly-completely-scrambled system behind it.

### item Usoftwareengineering-203928
Site: softwareengineering | Thread title: When to start thinking about scalability?
It's actually quite an easy choice.
Right now, you have zero users, and scalability is not a problem.
Ideally, you want to reach the point where you have millions of users, and scalability becomes a problem.

Right now, you don't have a scalability problem; you have a number-of-users problem. If you work on the scalability problem, you will not fix the number-of-users problem, which means you will have solved a problem you don't have yet, and you will not have solved the problem you do have. The most likely result is that your product won't make it, and all your work will be for nothing.

If you work on the number-of-users problem, you will solve a problem you have right now, and then you can focus on the next problem, which might be scalability.

The nice thing about scalability problems is that, by definition, having them usually means business is pretty damn good, and this in turn means you can afford to spend money on optimizing for scalability. You don't go from zero users to ten million overnight, and if you keep an eye on the system's performance, you will have plenty of time to optimize when the time comes.

Of course it helps to keep scalability in mind while writing the code you need right now, but it doesn't make a lot of sense to spend dozens or even hundreds of man-hours on a feature of which you don't know if you'll ever need it, and the most likely scenario is that you won't. Right now, your main concern is to ship. What happens after that; well, you can worry about that later.

### item Uunix-43526
Site: unix | Thread title: Is it possible to create and use menus in (terminal-based) vim?
Yes, it is possible. You can load menu.vim (the default gvim menu definitions), or you can just start from scratch and create your own, then access them through :emenu. This doesn't give you nano-like always-visible menus, though; it gives you the ability to navigate menus using command-line tab completion.
If the user doesn't have a vimrc, you'll want to start by disabling vi compatibility:
:set nocompatible

Enable smart command line completion on <Tab> (enable listing all possible choices, and navigating the results with <Up>, <Down>, <Left>, <Right>, and <Enter>):
:set wildmenu
Make repeated presses cycle between all matching choices:
:set wildmode=full
Load the default menus (this would happen automatically in gvim, but not in terminal vim):
:source $VIMRUNTIME/menu.vim

After those four commands, you can manually trigger menu completion by invoking tab completion on the :emenu command, by doing :emenu<space><tab>
You can navigate the results using the tab key and the arrow keys, and the enter key (it both expands submenus and selects items). You can then make that more convenient by going a step further, and binding a mapping to pop up the menu without having to type :emenu every time:

Make Ctrl-Z in a mapping act like pressing <Tab> interactively on the command line:
:set wildcharm=<C-Z>
And make a binding that automatically invokes :emenu completion for you:
:map <F4> :emenu <C-Z>

### item Udba-84508
Site: dba | Thread title: SQL to select all siblings with specific child
In the WHERE you can simply filter for the parts which have an assemblie id equal to the assemblie id of 'Part B'
SELECT a.*, p.* 
FROM assemblies a
LEFT JOIN parts p USING (AID)
WHERE p.AID IN 
 (
 SELECT AID FROM parts WHERE P_NAME='Part B'
 );

### item Udevops-1944
Site: devops | Thread title: How to evangelize DevOps and tools in a low acceptance environment?
This is not docker-specific, but this general rule for evangelism applies: different audiences require different evidence. In general, software developers (and managers from a development background) want to see it in action, so POC's with measurable outcomes are preferred. Other disciplines and executive stakeholders may be OK with case studies and presentations before giving the greenlight; your goal is to identify which audience you're talking to, and begin to build a comprehensive argument.

Start small; find one key stakeholder, and present your case using the evidence that best suits them. Be patient; change in mature organizations is usually slow, so getting a small project up and running is a major accomplishment.

### item Unetworkengineering-44650
Site: networkengineering | Thread title: Can a network with a default gateway successfully ping a PC in another network without gateway?
Well I suppose it is without gateway but only works if you have network address translation which really takes place on routers. The details of the addresses aren't however correct on segment 1. (The first ping packet would ping the router and get a direct reply.)
PC1 sends src=192.168.1.2 dst=192.168.2.2 to routerether1 on seg1
Router sends src=192.168.2.1 dst=192.168.2.2 to PC2ether on seg2
PC2 receives it and replies to src=192.168.2.2 dst=192.168.2.1 to routerether2 on seg2 as it is local

Router sends src=192.168.2.2 dst=192.168.1.2 to pc1ether on seg1
NAT requires considerable complexity and remembers a great deal in order to remember which connection is supposed to go where; NAT for ping is especially complex in maintaining the table of mappings.
NAT might be very common on domestic routers and inside 4g networks and so on, but you've really got to get the base case super clear before understanding NAT.
Hope that helps,
Jonathan.

### item Usecurity-172106
Site: security | Thread title: Finding DKIM selectors without mailing
There is no way to detect if DKIM is implemented by the sender without getting a mail from the sender, extracting the selector from the DKIM-Signature header and getting the DKIM policy from DNS based on this selector.

One can check if some commonly used selectors can be found in DNS. But a successful check does not mean that any of these selector actually gets used for signing nor does it mean that the messages gets signed at all. And, no typical selector found does not mean that DKIM is not implemented.

### item Userverfault-175249
Site: serverfault | Thread title: How to setup SSL on Amazon EC2?
In your EC2 control panel, look at your instance and note the Security Group that is assigned to it. Then, navigate to the Security Groups section in the control panel, open your group, and make sure that port 443 is allowed over TCP.
This must be open to allow SSL traffic to your instance. A simple way to check if the port is open to the outside is to telnet into your server's IP on port 443, and see if you can connect and get a response.
telnet yourhost.com 443

### item Usoftwareengineering-250040
Site: softwareengineering | Thread title: Is it wrong to use Agile when clients' requirements don't change at all?
Would this be considered as bad, cowboy coding, anti-pattern.
Short answer: no. Doing "agile" correctly does not mean "no planning", it does mean not to overanalyse things.
one of the major reasons why Agile is used is because clients often change the requirements.

That's an oversimplifying statement. "Changing requirements" is also about how the team's understanding of the requirements change. And it is about how the customer's priorities about the requirement change when he actually sees a few releases of the software.

In fact, "agile" works IMHO best exactly in the situation you describe - the client has a good knowledge about his overall requirements, you can write a general plan from it, fill your backlog with lots of "user stories", and have already enough information to choose the right system architecture.
The short iterations of an agile development strategy then will help to make the "vague requirements" more precise, with lots of feedback if you are still going into the right direction.

It will also give you early feedback about the real effort and costs (which is something you can still fail in a waterfall approach, even if you know every single bit of requirement in detail).

### item Uunix-258512
Site: unix | Thread title: How to remove a positional parameter from $@
POSIXly:
for arg do
 shift
 [ "$arg" = "-inf" ] && continue
 set -- "$@" "$arg"
done
printf '%s\n' "$@"
The above code even works in pre-POSIX shells, except the original Almquist shell (Read Endnote). Change the for loop to:
for arg
do
 ...
done
guarantee to work in all shells.
Another POSIX one:
for arg do
 shift
 case $arg in
 (-inf) : ;;
 (*) set -- "$@" "$arg" ;;
 esac
done
With this one, you need to remove the first ( in (pattern) to make it work in pre-POSIX shells.

### item Udba-115825
Site: dba | Thread title: JSONB with indexing vs. hstore
Relational databases are designed around joins, and optimized to do them well.
Unless you have a good reason not to use a normalized design, use a normalised design.
jsonb and things like hstore are good for when you can't use a normalized data model, such as when the data model changes rapidly and is user defined.

If you can model it relationally, model it relationally. If you can't, consider json etc. If you're choosing between json/jsonb/hstore, generally choose jsonb unless you have a reason not to.

That's what I said in my blog post, which addresses just this topic. Please read the whole post. The paragraph you quoted points out that if you're choosing a dynamic structure you should choose jsonb over hstore, but the rest of the blog post is about why you should usually prefer to model relationally if you can.

So. Model the main structured part relationally. If the tables are really wide with lots of columns, this might be a sign that further normalization is required. Do not be afraid of joins. Learn to love joins. Joining many small tables will often be faster than querying and maintaining big denormalized tables. Denormalize only if you need to for specific cases, and preferably via materialized views ... but don't do it until you know you need to and have an actual concrete problem to solve.

For user-contributed data that's freeform and unstructured, use jsonb. It should perform as well as hstore, but it's more flexible and easier to work with.
One relevant thing to understand: GiST and GIN indexes like those used on jsonb are generally much less efficient than a plain b-tree index. They're more flexible, but a b-tree index on a normal column will almost always be much, much faster.

### item Udevops-1540
Site: devops | Thread title: Decoupling data of devops tools eg jenkins nexus
You might want to explore immutable architecture.
Steps
CI with static analysis(Sonarqube, because free!), pushing version artefacts to Nexus.
Base Image using Packer. These must be revisited from time to time. Base Image has security hardening, log shippers, monitoring tools etc.
Environment/Application specific images from Base image.
healthCheck and version API for each application(healthCheck API in deployment and version for visibility of code in different VMs).

Deploy App using Terraform and Ansible.
Can use Jenkins 2.0 (pipeline as code) to achieve points 1,2,3. It can be part of each application itself.
Let me know if this answers your question.

### item Unetworkengineering-507
Site: networkengineering | Thread title: How many contexts can be created on a Cisco ASA Active/Standby Pair?
Each physical firewall is licensed for two contexts with the base license. For example: an operational and an admin context. If you create an active/standby failover pair up to four contexts can be created as the licensing is shared between the physical devices. For Example: Operational 1, Operational 2, Operational 3, and an admin context.