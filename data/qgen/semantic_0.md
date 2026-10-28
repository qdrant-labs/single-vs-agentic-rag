### item Tsecurity-43172
Site: security | Thread title: Evaluate the signature of an X509 certificate in .NET
[chunk 873252] X.509 certificate validation is a complex process. With .NET, you are supposed to use the X509Chain class to perform such a validation, which entails path building, verifying signatures, revocation status, and a gazillion of other things. See this answer for an example.

[chunk 873253] X509Certificate2 also has a Verify() method, but that one checks the certificate with regards to the machine defaults: the user's trust store, the user's policies... which may or may not map well to your specific case. To have full control on the process, use X509Chain.

[chunk 873254] (Extracting the signature value, and the exact byte sequence which is signed, is not overly complex if you know a bit of ASN.1/DER, but the point is that there is much more to certificate validation than mere signatures. Doing things manually is a path which I have personally walked several times, and it entails a lot of suffering. Using the implementation already provided by .NET will save you a lot of time; and that implementation is X509Chain.)

### item Tserverfault-808788
Site: serverfault | Thread title: Nginx wildcard/regex in location path
[chunk 219700] The = modifier in location block is an exact match, without any wildcards, prefix matching or regular expressions. That's why it doesn't work.
On your regex attempt, [a-z] matches a single character between a and z. That's why it doesn't work for you.
You need to have your locations set up like the following. Note the order of location statements. nginx picks the first matching regex condition.
location ~ ^/sitename/[0-9a-z]+/index.php$ {
 fastcgi_pass phpcgi;
}

[chunk 219701] location ~ \.php$ {
 return 404;
}
I use case sensitive matching here (~ modifier instead of ~*). In the first case, I match the first part of path, then one or more number of alphabetic / number characters and then index.php. You can modify the match range, but remember the + for "one or more" repetitions.
The second one matches any URI ending with .php. You don't need the extra characters in your version because of the way regular expressions work.

### item Tsoftwareengineering-6146
Site: softwareengineering | Thread title: Is mod_security a good thing?
[chunk 526932] I personally see mod_security as a patch. I use it on some of our servers where we can't control the code that's uploaded (shared hosting servers, for example), but it's never really felt like a good solution to me. Based on it's wide and very general blacklist approach, it's more of a patch to cover up security holes than a good security policy.

[chunk 526933] It can also provide a false sense of security. mod_security can reveal some common attacks but can by no means prevent any attack. Again, it's a blacklist of common known attacks. If you simply install mod_security and think that you're magically secure, you're horribly mistaken.

