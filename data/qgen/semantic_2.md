### item Tdevops-16149
Site: devops | Thread title: Can not authenticate to DockerHub docker.io with ctr; works fine with crictl
[chunk 999520] docker.io/library/$IMAGE:$TAG
The problem here is simple the right syntax for ctr isn't docker.io/alpine:latest but docker.io/library/alpine:latest that should now work with --creds "evancarroll:$TOKEN" too.
ctr images pull docker.io/library/alpine:latest
IRC logs
Thanks goes out to larks and ada on IRC #docker for helping out with this,

[chunk 999521] larsks> EvanCarroll: you probably need to include the tag there (ctr images pull docker.io/library/alpine:latest). The /library is there because that's the actual path to the image repository. There's some magic somewhere that transforms docker.io/alpine into docker.io/library/alpine; I don't know if that's client side or server side; ada will know much more about that than I do.
And thanks to @ada for showing where this is documented in the code, and clarifying

[chunk 999522] library/ is the namespace for all the top-level images on dockerhub with docker, that namespace is implied if you leave off the registry & namespace part of the tag : docker pull alpine == ctr images pull docker.io/library/alpine

### item Tnetworkengineering-7051
Site: networkengineering | Thread title: How do load balancers fit in to a data center with much higher throughput than they can handle?
[chunk 973726] Do the load balancers not become a bottleneck in certain traffic conditions?
Certainly, but this is generally not the case in a well engineered network.
You should be able to design your network in a way that would allow the majority of your internal server-to-server traffic ("east-west" as you put it) even if it does need to cross your core or between data centers.

[chunk 973727] While often the load balancer is the default gateway for the servers behind it, I have seen setups where a routing protocol (i.e. OSPF or RIP) is run to allow the "east-west" traffic to circumvent the load balancer, or in smaller deployments where static routes were used.
If the load balancers are going to be a bottleneck even in with a good design (i.e. the volume of traffic is just that high), then there are ways of load balancing across multiple load balancers as well.

### item Tsecurity-187042
Site: security | Thread title: Securing Apartment Wifi
[chunk 938344] Thank you to everyone for the comments and suggestions. After ordering a new router - I popped open the box and ran some longer cords out. I was able to use the internet connection just fine, and rename and secure my network.
Thanks to @Peter Harmann for the suggestion there - sort of a no brainer.

[chunk 938345] I also think @Josef's answer was the confirmation I needed to know that this problem does need to be solved and no one should be relinquishing control of their home network to their apartment complex. In general - they did a shitty job to boot. Thanks for the tips!
Installing my new router had some great side effects:

[chunk 938346] My internet speed went from 20mb up/down to literally 300mbps up, 250down. We have a fiber connection, but I was told it was throttled at 100mbps down, 50 up. Maybe they throttled this at the router? Either way its blazin now.
I was able to add a VPN to home network so I can access it remotely, including a connected HDD. (hell yeah!)
Improved my password of course, instead of using the default that came with the router (shame on the ISP)

[chunk 938347] I have complete access and control over my network, can monitor connected devices, etc etc.
Super happy with the result, and it feels good to see my network as a unique name among all the other units. Score one for the nerds!
PS - no routers were left hanging by the wire :)

### item Tserverfault-533893
Site: serverfault | Thread title: How well does elasticsearch compress data?
[chunk 160433] The answer is: it depends.
A blog post by Adrien Grand, who works on Elasticsearch did some benchmarking with this from the Lucene standpoint. It looks like he was getting about 2x improvement.
He also mentions LUCENE-4226, where some of this underlying compression work was done. There's a few benchmarks listed within, comparing the various compression algorithms tested.

[chunk 160434] As well, based on this Elasticsearch 0.19.5 release announcement, it appears that store-level compression defaults to LZF, with Snappy coming some time in the future. Further looking around showed that Snappy experimental support appeared in 0.19.9

### item Tsoftwareengineering-338384
Site: softwareengineering | Thread title: Do client functions need to be included in the UML diagram of a project which uses both object-oriented and procedural programming?
[chunk 657294] Do I need to add these client functions in the UML? If so, how should that be done?
The answer depends on what your purpose is for the UML.
Most people use UML for a high level overview aimed at future developers and maintainers. In that case, most of those details can be left out - and it is your choice which details to leave out.

