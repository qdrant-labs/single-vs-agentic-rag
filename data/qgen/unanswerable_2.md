### item Usoftwareengineering-137948
Site: softwareengineering | Thread title: Should a one person team use a process model?
As a young guy fresh out of the college - i never used to use Source control. However, now after having used to SCM, even if i do the project alone it makes life easier by using SVN. Imagine how easy it is to retrieve yesterdays' work if i mess up the code - and also take a look back of how things evolve. I don't have to keep all this in my mind.

This questions usually arrive because lot of times people think of Process they think of a lot of documentation, and whole bunch of formalities that looks like a waste of time. Yes, if you are alone, don't do anything which looks like a waste of time. (In fact in our company i leave people to question the proces and don't do it if it is a waste of time; but that is probably too much of stretch).

The point is: in a true sense a process is a tool, a mechanism that will ensure that simple mistakes (rather goof-ups) don't happen and don't create disasters-
A seasoned carpenter will always measure and remeasure the wood before putting a cut,
A good driver will always put the seat belt on while driving,
A good chef of a restaurent will have a simple way to test food
-- the sameway a good programmer will check-in the code before he goes back to sleep.

The complexity of the tool varies, but it is always important that practices are used in the way that helps you and it is really nothing about being alone or in the team.

### item Uunix-40210
Site: unix | Thread title: How to include program which only works with in/out files into a pipeline?
if this satisfies you, here is proposition how to do this using pipes.
Assumption is that input and output files of "badtool" can be pipes.
mkfifo IF
mkfifo OF
# one therminal
tool | tool2 |... tooln > IF
# second terminal
bad_tool IF OF
#third terminal
tooln+1 < OF | tool n+2 | tool n+3 ...
If you would like to create script you can wrap those parts into functions:
function A(){ ... }
function B(){ ... }
function C(){ ... }
# and run in background in parallel
A&
B&
C&

Continue with all your images (pipes IF and OF are "reusable") and after whole job delete them
rm IF OF

### item Udba-176992
Site: dba | Thread title: How to create an index on CASE expression in Postgres
You need to add extra parentheses around the CASE expression:
CREATE UNIQUE INDEX test_index 
 ON test ((CASE WHEN i=1 THEN j END)) ;
As the docs state in CREATE INDEX:
The key field(s) for the index are specified as column names, or alternatively as expressions written in parentheses.

Consider also using a filtered index, which is equivalent in terms of functionality but would be using less space, as it will be storing the j values only for rows with i = 1 and not the (possibly millions) or the rest NULL values:
CREATE UNIQUE INDEX test_index_2 
 ON test (j) WHERE i=1 ;

### item Udevops-10499
Site: devops | Thread title: How to create GitHub Actions for unit testing in .NET projects?
You do not need to include anything into your assembly to run your tests using GitHub Actions. Just create workflow file in .github/workflows folder with the following content (assuming that you have .NET Core project):
---
name: Tests
on: push
jobs:
 tests:
 name: Unit Testing
 runs-on: windows-latest
 steps:
 - uses: actions/checkout@v2.1.0
 - run: dotnet test

dotnet is pre-installed on windows machine but is not pre-installed on macos and ubuntu. So, you have to install dotnet by adding an extra step in case you want to run it on one of these machines. You can use actions/setup-dotnet action for this purpose.

### item Unetworkengineering-58517
Site: networkengineering | Thread title: Use BFD on a Virtual-Template Interface
Bidirectional Forward Detection (BFD) has been deactivated on virtual and dialer interfaces on newer IOS and IOS-XE versions.
On earlier releases like IOS-XE 3S, the Cisco IOS software incorrectly
 allowed configuration of BFD on virtual-template and dialer
 interfaces; however, BFD functionality on virtual-template and dialer
 interfaces is not supported. Avoid configuring BFD on
 virtual-template and dialer interfaces.
That is what the Cisco configuration guide says for BFD on IOS XE:

https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_bfd/configuration/xe-3s/irb-xe-3s-book/irb-bi-fwd-det.html

### item Usecurity-139407
Site: security | Thread title: Low priv users for Windows Services
Here is my question: Could I run a simple server (like described
 above, access to file system/registry, network access) as NETWORK
 SERVICE? Are these 2 users provided by MS for such a situation?
Yes you can and you should.

