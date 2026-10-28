### item Unetworkengineering-22653
Site: networkengineering | Thread title: Bridging LAN networks privately in office environment
Bridging means that you are placing the bridged devices onto the same network.
A common method for what you are trying to achieve is to use a firewall and place the things you don't want to get to your office network on the outside interface of the firewall. Your office network can then get to the devices, but the devices cannot get to the office network.

### item Usecurity-98187
Site: security | Thread title: Spoof IP address after a TCP handshake
Is it possible to spoof the IP once a TCP handshake was performed successfully?
No.
A TCP session is defined by four items:
Source IP address
Source IP port
Destination IP address
Destination port
This comes from RFC 793:
To provide for unique addresses within each TCP, we concatenate an internet address identifying the TCP with a port identifier to create a socket which will be unique throughout all networks connected together.
A connection is fully specified by the pair of sockets at the ends.

If you were to:
Use the session (with a different IP) and send a request
When you change any one of those four parameters, like the source IP, the new packet is no longer a part of that TCP session, and will not be "delivered" because it does not match the session definition. Instead, it'll be an out-of-state packet, and dropped or rejected.

### item Userverfault-170605
Site: serverfault | Thread title: Nginx - Route all requests to single script
I figured it out on my own! Yeah!
All I needed for the location block was:
location / {
 include /etc/nginx/fastcgi_params;
 fastcgi_param SCRIPT_FILENAME $document_root/index.php;
 fastcgi_pass 127.0.0.1:9000;
}
Everything else remained largely the same.

### item Usoftwareengineering-188895
Site: softwareengineering | Thread title: Using natural language grammar in fluent API
I think it's very wrong. I study natural langage and it's full of ambiguity that can only be resolved with context and a lot of human knowledge. The fact that programming languages are not ambiguous is a very good thing! I don't think you want meaning of methods to change according to context:
This is adds more surprises since you bring ambiguity
Your users will want to use constructions that you will not have covered, eg. find("user").where("name").and("email").equals("foo");

It's hard to report errors: what can you do with find("user").where("name").not().is().null();?
Let's also presume that I can cover most correct English sentences -
 after all, the grammar itself is limited to the verbs and conjuctions
 defined by SQL.

No, you can't cover most correct English sentences. Others have tried before, and it gets very complicated very quickly. It's called Natural language understanding but nobody really tries that: we're trying to solve smaller problems first. For your library, you basically have two options:
either you restrict yourself to a subset of English: that gives you SQL,
or you try to cover "English" and you find out that it's not possible due to the ambiguity, complexity and diversity of the language.

### item Uunix-500887
Site: unix | Thread title: Given a block device, how to detect if names of partitions must contain "p"?
If device name ends with digit then kernel adds 'p' symbol to separate partition number from device name.
/dev/sda -> /dev/sda1
/dev/mmcblk0 -> /dev/mmcblk0p1
For details see disk_name function in Linux kernel sources (linux/block/partition-generic.c):
if (isdigit(hd->disk_name[strlen(hd->disk_name)-1]))
 snprintf(buf, BDEVNAME_SIZE, "%sp%d", hd->disk_name, partno);
else
 snprintf(buf, BDEVNAME_SIZE, "%s%d", hd->disk_name, partno)

### item Udba-205088
Site: dba | Thread title: Postgres query column with comma-delimited strings for array of strings
You need to convert the comma separated values to an array, then you can use the overlaps operator &&
select *
from pubnet
where string_to_array(oe, ',') && array['F3DH19860AA', 'F4DHAA']

### item Udevops-526
Site: devops | Thread title: How to remotely update AMI id in Jenkins EC2 plugin?
The PR you are linking to contains a link to a python script that does exactly this, since you can run that script from anywhere you can access your Jenkins server.

### item Unetworkengineering-51426
Site: networkengineering | Thread title: Difference between router and gateway
Router describes the general technical function (layer-3 forwarding) or a hardware device intended for that purpose, while gateway describes the function for the local segment (providing connectivity to elsewhere). You could also state that "you set up a router as gateway". Another term is hop which describes the forwarding in between subnets.
It's just a matter of perspective, the device is the same.

