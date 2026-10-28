### item Tunix-290235
Site: unix | Thread title: Generate line number / "index" within a range from a date seed value
[chunk 392067] A somewhat different solution: Scramble the lines in your text files with a cron job every day. Your script then picks the first line.
Cron job (requires a sort that can "sort" data randomly with -R):
0 0 * * * sort -R -o wotd_data.txt wotd_data.txt
Or, if your cron understands @daily (see man 5 crontab):
@daily sort -R -o wotd_data.txt wotd_data.txt
Script:
head -n 1 wotd_data.txt
Full paths to wotd_data.txt are obviously required.

### item Tdba-87327
Site: dba | Thread title: How to organize database for translations, performance?
[chunk 753870] Generally, it's better practice to encapsulate the data as you did in your second approach.
This is because...
When a fully normalized database structure is extended to allow it to accommodate new types of data, the pre-existing aspects of the database structure can remain largely or entirely unchanged. As a result, applications interacting with the database are minimally affected.

[chunk 753871] By following this tenant of normalizing, it's far easier to add, update, or remove rows to a table than it is to alter the table by adding/removing columns. Languages may change over time, but the table ideally should stay the same and not need to be in flux to accommodate changes in the data.

### item Tdevops-2149
Site: devops | Thread title: How to know which user created the GCE Instance
[chunk 995218] Note: I'm not a GCE user yet, the answer is based solely on documentation.
You could be Viewing Audit Logs in the Google Cloud Console, more specifically the Admin Activity logs:

[chunk 995219] Admin Activity logs contain log entries for API calls or other
 administrative actions that modify the configuration or metadata of
 resources. For example, the logs record when VM instances and App
 Engine applications are created and when permissions are changed. To
 view the logs, you must have the IAM roles Logging/Logs Viewer or
 Project/Viewer.
You would be looking for the User identities in audit logs:

[chunk 995220] Audit logs record the identity of the user performing logged actions.
 The identity is held in the AuthenticationInfo field of AuditLog
 objects.
Ideally you'd be looking for the GCE instance creation events, but some/all of those may be too old for the logs retention policy. Then maybe search for VM instance start or other relevant events.
You could also check and maybe cross-reference the audit logs info with that from Usage Reports or exported billing info.

[chunk 995221] If this is a regular, on-going activity you may want to setup an automated log exporting and processing pipeline.

### item Tnetworkengineering-16131
Site: networkengineering | Thread title: Why bb:bb:bb:bb:bb:bb is non-unicast mac address?
[chunk 975498] The least significant bit (LSB) in the MAC-Address is the Individual/Group type specification. IEEE 802.3 specifies the MAC-Address like this (with LSB first):
+---------+---------+----------------+
| I/G Bit | L/G Bit | 46-Bit Address |
+---------+---------+----------------+

[chunk 975499] I/G Bit: If this bit is 0, it shall indicate that the address field contains an individual address. If this bit is 1, it shall indicate that the address field contains a group address that identifies none, one or more, or all of the stations connected to the LAN. In the Source Address field, the first bit is reserved and set to 0.

[chunk 975500] L/G Bit: The second bit shall be used to distinguish between locally or globally administered addresses. For globally administered (or U, universal) addresses, the bit is set to 0. If an address is to be assigned locally, this bit shall be set to 1. Note that for the broadcast address, this bit is also a 1.

[chunk 975501] When you convert the first byte of your address bb into binary, you get 10111011. Here the LSB is last, so the last bit in the first octet/byte is the I/G bit, which is 1. This makes your MAC address a group MAC address which your router rejects. If you use aa, you get 10101010 where the last bit is 0, making this an individual (unicast) MAC-Address.

[chunk 975502] To make your MAC-Adress unicast and also make clear that you've locally assigned it (and to prevent MAC collision) you should use an address where the I/G bit is turned off and the L/G bit is turned on. This means one of the following addresses:
X2:XX:XX:XX:XX:XX
X6:XX:XX:XX:XX:XX
XA:XX:XX:XX:XX:XX
XE:XX:XX:XX:XX:XX
You can use any hex value you want for X.