[chunk 657295] If I do this, I might add a single box labelled "I/O Functions" without detailing which ones. Or I might create a separate diagram to detail them. But I certainly won't mention each and every function in a single diagram; Too many details will only cloud the picture.

[chunk 657296] If your purpose is to mention every single detail of your project in UML, then in essence you are writing code in a graphical way. Every attempt at that has failed, including UML. So I would strongly advice to rethink why you are using UML in that case. [1]
I'm sure there is an official place to put those details, but in practice barely anyone cares enough to remember where.

[chunk 657297] [1] Unless this is a course, and your teacher requires you to do this. In that case, put those functions wherever he says you should put them.

### item Tunix-59501
Site: unix | Thread title: Convert file path to URI in bash
[chunk 309091] One way to do this is using urlencode (install it on Ubuntu via sudo apt-get install gridsite-clients).
urlencode -m "$filepath"
will convert the path to an URI. The "file://" part of the URI will be left out, but you can easily add that via a bash one-liner:
uri=$(urlencode -m "$1"); echo "file://$uri"
or directly
echo "file://$(urlencode -m "$1")"
or
echo -n file://; urlencode -m "$1"
Many thanks to Michael Kjörling for the references!

### item Tdba-120748
Site: dba | Thread title: Can I find out which database is queried on the most?
[chunk 766634] You can use sys.dm_exec_sessions. This will only give you the count based on the current activity. You would need to store this historically if you wanted to trend it. Keep in mind that session ids of 50 or less are system sessions.
--By Database
select 
 db_name(database_id) DatabaseName
 ,count(session_id) as Session_count 
from sys.dm_exec_sessions
where
 session_id > 50
group by
 database_id

[chunk 766635] --By Login
select 
 login_name
 ,count(session_id) as Session_count 
from sys.dm_exec_sessions
where
 session_id > 50
group by
 login_name

### item Tdevops-10749
Site: devops | Thread title: Dockerizing a tool to test web apps?
[chunk 997900] You can dockerize/containerize pretty much anything fairly easily. You basically just have to add a Dockerfile that:
Inherits from some base image; this provides the basic OS features and whatever else you need. E.g. a Java app may inherit from alpine-jdk-8 (a slim linux type image) that comes pre-bundled with the Java Development Kit.
Copies in your code and any dependencies.
Sets any variables you require.
Exposes any ports your app needs (e.g. ports 80/443 for serving a web page).

[chunk 997901] Mounts any volumes to save permanent data. Generally anything in a container is ephemeral; it will be gone when the container dies. So, if you want to save/export results permanently you can mount a volume for, say, your local computer's file system, or for an amazon s3 bucket, or whatever.
Specifies how to start the app (the entry point).
Here's an example for arbitrary python scripts; but it's the same deal for any other language/tool:

[chunk 997902] https://runnable.com/docker/python/dockerize-your-python-application
If you're taking an existing executable which may be your case, you just do the same thing but instead of loading in your code, you load in the binary and set that as your entry point.
The container lives until the entry point program ends. So, some containers can be short lived - like just executing a CURL or something. Some are permanent until they die/are killed (e.g. a web service).

[chunk 997903] Again, to save state/results, unless you're writing them to a database or some other external system, you will want to mount a volume.
You build your Dockerfile into an image with a docker build command; then it will show up in your local docker image registry (docker image ls -a). After that, you can run it with a standard docker run command (where you will likely want to expose any ports/etc that are needed). I assume you're good with this one since you already run existing images in docker.

[chunk 997904] Generally you will need to store your image in a registry so you can use it on/from other systems. But if running it locally is all you need you're done now :).
You can store your own containers in DockerHub or in Amazon AWS ECR or in any other number of options if you require a registry.

### item Tnetworkengineering-13422
Site: networkengineering | Thread title: Command to power off (not reset) module in Cisco 4500?
[chunk 975234] To power off a particular module, use Switch(config)# no hw-module module _num_ power; you can find that command on Page 20 of this Cisco doc
FYI, there isn't a graceful shutdown command for the whole switch.
You should backup your config (just in case), issue a reboot, wait till you can audibly hear a change in fan speed, and then remove power before system starts booting.

