### item Usoftwareengineering-443921
Site: softwareengineering | Thread title: How to apply TDD to very high level functionality?
TDD isn't limited to unit tests, it can be applied at any granularity.
What you're trying to do is covered by acceptance test-driven development (ATDD) which adds an outer loop to the classic red-green-refactor cycle: you write a failing acceptance test first which should help you come up with a skeleton of your overall program, then you write failing unit tests before finally implementing the actual logic.

The acceptance tests ensure that you are building the right thing and your various components are wired together correctly, while the unit tests ensure that your components are implemented correctly.
There is an excellent book on this topic called Growing Object-Oriented Software, Guided by Tests that goes into detail about this process and includes a worked example of a GUI application built from scratch using TDD.

### item Uunix-342527
Site: unix | Thread title: Why are there nulls in /var/log/kern.log?
Log messages are prepared internally as null-terminated strings. Since a null byte terminates the message, it's impossible to have one inside the message.
Finding null bytes in the log file indicates a bug somewhere, either in your software or in your hardware. Given that you're experiencing problems with the device that the logs are sorted on, these problems are likely the source of the problem with the log.

Tracing the exact way in which such symptoms relate to the root cause can be difficult. Since your storage setup is suspected of data corruption, I recommend that you stop relying on it and look for a replacement. If you make a last-minute backup, beware that some of your data may already be corrupted, so don't overwrite your existing backups.

Before you replace the SSD, keep in mind that such problems could also be due to a bad connection, so check your cables. RAM could also be the culprit, so do a memory test.

### item Udba-191979
Site: dba | Thread title: Best Data Type to Store Result of HASHBYTES('MD5', ...)
According to Books Online:
The output conforms to the algorithm standard: 128 bits (16 bytes) for
 MD2, MD4, and MD5; 160 bits (20 bytes) for SHA and SHA1; 256 bits (32
 bytes) for SHA2_256, and 512 bits (64 bytes) for SHA2_512.

So despite the fact that the function technically returns varbinary(8000), you'll only ever get 16 bytes with MD5. If you are completely certain you only need MD5, then a binary(16) will do it. If you want to play it safe, and allow any possible algorithm (current or future) that HASHBYTES can handle, go with varbinary(8000).
I definitely wouldn't recommend a char type, since that will involve string conversion overhead, and unnecessary storage overhead.

### item Udevops-2388
Site: devops | Thread title: Monitor program progress on multiple servers
Any time you're running ad-hoc long-running commands, you should step back and rethink your process, because that should be automated, including error handling.

Rather than connecting in to the servers to see status, a better approach is to push that information out. You can do a wide variety of things if your want to write a bunch of custom code, but the simplest thing is probably to start sending the output through syslog to a centralized logging system (syslog itself, or ELK, or whatever). That way you can monitor everything from a central location.

Thinking forward, if this isn't a one-off task, monitoring should be automated. That is, you should never have to just watch logs to see if things are progressing as they're supposed to. Instead, you should assume they are (and continue with other work) until your alerting fires off. This is an investment of time into getting reliable and wide-coverage alerting, but as your systems grow in complexity, it will pay off as you don't have to monitor everything any time you change anything.

### item Unetworkengineering-7836
Site: networkengineering | Thread title: Enable traps on FIB (Forwarding Table) changes
CEF-MIB wasn't added to the cisco MIB until iOS relase 12.2(31)SB so you will need that version or higher before you can alert on CEF.
However it doesn't look like CEF-MIB ever made it to the 2600 series platform, at least as of 12.3(6f). I also looked through various iOS images for the 2600 series and could not find CEF-MIB. Needless to say without the needed OIDs present, you will not be able to alert specifically for CEF.
MIB Instance Identifiers for CEF:
cefResourceFailureNotifEnable.0 -i 1

cefPeerStateChangeNotifEnable.0 -i 1
cefPeerFIBStateChangeNotifEnable.0 -i 1
cefInconsistencyNotifEnable.0 -i 1
You can check for CEF instance identifiers with the following command:
Router# show snmp mib | inc cef
Sources:
http://www.cisco.com/c/en/us/td/docs/ios/12_2sb/feature/guide/sbcefmib.html#wp1072297
To find specific MIB information on your device and available images, you can use Cisco's MIB Locator tool to see if CEF-MIB is available.
http://tools.cisco.com/ITDIT/MIBS/servlet/index

