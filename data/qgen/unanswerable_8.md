### item Usecurity-20958
Site: security | Thread title: x.509 CRLs: next update?
There are two distinct semantics that the nextUpdate field is used to convey:
the date at which a newer CRL should be available, thus making it worth a new download (similarly, before the date given in the nextUpdate field, a cached CRL should be considered to be the newest);
the date after which a given CRL should be considered obsolete.
It is expected that CRL overlap, so that transitions are smooth and network traffic spread throughout the day.

Typically, a CA would produce a new CRL every hour (so that fresh information is available) but would "allow" a given CRL to be valid for one day (24 hours).
Since a CRL can be somewhat large, downloading it is expensive, thus implementations would prefer not to do it too often if it has no practical use.
But since each CA has its own policy, a generic certificate validator cannot know a priori what kind of schedule a given CA uses; it must learn it through the data in the certificates and CRL.

The first meaning is what X.509 mandates.
However, everybody uses it with the second meaning.
In effect, implementations of X.509 (e.g.
in Web browsers, when they validate the certificate of a Web server) handle nextUpdate as if it was an endOfValidity date.
Lately, Microsoft has defined a new extension called nextPublish which assumes the first meaning (the extension can be seen in annex A.1 of this draft, in an OCSP context).

This extension (which seems to be, so far, private to Microsoft, not standard) somehow acknowledges that the common practice deviates from theory with regards to the meaning of nextUpdate.

### item Userverfault-190493
Site: serverfault | Thread title: How can I log iptables in Ubuntu just in /var/log/firewall with rsyslogd
Use a discard action after the iptables log, but before the other logs.
kern.warning /var/log/firewall.log
kern.warning ~
*.* /var/log/messages

### item Usoftwareengineering-273759
Site: softwareengineering | Thread title: Persistent RESTful state on client without cookies
There's HTML5 local storage, which allows you to keep data without it contaminating the HTTP requests you make. It's intended for pretty much exactly this use case: complex Javascript applications that want to store persistent information locally.
http://www.w3.org/TR/webstorage/

Note that REST doesn't mean banning all state from the server, sometimes you genuinely want to update things; especially in the "airline ticket" example you might want to explicitly create a "reservation" object before payment with a POST that returns a URL for the reservation. The client then hangs onto the URL, but the server-side object exists to prevent booking the same seat twice.

### item Uunix-87265
Site: unix | Thread title: How do I get the creation date of a file on an NTFS logical volume?
From https://github.com/tuxera/ntfs-3g/wiki/Using-Extended-Attributes#file-times,
An NTFS file is qualified by a set of four time stamps “representing the number of 100-nanosecond intervals since January 1, 1601 (UTC)”, though UTC has not been defined for years before 1961 because of unknown variations of the earth rotation.
You'll find even more information in there including:
Newer versions of ntfs-3g expose a ntfs.ntfs_crtime and ntfs.ntfs_crtime_be attribute.
So:

getfattr --only-values -n system.ntfs_crtime_be /some/file |
 perl -MPOSIX -0777 -ne '$t = unpack("Q>");
 print ctime $t/10000000-11644473600'
See also:
ntfsinfo -F /file/in/ntfs /dev/fs-device
With older ntfs-3g, this should work:
getfattr --only-values -n system.ntfs_times /some/file |
 perl -MPOSIX -0777 -ne 'print ctime unpack(Q)/10000000-11644473600'
Or with GNU tools and sub-second precision:

date '+%F %T.%N' -d "@$({ echo 7k
 getfattr --only-values -n system.ntfs_times /some/file |
 od -A n -N 8 -vt u8; echo '10000000/ 11644473600-p'; } |dc)"

### item Udba-89460
Site: dba | Thread title: Deadlock due to concurrent updates (with SIU lock)
The deadlock diagram is:
The particular issue here is that (4) IX is not compatible with (1) SIU, whereas it is compatible with the more usual IU lock seen in this situation.
The SIU lock occurs because somewhere between selecting the row in question with the UPDLOCK hint (which takes IX at the object level, IU at the page level, and U at the row level), a statement in the transaction is acquiring a shared (S) page-level lock on the nonclustered primary key index structure.

The existing IU page lock is converted to SIU. Although shared locks are usually released very quickly under the read committed isolation level, that does not occur when the shared lock is merged into a combination lock like SIU. The lifetime of that lock is the same as the IU component (the life of the transaction here).

You can avoid this specific deadlock by ensuring page-level shared locks are not taken on the same access method after the UPDLOCK statement (row-level shared locks would be ok). This will avoid the SIU page lock. The page granularity explains why operations on two different id values can deadlock.

