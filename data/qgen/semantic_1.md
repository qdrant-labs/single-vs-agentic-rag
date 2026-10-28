### item Tnetworkengineering-51891
Site: networkengineering | Thread title: GRE-IPsec Tunnel between Cisco Router and a Linux Router
[chunk 985789] We had to change the lifetime durations for IKE Phase1 & Phase 2 on the Linux Box to get the result. It was more of a bug/tweaking required on the Linux Router.
Thank you for all your help!!!

### item Tsecurity-122140
Site: security | Thread title: Single Page Application with REST API backend based on XML, queried by dynamic XPath
[chunk 910406] Your primary problem when handling client-provided is going to be XML External Entities (XXE) attacks. Systems with such vulnerabilities can often be exploited to read files or enumerate the internal network which the server is on. In PHP you can help fix this by calling libxml_disable_entity_loader(true); in order to disable external entities.

[chunk 910407] Another problem is, potentially, the Billion Laughs attack. This is a CPU and memory exhaustion DoS attack which uses nested element type declarations. This SO question should give you a good idea on how to pre-validate XML before loading it to avoid this kind of attack, but the short answer is that libxml allows you to set a custom DTD validator / loader callback.

[chunk 910408] You may also want to consider XPath Injection, though I'm not sure how critical this would be in your use-case. It's hard to tell what kind of impact it might have on your system's business logic without having a wider understanding of the application.

### item Tserverfault-588701
Site: serverfault | Thread title: Sharing unix socket via docker volume - permission denied
[chunk 173915] Different containers cannot talk to each other via UNIX domain sockets when they are in different network namespaces. There is an unofficial kernel patch that allows this, but you're on your own if you use it.

### item Tsoftwareengineering-203635
Site: softwareengineering | Thread title: TDD Mock call verification - is it an anti-pattern?
[chunk 603785] Well, you should be trying to test inputs and outputs. You should be verifying externally visible behavior. The "promises" or "contract" that your class makes.
At the same time sometimes there's no better way to test a method than to do what you said.

[chunk 603786] I do think that it makes your test more brittle, so you should avoid tests that rely on implementation details if you can, but it's not an all-or-nothing deal. It's OK sometimes, the worst thing that happens is you change the implementation and have to update the test.

### item Tunix-502612
Site: unix | Thread title: KDE no longer automatically switches desktops
[chunk 453655] KDE Desktop Switching
Your problem is underlaid with the "focused" window situation, nothing changed on the new version of KDE but new features have been added (i am referring to the changes done to the focus stealing feature)
What's happening is when your window is activated, as it was not activated by an "active selection" it does not get the focus and thus the desktop is not automatically switched.
Solution
Change the Focus stealing prevention settings to none and your problem will be fixed

[chunk 453656] Open/run systemsettings5 > Window Management > Window Behavior > Set focus stealing prevention to none
Alternative solution
Focus stealing feature can be set on per window/application: right click on the title bar of firefox for instance and select "More actions" > "Special window settings" then in "apparence & fixes" you can customise the focus stealing setting for firefox.

[chunk 453657] With this solution you could keep the focus stealing prevention feature and also the old behavior. Also in the same setting location you can set firefox to always start on a specific desktop if this would match your needs

### item Tdba-23599
Site: dba | Thread title: BULK INSERT permission on a single database
[chunk 725895] Ok folks,
I've asked this on Brazilian msdn forum as well and I got the answer (Forum discussion: BULK INSERT por DATABASE). The user Roberson Ferreira _ helped me. I imagine you can't read Portuguese so I will describe the answer here.
Answer:
It doesn't matter if the ADMINISTER BULK OPERATIONS is server-wide, the user won't be able to BULK INSERT into a certain database if they don't have the INSERT permission as well. The INSERT permission is a database/table-level permission.

[chunk 725896] Additionally, the ADMINISTER BULK OPERATIONS is not going to grant the user any other permissions over the server or database, all the user will be able to do is BULK INSERT in the database where they have INSERT permission as well.

### item Tdevops-6591
Site: devops | Thread title: One Jenkinsfile or multiple?
[chunk 996941] It really comes down to personal preference.
One additional tool you might not be aware of are shared libraries for Pipeline. These allow you to quickly write custom Pipeline steps or factor out common Pipeline code without writing a Jenkins plugin in Java.

[chunk 996942] Between multiple Pipeline jobs and shared libraries, there are many ways to split up your job's code and there's no one right answer on how to do it. One suggestion I have is to determine what steps in your process are "atomic" - that is, what are the smallest group of steps that you envision admins/ops/devs/etc. might need to run on their own? Each "atomic unit" should then become its own job.