### item Usecurity-180357
Site: security | Thread title: Store Auth-Token in Cookie or Header?
Cookie Based Authentication
Pros
HttpOnly Flag: Session cookies can be created with the HttpOnly flag which secures the cookies from malicious JavaScript (XSS-Cross-Site Scripting).
Secure flag: Session cookies can be created with Secure flag that prevents the cookies transmission over an unencrypted channel.
Cons
CSRF: Cookies are vulnerable/susceptible to CSRF attacks since the third party cookies are sent by default to the third-party domain that causes the exploitation of CSRF vulnerability.

Performance and Scalability: Cookie based authentication is a stateful authentication such that server has to store the cookies in a file/DB in order to maintain the state of all the users. As the user base increases the backend server has to maintain a separate system so as to store session cookies.
Token Based Authentication:
Pros

Performance and Scalability: Tokens contains the metadata and its signed value(for tamper protection). They are self-contained and hence there is no need of maintaining state at the server. This improves the performance and thus scalability when the expansion is required.
CSRF: Unlike cookie-based authentication, token-based authentication is not susceptible to Cross-Site Request Forgery since the tokens are not sent to third party web applications by default.
Cons

XSS: Since the session tokens are stored in the local data storage of the browser and it is accessible to the JS of the same domain. Hence there is no option to secure session identifier from XSS attacks unlike HTTPOnly security flag which is available in the cookie-based authentication.
Conclusion

Both of the mechanisms have their own pros and cons as mentioned.In the present era of Application Development Frameworks, cons such as XSS and CSRF are taken care by the underlying framework itself and hence I feel it is without a doubt a clear trade-off on which developers and the stakeholders takes the decision.

### item Userverfault-312221
Site: serverfault | Thread title: Can a single network card have 2 IP addresses?
On linux, the command is ip addr add IFADDR dev STRING, where IFADDR and STRING are replaced by the IP address and device name. You can see some examples in the Guide to IP Layer NEtwork Administration with Linux. You'll also want to specify your routes that use that IP address using ip route. Again, the guide comes through.

Even though the syntax of the ip commands makes it seem that you are associating the IP address with a specific network card, linux considers the IP address as belonging to the overall system. Thus in some circumstances you may want to twiddle with ARP settings.

### item Usoftwareengineering-373959
Site: softwareengineering | Thread title: How do huge open source libraries get maintained while having code far from "clean code" practices?
Good answer here already, but let me say a word about your butterknife example: though I have no idea what the code does, at a first glance, it does not look really unmaintainable to me. Variables and method names seem to be chosen deliberately, the code is properly indented and formatted, it has some comments and the long methods at least show some block structure.

Yes, it does in no way follow Uncle Bob's "clean code" rules, and some of the methods are sure too long (probably the whole class). But looking at the code I still see enough structure so that they could be easily "cleaned up" by extracting those blocks into methods on their own (with a low risk of introducing bugs when using refactoring tools).

The real problem with such code is, adding one block and another block and another block works to some degree, sometimes over years. But every day the code gets harder to evolve a little bit, and it takes a little bit longer to modify and test it. And when you really have to change something which cannot be solved by "adding another block", but requires restructuring, then you will wish someone had started to clean up the code more early.

### item Uunix-604875
Site: unix | Thread title: Bash Alias - Precedence/Shadowing (/hiding/failing)
Bash does allow aliases to contain aliases but it has built-in protections against infinite loops. In your case, when you type lsc, bash first expands the alias to:
ls -Flatr --color=always
Since ls is also an alias, bash expands it to:
lsc -Flatr --color=always
lsc is an alias but, quite sensibly, bash refuses to expand it a second time. If there was a program named lsc, bash would run it. But, there is not and that is why you get command not found.
Addendum