That said, unless the question is missing some detail, you will still have an update statement that is prone to deadlock in another way. The base table appears to be a heap, and the update plan will likely feature an RID lookup:

This is a well-known pattern that often results in a conversion deadlock under high concurrency. The reading side of the plan accesses the nonclustered index first, then the base table. The update side of the plan accesses the base table first, then the nonclustered index. By touching the same resources in reverse order, multiple concurrent executions of the same plan can deadlock.

The RID lookup is needed for the query processor to check if the value of Column1 is being changed. If it is not changing, a redundant nonclustered index update can be avoided. You can remove this RID lookup by including Column1 in the nonclustered primary key, or by changing the primary key from nonclustered to clustered.

### item Udevops-3275
Site: devops | Thread title: How to populate docker volumes in a build step to be used by a different container
docker-compose is just a glorified wrapper around docker which gives you a nice textual representation of all the options you would regularly give to docker build or docker run. Plus, of course, it bundles several docker images/containers together. That said, it has no provisions to run anything else than you would get by calling docker.

I don't see how you would use docker-compose build to populate a volume. Volumes are, by definition, not living inside docker images/containers, but outside (on the host system). docker build never writes to the host system, and you cannot mount volumes during docker build. docker-compose build basically only runs docker build for you, and also has no way to run or write anything on the host.
So, no, docker-compose build will not be able to create the static files.

You could make your compose file so that it runs your generator (inside a docker container, writing to a named volume), and runs your server (nginx or whatever) in another container, mounting the same named volume (this would be your case 2, I believe).
Then, with docker-compose up, it would fire up both those containers.
The first one would populate your static files; the second would serve.

The first would hang around and do nothing afterwards, which you could just ignore, but which would certainly be ugly.
Unfortunately, you cannot use something like docker-compose up --rm to automatically the unneccessary jekyll container.
So, your best bet is to start the jekyll container yourself (docker run --rm jekyll:xyz -v ...:...), the --rm will remove the container after it is finished. Then docker-compose up with the actual server(s).

### item Unetworkengineering-17839
Site: networkengineering | Thread title: Is a VPN concentrator different from a VPN gateway?
Yes, though they are often used interchangeably.
A VPN gateway may refer to a router, firewall, or VPN Concentrator that provides Virtual Private Networks.
A VPN Concentrator is a dedicated [VPN gateway] appliance (physical or virtual).
All VPN Concentrators are VPN Gateways, but not all VPN Gateways are VPN Concentrators.

### item Usecurity-101137
Site: security | Thread title: I don't recognise my DNS server's address: does this mean I am compromised?
Something in your environment has definitely been compromised. It seems more likely that your router has been compromised. You haven't provided much information, so I'm going to make some basic assumptions:
You're at home
You are behind a commercial router, provided by your ISP
You haven't done anything to secure your router
Your linux desktop is a DHCP client of the router.

These devices often have default passwords that users never change and critical firmware vulnerabilities that go unpatched.
As a DHCP client of the router, your Linux desktop is going to pull DNS information as part of its DHCP request, and so will see the behavior you've described above.
Configuring other DNS servers in resolv.conf is only a workaround.
I strongly suggest that you try to log in to your router (probably @ 192.168.1.1, based on your screenshot).
I bet you won't be able to.

You'll probably have to reset it to factory defaults, then log in.
You'll want to secure it better - update firmware, change default passwords, and hope that's enough.
For confirmation without logging into your router, check the DNS configuration on your Windows desktop. If it points to the same 46.161.40.29, then it's very likely the router.

### item Userverfault-28085
Site: serverfault | Thread title: Network Diagramming Software, FREE or Open-Source
Dia is a such program. DiaCze is a windows only version packaged with icon for network diagramming (but you can extract content on a windows computer and copy it to a unix system).
Edit: I discovered Kivio today, a Visio like (but still in development)

### item Usoftwareengineering-45477
Site: softwareengineering | Thread title: What do you think about gems and eggs? Alternatives?
There are numerous python modules available via the Ubuntu package manager, for example. Just like any other software out there, it's the distributor's job to put it into their own package format, and it's the user's job to notice and use the native OS packages when they are available. I don't think it's the job of the developer to account for all possible package formats out there.

Eggs and gems are a great distribution method for modules yet to get a system package, and for those operating systems which are inexplicably popular despite the lack of anything resembling a package manager.