### item Tsecurity-143349
Site: security | Thread title: Why does my password appear in clear text with my smartphone mail IMAP application?
[chunk 920140] It appears in cleartext because you don't use transport layer security (tls) when connecting to your mail host.
In order to change it, reconfigure your mail account on the galaxy (both the incoming and outgoing mail server) and choose ssl or tls for the security type field. You find this under the mail account's server options/server configuration. Depending on your mail host, it might also be necessary to change the suggested port number.

[chunk 920141] Not all mail providers support tls (and not all of them on the same ports, though usually the default ports the mail app suggests should work). If you're stuck with one that doesn't provide it, you have no choice but to transmit the cleartext password.

### item Tserverfault-282725
Site: serverfault | Thread title: Permission denied to remount tmp for exec
[chunk 91820] I have had the same trouble while trying to install PHP APC. I followed the instructions at the bottom of this guide: https://kb.mediatemple.net/questions/1987/Noexec+and+%7B47%7Dtmp+Troubleshooting#ve about creating a chrooted environment.
Hope this helps!

### item Tsoftwareengineering-277206
Site: softwareengineering | Thread title: Sometimes, "programming to interfaces" introduces possible (and avoidable) runtime exceptions?
[chunk 631891] Java does this in a few occasions and it is an abomination unto man.
This sort of thing is a textbook violation of the Liskov Substitution Principle, which leads to the sort of bugs you describe. Well written code does not do that.

[chunk 631892] You are right that making an interface for every single class is absurd. You need to use a little pragmatism in deciding what to make an interface for and what not to. The other thing to remember is that advice existed back in the C, C++ days. "Program to an interface" does not mean a literal interface in Java or C#. It works just as well with web apis or Internet protocols... Here an interface is a guaranteed/exposed behavior, not the underlying implementation.

### item Tunix-151623
Site: unix | Thread title: Service script calls another script with variables
[chunk 346856] You can use su with -c:
/bin/su tomcat -c "$CATALINA_HOME/bin/catalina.sh stop 30 -force"
From su man page:
-c, --command=COMMAND
 pass a single COMMAND to the shell with -c

### item Tdba-187436
Site: dba | Thread title: Locking on database from SELECT INTO #TempTable
[chunk 794933] I would expect the same behavior with or without the INTO. Remote queries run with default READ COMMITTED isolation level behavior acquire and release shared locks during execution just like local queries. Those locks can block writers of the remote tables, especially with poorly written queries and if shared table-level locks are held for the duration of the query.

[chunk 794934] Separately, the local SELECT INTO query consists of two separate transactions when run in autocommit mode. This is done to avoid holding long-term locks on the system catalog objects which could otherwise block object creation by other sessions. Creation of the new table is done in the first transaction and then the table is loaded using the remote query source in the second transaction.

### item Tdevops-2267
Site: devops | Thread title: Is Azure's confidential computing essentially encrypted RAM?
[chunk 995275] The article you are referencing mentions encrypted RAM but that was only a reference to possibilities of enhancing the technology more in the future, not about the current state of confidential computing.
Confidential computing means, that when data is in use these things are prevented:
Malicious insiders with administrative privilege or direct access to hardware on which it is being processed
Hackers and malware that exploit bugs in the operating system, application, or hypervisor

[chunk 995276] Third parties accessing it without their consent
according to Microsoft own announcement
So in other words, it is kind of equivalent to encryption and firewall that are seen in communication but this time applied to running programs in a Trusted Execution Environment (TEE), which the term for the area which is protected when server runs a program.

### item Tnetworkengineering-29168
Site: networkengineering | Thread title: How can a DHCP OFFER message be unicast?
[chunk 979199] While an address of 0.0.0.0 can be used as a source address for DHCP, it shouldn't be used as a destination address on the network. The server can send a unicast message since it knows the host's MAC address. Remember that all traffic delivered to the host is on layer-2, so the important address is the MAC address.