The network service account is (as I remember it) the least privileged machine account with limited permissions.You actually will get an Insufficient Exception, if it turns out, your application requests resources for which the Network Service account does not have the rights to.

You would then simply grant rights to what ever resource you're trying to access and then build on that, but for your high level requirements you describe here, access to file/registry and network it should be sufficient.
True, if your application creates a new eventlog source or registry key, you would need to explicit grant the rights to the network service account, should be no big deal for you/devops.

You could also consider using a domain account, say if you want to isolate your application/service from how shall I say it: an over time fragmented permissions changes to the general Network service account.
I would suggest you read up on those accounts in general:
https://msdn.microsoft.com/en-us/library/windows/desktop/ms686005(v=vs.85).aspx

If you succeed to inject code into a php application running on apache
 as www-data you still need a tedious privilege escalation to fully
 compromise the machine
regardless of priv. esc. of (www) is tedious or less tedious (personally I think it's pure fun), if you're at that point where you found a bug in your service that can be priv. escalated, it usually boils down to poor patch management on your box and not so much your service at that stage.

### item Userverfault-244818
Site: serverfault | Thread title: Setting "max_allowed_packet" -- commandline vs config?
set global max_allowed_packet = 1000000000
This sets max_allowed_packet it to 1 billion bytes or 1 GB.
max_allowed_packet=100M
This sets it to 104857600 bytes or 100 MiB.
Assuming your extra zero is unintended, the only difference between setting via command line and config is that the config file supports shorthand using JEDEC binary prefixes. Plus, the set global will be lost on server restart.

### item Usoftwareengineering-322613
Site: softwareengineering | Thread title: Making DAO's independent on each other
The easy way would be making a DAO for each one and have
 the CompanyDao use the EmployeeDao internally.
Due to no link to StackOverflow has been shared, I just want to mention why is code smell.
In short:
it would introduce undesirable coupling. Potentially one of the DAOs would end up subordinated to the other.
It has all the recipes for a circular dependency. See also Circular references.
Regarding to the code (the exmaple of DBService)
Is this a good way to do this?

So far, the code is at the doors of the well known Repository pattern (despite the actual name) which is broadly adopted by the community. You will find many references to the pattern looking for DDD.
The Repository pattern introduced in Eric Evans' DDD, has nothing to do with the implementation details, so the implementation will vary according to the specific requirements and needs.
What doesn't vary is the concept. The purpose.

So, based only in the info you provide, I would say that you are doing fairly good.

### item Uunix-23383
Site: unix | Thread title: show gateway IP address when performing ifconfig command
You can with the ip command, and given that ifconfig is in the process of being deprecated by most distributions it's now the preferred tool. An example:
$ ip route show
212.13.197.0/28 dev eth0 proto kernel scope link src 212.13.197.13
default via 212.13.197.1 dev eth0

### item Udba-18906
Site: dba | Thread title: How can I get the Oracle TNSListener to start after changing my host name?
When you run lsnrctl status, one of the things that it tells you is the location of the Listener Parameter File (the listener.ora file)
LSNRCTL for 64-bit Windows: Version 11.2.0.1.0 - Production on 06-JUN-2012 13:12:22
Copyright (c) 1991, 2010, Oracle. All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=EXTPROC1521)))
STATUS of the LISTENER
------------------------
Alias LISTENER
Version TNSLSNR for 64-bit Windows: Version 11.2.0.1.0 - Production
Start Date 06-JUN-2012 09:33:58
Uptime 0 days 3 hr.
38 min.

24 sec
Trace Level off
Security ON: Local OS Authentication
SNMP OFF
Listener Parameter File C:\oracle\product\11.2.0\dbhome_1\network\admin\listener.ora
Listener Log File c:\oracle\diag\tnslsnr\jcave8560w\listener\alert\log.xml
Listening Endpoints Summary...
(DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(PIPENAME=\\.\pipe\EXTPROC1521ipc)))
 (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=127.0.0.1)(PORT=1521)))
Services Summary...
Service "CLRExtProc" has 1 instance(s).

Instance "CLRExtProc", status UNKNOWN, has 1 handler(s) for this service...
Service "jcave11gR2XDB" has 1 instance(s).
Instance "jcave11gr2", status READY, has 1 handler(s) for this service...
Service "jcave11gr2" has 1 instance(s).
Instance "jcave11gr2", status READY, has 1 handler(s) for this service...
The command completed successfully
If you open that file, there will probably be an entry like this