### item Uunix-712425
Site: unix | Thread title: PulseUI on Ubuntu 22.04 needs Chromium Embedded Browser, which doesn't download
While creating the post I found the instructions for manually installing CEF. I did (with root permissions):
/opt/pulsesecure/bin$ ./setup_cef.sh install
And verified with
/opt/pulsesecure/bin$ ./setup_cef.sh check_installed

### item Udba-167178
Site: dba | Thread title: Missing execution plans for stored procedures
There are two plan cache DMFs:
sys.dm_exec_query_plan - returns cached plans in XML format, but only up to a certain size (and only as long as they can be formatted as XML in SQL Server, which means up to 128 nested levels.)
sys.dm_exec_text_query_plan - returns cached plans in text format, of any size. But the drawback is that when plans are large, you can't convert them to XML inside SQL Server, and even TRY_CONVERT as XML returns a null.

sp_BlitzCache only hits the former DMV (because it needs to analyze query plans as XML to do all kinds of slicing and dicing.) I made Github issue #838 to improve this so we could at least alert users to go check sys.dm_exec_text_query_plan for their bigger queries. We still won't be able to do XML analysis on it, though.

### item Udevops-2029
Site: devops | Thread title: How to shut down a stateless app gracefully?
A stateless app can always handle kill -9?
Yes.
But even a stateless app handles connections from the outside (or it would do nothing, really!).
That is the issue here.
If your app, say, some HTTP server that only serves static files, and is thus stateless, were to be routinely killed with -9, then ever so often, you would kill it with an active connection.
So your customer would get some HTTP error code.

In the best case, it is an unimportant small image and he doesn't even notice; in the worst case, it is your main .js or .css file and he will indeed notice badly.
So, by using a weaker signal, you give your stateless app the chance to finish the current request before shutting down.
Obviously, you can finish it off with -9 if it does not go away after a second or two (or however long you wish to give it time to end its business).

### item Unetworkengineering-5344
Site: networkengineering | Thread title: Cisco: storm-control unicast
So does storm-control unicast only measure the pps rate (or bps rate) of frames that are for destinations not in the CAM tables, or all destinations that aren't a broadcast or multicast address (so just the total number of unicast frames)?

I have to confess that I mistakenly trusted the Nexus doc below which said only unknown unicast is rate-limited; however, that's definitely wrong for Cisco IOS. The reality is (at least on IOS platforms) that unicast storm control affects all unicast traffic; the Cisco Nexus doc I quoted said it only affected traffic that was unknown unicast. I will endeavor to test on Nexus at a later date.
In an effort to atone for my mistake, I built a quick screencast of what happens when I:

Configure a Cisco IOS switch with unicast storm-control to throttle at 1Mbps.
Use speedtest_cli.py to start a unicast download from speedtest.net
Reconfigure the switch without unicast storm control
Download from speedtest.net again...
Hit your refresh button to restart the screencast at the beginning
Bottom line
Unicast storm-control affects all unicast traffic in Cisco IOS
Unicast storm-control is applied on traffic inbound to the switchport

My Original quote from the Nexus docs, which I applied to the OP's Cisco 2960
Quoting the Nexus Storm Control Docs (emphasis mine):
"You can use the traffic storm control feature to prevent disruptions on Layer 2 ports by a broadcast, multicast, or unknown unicast traffic storm on physical interfaces. "

Storm control operates the same way across Cisco platforms; if the destination-mac-address is not in the CAM table, then then the switch must flood it out all ports in the Vlan (except the one it came in on). Suffient quantities of this kind of traffic would trigger your Unicast Storm Control thresholds.