### item Usecurity-177133
Site: security | Thread title: Reducing resolution of timers as mitigation against Meltdown and Spectre
The reason it is only applied to browsers is because there is no way to fully eliminate high-resolution timing information from code being natively executed.
For example, the RDTSC instruction provides precise, sub-nanosecond resolution timing information to any process.
While it is possible to disable this instruction by making it executable only by privileged code (by setting the CR4.TSD bit), much of userland relies on it.

However even if you did successfully disable it without breakage, a timer of similar resolution could be jerry-rigged by incrementing a variable in a fast loop.
Userspace code will always have nanosecond-precision timing information.
Such a timer could be implemented easily:
#include <pthread.h>
volatile unsigned long counter = 0;
static void *counter_thread(void *arg)
{
 while (1)
 counter++;
}

static void __attribute__((constructor)) init_counter(void)
{
 pthread_id id;
 pthread_create(&id, NULL, counter_thread, NULL);
}
unsigned long get_counter(void)
{
 return counter;
}
Loading this sample library starts a new thread that rapidly increments a variable. It exports a function get_counter() that returns the current value of that variable at the time it is called. The counter is incremented at a very high and fairly steady rate, providing a high-resolution timer similar to RDTSC.

As a result, there is no way to hide precise timing information from machine code executing on the CPU.
It is sometimes possible in JavaScript because it is a managed, high-level language which does not have raw access to CPU instructions, and timing must go through dedicated APIs such as performance.now() which can have its granularity adjusted by modifying the JavaScript engine.

Note that this is not always sufficient, as a number of other techniques exist which can be used to implement high-resolution timers in JavaScript.
Some of these additional techniques have been mitigated, but not all.
Disabling JIT can drastically reduce timing attacks in JavaScript.

### item Userverfault-459948
Site: serverfault | Thread title: How to change vCenter server appliance IP from command line?
I found a comfortable way of doing this here:
Allocate a static IP address to the VMware vCenter Server Appliance (VCSA) | Ivo Beerens' Blog
It also allows you to change hostname, DNS, default gateway and proxy.
To sum it up:
Open a console session of the VCSA
Login as: root
Default password is: vmware
Execute the following command: /opt/vmware/share/vami/vami_config_net

After executing the command, a
menu is displayed. Within the menu It is possible to change the IP
address, hostname, DNS, Default gateway and proxy server.
After allocating a static IP Address to the VCSA, the post configuration can be done by using the following URL:
https://static-ip-address:5480

### item Usoftwareengineering-133495
Site: softwareengineering | Thread title: What's the simplest example out there to explain the difference between Parse Trees and Abstract Syntax Trees?
A parse tree is also known as a concrete syntax tree.
Basically, the abstract tree has less information than the concrete tree. The concrete tree contains each element in the language, whereas the abstract tree has thrown away the uninteresting pieces.
For example the expression: (2 + 5) * 8
The concrete looks like this
( 2 + 5 ) * 8
 | \ | / | | |
 | \|/ | | |
 \___|__/ | |
 \______|/
Whereas the abstract tree has:
2 5 
 \/ 
 + 8
 \/
 *

In the concrete cases the parentheses and all pieces of the language have been incorporated into the tree. In the abstract case the parentheses are gone, because their information has been incorporated into the tree structure.

### item Uunix-107939
Site: unix | Thread title: How to restart the Python script automatically if it is killed or dies
On Ubuntu (until 14.04, 16.04 and later use systemd) can use upstart to do so, better than a cron job. You put a config setup in /etc/init and make sure you specify respawn
It could be a minimal file /etc/init/testing.conf (edit as root):
chdir /your/base/directory
exec python testing.py
respawn
And you can test with /your/base/directory/testing.py:
from __future__ import print_function
import time
with open('/var/tmp/testing.log', 'a') as fp:
 print(time.time(), 'done', file=fp)
 time.sleep(3)

