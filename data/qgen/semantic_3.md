### item Tdba-174791
Site: dba | Thread title: Does SQL Server use multiversion concurrency control (MVCC)?
[chunk 789699] Does SQL Server really implement MVCC anywhere
Yes, since SQL Server 2005.
The SQL Server terminology is "row-versioning isolation levels". See the product documentation tree starting at Locking and Row Versioning. Note in particular that there are two separate "MVCC" implementations, read committed isolation using row versioning (RCSI) and snapshot isolation (SI).
and how does that reconcile with the idea of with (tablock, holdlock) if it does?

[chunk 789700] Using that combination of hints serializes access to whole table(s). It is the least concurrent option available, so using these hints should be very rare. Whether a particular use could be replaced with RCSI or SI isolation depends on the specific circumstances. You could ask a follow-up question with a specific example if you want us to address that aspect in detail.
You might also like to read my series of articles on SQL Server isolation levels.

### item Tdevops-942
Site: devops | Thread title: How to cache third party resources in a build pipeline?
[chunk 994514] I'm not overly familiar with Docker particularly but it sounds a lot like issues one would get when building a normal .NET application or java app with the need to store their external dependencies (DLL or jar).

[chunk 994515] To solve this I'm quite fond of artifactories. Two of the most popular are sonatype's Nexus and JFrog's Artifactory. Both offer a free Open Source version and both will have some way to store customised package or use it as a raw depot. There are other options out there, I just listed these two because I've worked with them already and know they will do what you need. As a bonus you might also be able to use them to manage the docker image directly as well.

[chunk 994516] There are others too worth mentioning, you can find a comparison table for them, you'll get a better view of their capabilities. (thanks to Karl Harnagy for the link)
Note that some of these options might require one or another of the paid versions so YMMV.
Some continuous integration systems will also support the concept of artifacts (from experience Jenkins and team-city do this, others might as well though) which should allow you do achieve similar results directly.

[chunk 994517] If none of these do it for you you can look into other technologies or roll your own. I personally like to leverage whatever I already have this reduces the maintenance required in long term and makes passing the buck easier when comes time to look for new challenges elsewhere.
Hope this helps

### item Tnetworkengineering-30509
Site: networkengineering | Thread title: Juniper EX4200 how to select s-vlan from c-vlan on dot1q-tunneling access port?
[chunk 979692] This should do what you are after:

[chunk 979693] set interfaces ge-0/0/0 unit 0 family ethernet-switching port-mode access
 set interfaces ge-0/0/0 unit 0 family ethernet-switching vlan members SVID4
 set interfaces ge-0/0/0 unit 0 family ethernet-switching vlan members SVID5
 set vlans SVID4 vlan-id 4
 set vlans SVID4 dot1q-tunneling customer-vlans 41-42
 set vlans SVID4 dot1q-tunneling layer2-protocol-tunneling all
 set vlans SVID5 vlan-id 5
 set vlans SVID5 dot1q-tunneling customer-vlans 51-52
 set vlans SVID5 dot1q-tunneling

[chunk 979694] layer2-protocol-tunneling all
Cheers,
H

### item Tsecurity-31860
Site: security | Thread title: Evernote hacked - precautions?
[chunk 865206] Whenever a service you use gets hacked and the result is a leak of authentication credentials, there are some precautions you can take to minize your risk.
First of all, change the service's password, even if you had a long and complex one. This will make it impossible for the attackers to get your current credentials.
Make sure you never use the same password for two different applications. I know, same old suggestion, but this is exactly the case where it makes a difference!

[chunk 865207] You have to consider that Evernote uses an e-mail address as username (too), hence creating a higher risk if you use the same password for other services that require a unique e-mail (e.g. Facebook).
Finally, I'd suggest the use of a password manager in order to generate safe passwords and to use them without having to rely on simple schemas (e.g. Evernote1!) or on post-it notes.

### item Tserverfault-576910
Site: serverfault | Thread title: How to find full process arguments and associated listening ports?
[chunk 170782] ss -lnptu piped to awk with a call to ps -p. I'm on a mobile device, so it is a little tricky to type out a full example at the moment.
Listening Sockets:
ss -lnptu | awk 'NR>1 { split($7,p,","); printf "Listen: "$5 " Command: "; system("ps --no-headers -o args p "p[2]); }'
All Sockets (will likely require some additional filtering due to sockets without process information in TIME_WAIT, etc):