LISTENER =
 (DESCRIPTION_LIST =
 (DESCRIPTION =
 (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
 (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
 )
 )
where the host is specified. Change the host there and restart the listener.

### item Udevops-10542
Site: devops | Thread title: Ansible ad-hoc command to reboot servers in serial with a pause
@Argyle explained the --fork 1 trick to achieve a serial run.
I suggest you have a look at the reboot module that might be better suited than running a command directly.
A quick example that will reboot all your nodes one by one waiting for each to be fully booted before moving to the next one.
ansible -i inventory nodes --forks 1 -m reboot
Pass needed parameters to the module depending on your requirements with the -a option.

### item Unetworkengineering-2155
Site: networkengineering | Thread title: Site-to-Site VPN Tunnel Up Not Passing Traffic
The resolution to my problem is to upgrade my ASA image to 8.6.1(5).
This resolves bug CSCtq57752
The workaround to the bug is to lower the crypto map's timed lifetime and increase the crypto map's traffic volume threshold:
crypto map *YOUR-CRYPTO-MAP ID* set security-association lifetime seconds 3600
crypto map *YOUR-CRYPTO-MAP ID* set security-association lifetime kilobytes 2147483647

The above crypto map lowers the lifetime to 3600 seconds and increases the kilobytes threshold to the highest value. In my case, I just have to ensure the seconds lifetime is depleted before the kilobytes threshold.

### item Usecurity-232613
Site: security | Thread title: Can a large corporation make a believable promise
Companies make promises they can't renege on all the time - that's what a contract is. After all, insurance wouldn't exist if an insurer could wriggle out of paying claims through things like secret policies.
That's not to say you can't breach a contract - of course you can, things go to court all the time. But a contract is as binding as anything you can do with directors and shareholders passing resolutions, and would need equally careful drafting.

The weaknesses of contracts in this situation are:
The courts can't put the toothpaste back in the tube (and compensation may not be sufficient for your situation)
The courts can't deal with things that are undetectable
As such applications with serious needs will often call for public transparency, hardware security modules, witnesses from multiple organisations, certifications from audit firms, and suchlike.

### item Userverfault-9558
Site: serverfault | Thread title: Remote Desktop Security
I run a linux virtual machine for playing around with ruby as well as running an SSH server.
Then I use putty and I tunnel my RDP session through the SSH tunnel to ensure its security.
Information on doing this available here:http://www.engr.wisc.edu/computing/best/rdesktop-putty.html
A bonus: you can just add a tunnel to putty and access another PC at home if you have one, or you can make web requests, etc straight to services at home without exposing them to the internet.

### item Usoftwareengineering-216944
Site: softwareengineering | Thread title: MVC is a GUI Architecture or a Architecture to GUI and Domain?
MVC was originally designed to solve the problems in architecting GUIs. It decouples the process of extracting data from the model in order to present it from the process of presenting it. Basically it is an application of the Single Responsibility Principle to GUIs.

This has a number of large advantages: it takes away the need to have logic code from the presentation layer and it makes the controllers testable, thereby increasing quality and reliability. Early web GUIs, like classic ASP, had logic code embedded in HTML pages which was hard to maintain and just made you feel dirty.

The Model is basically a black box representing the application and its data, and will typically be an n-tiered application. The View is to display the data from the application and typically pass commands and data back to update the application. The Controller mediates between the Model and the View, presenting data to the View and commands to the Model.

So the Model is, as you say, the business rules or domain (or it could just be a database), but the entire architecture - Views to present data and Controllers to pass data and commands back and forth between the Model and the Views - is very much a GUI framework.

### item Uunix-170630
Site: unix | Thread title: Formatting file in command line for printing
Use fold. Extracts from the man page:
Wrap input lines in each FILE (standard input by default), writing to
standard output.
-b, --bytes
 count bytes rather than columns
-c, --characters
 count characters rather than columns
-s, --spaces
 break at spaces
-w, --width=WIDTH
 use WIDTH columns instead of 80
Use fold (maybe using the -s option so that it doesn't break your lines mid-word) to set your document to about 80 characters wide and print:
fold -s myfile.txt | lpr

Or, to save the formatted version:
fold -s myfile.txt > output.txt

### item Udba-55053
Site: dba | Thread title: SQL Server 2012 32 bit - will enabling locked pages allow it to use more memory?
Can I have this 32 bit installation use more memory using locked pages?
In the past, my answer would have been (a heavily qualified) "yes".
Using AWE (address windowing extensions) would enable up to 64GB memory. Unfortunately (from your point of view, perhaps) 32-bit AWE was removed from the database engine starting with SQL Server 2012.

In previous versions, 32-bit SQL Server running on a 64-bit version of Windows (WOW mode) was a supported configuration but one that I never encountered personally. Anecdotally, such configurations were often problematic; if you enjoy tracking down weird problems, 32-bit AWE SQL Server on 64-bit Windows is for you.
My very strong recommendation would be to use 64-bit SQL Server 2012 instead.

### item Udevops-1885
Site: devops | Thread title: VM Hosts: Single Large Host or Few Smaller Hosts?
A good rule of thumb is to try and avoid using one bit of logical kit (be it a single VM or a single physical host) for more than one thing.
If a physical server is going to be a VM host then that's all it should be. If a VM or a physical host is going to be a source code repository then that's all it should be etc. You can squeeze a bit extra out of your infrastructure if you consider everything to be a VM host and you then partition up those VMs to be single purpose hosts themselves.

The rationale behind this is that
A single host going down shouldn't impact your entire stack. Trust me this will hurt you badly as soon as you need downtime for an upgrade.

The cost to scale any individual component increases drastically if you want to try and scale on multiple similar servers (which will save you management dollars by reducing complexity) or it will cost you to scale out adhoc hardware as needed because you then need to deal with many different-sized hosts that are a pain to manage and require anyone managing them to know the platform intimately.

recommendation: split your infrastructure into as small a unit as is logical. If you can only afford to buy a single large bit of kit then make sure you split it into logically separate VMs or containers so that if you need to pop a bit of your infrastructure onto another server, or you need to scale stuff at different rates you can easily expand out but investing in a smaller upgrade.

Obviously the realities of software licencing, especially for windows OS's might make this cost prohibitive but, while I haven't caught up on windows licensing models in a while, I'm sure there are development centric licensing models that can suit your specific needs.

### item Unetworkengineering-24700
Site: networkengineering | Thread title: Multiple VLANs to a router with OSPF
This is with some assumptions since you didn't include a drawing or configurations.
If you have a router connected to a layer-3 switch, you should probably make the link between the two a point-to-point routed link (use no switchport on the layer-3 switch port) and give the link a point-to-point address like /30 or /31.

On the layer-3 switch, you have SVIs with IP addresses for your VLANs, and you use network statements (or redistribute connected routes) in the OSPF configuration so that OSPF will share the networks with the router.
You probably want the router to send a default route to the layer-3 switch, so you use the default-information originate command on the router, and it will inject the default route into OSPF if it exists in the routing table.

### item Usecurity-206824
Site: security | Thread title: Email verification by sending mail instead of receiving
Relying just on a mail claimed to be send by a specific user will neither be sufficient not practical to verify the sender, even with SPF and/or DKIM validation.

Neither SPF nor DKIM validate the sender of the email in the first place. They verify at most that a mail was send using a mail server which is allowed to send mail for the claimed domain - where the claimed domain is unrelated to the domain in From field in the mail header (i.e. what is usually seen as the senders address). Only DMARC will align the domain in the From field of the mail header with the claimed domain in the SMTP dialog (SPF) or the DKIM-Signature (DKIM).

Even then - this will only align the domain part but not the actually full address. Thus relying only on this would allow attacker@example.com to claim in the From field of the mail header to be goodguy@example.com and neither SPF nor DKIM nor DMARC would complain.

In addition to that it is common to have domain often explicitly allow service providers (like Office365, Mailchimp,...) to send mail in their name by adding their IP addresses or domains to the SPF policy or providing them with the key needed for DKIM. These service provider have the infrastructure typically shared between all clients which badly affects the granularity SPF would offer and also means that somebody except the domain owner can send DKIM signed mails with the owners domain.

Apart from being insufficient to validate the sender it would also require the clients infrastructure to have DMARC and at least one of SPF or DKIM properly implemented - which only very few have.