[chunk 996943] For instance, let's say you're automating a deploy process, and your process in a general sense looks like this:
build
deploy to dev
deploy to prod
Then I would create three jobs, one for each bullet point. This gives you some nice advantages:
You can re-run each job individually in case something fails instead of having to restart the entire process over from the very beginning. Deploy to prod failed? You only need to re-run the deploy to prod job. You don't need to rebuild or re-deploy to dev.

[chunk 996944] Each stage in the process is separated out so you can see how often it succeeds or fail. Some stages in your process may be more robust or fragile than others; this kind of separation gives you insight into that.
This level of abstraction makes it easy for non-ops people to perform ops tasks (if that is something you want/need at your org).
When everything is monolithic, the only thing non-ops people can do is run the entire process from the beginning.

[chunk 996945] When everything is split up into tiny jobs, you need intimate ops knowledge to know which pieces to run in what order.
By separating your jobs into independent, easy-to-understand, appropriately bite-size chunks, a non-ops person only needs to press a single button to kick off an automated ops process.

### item Tnetworkengineering-5104
Site: networkengineering | Thread title: Cisco IOS outbound filtering
[chunk 972963] The reason why the port forwarding is not working with the access-list applied to the interface is quite simple.
Let's see what happens when the outside client requests the https webpage.
The destination port in the request packet is 443, while the source port is random. This request gets translated by nat at the router, then goes all the way to the server, server answers with the packet sourced from port 443 and destined to that client's random number port.

[chunk 972964] The packet in its journey back to the client gets to your router, but router wouldn't let the packet leave, because the destination port (that random port) is not specified in the access-list you have created.
And that would be the reason you are looking for.

### item Tsecurity-135129
Site: security | Thread title: How to identify L2 devices in a Wide Area Network?
[chunk 916018] You can see some hop counts in the traceroute results, but there are
 certainly many devices in the middle; if you could capture traffic you
 could see that when a packet passes a device the source MAC address
 would change
This is incorrect. L2 devices do not change source/dest hardware address.
More to the point of your question, if you're inside the target network you could try sniffing for lldp/cdp/stp traffic to gather information about the connected L2 devices.

[chunk 916019] Once the packets goes through a router any information below layer 3 is lost.
The "timed out" and missing hops in your traceroute are not invisible l2 devices, they're hops (routers) that do not send ICMP type 11 packets to inform the TTL was exceeded.

### item Tserverfault-515278
Site: serverfault | Thread title: Will IIS finish pending requests on Stop-WebSite?
[chunk 155865] When running this simple test:
int ms = 2000;
try
{
 Log("1");
 Thread.Sleep(ms);
Log("2");
 Thread.Sleep(ms);
Log("3");
 Thread.Sleep(ms);
Log("4");
 Thread.Sleep(ms);
Log("5");
}
finally
{
Log("6");
}
and stopping the web site a second after I called the page, I always get all six log entries.
So, in general your (and mine) original assumption is correct, the running process is finished before the site is shut down.

[chunk 155866] Is it impossible that a certain request may not finish? What if it runs for hours? what if something goes wrong and the worker process hangs?
I would look for other reasons why your 'Log("End");' does not work.

### item Tsoftwareengineering-323547
Site: softwareengineering | Thread title: MVVM Commands - one command for everything or multiple commands?
[chunk 650390] I think using the switch statement with strings is a terrible idea for the following reasons:
Your commands can't take an actual parameter because you've used the CommandParameter to identify the command itself.
Your Execute and CanExecute methods become large blobs where it's impossible to tell if you are actually handling all of your commands since you have to cross-reference the ViewModel with every single XAML file that is bound to it.

[chunk 650391] Some commands do not need a CanExecute. If you have each command as an individual property, it's very easy to tell which commands support CanExecute and which do not. With the switch statements, it's a lot harder to determine that.

[chunk 650392] It is very difficult to override behavior for a single command in a derived class. If you had a child ViewModel class, the only way to override behavior for one command is to copy the entire Execute(String parameter) method and change the one case statement that you're interested in.
Static analysis tools cannot tell you that your command binding in the XAML is wrong because your CommandParameter is just an arbitrary string.

[chunk 650393] I think that the downsides to the switch statement with string approach are so strong that I would encourage refactoring existing projects to not do it that way.