and start with:
sudo start testing
and follow what happens (in another window) with:
tail -f /var/tmp/testing.log
and stop with:
sudo stop testing
You can also add [start on][2] to have the command start on boot of the system.

### item Udba-12715
Site: dba | Thread title: Having a unique ID for 2 different tables
This should do it I think.
CREATE TABLE Foo 
(
FooId INT PRIMARY KEY,
Active BIT NOT NULL,
UNIQUE(FooId, Active)
)
CREATE TABLE FooActive 
(
FooId INT PRIMARY KEY,
Active AS CAST(1 AS BIT) PERSISTED,
FOREIGN KEY (FooId, Active) REFERENCES Foo(FooId, Active)
)
CREATE TABLE FooInActive 
(
FooId INT PRIMARY KEY,
Active AS CAST(0 AS BIT) PERSISTED,
FOREIGN KEY (FooId, Active) REFERENCES Foo(FooId, Active)
)

### item Udevops-513
Site: devops | Thread title: How to implement a frozen test environment?
My answer in the context of the question is a very expensive test environment (like mainframes or very large telecom equipment, for example) which are expected to be shared by multiple users for multiple tests, even simultaneously.

In many cases such equipment has a software management system responsible for, among other things, controlling software (un)installation/upgrades/downgrades/etc. Which should have some mechanism for blocking such operations (which would be, if I understood the question correctly, equivalent to freezing the environment) based on some more or less programmable policies.

In such case a specific policy could be developed exactly to support the desired freezing schedule necessary for the test environment. Ideally automated, accepting freezing/thawing triggers from the external sources which could be the test execution wrappers or CI systems. And maybe with human-triggered overrides, if deemed necessary.

Of course, such feature of the software management system would be helpful when testing other components of the equipment, but maybe not for tests of the software management system itself.

### item Unetworkengineering-58126
Site: networkengineering | Thread title: What exact does MIB represent in SNMP? How is it different from OID?
The MIB is the entire catalog of OIDs (for a particular device).
An OID is a specific reference to an individual item within the MIB.
An analogy: The MIB is like the phone book for my city. The OID is like my name in the phone book.

### item Usecurity-152935
Site: security | Thread title: Why is there no adoption of RFC 7616 (HTTP Digest Auth)
Most sites don't use any of the HTTP authentication mechanism, i.e. Basic Authentication or MD5 based Digest Authentication, because these mechanisms are very limited in what they offer. It is not even possible to logout using these authentication mechanisms.

But even the few sites which use HTTP authentication usually prefer basic authentication over HTTPS instead of digest authentication, since the last one requires that the passwords are stored at the server as plain text or equivalent, which of course is bad from a security perspective.
Thus the only advantage digest authentication has against other authentication forms is if is used with unencrypted connections.
In all other cases it is worse than the other established ways of authentication.

But, any kind of login over insecure connections is considered bad anyway today.
Therefore there is no need to slightly improve an already bad authentication mechanism without addressing the basic problems of it, i.e.
the necessary plain text (or plain text equivalent) storage of the password.

Apart from that the weaknesses of MD5 like a bad resistance against collision attacks and pre-image attack don't really affect its use in Digest authentication, i.e. it is still suitable for this use case when used together with a proper random server defined nonce.

### item Userverfault-348019
Site: serverfault | Thread title: SAS Expanders for DIY JBOD Arrays
I do not know about the MD1000, but probably they will be using some custom-made PCBs to have an expander run without a mainboard.
The SAS expanders usually will need the mainboard / PCIe slot for power supply only, so theoretically, you could use any mainboard, even without a CPU. There is this rather well documented DIY-JBOD project where an industrial PCIe PCMIG backplane (originally used for slotting SBCs but obviously providing power to any PCIe card) has been used instead of a full board:

### item Usoftwareengineering-8257
Site: softwareengineering | Thread title: Load Test Methodology for a cache
Do you have a way to reset the data once the test is run (if this is even necessary)?
If so, what about running the non-random test first - to look for failures when run that way (and possible anomalies caused by the data itself)? Then, after resetting (if necessary), run the random tests to reflect the real world load.

