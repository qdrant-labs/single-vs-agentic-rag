### item Udba-25105
Site: dba | Thread title: What does "*password------------" mean in a profile deadlock report?
It just means that the text of the statement contained the string "password" and SQL Server "helpfully" has masked it as a security feature to prevent you seeing some one else's password.
I was able to reproduce this as follows
CREATE TABLE T(X varchar(1000))
Connection 1
BEGIN TRAN
INSERT INTO T VALUES('password1')
WAITFOR DELAY '00:01:00'
SELECT * FROM T WHERE X = 'password2'
ROLLBACK
Connection 2
BEGIN TRAN
INSERT INTO T VALUES('password2')
WAITFOR DELAY '00:01:00'

SELECT * FROM T WHERE X = 'password1'
ROLLBACK
Then retrieving the graph from the extended events trace

### item Udevops-4065
Site: devops | Thread title: How to notate ipv6 addresses in inventory file?
This blog post covers all of the methods:
excerpt - Host names and patterns in Ansible 2
Inventory hostnames
Ansible 2 requires inventory hostnames to be valid IPv4/IPv6 addresses or hostnames (i.e., x.example.com or x, but not x..example.com or x--). As an extension, it accepts Unicode word characters in hostname labels. Any mistakes result in specific parsing errors, not mysterious failures during execution.

Inventory hostnames may also use alphabetic or numeric ranges to define more than one host. For example, foo[1:3] defines foo1 through foo3, while foo[x:z:2] expands to fox and foz. Addresses may use numeric ranges: 192.0.2.[3:42].
IPv6 addresses
A number of problems with the parsing of IPv6 addresses have also been fixed, and their behaviour has been made consistent across the inventory (.ini files) and in playbooks (e.g., in hosts: lines and with add_host).

All of the recommended IPv6 address notations (from spelling out all 128 bits to the various compressed forms) are supported. Addresses with port numbers must be written as [addr]:port. One can also use hexadecimal ranges to define multiple hosts in inventory files, e.g. 9876::[a:f]:2.

A couple of small but necessary bugfixes go hand-in-hand with the parsing changes, and fix problems with passing IPv6 addresses to ssh and to rsync. Taken together, these changes make it possible to use IPv6 in practice with Ansible.
Therefore patterns such as these IPv6's would be allowed:
fully specified 128 bit address
[addr]:port
hexadecimal ranges - 9876::[a:f]:2
various forms of compressing ranges - FF01::[1:6]
Simplified examples:

# IPv6 Address # Simplified Notation
----------------------------------------- ----------------------------
- FF01:0000:0000:0000:0000:0000:0000:0001 - FF01::1
- 2031:0000:130F:0000:0000:09C0:876A:130B - 2031:0:130F::9C0:876A:130B
- 0000:0000:0000:0000:0000:0000:0000:0001 - ::1
- FE80:0000:0000:5EFE:0192.0168.0001.0123 - FE80::5EFE:192.168.1.123
- FE80:0000:0000:0000:1585:4868:495F:D521 - FE80::1585:4868:495F:D521
References
NETWORK BASICS: IPV6 ADDRESS SIMPLIFIED NOTATION

### item Unetworkengineering-186
Site: networkengineering | Thread title: Migrating from VLANs to MPLS on JunOS
This looks like a simple layer two domain. MPLS is typically used only as backbone or distribution transit, that is, among routers. To implement MPLS, you would need to push the VLAN interfaces down to the access switches (and thus split Host5 into a new network or move it to switch 2) and run MPLS among the multilayer switches. Although, this wouldn't bring much benefit to the topology shown.

### item Usecurity-18513
Site: security | Thread title: Tracking unique web site visits without logging IP addresses
First of all: Why are you so concerned with not storing IP addresses? It's not private data; the OS or NAT router happily includes it with every sent packet. Okay it's kind of necessary, but what I mean is that they aren't really private. Also, random IPs are not really useful for hackers, and it's not a privacy concern when you can only see them yourself.
Secondly, it's not really useful to save IP addresses with the goal of counting unique visits.