It is different when lscR runs. lscR expands to:
ls -FlatrR --color=always
Since ls is an alias, this expands to:
lsc -FlatrR --color=always
Since lsc is an alias, this expands to:
ls -Flatr --color=always -FlatrR --color=always
Since ls has already been expanded once, bash refuses to expand it a second time. Since a real command called ls exists, it is run.
History
As noted by Schily in the comments, bash borrowed the concept of not expanding an alias a second time from ksh.
Aside

Aliases are useful but not very powerful. If you are tempted to do something complex with an alias, such as argument substitution, don't; use a shell function instead.

### item Udba-21778
Site: dba | Thread title: How to detect compatibility errors - SQL Server 2012 
Can you show the query? Just because it runs doesn't mean it's correct. :-) For example this is not legal, but it works:
SELECT CONVERT(SMALLDATETIME, modify_date) AS modify_date
FROM sys.objects AS o
ORDER BY o.modify_date;
Technically, it should be as follows, since o.modify_date is not in the SELECT list:
SELECT CONVERT(SMALLDATETIME, modify_date) AS modify_date
FROM sys.objects AS o
ORDER BY modify_date;

In this Connect bug, it was stated that this rule would be removed from the Upgrade Advisor. I suspect that one of the following (or both) happened:
They forgot to remove the rule as they said they would
They had other complications which prevented the above syntax from being blocked by the parser
That all said, there are some breaking changes the upgrade advisor will never catch. For example, this will work on 2005, 2008 and 2008 R2:
CREATE TABLE #foo(id INT);

IF OBJECT_ID('tempdb..#foo') > 0
BEGIN
 DROP TABLE #foo;
END
GO
CREATE TABLE #foo(id INT);
This will break in SQL Server 2012, however, since #temp tables now get a negative object_id. The proper way to test is:
IF OBJECT_ID('tempdb..#foo') IS NOT NULL
I go over a few other issues in this blog post. A couple of other breaking changes:
https://sqlblog.org/2011/06/28/sql-server-v-next-denali-breaking-change-to-fn_virtualfilestats

https://sqlblog.org/2011/07/08/sql-server-v-next-denali-breaking-change-to-system-databases-database_id-db_id
If you use any of the memory-related DMVs there has been a major overhaul to some of the columns:
https://blogs.msdn.microsoft.com/sqlosteam/2012/07/11/memory-manager-surface-area-changes-in-sql-server-2012/
Again, most of these are not caught by the upgrade advisor, so running that tool and not doing any thorough testing could really put you in a bad spot.

And I agree with Eric's answer - you should try to track deprecated events. For completeness, here are three approaches:
Profiler
Server-side trace
Extended Events

### item Udevops-5330
Site: devops | Thread title: How to run Dockerized graphical applications on a headless server with packages required for display remotely on clients as part of a separate image?
You can't run a program running on x11 without a x11 buffer somewhere, be it vnc, xvfb or whatever. You will always need x11 libraries on the system running the program or it couldn't work at all. That's akin to trying to run a C program without libc on the system.

Using system libraries from a different container with a volume is a bad idea, as it create a hard dependency on both containers using the same libraries, and is likely to crash somewhere when both systems try to acquire a lock on the library to load it.
I assume with a lot of tweaks it should be doable, but the added complexity is a real footgun and create more dependencies than should exist.

### item Unetworkengineering-8143
Site: networkengineering | Thread title: Cisco PBR with DMVPN and Dual ISP
Here's what I came up with until I find a better way.

event manager environment downInterface t1
 event manager environment upInterface t1
 event manager applet ShutInterface
 event track 89 state down
 action 0 cli command "enable"
 action 1 cli command "conf t"
 action 2 cli command "interface $downInterface"
 action 3 cli command "shut"
 action 4 cli command "end"
 action 5 syslog priority errors msg "Shutting down $downInterface"
 event manager applet NoshutInterface
 event track 89 state up
 action 0 cli command "enable"
 action 1 cli command