### item Usecurity-196455
Site: security | Thread title: How should source code security be checked?
There are automated and manual approaches.
For automated, you could start with lgtm - a free static code analyser for open source projects and then move to more complex SAST solutions.
For manual - you could build a threat model of your app and run it through OWASP ASVS checklist starting from it's most critical parts. If there is file deletion in your threat model - just call something like this: grep -ir 'os.remove('.
Of course it's better to combine them both.

### item Userverfault-61915
Site: serverfault | Thread title: How do I make ssh fail rather than prompt for a password if the public-key authentication fails?
For OpenSSH there is BatchMode, which in addition to disabling password prompting, should disable querying for passphrase(s) for keys.
BatchMode
If set to “yes”, passphrase/password querying will be disabled.
 This option is useful in scripts and other batch jobs where no
 user is present to supply the password. The argument must be
 “yes” or “no”. The default is “no”.
Sample usage:
ssh -oBatchMode=yes -l <user> <host> <dostuff>

### item Usoftwareengineering-232946
Site: softwareengineering | Thread title: Is it a code smell if you are frequently creating an object just to call a method on it
I would consider it an architecture smell in that UpdateData probably should belong to a 'service' class.
Where the data is an Apple.
Where AppleAdapter is service/business-intelligence class.
Where AppleService is a Singleton reference to an AppleAdapter that exists outside of the current method.

private static volatile AppleAdapter _appleService = null;
private static object _appleServiceLock = new object();
private AppleAdapter AppleService
{
 get
 {
 if (_appleService == null)
 {
 lock (_appleServiceLock)
 {
 if (_appleService == null)
 _appleService = new AppleAdapter();
 }
 }
 return _appleService;
 }
}
public SomeAppleRelatedMethod(Apple apple)
{
 AppleService.UpdateData(apple);
}

I don't think what you are doing is wrong necessarily but if SomeDataAdapter does indeed represent some kind of stateless business service, then a singleton would be the best practice for it.
Hope that helps! The example provided is fancy way to ensure no contention of the _appleService if it happened to be both null and accessed at exactly the same time by two or more threads.

You know what? If SomeDataAdapter is an ADO IDbDataAdapter (which it almost certainly is), disregard this entire response!
:P
I don't have permission to add a comment to the original question, but if you could specify where this code exists.

If this code represents a custom implementation of an IDbDataAdapter, and UpdateData is creating an IDbConnection, IDbCommand, and wiring it all up behind the scenes, then no I wouldn't consider that a code smell because now we're talking about streams and other things that need to be disposed of when we're done using them.

### item Uunix-481073
Site: unix | Thread title: Perl command line regex to modify all pattern matches
str="a1b2c3"
perl -pe 's/\d+/$&+1/ge' <<<"$str"
The g flag to the substitution would make Perl apply the expression for each non-overlapping match on the input line.

Nitpick: There are actually no capture groups involved here (the original question mentioned capture groups). The Perl variable $& is the "string matched by the last successful pattern match". This is different from e.g. $1 and $2 etc. that refer to the string matched by the corresponding capture group (parenthesised expression). There are no capture groups in \d+, but you could have used s/(\d+)/$1+1/ge instead, which does use a single capture group.

There is no difference between s/(\d+)/$1+1/ge and s/\d+/$&+1/ge in terms of outcome. In this short in-line Perl script, it makes no difference whether you choose to use one or the other, but generally you'd like to avoid using $& in longer Perl programs that do many regular expression operations, at least if using an older Perl release.
From perldoc perlvar (my emphasis):
Performance issues

Traditionally in Perl, any use of any of the three variables $`, $& or $'
 (or their use English equivalents) anywhere in the code, caused all
 subsequent successful pattern matches to make a copy of the matched
 string, in case the code might subsequently access one of those variables.
 This imposed a considerable performance penalty across the whole program,
 so generally the use of these variables has been discouraged.
[...]

In Perl 5.20.0 a new copy-on-write system was enabled by default, which
 finally fixes all performance issues with these three variables, and makes
 them safe to use anywhere.

### item Udba-205686
Site: dba | Thread title: Finding the default isolation level in SQL Server 2017 and Azure SQL DB
It's referring to Azure SQL Database which uses RCSI by default.
Isolation Level SQL
Database default database wide setting is to
enable read committed snapshot isolation (RCSI) by having both the
READ_COMMITTED_SNAPSHOT and ALLOW_SNAPSHOT_ISOLATION database options
set to ON, learn more about isolation levels here. You cannot
change the database default isolation level. However, you can control
the isolation level explicitly on a connection.

In on-premises SQL Server, the default isolation level is Read Committed.
Finding the "default" isolation level is a bit of a goose chase. It will depend on the database where a query is initiated from, and if any hints exist in the query to override a database level setting.
That said, you could query sys.databases to find out if RCSI or SI is enabled.
SELECT d.name, 
 d.is_read_committed_snapshot_on, 
 d.snapshot_isolation_state
FROM sys.databases AS d;

Note that the READ_COMMITTED_SNAPSHOT is not technically an isolation level. Rather, it is a database option that controls the implementation so that row versioning instead of locking is used to provide read consistency for sessions using the READ_COMMITTED isolation level.

### item Udevops-4912
Site: devops | Thread title: How to keep configuration files automatically during apt-get upgrade or install?
There are options you can pass through apt-get to dpkg that will handle the config choices. We usually do something like:
apt-get install -y --no_install_recommends -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' <package_name>
When using ansible you can do:
apt:
 pkg: "{{ item }}"
 only_upgrade: yes
 install_recommends: no
 force: yes
 dpkg_options: 'force-confdef,force-confold'
 state: latest
 with_items:
 - <package_name>

For further details on the ansible apt module options look here