Not only can one IP have hundreds or thousands of users (like schools), but a single user can also easily occupy a /16 subnet or two (many people's IP changes every few days or so), not to mention laptops and mobile phones.
A better technique would be session cookies, which are unfortunately restricted to the browser (and thus one device, so not counting people but the number of browsers really), but it's a lot better than IP addresses.

Lastly, if you still want to go with storing IP addresses, there are basically two ways:
Bloom filter, as mentioned before. This is not 100% correct though, but probably good enough for this purpose.
Using a hashing function which takes forever to compute. Sha-2'ing the IP a couple million times, it's impractical to brute-force it.

(There are about 3.7 billion globally usable and unique IP addresses, so if it takes 50ms to compute one hash, it takes 2.9 years before you have 50% chance of brute-forcing one of them, not taking Moore's law into account.)

### item Userverfault-476086
Site: serverfault | Thread title: Samba Winbind User Resolution
Now resolved, this worked for me:
Cleared all Winbind caches and flushed net cache.
Remember to take a backup before deleting anything!
Stop the Winbind and Samba services:
service winbind stop
service smb stop
Clear the Samba Net cache:
net cache flush
Delete the Winbind caches:
rm -f /var/lib/samba/*.tdb
rm -f /var/lib/samba/group_mapping.ldb
Start the Samba and then Winbind services - Note: The order is important
service smb start
service winbind start
Test it by trying to resolve a user.

### item Usoftwareengineering-322170
Site: softwareengineering | Thread title: Release first or document first?
Simple: Release a beta version! Then when documentation is done, do final release of the new version.
If you have users willing to try out the new stuff, then by all means take advantage of that. You will get bug reports, you probably get community questions about the difficult points so you know where to concentrate on the documentation, etc. You may also want to tweak some things based on user feedback, which may affect documentation.
Basically, everybody wins.

One reason to not do early release is, if you think your users will not be receptive of a "beta version", then you should think twice about doing it, but going by what you write, sounds like they would be happy about it.
Another reason would be, if there are technical difficulties about doing a beta release using whatever release channels you use.
Then it might be more hassle than it's worth to do separate beta and final releases.

If you think your software is complete, then in this case I'd lean on early release, update documentation when it's done.
Otherwise there's the risk that the documentation gets delayed, and then the whole release gets delayed or you end up releasing without final documentation anyway, so just do it now.

### item Uunix-168408
Site: unix | Thread title: Do different distros (but same kernel ver) have same hardware support
The short answer is no.
The driver support for the same kernel version is configurable at compile time and also allows for module loading. The actual devices supported in a distro therefore depend on the included compiled in device drivers, compiled loadable modules for devices and actual installed modules.

There are also devices not included in the kernel per se that a distro might ship.
I have not run into problems lately, but when I started with Linux at home I went with SuSE, although they had the same, or similar, kernel versions as RedHat, SuSE included ISDN drivers and packages "out of the box" (that was back 1998).

### item Udba-15269
Site: dba | Thread title: Monumental difference in execution time between queries when using RECOMPILE query hint
As documented in the article Statistics Used by the Query Optimizer in Microsoft SQL Server 2005
If you use a local variable in a query predicate instead of a
 parameter or literal, the optimizer resorts to a reduced-quality
 estimate, or a guess for selectivity of the predicate. Use parameters
 or literals in the query instead of local variables

When the optimiser has no usable statistics at all for a column it will guess that an = predicate will match 10% of rows, BETWEEN 9%, and any of >, >=, < and <= will match 30%. If there are column statistics available an = predicate will be treated differently as below.

Even when local variables are used in a query, an estimate that is
 better than a guess is used in the case of equality predicates.
 Selectivity for conditions of the form "@local_variable = column_name"
 is estimated using the average value frequency from the histogram for
 column_name. So, for example, if the column column_name contains all
 unique values, then a selectivity estimate of 1/(number of unique
 values in column) will be used, which is accurate.

So this is essentially the same as using for OPTIMIZE FOR (UNKNOWN). It may well be more accurate than a flat 10% guess but it isn't tailored to the specific values that you are querying.
To force SQL Server to optimize a query every time it is run, and use
 the values of local variables to estimate cardinality and cost during
 optimization of the query, add the RECOMPILE query hint to the query.

With the use of RECOMPILE you presumably are getting more accurate cardinality estimates and therefore a different plan with join orders/ join types more suited to the number of rows returned from different parts of your actual query.

### item Udevops-11979
Site: devops | Thread title: How to have jenkins add a review to a pull request
I guess the simplest and direct solution would be to use GitHub API: https://docs.github.com/en/rest/reference/pulls#create-a-review-for-a-pull-request
But for the requirement you have, PR checks is usually the way to go and you have a plugin that does the API communication for you: https://www.jenkins.io/doc/pipeline/steps/pipeline-githubnotify-step/

### item Unetworkengineering-3344
Site: networkengineering | Thread title: What are the different modes in Cisco routers, and why these modes?
Cisco's IOS uses the different EXEC modes as a basic way to control user privileges. These user privilege controls can be delegated through an enable password, the local user database or AAA (RADIUS, TACACS+).
The two EXEC modes are user mode and privileged mode.
user EXEC mode> is limited to an array of show commands, basic reachability tests, such as ping and traceroute, as well as other ways of viewing configurations and status info of a Cisco device without the ability to make changes.

privileged EXEC mode# is for users that have been delegated admin privileges and need to make changes, view more show commands and debugs as well as using the ability to move further down the configuration hierarchy (such as global configuration mode, interface configuration mode, MQC, etc).

Additionally, both the user EXEC and privileged EXEC modes are subject to further controls known as privilege levels. By default the user EXEC mode has a privilege level of 1(includes all user-level commands) and the privileged EXEC mode has a privilege of 15(full privileges).
Here is a nice visual along with more information.

### item Usecurity-73119
Site: security | Thread title: Can password_verify() be used to identify password after database breach?
password_verify() takes two arguments: a string of which you want to check if it's the correct password, and the value you calculated earlier with password_hash(), which you presumably stored somewhere in a database or so.
A typical application could be:
<?php
$hash = password_hash('my-secret', PASSWORD_DEFAULT);
// normally you would save the hash somewhere, but we'll just continue in this example

$check_a = 'other-secret';
$check_b = 'my-secret';
if (password_verify($check_a, $hash))
 echo 'Check A was the original password: ' . $check_a;
if (password_verify($check_b, $hash))
 echo 'Check B was the original password: ' . $check_b;
The output will be:
Check B was the original password: my-secret

If you want to get the original password from a hash calculated by password_hash(), you'll need to try all possibilities - that's what this example shows. Because of the architecture of password_hash(), finding a password like this will take a long time, so it's not worth it.
Note also, from the password_hash() doc:

PASSWORD_DEFAULT - Use the bcrypt algorithm (default as of PHP 5.5.0). Note that this constant is designed to change over time as new and stronger algorithms are added to PHP. For that reason, the length of the result from using this identifier can change over time. Therefore, it is recommended to store the result in a database column that can expand beyond 60 characters (255 characters would be a good choice).

The algorithm is designed to change over time, so that it stays secure, and finding a password by brute force won't become possible with faster computers (presuming, the PHP installation on your server is up to date)
In any case, a hash is one-way: you can't turn it around. You can only verify a given password by computing the hash of that one, and checking if it's the same.

### item Userverfault-64474
Site: serverfault | Thread title: When to add a domain controller at a remote location?
As I read the OPs post, there is only 1 data line to this remote site. If so, then the answer to my question below is most likely negative...
In my (limited) experience, it is not a matter of performance, it is a matter of uptime.

How much work could those remote users get done if the T1 is down, and what is the expected and worst-case reliability of that T1? Could a remote DC provide authentication and DHCP/DNS for the users so that a 'meaningfully large' set of applications would continue to be available, even if the T1 is down?

If the site is dead in the water as soon as the T1 is down, i.e. the remote users can't really get any meaningful work done without that data link, then a remote DC makes no sense IMHO. The same goes if the site has lots of meaningful work to do, but that work doesn't require any IT systems. But if the DC could enable the use of other IT systems, then it is valuable.

If you set up a remote DC, then think about Windows 2008's Read-Only Domain controllers, and consider moving other services closer to the users for performance.

### item Usoftwareengineering-76999
Site: softwareengineering | Thread title: Is there any value in Open sourcing your for fun projects
Sure!
Limited usefulness can be extended by others.
Others might need exactly the same sort of code or it could be used as teaching material.
Due to huge internet demographics there is sure someone who is interested.
On the other hand:
OpenSource code should be well documented or commented.
Code should be understandable and readable.
Code should be working.
Keep in mind:
Others may tidy up your code if they got your mind.
Others may optimize your code and teach you something.

### item Uunix-66007
Site: unix | Thread title: What is the difference between declare and typeset?
In bash, typeset and declare are exactly the same. The only difference is that typeset is considered obsolete.
typeset: typeset [-aAfFgilrtux] [-p] name[=value] ...
 Set variable values and attributes.
Obsolete. See `help declare'.
The man page even lists them in the same breath:
declare [-aAfFgilrtux] [-p] [name[=value] ...]
typeset [-aAfFgilrtux] [-p] [name[=value] ...]
 Declare variables and/or give them attributes.

typeset is portable to some other shells, for example, ksh93. If you are aiming for cross-shell portability, use typeset (and make sure that the way you are calling it is portable). If you don't care about such portability, use declare.

### item Udba-17433
Site: dba | Thread title: Oracle extents - How can I have so many with this small size?
The data you're getting from Toad appears to be incorrect or, at least, misleading.
If you are using a locally managed tablespace with automatic extent allocation, Oracle will determine your initial and next extent sizes automatically.
In 11.2, the first 16 extents are going to be 64k in size (for a total of 1 MB).
The next 63 extents are going to be 1 MB in size.
So if you have 26 extents, that implies that the table occupies 11 MB of space on disk.

An initial extent of 1.44 GB makes no sense and a size of 4.18 MB seems rather low if you're saying it hasn't shrunk.
What does
SELECT tablespace_name,
 extent_id, 
 bytes/1024 kb
 FROM user_extents
 WHERE segment_name = <<name of table>>
show you? If you have 26 extents, you should see that extents 0-15 are 64 kb in size and extents 16-25 are 1 MB in size.
SELECT SUM(bytes)/1024/1024 size_in_mb
 FROM user_extents
 WHERE segment_name = <<name of table>>

will show you the total size of the table's extents on disk.

### item Udevops-2408
Site: devops | Thread title: How to log outcome from multiple hosts in Ansible?
This question has two approaches, and both has answers on SO:
Convert all Ansible output to JSON with json stdout callback and parse it with your favourite tools. The eos_command output for each device will be under different host key in the resulting json.
See this and this.
Make run_once task to collect data from other hosts, like this:
- debug:
 msg: "{{ ansible_play_hosts | map('extract', hostvars, 'result') | map(attribute='stdout_lines') | list }}"
 run_once: yes
See this.

### item Unetworkengineering-51114
Site: networkengineering | Thread title: Is QoS an issue for VOIP calls over the Internet? If not, why not?
VoIP over the public Internet can be a problem, but it usually works good enough, most of the time, although there can be times where it sucks. Most ISPs have extra cost features where they will honor some of your QoS markings and policies.

(I know Verizon Business, among others, has some specific packages for QoS, and you may need to adjust your policies and markings sent to it to match one of its packages. We have a problem where we use multiple ISPs, and the QoS packages don't match between them, so we need to fine tune for the particular ISP, or pick a close enough package.)

The problem arises when the traffic must pass through other ISPs. You have no control over what happens in that case. The larger ISPs will have better (possibly direct) connections to many VoIP providers, as the VoIP providers will try to directly connect to the large ISPs or a Tier 1 ISP that directly connects to the large ISPs.
There may also be a possibility of having a VoIP provider, especially a telco like AT&T or Verizon, connect SIP trunks directly into your data center(s).

The big monkey wrench in the works today is the requirement for E911.
You, and the VoIP provider, will need to maintain a database of where each phone is connected so that emergency services will get not only the address of a 911 call, but the floor and section of the floor.

(We have spent large sums of money to meet the E911 requirements.) While this requirement is not necessarily in every state today, it is being phased in for all the states, and it is not something you can ignore if you don't yet have the requirement (it is far easier to put it in place as you roll out VoIP than it is to try to retrofit it at a later time).

### item Usecurity-2391
Site: security | Thread title: TLS replay attack - requirements of the serverHello nonce
Within SSL/TLS, the nonces are used for generating symmetric keys, and as part of the signatures and checks during the handshake. For all those usages, the nonces are simply concatenated (with some other data) and hashed. Assuming that the hash functions behave like "random oracles" (the mythical perfect hash function), then unique nonces are sufficient.

However, SSL/TLS up to (and including) TLS 1.1 uses MD5 and SHA-1 as hash function, for which weaknesses have been demonstrated. They are not random oracles. I am not aware of any result about turning these weaknesses into attacks on SSL/TLS itself; however, better be safe than sorry: use unpredictable nonces. This will not harm, and both client and servers must already have access to a cryptographically secure source of alea, hence unpredictable nonces should not be a too heavy requirement.

### item Userverfault-614171
Site: serverfault | Thread title: Share folder with realmd / sssd and AD integration
Answering my own question :
the only thing wrong was the valid users section in smb.conf - it appears that %S didn't work at all.
Thus, for a security group named "WebDevGrp" in Windows, on CentOS it will be shown as webdevgrp@mydomain.local ( you can test via groups myuser@mydomain.local ), and you can then make the Samba share like so :
[vHosts]
 comment = Virtual Host repository
 path = /var/www/vhosts
 public = no
 writable = yes
 guest ok = no
 valid users = @"webdevgrp@mydomain.local"

and you don't even get prompted for a password - it's all seamless!
PS. when debugging Samba, add log level = 3 to your config, makes a heck of a difference!.
PPS. I've written a guide to the whole process - going from vanilla freshly installed CentOS 7 to having Samba shares with AD authentication / authorization which you can find 
at my blog here

### item Usoftwareengineering-201972
Site: softwareengineering | Thread title: How to overcome programming by coincidence?
You don't have to think ahead, merely be very clear on what was done, and be very clear on what you are doing right now.
Subroutines should say what they do, do what they say, and not have hidden dependencies. Then someone calling them can more easily reason about what they will do.
Avoid global state. (Variables, singletons, etc.) The more state that you have to have in your head to understand what things do, the harder it is to understand what is supposed to happen and find the edge cases.

Write unit tests. Unit tests are great for capturing the actual behavior of code that you just wrote, rather than the ideal behavior that you are hoping to find.
Shorten your edit/compile/test cycle.
When you add a large chunk of code and test poorly, then the odds are that it will behave differently than you think.
Then you "fix" it with some random change, and you got the right answer for the moment, but have no idea how it actually happened.
You're now programming by coincidence.

But when you add 5 lines and then test, the odds that you got the right answer because it works like you think it works are much better.
I can say from experience that 5 chunks of 10 lines each, individually tested, is a very different beast than 50 lines of code tested all at once.
Refactor ruthlessly.
Many times I've spotted a refactor that will make my code somewhat simpler but take a bunch of work that I didn't want to do.

After I began deliberately tackling those refactors as a priority, I have found that it usually pays off for itself inside of a month.
But note the key, the refactors that I focus on are ones that make day to day life simpler, and not ones that meet some arbitrary aesthetic of better or more general.
Those refactors I've learned to be much more cautious with.

None of these things require advance planning. But they all make it easier to understand your existing code, and therefore make it easy to implement your next little chunk in a deliberate way.