"conf t"
 action 2 cli command "interface $upInterface"
 action 3 cli command "no shut"
 action 4 cli command "end"
 action 5 syslog priority informational msg "Enabling $upInterface"

### item Usecurity-36156
Site: security | Thread title: User entered Javascript security implications
The Same Origin Policy for DOM access isolates sub-domains, therefor the impact of XSS is isolated to a specific sub-domain. The Same Origin Policy for Cookie scope isolates sub-domains in that they cannot read or write another sub-domain's cookies. Just make sure your main site is www.site.com and no cookie is scoped to *.site.com, as this would be accessible (if it was an HTTPOnly cookie, it would not be accessible from JavaScript regardless of its scope).

### item Userverfault-847302
Site: serverfault | Thread title: SSL certificate working in chrome but not openssl s_client or curl
Found a clearer tutorial that had a much simpler openssl.conf. In my original attempts to add SANs I must have un-commented extra lines in the conf that were adding extra info to the certs causing conflicts. Followed this template and my certificate is working all round:
[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req

[req_distinguished_name]
countryName = Country Name (2 letter code)
countryName_default = US
stateOrProvinceName = State or Province Name (full name)
stateOrProvinceName_default = MN
localityName = Locality Name (eg, city)
localityName_default = Minneapolis
organizationalUnitName = Organizational Unit Name (eg, section)
organizationalUnitName_default = Domain Control Validated
commonName = Internet Widgits Ltd
commonName_max = 64

[ v3_req ]
# Extensions to add to a certificate request
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = kb.example.com
DNS.2 = helpdesk.example.org
DNS.3 = systems.example.net
IP.1 = 192.168.1.1
IP.2 = 192.168.69.14
Thanks for your comments @garethTheRed. Your comments helped me re-think my approach to debugging this issue.

Even starting a post here helps me lay out what I've tried and helps the brain think up more possible solutions.

### item Usoftwareengineering-108449
Site: softwareengineering | Thread title: Why are so many HTML tables used in page markup?
To lay out tabular data.
Here are a few questions to ask yourself when choosing between tables and css containers.
Tables are for Tabular Data. Period.
The <table> tag is not evil. Despite what some people think and say, the point of CSS is not to never use it. However, a corollary to the principle of Semantic HTML is that you should never use tables for layout. Let me say that again, as its own paragraph, for emphasis:
Never use tables for layout. Ever.

If you can't decide whether or not a table is the right choice, ask yourself these questions:
“Do the rows or columns of information share a common attribute?”
“If I changed the order of the rows or columns, would it still make sense?”
“If I transposed the axes of the table (made rows into columns and vice-versa) would it still make sense?”
If the answer to the above is generally “Hrm...I guess not,” then you shouldn't be using a table.

If you need more convincing, see "Why Tables Are Bad (For Layout) Compared to Semantic HTML + CSS".

### item Uunix-493464
Site: unix | Thread title: "Variabilize" the ampersand (background a process)
It's not possible to use a variable to background the call because variable expansion happens after the command-line is parsed for control operators (such as && and &).
Yet another option would be to wrap the calls in a function:
mayberunbg() {
 if [ "$BCKGRND" = "yes" ]; then
 "$@" &
 else
 "$@"
 fi
}
... and then set the variable as needed:

$ BCKGRND=yes mayberunbg sleep 3
[1] 14137
$
[1]+ Done "$@"
# or
$ BCKGRND=yes
$ mayberunbg sleep 3
[1] 14203
$
[1]+ Done "$@"
$ BCKGRND=no mayberunbg sleep 3
# 3 seconds later
$

### item Udba-7077
Site: dba | Thread title: Best way to handle dates prior to 1000 A.D. in MySQL?
An alternative is to store each part of the date in a numeric field. So you would have three fields:
year SMALLINT # Store positive values for AD and negative for BC years.
month TINYINT
day TINYINT
This way it would still be human readable. The range of values for different numeric data types in MySQL are available at Overview of Numeric Types. The storage requirements are available at Data Type Storage Requirements.