### item Tunix-572637
Site: unix | Thread title: Pass options to AWK script bypassing AWK
[chunk 472052] For the sake of the challenge, it could be done with the FreeBSD env or with GNU env >= 8.30 (already assumed by the OP) in a shebang:
#! /usr/bin/env -S sh -c 'exec awk -f "$0" -- "$@"'
BEGIN { for(i = 1; i < ARGC; i++) print ARGV[i] }
./myscript -h 1 2 3
-h
1
2
3
It doesn't mean that it's a good idea, though.
You could try this, instead:
#! /bin/sh
BEGIN { 2>"/dev/null"
 exec awk -f "$0" "--" "$@"
}
BEGIN { for(i = 1; i < ARGC; i++) print ARGV[i] }

[chunk 472053] This assumes that you don't have a BEGIN command in your PATH.

### item Tdba-56746
Site: dba | Thread title: Disabling SET Statements / Forcing SET Options in SQL Server 2008R2/2012
[chunk 742084] There is no way to enforce a global setting or prevent people running
SET ANSI_NULLS OFF
SET ANSI_PADDING OFF
You can get a quick idea if your application is using any deprecated features by running
SELECT *
FROM sys.dm_os_performance_counters
WHERE object_name LIKE '%Deprecated%'
 AND cntr_value > 0
ORDER BY cntr_value DESC
If you do find areas of concern then you could set up a Server Side trace capturing the deprecation events.

[chunk 742085] This also returns the session id and SQL Handle of the offending batch to allow you to investigate further if you do see any events.
A slightly more sophisticated approach would be to set up a notification procedure to retrieve the text associated with the SQL Handle more quickly to reduce the probability that the offending SQL is no longer in the cache when you come to analyse the results.
Or you could probably use extended events to retrieve the TSQL along with the event.

### item Tdevops-3533
Site: devops | Thread title: Is it a common practice to include the version of an API into the rest interface itself?
[chunk 995899] Many APIs include a version number in the url of the service. Some examples:
https://api.twitter.com/1.1/statuses/home_timeline.json
https://graph.facebook.com/v2.2/me/adaccounts
https://vision.googleapis.com/v1/images:annotate?key=YOUR_API_KEY
https://maps.googleapis.com/maps/api/js?v=3.29
https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze
https://www.europeana.eu/api/v2/opensearch.rss?searchTerms=Rembrandt

[chunk 995900] However many people on the Internet argue that this is incorrect because it violates REST/HTTP specifications; "embedding of API version into the URI would disrupt the concept of hypermedia as the engine of application state". It’s more appropriate to use the Accept header to request a particular version. For the latter people suggest to use a Vendor MIME type, for example something like Accept: application/vnd.mycompany-api-v3+json

[chunk 995901] Nevertheless, the reason why many API designers do include an API version in the url is because it's easy to implement and debug (clearly visible which version you are using).

[chunk 995902] Side note: in our organization we recently decided to support both a versionless endpoint that always point to the latest stable version of our APIs, as well as an endpoint with a version specification. This allows users to choose if they want to commit to our latest API (which may require making changes when a newer version is released), or to connect to a fixed API version (which may become deprecated over time).

### item Tnetworkengineering-1949
Site: networkengineering | Thread title: Can adding VLANs to a VPC be done hot?
[chunk 972045] While it is certainly a good idea that a VPC has the same allowed VLAN list on all sides, it is not a requirement. Take a look at the output of "show vpc consistency-parameters global".

[chunk 972046] switch# show vpc consistency-parameters global 
Legend:
 Type 1 : vPC will be suspended in case of mismatch
Name Type Local Value Peer Value 
------------- ---- ---------------------- -----------------------
QoS 2 ([], [3], [], [], [], ([], [3], [], [], [], 
 []) []) 
Network QoS (MTU) 2 (1538, 2240, 0, 0, 0, (1538, 2240, 0, 0, 0, 
 0) 0) 
Network Qos (Pause) 2 (T, F, F, F, F, F) (T, F, F, F, F, F) 
Input Queuing (Bandwidth) 2 (50, 50, 0, 0, 0, 0) (50, 50, 0, 0, 0, 0) 
Input Queuing (Absolute 2

[chunk 972047] (F, F, F, F, F, F) (F, F, F, F, F, F) 
Priority) 
Output Queuing (Bandwidth) 2 (50, 50, 0, 0, 0, 0) (50, 50, 0, 0, 0, 0) 
Output Queuing (Absolute 2 (F, F, F, F, F, F) (F, F, F, F, F, F) 
Priority) 
STP Mode 1 MST MST 
STP Disabled 1 None None 
STP MST Region Name 1 "" "" 
STP MST Region Revision 1 0 0 
STP MST Region Instance to 1 
 VLAN Mapping 
STP Loopguard 1 Disabled Disabled 
STP Bridge Assurance 1 Enabled Enabled 
STP Port Type, Edge 1 Normal, Enabled, Normal, Enabled, 
BPDUFilter, Edge