### item Uunix-485857
Site: unix | Thread title: Add lines to files to make them equal length
Thanks @Sparhawk for the suggestions in the comments, I update based on those,
#!/bin/bash
emptyLine=;;;;;;;
rr=($(wc -l files*pattern.txt | awk '{print $1}' | sed '$ d'))
max=$(echo "${rr[*]}" | sort -nr | head -n1)
for name in files*pattern.txt;do
 lineNumber=$(wc -l < $name)
 let missing=max-lineNumber
 for((i=0;i<$missing;i++));do
 echo $emptyLine >> $name
 done
done

Well, not elegand nor efficient. Actually, it takes a couple of seconds which sounds an eternity given the small size of the data. Nevertheless it works,
#!/bin/bash
emptyLine=;;;;;;;
rr=($(wc -l files*pattern.txt | awk '{print $1}' | sed '$ d'))
max=$(echo "${rr[*]}" | sort -nr | head -n1)
for name in $(ls files*pattern.txt);do
 lineNumber=$(cat $name | wc -l )
 let missing=max-lineNumber
 for((i=0;i<$missing;i++));do
 echo $emptyLine >> $name
 done
done

I just put this file together in the directory where I have the files provided that there is a pattern I can use to list them with files*pattern.txt

### item Udba-28556
Site: dba | Thread title: Manually increase PostgreSQL's table size limit of 32 TB?
Just use a different setting for the block size:
--with-blocksize=BLOCKSIZE
The default, 8 kilobytes, is suitable for most situations; but other
 values may be useful in special cases. The value must be a power of 2
 between 1 and 32 (kilobytes).
Using 32 kilobytes, your table has a maximum size of 128TB.

### item Udevops-366
Site: devops | Thread title: Load balancing Nexus artifact repository
Sonatype's Nexus 3 Pro supports High Availability through a couple of mechanisms that are collectively known as Component Fabric:
Peer-to-peer Repository Managers means there is no one master, also known as a single point of failure. Packages are replicated between the nodes to ensure they are eventually consistent.
Storage Backends mean you can use high durability storage such as S3.

Dynamic Nodes enable auto-scaling support to increase capacity when demand is high and decrease it when demand is low to reduce costs.
It's not really in Sonatype's interests to support HA for the community project as it would cannibalize some of the enterprise customers from their paid product.

### item Unetworkengineering-1280
Site: networkengineering | Thread title: Difference between LLDP and LLDP-MED
Media Endpoint Discovery is an enhancement of LLDP, known as LLDP-MED, that provides the following facilities:
Auto-discovery of LAN policies (such as VLAN, Layer 2 Priority and Differentiated services (Diffserv) settings) enabling plug and play networking.
Device location discovery to allow creation of location databases and, in the case of Voice over Internet Protocol (VoIP), Enhanced 911 services.
Extended and automated power management of Power over Ethernet (PoE) end points.

Inventory management, allowing network administrators to track their network devices, and determine their characteristics (manufacturer, software and hardware versions, serial or asset number).
The LLDP-MED protocol extension was formally approved and published as the standard ANSI/TIA-1057 by the Telecommunications Industry Association (TIA) in April 2006.

### item Usecurity-184344
Site: security | Thread title: Why use usernames and not just email addresses to identify users?
Your question is missing a lot of context, but what you do say sounds like you’re looking to settle an argument. So my answer will start with “It depends...”
One reason to have unique usernames that aren’t email addresses is to protect privacy when other users can see the username. For example, GitHub profiles indicate the username in the profile URL, and as authorship indicators on commits, issues, comments, etc.

Providing a username as the user’s public face instead of their email address allows them a layer of privacy.

In some rare cases, a service may elect not to collect email addresses at all... since email addresses can be considered sensitive and personally identifiable information. The downside to not collecting an email address at all is that account recovery for someone who forgets their password, or has their account breached, will be more difficult without a verified channel to use for recovery.

Or for the hybrid approach, one might collect
the email address, but store it in the database behind strong encryption. Strong encryption is generally difficult to search on, so having a less sensitive identifier to use that can be store in plaintext would be convenient.