[chunk 526934] I have found a much better policy to me managed servers where my team reviews all code that is placed on them, combined with lots of logs, logfile analysis, reporting systems, and intrusion detection/intrusion prevention systems (IPS). Everytime third-party or open-source software is installed (I'm looking at you, WordPress!) we keep a log of where it was installed, and when new versions are released we update every copy that was installed.

[chunk 526935] Again, you're more likely to find mod_security on a shared hosting server, as you're experiencing now. As you grow you can move to a VPS or clod based hosting provider where you get your own managed environment and can more tightly control the available software.

### item Tunix-6938
Site: unix | Thread title: What does 'uni' mean in unistd.h
[chunk 284269] The stuff in there is largely Unix-idiom (chown, fork, gethostname, nice), so I'm guessing that it originally did mean Unix. It's part of the POSIX standard, though, so it's no longer just Unix.

### item Tdba-131399
Site: dba | Thread title: Is there a maximum length constraint for a postgres query?
[chunk 771445] For current PostgreSQL version (up to 9.5), queries are received by a backend in a Stringinfo buffer, which is limited to MaxAllocSize, defined as:
#define MaxAllocSize ((Size) 0x3fffffff) /* 1 gigabyte - 1 */
(see http://doxygen.postgresql.org/memutils_8h.html)
So a query is limited to 1 gigabyte (2^30) in size, minus 1 byte for a terminating null byte.
Should a client try to send a larger query, an error looking like this would come back:
ERROR: out of memory

[chunk 771446] DETAIL: Cannot enlarge string buffer containing 0 bytes by N more bytes.
where N is the size of the query.
Be aware that a query just below 1GB might require large amounts of memory to be parsed, planned or executed, in addition to that 1GB buffer.
If you need to push a large series of literals into a query, consider the alternative of creating a temporary table, COPY rows into it and have the main query refer to that temporary table.

### item Tdevops-2187
Site: devops | Thread title: Build FreeBSD Docker image using Ubuntu host OS
[chunk 995241] As you can't build a docker image for an arm kernel from a x86 one neither.
Nor can't you build an image with a glibc lib targetting a 4.x kernel on a host running a 3.X kernel.
Docker isolate processes and give a virtual filesystem but that's still the host kernel who own the process, so obviously without a layer of hardware virtualization like virtualbox, vmware, xen, kvm, there's no chance to build an image with binaries made for a different kernel type.

### item Tnetworkengineering-48228
Site: networkengineering | Thread title: ACL on trunk Port
[chunk 984636] Your mistake is that the trunk interface is a layer-2 interface, but you are trying to apply a layer-3 ACL. Layer-2 switching doesn't look at the layer-3 addressing, which is what your ACL is using. You need to apply the ACL to a layer-3 (SVI) interface.

[chunk 984637] The point of VLANs is that traffic cannot get from one VLAN to another VLAN, except through a router (or routing module in a layer-3 switch). A trunk keeps traffic in each VLAN separate, just as if you had separate physical switches, by tagging the frames with VLAN tags.
Routing will, by default, route traffic from one VLAN to another, but you can place ACLs in the routed interfaces (those with IP addresses assigned to them) to allow or block specific traffic.

[chunk 984638] You are using extended ACLs, so you should place them as close to the traffic source as possible.

### item Tsecurity-49319
Site: security | Thread title: Is a simple Whirlpool hash with random salt secure enough?
[chunk 876899] I'm not sure of the advantages of using one of these or why the current one is wrong. Does anybody mind explaining their reasoning?
Bcrypt CAN BE stronger than whirlpool, it depends on your strength setting. This is one of the most important advantages about bcrypt, that you can increase the strength as computers get more powerful, plus it's extremely difficult to crack using a GPU compared to simple SHA/Whirlpool hashes.

[chunk 876900] Since PHP 5.5, we've had bcrypt available as easy to use functions. To create a hash you would use password_hash($pass), you don't need to worry about salts because one is automatically generated and placed inside of the hash, because of this you need to use password_verify($pass, $hash) to check a hash, as generating a hash will use a different salt every time (and your strength settings could change).

[chunk 876901] There is almost no reason not to use this for a new application, as it's proven to be much much more secure than standard hashing algorithms. If you're on a version of PHP older than 5.5 there are a variety of libraries available to assist with this, most commonly ircmaxell's password_compat.

### item Tserverfault-247364
Site: serverfault | Thread title: Can I create SQL v10.0 databases in SQL R2 server?
[chunk 81155] Is there a way to create non-R2
 databases in an R2 database server?
No. Once a database has been attached to a version of SQL server, it can never be re-attached to a previous version, even if the compatibility level stays the same.
Am I only stuck with installing the
 non-R2 SQL server to run side-by-side
 with my R2 database server?
Yes.

### item Tsoftwareengineering-311003
Site: softwareengineering | Thread title: JsonAPI - Updating the relationship for a resource
[chunk 644879] If you want to change who the author is, that's a relationship on the article. You would patch /articles/:id and include the new author, as per the spec.

### item Tunix-75634
Site: unix | Thread title: How can a version of a package conflict with itself?
[chunk 315648] This kind of error messages can appear if you try to install a package whose previous installation got aborted without completing.
rpm by default won't install a package if any of the file it needs to install already exists in the filesystem.
So, if a previous installation aborted and some files were left behind, all succesive attempt will fail.

[chunk 315649] The error message is quite confusing because rpm will try to find out which package the problematic file belongs to and in this case, it's the very same package it tries to install.
The --force option tells rpm not to care and erase what it needs to perform the operation (that's why it may be risky, but if no other package claims the file, it's safe).

### item Tdba-211753
Site: dba | Thread title: How to let particular logins to work on the secondary replica only?
[chunk 804761] You can configure this by setting the "Connections in primary role" setting when configuring read-only routing. You have 2 options:
Allow all connections (default)
Allow read/write connections - which really means, "Connections where the Application Intent connection property is set to ReadOnly are not allowed. This can help prevent customers from connecting a read-intent work load to the primary replica by mistake."

[chunk 804762] This setting isn't configured at the login level though - this relies on what you said in the first part of your question, that your logins are using ApplicationIntent=ReadOnly in their connection string.

[chunk 804763] If they don't ask for that specifically - meaning, if they don't declare that they're only going to write - then SQL Server has no fast way of knowing that they have no writeable permissions in any database, on any object. After all, they could even execute a stored procedure signed with a cert, and that cert could allow them to do writes.

[chunk 804764] So if you really want to stop them from logging in even if they don't use ApplicationIntent=ReadOnly, then I'd do it by simply disabling their logins on the primary. Then, run an Agent job every minute on every replica, checking to see if this particular replica is a primary. If a failover has occurred, and this replica is now a primary, disable the reporting-only logins. If the replica is a secondary, and the reporting-only logins are disabled, then enable them.

[chunk 804765] This will of course run into problems if you really do want to disable someone's login - it'll instantly be enabled again in a minute.

### item Tdevops-1188
Site: devops | Thread title: Alarms management with Elasticsearch and Kibana
[chunk 994621] I have no experience with it myself, but Elastalert (http://elastalert.readthedocs.io/en/latest/elastalert.html) sounds like what you need (for the alarms/threshold part)

[chunk 994622] But besides that, it sounds like your interested in monitoring. In my opinion ELK is not a classic monitoring tool (more: data collection, data processing and data visualization). You should take a look at Icinga2 (https://www.icinga.com/products/icinga-2/) which can can be configured highly dynamical and is compatible with nagios plugins

### item Tnetworkengineering-53
Site: networkengineering | Thread title: Are CoS and QoS ever interchangeable?
[chunk 970993] QoS is an umbrella term which covers the use of features such as policing, shaping, traffic classification, and advanced queuing mechanisms.
CoS is a form of QoS limited to layer-2 Ethernet and it uses 3-bits (8 values) of the 802.1Q tag to differentiate your traffic. Therefore no trunking, no CoS.

[chunk 970994] DSCP is the most commonly acted upon value at layer-3 and it is found in 6-bits (64 values) of the IP header. Typically only 14 of the values are used and are referred to using the notations of best effort, expedited forwarding (EF), and assured forwarding (AF). AF values are in the form AFxy, where x is 1-4 and refers to the precedence and y is 1-3 and refers to the drop probability.

[chunk 970995] Telco vendors (such as AT&T specifically) use the term CoS to define the bandwidth allocation classes that they support in their MPLS offerings. Basically they turned CoS into a marketing term. Typically a Telco uses DSCP to know which of their CoS classes your traffic is supposed to be a part of.

[chunk 970996] Another important point for configuring these features is that in a Cisco switch or router you 
need to use a command such as 'mls qos trust dscp' or 'mls qos trust cos' or else the device will reset the QoS marking to zero.
There are some exceptions based on model, configuration, and IOS version but this has been true for everything within the last few years in my experience.

[chunk 970997] This configuration is required because the device needs to know which marking you want it to act upon since it cannot use both.
I like using DSCP.
I haven't found a solid reason to use CoS over it but I'm sure someone has one.

### item Tsecurity-105874
Site: security | Thread title: What happens if a (google authenticator) one time password QR code is leaked?
[chunk 903453] The QR code remains valid and usable; nothing will make it stop working.
This actually makes it very dangerous to leak the QR code.
If an attacker sees it, even years after you use it the first time, they can set up their own TOTP (Authenticator) app to use your code, and it will generate the same tokens yours does, which can potentially help the attacker hijack whatever account the TOTP code is protecting.

[chunk 903454] If it's something sensitive, you should generate a new code (this can usually be done by turning 2-factor auth off, and then on again).
Then, even if anybody got the old code, it won't do them any good.

### item Tserverfault-654293
Site: serverfault | Thread title: SNMP - snmpwalk does not return textual OIDs
[chunk 188619] Sounds like you are missing the MIB files that do the translation. To install them run:
apt-get install snmp-mibs-downloader
For licensing reasons they arent included by default. Installing that package will go download the standard ones from the internet. For specific manufactuer's custom SNMP values you will need to find their .mib files from the manufactuer's website.
Oh and you need to tell snmp to actually use the mibs! Edit /etc/snmp/snmp.conf to read:
mibs +ALL

### item Tsoftwareengineering-268145
Site: softwareengineering | Thread title: Are there real-life usage and applications for "do while" loops?
[chunk 628006] Real-world application, reading data from a file in blocks until end of file:
do
 result = readData(buffer)
while result != EOF
Without do-while you have to do something like
result = 0 # magic value that must not be EOF
while result != EOF
 result = readData(buffer)
or
while true
 result = readData(buffer)
 if result == EOF
 break
Both of which are uglier in my opinion.
When I mostly did C++ programming, I used the do-while all the time, in real, shipping applications.

### item Tunix-351261
Site: unix | Thread title: How to install the latest version of gcc and boost on an old version of openSUSE?
[chunk 409847] In theory you can recompile everything with supported version dependencies.
However this can involve a lot of grunt work and the fastest way to get things working is to get someone else to do the grunt work for you.
So, in addition to your normal system, install one or more distribution for development work.
This doesn't have to have a lot of overhead: you don't need to set up a virtual machine, a chroot environment will do fine.

[chunk 409848] Schroot is a handy tool to set up chroot environments with a different system but the same home directory.
I've written a guide for Debian-like distributions; you could follow this guide and install Debian unstable on SuSE, and this blog post by masterpatricko describes) explains a setup with a SuSE host.

[chunk 409849] For more fine-grained control of development tool versions, you could use the Nix package manager to install software in your home directory. Nix-user-chroot is a tool similar to schroot that lets you easily run software from a different (Nix-managed, in this case) installation.

### item Tdba-96610
Site: dba | Thread title: Sampling in PostgreSQL
[chunk 756810] In Postgres 9.3+, you can use the folowing:
select t.*
from 
 generate_series(1, 10) as x(i)
 cross join lateral
 ( select *, x.i
 from Table_Name
 -- where random() < 0.01
 order by random()
 limit 1 
 ) ;
which basically chooses 1 random row, 10 times.
In older versions, you can use a simple cross join (no lateral):
select t.*
from 
 generate_series(1, 1000) as x(i)
 cross join 
 Table_Name as t
 -- where random() < 0.01
 order by random()
 limit 10
 ) t ;

[chunk 756811] which creates a 1000-fold copy of the table (so each row is there 1000 times) and then chooses 10 rows with the same method as your query. If the number of copies (1000) is large enough compared to the wanted rows (10), the probabilities are almost equal to the probabilities you would have got with replacement.
Performance of this second query will of course be horrible, even with small tables.

### item Tdevops-838
Site: devops | Thread title: Where does CircleCI-2.0 store the ssh private keys?
[chunk 994420] I still don't get how your config.yml could launch ansible without a step part. Here is my findings, but I'm unsure it is what you're after, but that was too long for a comment.
According to the documentation here you have to add a add_ssh_keys with the fingerprint of your key as seen in the UI.
- add_ssh_keys:
 fingerprints:
 - "48:a0:87:54:ca:75:32:12:c6:9e:a2:77:a4:7a:08:a4"