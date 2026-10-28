### item Userverfault-282285
Site: serverfault | Thread title: Why do I get "Operation not permitted" when trying to mount a volume using sshfs and MacFUSE?
It's possible that your user account is not able to mount volumes into the /Volumes directory directly. Have you tried mounting sshfs into a directory within your own home directory?
Failing that, you might need to have administrative (sudo) permissions to run sshfs. Try prefacing that command with sudo like so:
sudo sshfs daryls:/ /Volumes/daryls -oauto_cache,reconnect,volname=daryls
As an aside: to determine whether your Mac is running in 64-bit mode:
Choose About This Mac from the Apple menu.

Click More Info.
Select Software in the Contents pane.
Look for "64-bit Kernel and Extensions: Yes (or No)" under the System Software Overview heading.

### item Usoftwareengineering-105158
Site: softwareengineering | Thread title: Does Microsoft have a free version of Visual Studio?
Visual Studio Express is a set of freeware integrated development environments (IDE) developed by Microsoft that are lightweight versions of the Microsoft Visual Studio product line.
A comparison is available here.
If you are a student you may want to take a look at DreamSpark.

### item Uunix-499694
Site: unix | Thread title: Checking server is listening without telnet, from CLI?
You can try several ways to check if something listen on particular port:
With wget/curl
wget your_IP:port
With netstat
netstat -an|grep LISTEN|grep :port
With lsof
lsof -i :port
With netcat
nc -vz your_IP port
With /proc filesystem (probably will work only on linux)
(explained here)
With ss
ss|grep LISTEN|grep :port
With nmap
nmap -sS -O -pport your_IP

EDIT1 Also (almost) every ssh,http,ftp client can be used, but sometime will be hard to understand if port is closed by firewall or not available.
EDIT2 Found in this Q/A sample way to use cat and echo to do the job:
true &>/dev/null </dev/tcp/127.0.0.1/$PORT && echo open || echo closed
or with only exec command (if you do not see error port is open):
exec 6<>/dev/tcp/your_IP/port
And I found a way to use only awk to do the job (original here):

awk -v port=your_port 'function hextodec(str,ret,n,i,k,c){
 ret = 0
 n = length(str)
 for (i = 1; i <= n; i++) {
 c = tolower(substr(str, i, 1))
 k = index("123456789abcdef", c)
 ret = ret * 16 + k
 }
 return ret
}
function getIP(str,ret){
 ret=hextodec(substr(str,index(str,":")-2,2)); 
 for (i=5; i>0; i-=2) {
 ret = ret"."hextodec(substr(str,i,2))
 }
 ret = ret":"hextodec(substr(str,index(str,":")+1,4))
 return ret
} 
NR > 1 {{local=getIP($2);remote=getIP($3) }{ if (remote ~ "0:0" && local ~

":"port) print local}}' /proc/net/tcp
EDIT3 As mentioned in to comment some of the methods, especially based on /dev filesystem may bot work in your environment
EDIT4 For Solaris I found excellent Q/A which use pfiles to get open port.

### item Udba-127847
Site: dba | Thread title: Datawarehouse indexing
I'm working on the assumption that the table in question is a fact table, not a dimension table with a huge composite key:
Just to fix the performance issue in the short term, I would add all of these key columns as the table's clustered index, which means you won't have to INCLUDE a lot of measures and stuff, like the suggested index does. Also, make the index unique if the data allows for this.

As for the column order of a clustered index on a fact table, it depends on how you're accessing them. If you're only using a cube to read large chunks of data, I would probably prioritize INSERT priority by making the index chronological, i.e. putting the date column first - that way, new rows get added to the end of the index (in the best of worlds).

If you're running user T-SQL queries on the fact table, I would try to arrange the index columns in an order that gives you Index Seeks or Range Scans as much as possible: first, columns that are filtered on single dimension keys (think "year", "type", "unit" or "department"-type dimensions), then those columns that are filtered on multiple dimension members, ranges, or used for sorting.
There are, of course, other schools on how to build indexes - this is not a "single correct answer".