[chunk 170783] ss -anptu state listening state established state connected state unconnected | grep -v TIME_WAIT | awk 'NR>1 { split($7,p,","); printf "Listen: "$5 " Command: "; system("ps --no-headers -o args p "p[2]); }'

### item Tsoftwareengineering-135660
Site: softwareengineering | Thread title: IRC Bot permission structure, best approach?
[chunk 573741] I like not relying on the schema of the database too much. It makes later changes harder.
I would have one Table
users: <user-id> <user name>
another Table
local-permissions: <user-id> <channel(-id)> <permission>
and yet another Table:
global-permissions: <user-id> <permission>
I would use a String column for permission, if you want you can use a database-check for allowed values. It's easier to read and write if you're manipulating the database directly (which you will at some point).

[chunk 573742] Since you want multiple permissions, put multiple rows in the tables and then figure out the hierarchy in the application.
If you want to make it more visible which permissions a particular user has, you can also go for just one row/entry and separate them by space in the column like that: "op kick ban" (be fault-tolerant in the application for that!).
It doesn't seem pretty, but as i said, i'd rather have the schema/data-interpretation in the application then in the database.

### item Tunix-8414
Site: unix | Thread title: How to have tail -f show colored output
[chunk 284973] Try out multitail¹. This is an übergeneralization of tail -f. You can watch multiple files in separate windows, highlight lines based on their content, and more.
multitail -c /path/to/log
The colors are configurable. If the default color scheme doesn't work for you, write your own in the config file. For example, call multitail -cS amir_log /path/to/log with the following ~/.multitailrc:
colorscheme:amir_log
cs_re:green:INFO
cs_re:red:SEVERE

[chunk 284974] Another solution, if you're on a server where it's inconvenient to install non-standard tools, is to combine tail -f with sed or awk to add color selection control sequences. This requires tail -f to flush its standard output without delay even when its standard output is a pipe, I don't know if all implementations do this.
tail -f /path/to/log | awk '
 /INFO/ {print "\033[32m" $0 "\033[39m"}
 /SEVERE/ {print "\033[31m" $0 "\033[39m"}
'
or with sed

[chunk 284975] tail -f /path/to/log | sed --unbuffered \
 -e 's/\(.*INFO.*\)/\o033[32m\1\o033[39m/' \
 -e 's/\(.*SEVERE.*\)/\o033[31m\1\o033[39m/'
If your sed isn't GNU sed, replace \o033 by a literal escape character and remove --unbuffered.
Yet another possibility is to run tail -f in an Emacs shell buffer and use Emacs's syntax coloring abilities.
¹ The historical website vanished in early 2021. The latest version is still available in many distributions, e.g. Arch, Debian.

### item Tdba-191281
Site: dba | Thread title: SQL Profiler for Mac OS
[chunk 796758] No, but here's a few options:
Run a server-side trace. You don't get the Profiler GUI, but the good news is that this kind of tracing is faster. (Heck, I recommend this to folks even when they have Windows on the desktop.) SQL Server Central has a good Stairway to Server-side Tracing. Server-side traces can output to file or to table - I'd caution against writing the trace data into a table on the same server that you're monitoring because that'll have a performance impact.