### item Tsecurity-5955
Site: security | Thread title: Truecrypt hidden partition deleted original drive data
[chunk 848790] Based on what you say, I believe that you formatted your outer partition when creating the inner "hidden" partition. If I recall how Truecrypt works correctly, there is no metadata that allows it to look at a container and say "Oh, this has a hidden partition" in it. If that metadata existed, then others could tell a hidden partition was there, and it wouldn't be hidden.

[chunk 848791] As a result, when you enter the password to mount a partition, it applies that password. Bad passwords unlock nothing. The "outer" password unlocks the outer partition, and the info for that partition is all that Truecrypt sees. The "inner" password unlocks the hidden partition, and the info for that partition is all that Truecrypt sees.

[chunk 848792] I think that what happened is that Truecrypt created the inner partition, then went to open it for formatting, but because of the way hidden partitions work, it just tried the password which happened to unlock the outer partition instead, since they both used the same password. And it then proceeded to format that outer partition, thinking it was the hidden partition and not knowing any better.
Condolences.

[chunk 848793] Also, you should know: the last time I checked, you could not modify contents of an outer partition without possibly corrupting the inner partition (again, obviously, if the outer partition knew which blocks were "hidden", they wouldn't be hidden, would they?) So you shouldn't store things you actually use (add files, edit files, etc) in the outer half of a hidden partition pair.

[chunk 848794] [edit] It's also possible you're mounting the "hidden" partition when you're trying to mount the outer, and that's why it appears empty. Check the filesystem size and see if it matches the outer or inner size that you set. If this is the case, your data probably still exists, but you have to get to it, better to ask at truecrypt forums for that.

### item Tserverfault-822135
Site: serverfault | Thread title: How to start a program when CPU percent reaches X
[chunk 222232] Never did it, but easiest way would be by using alert in perfmon.
As you can see below, you can run a script when the action happen.
Select the Action tab, shown in Figure 3-18. You can now specify any
 of the following actions to happen when an alert is triggered:
 Log An Entry In The Application Event Log Creates log entries for alerts.
Send A Network Message To Sends a network message to the computer specified.

[chunk 222233] Run This Program Sets the complete file path of a program or script to run when the alert occurs.
More info there to set the alert
after in your script you could run it that way;
procmon /Quiet /Minimized /BackingFile log.PML
TIMEOUT /T 120
procmon /Terminate

### item Tsoftwareengineering-152733
Site: softwareengineering | Thread title: What is the term for a really BIG source code commit?
[chunk 581680] (1) Ben Collins-Sussman: "... "code bombs". That is, what do you do when somebody shows up to an open source project with a gigantic new feature that took months to write? Who has the time to review thousands of lines of code? ..."
(2) Dan Fabulich: "The Code Bomb, or: The Newbie with Big Ideas ... A code bomb is a patch that's so large that no one can review it."

[chunk 581681] (3) Google Summer of Code: Guidelines: "Commit early, commit often ... Please do not work the whole day and then push everything out in a single code bomb. Instead, every commit should be self-contained to one task only which should be summarized in the log message."
(4) Jeff Atwood: "code-bombs ... Rule #30: Don't go dark. ...

### item Tunix-388596
Site: unix | Thread title: The difference between nscd and sssd
[chunk 419935] The nscd is a daemon that provides a cache for the most common name service requests like passwd, group, hosts, service and netgroup.
sssd primarily provides daemons to manage access to remote directories and authentication mechanisms like LDAP, Kerberos, NIS, etc...so it is more about authentication and authorization. It does have its own caching mechanism e.g. for users and groups but there are some more. Consult the manpage of sssd.conf for further details.

[chunk 419936] As in the linked article explained, sssd and nscd should not be used at the same time as it can result in unexpected lookups. If you need nscd e.g. for caching hosts entry, which sssd does not cache, it is recommended to configure nscd only for hosts and rely on user, group, etc. caching on sssd.
I think the cases you need to run both services are very rare, since the hosts caching is the only entry that sssd does not cache.

### item Tdba-20277
Site: dba | Thread title: What is the actual lowest possible positive REAL number
[chunk 723916] The minimum positive (subnormal) single-precision floating-point value is 2−149 ≈ 1.4 × 10−45. The minimum positive normal value is 2−126 ≈ 1.18 × 10−38 (reference).
DECLARE
 @r1 real = POWER(2e0, -126),
 @r2 real = POWER(2e0, -23)
SELECT
 @r1,
 @r2,
 @r1 * @r2,
 CONVERT(binary(4), @r1 * @r2);
For double-precision, the minimum positive subnormal is:
DECLARE @r1 float = POWER(2e0, -1075);
SELECT @r1, CONVERT(binary(8), @r1);

### item Tdevops-5592
Site: devops | Thread title: Run scripts which are stored in GitLab from Jenkins
[chunk 996561] If you are using Gitlab merely as a source code repository, and you are triggering the jobs when there are changes to the repository.
The Jenkins Gitlab plugin documentations states:
This plugin is a build trigger that allows GitLab to trigger Jenkins builds when code is pushed or a merge request is created. Configuration done on a per-job basis.
So, you can trigger the builds. But to answer your question:

[chunk 996562] I put all the commands in Shell to execute. Can I store those commands in GitLab and execute from jenkins?
The answer is yes, but there is some leeway. It depends on how you've configured the jobs. If they are freestyle jobs, have them execute a shell command running the script in your repository. You can do this via the web-interface the Jenkins job editor.

[chunk 996563] However, I wouldn't recommend this as best practice. Instead, I would recommend having a pipeline description in the repository. See the plugin docs on github for more details on configuration.

### item Tnetworkengineering-28329
Site: networkengineering | Thread title: Does the source MAC address of a frame change when it passes through several switches?
[chunk 978916] No. If all the switches are layer-2 switches, the frames are switched without any changes.
Only with routers, including layer-3 switches where the packets need to cross to other VLANs, will the frames be stripped and rewritten for the new network or VLAN.

### item Tsecurity-18290
Site: security | Thread title: Is sha-1 hash always the same?
[chunk 858145] Hash functions are deterministic: same input yields the same output. Any implementation of a given hash function, regardless of the language it is implemented in, must act the same.
However, note that hash functions take sequences of bits as input. When we "hash a string", we actually convert a sequence of characters into a sequence of bits, and then hash it. There begins the trouble. Consider the string "café": among all the possible conversions to bits, all of the following are common:

[chunk 858146] 63 61 66 e9 ISO-8859-1 ("latin-1")
63 61 66 ca a9 UTF-8
63 61 66 65 cc 81 UTF-8 (NFD)
ef bb bf 63 61 66 ca a9 UTF-8 (with BOM)
ef bb bf 63 61 66 65 cc 81 UTF-8 (NFD with BOM)
63 00 61 00 66 00 e9 00 UTF-16 little-endian
00 63 00 61 00 66 00 e9 UTF-16 big-endian
ff fe 63 00 61 00 66 00 e9 00 UTF-16 little-endian (with BOM)
fe ff 00 63 00 61 00 66 00 e9 UTF-16 big-endian (with BOM)
63 00 61 00 66 00 65 00 01 03 UTF-16 little-endian (NFD)
00 63 00 61 00 66 00 65 03 01 UTF-16 big-endian (NFD)
ff fe

[chunk 858147] 63 00 61 00 66 00 65 00 01 03 UTF-16 little-endian (NFD with BOM)
fe ff 00 63 00 61 00 66 00 65 03 01 UTF-16 big-endian (NFD with BOM)
and all will yield very different hash values when processed with a given hash function. You have to be very precise about what you do when dealing with cryptographic functions; every bit counts.

### item Tserverfault-185011
Site: serverfault | Thread title: How much memory would be needed for a Wordpress site with 8.000 hits per day with the occasional spike?
[chunk 63114] No one can completely answer your question without knowing details about your install, such as what plugins you are running and the memory requirements of each plugin.
Wordpress does not scale well without some sort of Caching plugin. W3 Total Cache and WP Super Cache are both great plugins that will let your site scale much beyond a default Wordpress install. These plugins essentially minimize the dynamic PHP compilation and SQL hits and instead serve HTML files.

[chunk 63115] It then becomes a calculation much like any other busy web server. How many images are coming off of your server? Is output gzipped? Are you planning for future growth? Many factors go into how fast the website will serve up and how much RAM you will need.
That being said, at your current size I think I would go with at least 1GB of RAM, assuming you use a caching plugin and have minimal graphics serving off of your server. However there are big caveats above.

### item Tsoftwareengineering-284937
Site: softwareengineering | Thread title: Why can't there be any implicit conversions?
[chunk 634219] For what it's worth, len(str(100)), len(chr(100)) and len(hex(100)) are all different. str is not the only way to make it work, since there's more than one different conversion in Python from an integer to a string. One of them of course is the most common, but it doesn't necessarily go without saying that's the one you meant. An implicit conversion literally means, "it goes without saying".

[chunk 634220] One of the practical problems with implicit conversions is that it isn't always obvious which conversion will be applied where there are several possibilities, and this results in readers making errors interpreting the code because they fail to figure out the correct implicit conversion. Everyone always says that what they intended is the "obvious interpretation". It's obvious to them because it's what they meant. It might not be obvious to someone else.

[chunk 634221] This is why (most of the time) Python prefers explicit to implicit, it prefers not to risk it.
The main case where Python does do type coercion is in arithmetic.
It allows 1 + 1.0 because the alternative would be too annoying to live with, but it doesn't allow 1 + "1" because it thinks you should have to specify whether you mean int("1"), float("1"), ord("1"), str(1) + "1", or something else.

[chunk 634222] It also doesn't allow (1,2,3) + [4,5,6], even though it could define rules to choose a result type, just like it defines rules to choose the result type of 1 + 1.0.
Other languages disagree and do have lots of implicit conversions. The more they include, the less obvious they become. Try memorising the rules from the C standard for "integer promotions" and "usual arithmetic conversions" before breakfast!

### item Tunix-67468
Site: unix | Thread title: Bind to execute command with last argument of previous command
[chunk 312499] bind '"\ee": "g++ !$"' does exactly what you wrote, which is to insert g++ !$ on the command line. If you want the command to be executed, you need to press Enter.
bind '"\ee": "g++ !$\r"'

### item Tdba-290260
Site: dba | Thread title: Postgresql: Modify one value inside of a nested json column
[chunk 830155] You are looking for jsonb_set() (documentation)
update "Assets" 
 set "Parameters" = jsonb_set("Parameters"::jsonb, '{params2, k}', to_jsonb(2.2))
where ...

### item Tdevops-173
Site: devops | Thread title: How to check Jenkins build executor free memory?
[chunk 993840] Have a look at the Monitoring plugin. Here are some more details about it (from the linked page):
Charts of memory, cpu, system load average, http response times by day, week, month, year or custom period
Statistics of http requests with mean response times, mean cpu times, mean response size by request and by day, week, month, year or custom period
Errors and logs
Current http requests
Threads
Heap histogram (instances and sizes by class)
Http sessions
Process list of OS
MBeans

[chunk 993841] Actions for GC, heap dump and invalidate session(s)
Report in html or pdf
In English, German, French, Portuguese or Chinese
Jenkins security
For Jenkins nodes (slaves in general):
The report for the nodes is available at http://yourhost/monitoring/nodes
Charts aggregated for all nodes of memory, cpu, system load average, number of running builds, build queue length, build times by period
Detailed statistics of the build times and of the build steps by period

[chunk 993842] Threads, process list and MBeans for each nodes
Heap histogram aggregated for all nodes
For each individual node (each node in http://yourhost/computer), reports and actions are available from the "Monitoring" page in the contextual menu or in the detail of the node:
Threads, process list, MBeans of that node only
Heap histogram of that node
Actions for GC, heap dump
And more...

[chunk 993843] Credits: Assaf Lavie (who first mentioned it in a comment, but for some reason didn't post that as an actual answer ...).

### item Tnetworkengineering-19881
Site: networkengineering | Thread title: Pinging broadcast address
[chunk 976641] Not all machines will answer a broadcast ping. (all broadcast -- 255.255.255.255, or subnet broadcast -- eg. x.x.x.255) Some see it as a "security feature", because one could spoof the origin to flood any host on the network.

### item Tsecurity-69440
Site: security | Thread title: Is it unsafe to have hashes of parts of a private string
[chunk 886538] Extra information can only help the attacker; but that extra help might be negligible.
If we model the hash function as a random oracle, then showing h(P+B) for a given non-empty string B does not yield extra information useful for the attacker (I take "+" to mean here string concatenation, not numerical addition).
A "random oracle" is (in rough terms) a function such that you know nothing on its output for any given input without trying it.

[chunk 886539] When you have h(x), you can gain information on x only through brute force, i.e.
trying out potential values for x until a match is found.
Thus, h(P+B) does not give any extra power to the attacker, compared to h(P), and regardless how B was chosen: the attacker still has to try potential P values and hope to get lucky.

[chunk 886540] The best that the attacker can do to optimize things on his side is to choose a strategy that minimizes the computational cost of each try; since common hash functions have a cost that is proportional to the input size, the attacker will prefer to work with h(P) than h(P+B) anyway.
The trouble with the random oracle model is that usual hash functions are not random oracles.

[chunk 886541] However, in the case of Merkle–Damgård hash functions (a category that includes common hash functions such as MD5, SHA-1, SHA-256 and SHA-512), there is a property called "length extension attack": given h(P), it is possible to compute h(P+B) for B values that can be, to a large extent, chosen at will, and you can do that without knowing P (you need to know the length of P, but not its actual value).

[chunk 886542] The length extension attack is usually accounted for as either an harmless curiosity, or a weakness (in most protocols, it is harmless and can be ignored); but, in our case, it has an interesting consequence.
Namely, it allows us to show that revealing h(P+B) does not give extra information to the attacker, precisely because the attacker did not need wait for us: he could already compute h(P+B) for a large class of B values.

### item Tserverfault-431437
Site: serverfault | Thread title: HP P410 RAID + Samsung 830 SSDs + Debian 6.0 - What performance to expect?
[chunk 135742] There's a lot to cover here.
If you want more performance (in order from greatest to least impact):
Add another pair of disks and expand to RAID 1+0. This will provide the greatest benefit.
Tune your filesystem (noatime, journaling mode, remove write barriers, etc.) and/or move to a higher-performance filesystem like XFS or even ext4.
Go back to a deadline elevator. It will perform better under realistic workloads than your noop scheduler.

[chunk 135743] Upgrade the firmware of your HP Smart Array P410 controllers (and the server, as well)
Consider some more advanced tuning techniques.
Improve your benchmarking technique. dd is not an appropriate way to measure I/O performance. Try purpose-built applications like iozone, bonnie++, etc. and tweak them to your desired read/write patterns.
For purely sequential reads/writes, regular SAS drives aren't too bad a choice either...

[chunk 135744] As far as compatibility, I use non-HP disks with HP RAID controllers and servers often. Sometimes, things don't work, but if your SSD is connected, reports proper temperature and doesn't display any errors in the HP Array Configuration Utility, you're fine.
You are using HP Management Agents on the server, aren't you?
Edit:
I ran the same on one of my systems, featuring the same controller with four SATA SSD's, tuned XFS, deadline elevator, etc.

[chunk 135745] [root@Kitteh /data/tmp]# dd if=/dev/zero of=tempfile bs=1M count=1024 conv=fdatasync,notrunc
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB) copied, 3.1985 s, 336 MB/s
[root@Kitteh /data/tmp]# echo 3 > /proc/sys/vm/drop_caches
[root@Kitteh /data/tmp]# ll
total 1048576
-rw-r--r-- 1 root root 1073741824 Sep 24 14:01 tempfile
[root@Kitteh /data/tmp]# dd if=tempfile of=/dev/null bs=1M count=1024
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB) copied, 1.60432 s, 669 MB/s