Edit: More on clustered vs non-clustered indexes:
I'm guessing that you already have an existing clustered index, and that's why SQL Server suggests a non-clustered index. However, non-clustered indexes have to be explicitly defined with INCLUDE columns. Clustered indexes define the actual storage/sort order of the table, and as such, they will implicitly include all columns in the table (I won't go into LOB columns like varchar(max) and xml).

The clustered index is normally the "catch-all index" that takes care of queries that are not suitable for an existing non-clustered index, which makes it even the more important (in my opinion) that it's well-designed and not, for instance, just on an IDENTITY() column.
Plus, a non-clustered index will take up more drive space, so a non-clustered index that covers all of the table's columns will in effect take up as much space as the table itself. A clustered index is the table.

### item Udevops-9923
Site: devops | Thread title: Mitigate false positives due to daylight saving time in CloudWatch anomaly dectector
My current understanding is that it is not possible to avoid false positives. At least not if traffic comes from different time zones around the world (as in the context of this question).
AWS operates on UTC times, but this is irrelevant for the anomaly detection. It does play a role if you set timers, but it is not taking into account for the predictions of AWS. In other words, switching to UTC will not make false-positives less likely.

When thinking about it, it is hard to avoid false-positives. If a time-shift in Europe or the US happens, you could take that into account and predict the new traffic. But that requires extra domain knowledge. The AWS predictor only sees a generic time series.
There are other events such as Christmas, which will impact the expected traffic. Again, with extra knowledge you could improve predictions. But the problem is too difficult for the AWS predictor, as it does not have that domain knowledge.

In our concrete case, we still kept the alerts, as they do have value even with the known false-positives. Humans with knowledge about the underlying system, can reject the false-positive. It is not ideal, but it is a trade-off that we are willing to make.

Note that other types of graphs are not susceptible for these types of problems. For example, error rates instead of total number of errors. It is not always possible, but if you can use rates, the system will be more stable in my experience.
AWS allows to set alerts on math expressions such as errors / requests. The advantage is that normalized rates tend to be agnostic of external events.

### item Unetworkengineering-7583
Site: networkengineering | Thread title: why RIP sending only maximum of 512 bytes of data
You can find this on Page 19 of RFC 1058: RIP, the maximum UDP payload of a RIP update is 512 bytes:
The maximum datagram size is 512 octets. This includes only the
portions of the datagram described above. It does not count the IP
 or UDP headers. The commands that involve network information allow
 information to be split across several datagrams. No special
 provisions are needed for continuations, since correct results will
 occur if the datagrams are processed individually.

This means RIP can carry a maximum of 25 routes in a RIP update packet. When RIP was conceived, 512 bytes was a reasonable maximum

### item Usecurity-158166
Site: security | Thread title: How to add AltName from csr file to crt file using "openssl x509 -req"?
Using the '-extfile' parameter fixed it.
Additional config file
I have added an openssl-ext.cnf file containing:
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = $ENV::ALTNAME
Using '-extfile' parameter
And added that new config file to the openssl command using the -extfile parameter:

openssl x509
 -req
 -in dev.example.com.csr
 -CA dev.root.ca.crt
 -CAkey dev.root.ca.key
 -CAcreateserial
 -out dev.example.com.crt
 -days 3650
 -sha256
 -extfile openssl-ext.cnf

### item Userverfault-453722
Site: serverfault | Thread title: "No route to host" with ssl but not with telnet
Can you check whether you can actually ping the target host? (IPv4) It seems that
your IPv4 connection is broken
there is an AAAA and an A record
telnet manages to prefer IPv6
openssl avoids IPv6
This might merely be an issue boiling down to IPv4 connections not working to the target host. Is your IPv4 routing OK on both machines?

### item Usoftwareengineering-142734
Site: softwareengineering | Thread title: Do I have to deliver my utility and helper code to clients?
First, this is mainly about the contract you have with the client. If you have a contract which includes delivering of the source code, your client can expect source code they can compile by himself. If you refuse to do this, you break the contract - and it does not matter if the missing source in lib A or lib B or lib "Utility". From the client's point of view, there is no difference between those parts.

If you have specificially excluded some libs in your contract (and your client inattentively signed that), then you may rightfully refuse to deliver your source for that libs, but don't expect to keep the client in the future.

If you want to avoid that situation in the future, separate your utility library clearly in your contract and try to sell / license it to your customers as a closed-source-product, together with the sources of the main product your are creating for them. That will imply proper versioning and configuration management of your utitlity lib, of course.

### item Uunix-400191
Site: unix | Thread title: Connecting two clients on different physical interfaces using smcroute
Issue was with rp_filter. rp_filter was turned ON. So that kernel was filtering out all the multicast packets from reaching user space. Hence smcroute was not able to route the multicast packets.
echo 0 > /proc/sys/net/ipv4/conf/br1/rp_filter
echo 0 > /proc/sys/net/ipv4/conf/br2/rp_filter
Turned rp_filter OFF as above and it started working.

### item Udba-188585
Site: dba | Thread title: Select most recent inspection, break tie between inspections from same year
You can modify the order by clause in the window function:
row_number() over 
 (partition by road_id 
 order by extract(year from insp_date) desc, -- latest year
 length desc -- higher length
 ) as rn
Tested in dbfiddle.uk (only in version 11g).
In version 12c, you could also use the FETCH FIRST syntax.
The wanted PARTITION BY makes things more difficult than a simple FETCH though. We'll have to use a LATERAL inline view or CROSS APPLY:

select
 r.*
from
 ( select distinct road_id
 from road_insp
 ) d,
 lateral
 ( select
 ri.insp_id,
 ri.road_id,
 to_char(ri.insp_date, 'DD/MON/YY HH:MI:SSAM') insp_date_formatted,
 ri.length
 from road_insp ri
 where ri.road_id = d.road_id
 order by extract(year from ri.insp_date) desc,
 ri.length desc
 fetch first 1 rows only
 ) r 
;

### item Udevops-2076
Site: devops | Thread title: Cassandra DB: store binary file record via shell
The only way to do it with cqlsh is wrap binary file into CSV file and run cqlsh --some_args -e 'COPY table_name FROM binary_wrapped.csv', but in order to do so you have to generate a new primary key to use in CSV-file.
IMO: Since cqlsh is a wrapper around python client, your ops should just write simple python script for this operation, it would be much easier in many ways.

### item Unetworkengineering-37786
Site: networkengineering | Thread title: Regarding Multicast over the internet
Why is multicast not supported over the internet ?
There is only one multicast range. Sharing that range across the Internet would mandate an address allocation scheme akin to public unicast addresses, so that the addresses you use are really yours and not used by someone else.

Additionally, using global multicast would require a global announcement and subscription system. Possibly, something similar to BGP with ASNs (or an extension) could work, but designing that would represent a huge project.
Why do we need to encapsulate in GRE ?

GRE hides your (private/multicast/...) addresses in the inner packet from the rest of the Internet that only sees the outer packet. Also, you use the outer packet destination address to direct the traffic where you want it, ie. from one site to another.
When we use the term 'internet', what exactly does it refer to?
An internet is any number of networks that are interconnected to each other.

The Internet is a global internet where a large number of carriers, ISPs and other organizations interconnect to form a (mostly) universally available network.
The differences include
most internets are (by magnitudes) smaller than the Internet
the Internet uses unique public addressing coordinated by IANA
an internet can use any addressing scheme its participants agree on - it could even support multicast

### item Usecurity-191300
Site: security | Thread title: Why are Protection Rings called rings?
Warning: This answer contains educated speculation.
"Rings" clearly expresses the "nested set" aspect of protection rings, which were described as "concentric" in early papers describing them.
The earliest citation for rings which I can find is the 1967 paper "Protection in an Information Processing Utility" by Robert M. Graham. It states,
We define rings to be ordered, disjoint sets of segments, numbered
 from 0 to some maximum.

The 1972 paper "A Hardware Architecture for Implementing Protection Rings" by Michael D. Schroeder and Jerome H. Saltzer provides more language that reinforces this image (emphasis mine):
In a system which uses segmentation as a memory addressing scheme,
 protection can be achieved in part by associating concentric rings of
 decreasing access privilege with a computation.
and

Put another way, the sets of access capabilities represented by the
 various rings of a process form a collection of nested subsets, with
 ring 0 the largest set and ring r - 1 the smallest set in the
 collection.
The concentric circle metaphor clearly correlates to this notion of "nested subsets", in a way that other metaphors - like the OSI 7-layer "stack" model - do not.
The other language that works better with concentric circles is "gates." Again to quote Schroeder and Saltzer,

Restricting the start of execution in a particular domain to certain
 program locations, called gates, provides [protection]...

With a ring structure, a gate between two layers is the only clear connectivity point - whereas with a stack, a gate may exist on the line between the shared connection line, but other methods of access may be perceived by traversing the whitespace along the sides. Again, the OSI model more closely matches that, where layers may be 'leaped' and ignored. With a concentric ring structure, it becomes clear that every layer of access is cumulative (in one direction, in the case of protection rings.)

While gates do also lend themselves to the medieval castle design of concentric walls with gates between them, I cannot find any historic references equating Multics rings with castles; only modern references drawing the analogy in order to illustrate the concept.

### item Userverfault-545174
Site: serverfault | Thread title: CentOS partition reporting out of space
First try to figure out if there is any error in the partition using "dmesg" command. If you find any error, and if you are not much familiar to fix the issue, a simple reboot may fix the issue.
If it is truly a inode related issue, you may reduce your reserved space. It will give some space and also inode as well. (though it is not recommended for production environment. As soon as possible revert it back to 2% or 3%).

tune2fs -m 0 /dev/sda1
tune2fs 1.41.12 (17-May-2010)
Setting reserved blocks percentage to 0% (0 blocks)
Find zero sized or unused files using find command and remove it after analyzing the files.
If possible take backup of the entire file system and create filesystem again using the command,
mkfs.ext4 -i </dev/destination>
to specify the number of inodes and then restore the original contents into this.

### item Usoftwareengineering-132747
Site: softwareengineering | Thread title: Is having public constants "bad"?
In C# it's very bad for none of the reasons mentioned in this thread.
Public constants in C# get baked into referencing assemblies. Meaning, if you have a SomeOtherClass in a separate assembly referencing SomeString in MyClass, the CIL generated for SomeOtherClass will contain a hardcoded "SomeValue" string.
If you go to redeploy the dll that contains MyClass but not SomeOtherClass and change the const, SomeOtherClass won't contain what you think it will--it will contain the original value.

If you're 100% positive it's a universal constant like Pi, go crazy; otherwise tread carefully.
Here's a better explanation : https://stackoverflow.com/questions/55984/what-is-the-difference-between-const-and-readonly

### item Uunix-316586
Site: unix | Thread title: Replace lines matching a pattern with lines from another file in order
Easy can be done with awk
awk '
 /^!!/{ #for line stared with `!!`
 getline <"file2.txt" #read 1 line from outer file into $0 
 }
 1 #alias for `print $0`
 ' file1.txt
Other version
awk '
 NR == FNR{ #for lines in first file
 S[NR] = $0 #put line in array `S` with row number as index 
 next #starts script from the beginning
 }
 /^!!/{ #for line stared with `!!`
 $0=S[++count] #replace line by corresponded array element
 }
 1 #alias for `print $0`
 ' file2.txt file1.txt

### item Udba-33732
Site: dba | Thread title: What is the effect of replacing indexes with filtered (non-null value) indexes?
Very interesting approach. My upvote for the creativity.
Since you reclaimed the space, I assume the original indexes are no longer in place? The downsides of filtered indexes then are:
Too many of them may cause the search space of the optimiser to grow too large, leading to poor query plans as the optimiser times out

There are several situations where a filtered index will not even be considered, even though the non-filtered equivalent would be. Notably, this can happen when you get a hash join on the indexed column or if you try to ORDER BY the column (without a filter)
Query parameterisation doesn't work with filtered indexes (see: http://www.sqlservercentral.com/blogs/practicalsqldba/2013/04/08/sql-server-part-9-filtered-index-a-new-way-for-performance-improvemnt/)

In practical terms, this means that you have to be extremely careful with filtered indexes as they will often result in horrible query plans. I would not go so far as to call them useless, but I view them as an addition to traditional indexes, not as a replacement (as you are trying to do).

### item Udevops-8329
Site: devops | Thread title: How to cache node_modules folder when using Jenkins Multibranch Pipeline
It is possible to do this (not with any built-in steps; you essentially have to either use a global cache or write your own caching tool), but I do not recommend it. When I've tried this in the past, I often ran into race conditions. For example, one build would write to the cache while another build simultaneously reads from the cache, or two builds would write to the cache simultaneously, etc. I got a lot of builds with corrupted modules as a result.

Caches do not have these kinds of race conditions when limited to a single job (or in this case, a single branch for a multibranch job) because Jenkins can be configured not to run multiple builds of one job simultaneously.
If you take extra steps to ensure that all of the jobs which might access the cache can't run simultaneously, then you could probably get away with a shared cache.

But at that point, you're likely to lose the added speed benefit of sharing the cache anyway, since you've massively reduced Jenkins' capacity to run jobs in parallel.
The other scenario where you could get away with a shared cache is if you write to the cache extremely infrequently - and I really do mean extremely. If the cache is rarely written to, then there simply aren't many opportunities for these kinds of race conditions.

### item Unetworkengineering-5779
Site: networkengineering | Thread title: Connecting multiple switches without losing performance
You only need to keep in mind how clients are going to access the file server; I’m assuming this is done by direct IP. If that is the case, and your only real objective is to get clients to connect to the file server by it’s shortest path, then your easiest setup is to setup an IP address on each interface and point clients to their closest connection.
With this simple of a setup, I can’t imagine a scenario where your connection will be your bottleneck.

Have you done any benchmarks or taken any baselines on how that connection is currently used? Give that a go before you invest too much time into a solution that isn’t entirely necessary.