[chunk 796759] Run Profiler in a VM. After all, if you're managing SQL Server, you probably need SQL Server Management Studio anyway, and that's still Windows-only. (That's how I manage SQL Server personally - I'm a Microsoft Certified Master of SQL Server, and I've been using Macs since the mid-2000s.)

[chunk 796760] Run sp_BlitzCache. The open source sp_BlitzCache analyzes the most resource-intensive queries in your plan cache - without starting a heavy-overhead trace or XE session. SQL Server is already gathering this data for you on every supported version/edition. Yes, right now, even as you're reading advice on a web site. You can run it from anything app runs T-SQL, like Microsoft's new cross-platform SQL Operations Studio. (Disclaimer: I'm one of the sp_BlitzCache authors.)

[chunk 796761] Use Extended Events instead.
(This isn't really a solution, but I know someone's going to suggest it, so might as well get it out of the way.
The Extended Events people are like vegans, crossfitters, and atheists: they can't wait to tell you about their religion.) Extended Events is the replacement for Profiler, but the thing is, if you're just getting started, you're going to want to use SSMS's excellent wizard for setting up a new XE session - meaning, you still need SSMS.

[chunk 796762] There's also a "Profiler" extension for Azure Data Studio, but...that's actually Extended Events.
Get a third party monitoring tool. If you need to know what's happening on your SQL Server on a regular basis, this is usually more lightweight than running Profiler. Plus, they have way more smarts built in to tell you what's been happening.

### item Tdevops-5010
Site: devops | Thread title: DevOps tools and automation of manual processes
[chunk 996412] Alright... you're not going to implement every tool or automation at the same time, as some of them have quite deep impact on your development processes (and I daresay, development culture). Take a step-by-step approach; research each individual tool. Figure out what it actually does, what it is useful for. Play around with them, install them locally, go through tutorials, and see what they do, or whip up a quick VM somewhere (AWS, etc.) if you need more than one.

[chunk 996413] Then, take a look at the work your team/company is doing right now. What are the manual process you wish to automate? Ideas should spring up pretty quickly.
A nice, simple(-ish), bog-standard stack to start out with:
Vagrant to automate setting up VMs for your developers, or test environments.
Ansible to automate configuration management (relatively lightweight compared with Chef or Puppet)
Gitlab or Jenkins as your automated CI/CD driver, mostly depending on taste
Docker for your containers

[chunk 996414] docker-compose, docker-swarm, Kubernetes, OpenShift to automate container deployment
ELK or Splunk for your logging/monitoring, again depending on taste
Have fun!

### item Tnetworkengineering-3843
Site: networkengineering | Thread title: OpenVPN Bridge on pfsense: once LAN pings clients, connectivity breaks
[chunk 972865] Turns out there was an implicit rule in the firewall defined on the bridge which dropped fragmented packets. This is not shown in the normal firewall overview.
I ended up turning off this 'feature' in the system ->advanced -> firewall/NAT section.

### item Tsecurity-197004
Site: security | Thread title: What should a verification email consist of?
[chunk 943050] How are you generating the 25 character string which you include in the URL? Is it completely random, or is it based off the current time, or the users email? It should be random and not guessable.
You should make sure the verification page actually renders (not just that a GET request occurred). Browsers such as chrome (and antivirus programs) often load URLs without the user explicitly clicking them as either a pre-fetch or to scan for security reasons.

[chunk 943051] That could result in a scenario where a malicious actor (Eve) wants to make an account using someone else's email (Alice). 
Eve signs up, and Alice received an email. Alice opens the email because she is curious about an account she didn't request. Her browser (or antivirus) requests the URL in the background, inadvertently activating the account.

[chunk 943052] I would use JavaScript on the page to verify the page actually rendered, and also include a link in the email where users can report that they did NOT create this account.

### item Tserverfault-353930
Site: serverfault | Thread title: Migrating from Windows Domain (SBS) to Macs (workstations and servers)
[chunk 112902] It seems like exchange is the sticking point here. If they could get their LOB app to work sans-exchange and use the OS X Server mail server instead, suddenly everything gets a lot simpler.

[chunk 112903] You need to communicate this to your client: that you are willing to support it, it is their decision to make, but that this has the potential to be a very expensive and frustrating venture if they end up unable to eliminate the exchange server. Emphasize that Exchange+Outlook provides additional services beyond a standard e-mail and calendar system that the OS X Server+Mac Office is not at this time able to replicate, namely connectivity to the core software the powers the business.

[chunk 112904] Therefore, your recommendation is that they proceed slowly at first: invest in exactly 1 mac w/ office at this time and not proceed further unless/until you can complete a successful integration of that mac with their LOB app (ie: get all those word/excel/outlook macros working in the mac version of office). Then, if things don't work well you can at least put bootcamp and windows back on the mac and not be out much.

### item Tsoftwareengineering-142953
Site: softwareengineering | Thread title: Is there a sequence to read through the Android developer site for a user new to Android?
[chunk 577205] After going through the developer site I believe that my original premise is correct. If you want a clear (guided even) overview of the topic, use some other source first.
I was able to use Android Boot Camp 2012 to get an overview of the topic. (Of course, it's not that great for reference back to later)
After that, I'm better able to read what's on the developer website and put the pieces into a good context.
This just in... Android Training, including some beginning training

### item Tunix-265656
Site: unix | Thread title: Decoding ASN.1 messages using Openssl asn1parse tool
[chunk 384297] That openssl command doesn't support ASN.1 schemas.
Looking at the openssl asn1parse man page the -genconf expects a file in a openssl specific serialization format:
-genstr string, -genconf file

[chunk 384298] generate encoded data based on string, file or both using ASN1_generate_nconf format. If file only is present then the string is obtained from the default section using the name asn1. The encoded data is passed through the ASN1 parser and printed out as though it came from a file, the contents can thus be examined and written to a file using the out option.
Also, -genconf isn't supposed to be used in combination with -in, cf. the man page examples:
openssl asn1parse -in file.pem
and:

[chunk 384299] openssl asn1parse -genconf asn1.cnf -noout -out asn1.der
Perhaps some of the confusion comes from different uses of terminology. In strict terms, ASN.1 is a schema language. An ASN.1 structure is thus a part of a schema. A schema specifies how valid documents are structured. With ASN.1 different document encodings are supported - i.e. the so called encoding rules (e.g. BER -> basic encoding rules, DER -> Distinguished Encoding Rules).

[chunk 384300] There are some people who don't make these distinctions. For example, they also call encoded files ASN.1 files. Or refer to an DER tag as an ASN.1 structure. Take for example the asn1parse man page:
The asn1parse command is a diagnostic utility that can parse ASN.1 structures

### item Tdba-18771
Site: dba | Thread title: Database Schema for an address book with different mailing lists
[chunk 723052] I would leave the data in a single table.
Actually, the data is normalized now in the sense that you have a single Person table.
That person is identified by a name, and the remaining columns are data about that Person.
Each column depends on the name and varies with the name, which means it is already in 3NF.
If you were building a large application, say a corporate application, then it might make sense to create tables for email, phone, address, etc.

[chunk 723053] But since this is just a simple mailing list I would keep it one table.
I don't think you have value in having a table for addresses or churches, for example, when neither of these have meaning to you other than as they relate to the current person.
Now if you had do have a lot of data about that address, or about that church, for example, then these "entities" would need to become tables to store the data about each address or church.

[chunk 723054] Say your mailing list has the church name, church address, pastor, and average attendance.
Now you have a reason to create a church table.
You have columns - address, pastor, average attendence - that depend only on church name, not person name.
But if all you have is church name there is really no benefit in this case of creating a church table that has just an id and a name.

[chunk 723055] One area where you might normalize would be to remove the repeating groups - the email(s) and phones(s) - into child tables.
But you could also create multiple columns - say 3 for each - and I'm sure that would be plenty for this application.
While not normalized, the only downside in doing this is if you need to store 4 (unlikely, and this is just a mailing list) you are out of luck.

[chunk 723056] It also makes the query more complicated in that if you want to return all the phone numbers you have to select each column instead of joining to the child email table.
Bottom line is that normalization is about removing redundancy. It sounds like you have very little redundancy in the mailing list to begin with and breaking individual columns in the current mailing list into their own tables, if there is are no columns for those tables other than an id and a name, would be overkill.

### item Tdevops-9267
Site: devops | Thread title: What is the difference between DevOps and GitOps?
[chunk 997403] GitOps is a technique of using Git to manage infrastructure provisioning and software deployments. This technique uses many of the features of Git such as Pull Requests to manage and trigger deployments, and allows "diffing" (looking at the difference between commits) to view the differences between deployments.

[chunk 997404] DevOps is more of a culture or philosophy. It is not tied to the specific tool Git. Instead, DevOps is the joining of Development (Dev) and System Operations (Ops). Often continuous integration and continuous deployment are big focuses of companies that invest in a DevOps culture.
A company that has a DevOps culture may choose to use a technique like GitOps to manage their infrastructure. They may choose to use other tools though.

[chunk 997405] Note: DevOps is not a process. It is a culture. GitOps is a specific System Operations (ops) process tied to a specific tool (Git). A company that uses GitOps may not have a DevOps culture. Conversely, a company that has a DevOps culture may not use GitOps.

### item Tnetworkengineering-24404
Site: networkengineering | Thread title: vlan 0, 1, and 4095 are reserved: what are they reserved for?
[chunk 977853] The Wikipedia article you mention gives a succinct explanation:
VLAN identifier (VID): a 12-bit field specifying the VLAN to which the
 frame belongs.
The hexadecimal values of 0x000 and 0xFFF are reserved.
All other values may be used as VLAN identifiers, allowing up to 4,094
 VLANs.
The reserved value 0x000 indicates that the frame does not
 carry a VLAN ID; in this case, the 802.1Q tag specifies only a
 priority and is referred to as a priority tag.

[chunk 977854] On bridges, VID 0x001
 (the default VLAN ID) is often reserved for a management VLAN; this is
 vendor-specific.
The VID value 0xFFF is reserved for implementation
 use; it must not be configured or transmitted.
0xFFF can be used to
 indicate a wildcard match in management operations or filtering
 database entries.
As you can see, there isn't really a usable VLAN 0 or 4095. Cisco uses VLAN 1 as a default VLAN, and management protocols (STP, CDP, DTP, etc) are sent on VLAN 1.

[chunk 977855] You can use VLAN 1 for simple installations where there is no VLAN trunking, but good practice is to not put user data on VLAN 1 in a multi-VLAN environment.

### item Tsecurity-15910
Site: security | Thread title: Why would salt not have prevented LinkedIn passwords from getting cracked?
[chunk 856387] Krebs follows up on this question, and Ptacek does clarify what he meant:
BK: Okay. So if the weakness isn’t with the strength of the cryptographic algorithm, and not with the lack of salt added to the hashed passwords, what’s the answer?
Ptacek: In LinkedIn’s case, and with many other sites, the problem is they’re using the wrong kind of algorithm. They use a cryptographic hash, when they need to use a password hash.
In the next couple of paragraphs, he also elaborates on the reasons for it.

[chunk 856388] The long and the short of it is that SHA1, with or without salt, is far too fast to be used as a password hash.
It is so fast, that when computed using a GPU or something similar, you can brute force 10s of thousands of hashes per second.
As is elaborated on later in the interview, LinkedIn should have been using bcrypt, which is an adaptive hash that would have slowed the brute force time down to the order of 10s of hashes per second.

### item Tserverfault-405414
Site: serverfault | Thread title: mongod fork vs nohup
[chunk 128171] The difference is that with
mongod --fork --logpath=/my/path/mongo.log
Mongo itself forks the process so it can run as a deamon. This is the intended way because mongo might probably do something before forking the new process.
With
nohup mongod >> /my/path/mongo.log 2>&1 < /dev/null &
Mongo does not know it is forked.
I'd say it is always better to let server software do the forking so it can make optimizations. NoHUP is just for software that does not have a forking option.

### item Tsoftwareengineering-225674
Site: softwareengineering | Thread title: Why define a Java object using interface (e.g. Map) rather than implementation (HashMap)
[chunk 612889] The reason is that the implementation of these interfaces is usually not relevant when handling them, therefore if you oblige the caller to pass a HashMap to a method, then you're essentially obliging which implementation to use. So as a general rule, you're supposed to handle its interface rather than the actual implementation and avoid the pain and suffering which might result in having to change all method signatures using HashMap when you decide you need to use LinkedHashMap instead.

[chunk 612890] It should be said that there are exceptions to this when implementation is relevant.
If you need a map when order is important, then you can require a TreeMap or a LinkedHashMap to be passed, or better still SortedMap which doesn't specify a specific implementation.
This obliges the caller to necessarily pass a certain type of implementation of Map and strongly hints that order is important.
That said, could you override SortedMap and pass an unsorted one?

[chunk 612891] Yes, of course, however expect bad things to happen as a result.
However best practice still dictates that if it isn't important, you shouldn't use specific implementations. This is true in general. If you're dealing with Dog and Cat which derive from Animal, in order to make best use of inheritance, you should generally avoid having methods specific to Dog or Cat. Rather all methods in Dog or Cat should override methods in Animal and it will save you trouble in the long run.