[chunk 979200] This is important because a DHCP server may not be on the same LAN as the requesting host. A DHCP Offer may need to be routed, via layer-3, back to the network where the requesting host is connected.
Edit:
Thanks to richarb for providing the link to Clarifications and Extensions for the Bootstrap Protocol:
3.1.1 The BROADCAST flag
Normally, BOOTP servers and relay agents attempt to deliver
BOOTREPLY messages directly to a client using unicast delivery.

[chunk 979201] The IP destination address (in the IP header) is set to the BOOTP
'yiaddr' address and the link-layer destination address is set to
the BOOTP 'chaddr' address.
Unfortunately, some client
implementations are unable to receive such unicast IP datagrams
until they know their own IP address (thus we have a "chicken and
egg" issue).

[chunk 979202] Often, however, they can receive broadcast IP
datagrams (those with a valid IP broadcast address as the IP
destination and the link-layer broadcast address as the link-layer
destination).
If a client falls into this category, it SHOULD set (to 1) the
newly-defined BROADCAST flag in the 'flags' field of BOOTREPLY
messages it generates. This will provide a hint to BOOTP servers and
relay agents that they should attempt to broadcast their BOOTREPLY
messages to the client.

[chunk 979203] If a client does not have this limitation (i.e., it is perfectly
able to receive unicast BOOTREPLY messages), it SHOULD NOT set the
BROADCAST flag (i.e., it SHOULD clear the BROADCAST flag to 0).
DISCUSSION:
This addition to the protocol is a workaround for old host
 implementations. Such implementations SHOULD be modified so
 that they may receive unicast BOOTREPLY messages, thus making
 use of this workaround unnecessary. In general, the use of
 this mechanism is discouraged.

### item Tsecurity-177362
Site: security | Thread title: Is anyone seeing a performance decrease after applying recent kernel patch fixing Meltdown and Spectre?
[chunk 934189] The performance impact will vary greatly depending on what the program does.
After the Meltdown patch (KPTI) whenever there is a context switch from user-space to kernel-space there is a significant overhead because of the frequent flushing of the kernel page tables.
So this means that a program that relies on frequent context switching (like a database or an hypervisor) will see a big performance impact, while others may hardly notice any.

### item Tserverfault-267578
Site: serverfault | Thread title: How to make SQL Server 2008 redundant?
[chunk 86925] is it through clustering or Log shipping or VMware (hypervisor) High Availability features ?
No, no, no.
MIRRORING, 3 servers (one can be a small free one, just deciding which keeps working active).
Log shipping is slowe / delayed, clustering / vmware leaves one database as weak point that still can be corrupted.

### item Tsoftwareengineering-29001
Site: softwareengineering | Thread title: Copyright issues with encryption algorythms
[chunk 533409] As stated before, algorithms are not copyrighted, only individual implementations.
Algorithms can be patented, however.
You should read the licensing information for your platform to ensure that you are in the purview of their license grants.
Presuming that you are, in effect, dynamically linking to an encryption library provided by the platform, you would not be distributing any encryption software at all, merely software that makes use of an existing capability.

[chunk 533410] This may reduce some headaches for you but, as always, you should consult an attorney to get competent answers (and someone to hold accountable if the answers are wrong!).

### item Tunix-124305
Site: unix | Thread title: Automate DISA STIG controls for RHEL/CentOS?
[chunk 336761] I have some scripts that are probably still "beta" from a project on GitHub by the RedHatGov organization (Red Hat, Inc. government sector employees).
https://github.com/RedHatGov
While their project is not complete, nor universally applicable, it is a great start and I plan on forking, contributing, and requesting pulls for the projects.

[chunk 336762] Frank Cavvigia of Red Hat has also made this script publicly available (by forking the code from other projects such as Aqueduct), which will modify a RHEL 6.4 .iso with many settings and requirements for DISA STIG compliance. This creates a new .ISO you can burn and use to install a system with many compliant options from the get-go.
http://people.redhat.com/fcaviggi/stig-fix/

[chunk 336763] I have tested this script, with minor modifications, on CentOS 6.5 and it has been somewhat successful. Someday when I get it cleaned up I will document and share my findings/changes.