[chunk 972048] BPDUGuard Disabled Disabled 
STP MST Simulate PVST 1 Enabled Enabled 
Allowed VLANs - 1,10,100-101,200-201 1,10,100-101,200-201,2
 000 
Local suspended VLANs - - -
Type 1 parameters absolutely MUST match, else the vPC will be suspended. "Allowed VLANs" is neither a Type 1 or Type 2 parameter.
You should be able to modify the allowed VLAN list without problems, but obviously try to keep things consistent regardless, otherwise you'll still have issues, even though the vPC doesn't get suspended.

[chunk 972049] EDIT: You probably already know this but just to be sure - include the peer-link in your VLAN changes, as the VLAN (not the entire vPC) will show up as "suspended" on all vPCs until you do.

### item Tsecurity-29632
Site: security | Thread title: What should I know about SPDY before enabling it?
[chunk 863795] SPDY has been reported to be vulnerable to the CRIME attack, but this will be patched in next protocol version. The specifics of CRIME target HTTP cookies, so the fixed protocol will do something special when compressing cookies (namely, it will not compress cookies with the rest of the headers; instead, it will use a dedicated channel to transport the cookie values, with a specific code stating "same cookie than previously").

[chunk 863796] As a general rule, encryption leaks data length, and compression (any kind of compression) makes the length dependent on the data byte values, thus increasing the information leakage. Encryption and compression don't mix well together. I personally would recommend not activating SPDY for HTTPS. For plain HTTP, however, go on; it won't make things worse security-wise than the mere fact of using plain HTTP.

[chunk 863797] It would be interesting to gather some hard data on the actual bandwidth benefits of SPDY. Google initially boasted about making page loading "55% faster" but this was in lab conditions. Actual speed-ups may vary quite widely on the kind of request that the site handles. As usual, there is no performance issue unless demonstrated by unambiguous measures.

### item Tserverfault-344597
Site: serverfault | Thread title: Track, save and revert file system modifications made by a program under Linux
[chunk 109882] Possibly the easiest (?) way to do this is to boot off of a LiveUSB with a "persistent data partition." (Or, to replicate the effect yourself, in a chroot jail: mount a rw layer over a ro layer.) Take a snapshot of the rw filesystem -- which should be very slim after a fresh boot -- then run your installer. Every file it alters or creates will be on the rw "persistent data" overlay partition. Even removed files will appear as "magic dotfiles."

### item Tsoftwareengineering-183843
Site: softwareengineering | Thread title: How to preserve order of incoming requests on a multithreaded server
[chunk 594887] One name for this kind of requirement is "Unit of Order".
For example, in Weblogic JMS, it provide such feature that, conceptually, you can put an UOO identifier with your message when you are putting message to queue. Weblogic JMS will guarantee that messages of same UOO being processed in chronological order. However, messages under different UOOs can be processed in parallel.

[chunk 594888] It all depends on what platform or technology you are going to implement it, which I believe there are a lot of way to achieve similar effect.

### item Tunix-206922
Site: unix | Thread title: How to detect end of line with sed
[chunk 365872] With standard sed, you will never see a newline in the text read from a file. This is because sed reads line by line, and there is therefore no newline at the end of the text of the current line in sed's pattern space. In other words, sed reads newline-delimited data, and the delimiters are not part of what a sed script sees.

[chunk 365873] Regular expressions can be anchored at the end of the line using $ (or at the beginning, using ^). Anchoring an expression at the start/end of a line forces it to match exactly there, and not just anywhere on the line.
If you want to replace anything matching the pattern [A-Za-z]* at the end of the line with something, then anchor the pattern like this:
[A-Za-z]*$
...will force it to match at the end of the line and nowhere else.

[chunk 365874] However, since [A-Za-z]*$ also matches nothing (for example, the empty string present at the end of every line), you need to force the matching of something, e.g. by specifying
[A-Za-z][A-Za-z]*$
or
[A-Za-z]\{1,\}$
So, your sed command line will thus be
$ sed 's/[A-Za-z]\{1,\}$/replace/' file.txt
I did not use the non-standard -E option here because it's not strictly needed. With it, you could have written
$ sed -E 's/[A-Za-z]+$/replace/' file.txt
It's a matter of taste.

### item Tdba-54813
Site: dba | Thread title: What tables are affected by Change Data Capture
[chunk 741134] As mentioned in the question, we're trying to query multiple cdc tables and apply a similar process to all of them. The only way to do this is by querying each table individually (using the fn_cdc_get_all_changes_dbo_tablename function), there is no central place to check what has changed.