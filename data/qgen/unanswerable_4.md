### item Udba-102179
Site: dba | Thread title: Why is vertical scaling expensive?
In some cases (perhaps most) the servers are already at capacity physically. An increase in the number of CPU's would require a motherboard swap. To add RAM to an existing server could be expensive, depending on how old the server is. Memory modules more than 5 years old and sourced from a dealer can be prohibitively expensive.

What all this amounts to is that upgrading from an 8 processor box with 32GB RAM to a 64 processor box with 128GB would involve purchasing an entire new server to replace the old one. This is still vertical scaling from the database/application point of view. A server that supports this many CPU's is likely far more expensive than 7 servers with 8CPU's each (keeping the original one as the 8th).

As per mustaccio's comment: High-end hardware is not just about more processors and RAM; designing hardware to support throughput and power/cooling requirements for dozens of multicore processors is far from trivial. Thus, a 256-core 2TB RAM server might cost $150000, which is about an order of magnitude more expensive than 64 4-core 32GB commodity servers

### item Udevops-5203
Site: devops | Thread title: Passing variables between scripts in a Jenkins pipeline
For Declarative Pipeline:
This question already has a highly-upvoted answer on StackOverflow:
If you want to use a file (since a script is the thing generating the value you need):

pipeline {
 agent { label 'docker' }
 stages {
 stage('one') {
 steps {
 sh 'echo hotness > myfile.txt'
 script {
 // trim removes leading and trailing whitespace from the string
 myVar = readFile('myfile.txt').trim()
 }
 echo "${myVar}" // prints 'hotness'
 }
 }
 stage('two') {
 steps {
 echo "${myVar}" // prints 'hotness'
 }
 }
 // this stage is skipped due to the when expression, so nothing is printed
 stage('three') {
 when {
 expression { myVar != 'hotness' }
 }
 steps {
 echo "three:

${myVar}"
 }
 }
 }
}
A second solution would be to write out output from your script directly or with writeFile and then later read it back in with readFile. However, this comes with the significant caveat that both the reading and writing must take place on the same node, so you can't use this to send data across nodes.
You can also can archive files centrally with archiveArtifact and retrieve them with copyArtifact (and then read in the file with readFile).

Finally, there are some answers to a near-identical question on StackOverflow that offer alternative solutions.
However, if you can, I would suggest using Scripted Pipeline instead, which allows a much simpler solution:
def String myVar
stage('my-first-stage') {
 myVar = sh(script: 'my-command', returnStdout: true)
}
stage('my-second-stage') {
 sh("my-other-command --var='${myVar}'")
}
(I also already answered this question for Scripted Pipeline over on ServerFault.)

It looks like some of these solutions have already been proposed in the comments, but you are concerned that they are not elegant enough. I'm not really sure what kind of elegance you're looking for, because I can't think of any way to simplify these answers in Jenkins-Pipeline-land.

### item Unetworkengineering-23426
Site: networkengineering | Thread title: Juniper trunking with two links (not using LAG)
One thing to keep in mind with trunk redundancy is that STP fails over slowly, even with Rapid STP. If you set up the two links as an aggregated channel, the link failover is much faster. STP failover is the slowest, routing protocol failover is an order of magnitude faster, and the aggregation channel failover is another order of magnitude faster still.

### item Usecurity-181255
Site: security | Thread title: How does GCC's -mmitigate-rop work?
Looks like it was added:
https://gcc.gnu.org/ml/gcc-patches/2015-11/msg01773.html
I don't know if more was added later: but I think this code just looks for an instruction that can be re-interpreted as a return.

### item Userverfault-8439
Site: serverfault | Thread title: Limit total bandwidth use per user
@WerkkreW got me on the right track. The solution I'll be going with is to use squid and its delay_pools feature.
The basic concept is to set up per-host (class 3) delay pools in squid.conf, then set each of them to the maximum amount of bandwidth I want to allow per user per day. Then, set the "fill" rate to be that maximum amount of bandwidth divided by one day's worth of time, so each delay pool will fill completely in one day.

Finally, using iptables I'll transparently redirect incoming requests on port 80 from my LAN to squid rather than DNATing them directly, so that users on the internal network are subjected to the bandwidth restrictions.
Thanks again, WerkkreW, for pointing me in the right direction.

### item Usoftwareengineering-250128
Site: softwareengineering | Thread title: Designing module interfaces
A truly independent module would expose API to create objects that it exposes and every such object would expose an interface that is clear to what the object is supposed to do.
Instead of any one gigantic API somewhere. 
For example jQuery - one object because it does one thing. 
jQueryUI is not one object but offers individual objects as widgets.
So from a client (code) from of view what the module does is well documented. 
Complex steps to create the objects is simplified.

How and when do you specify those dependencies?
The client code should be only adding the module as a dependency.
If module has other dependencies they need to be resolved as the module dependency is resolved. (RequireJS, Maven Dependencies)
Dependency Injection

This is different than the code dependency as you have noted. Model should be injected in the Module interface. Your service objects can also be injected here but in that case it is your services which will inject the Model and the service objects could be created only from your MyModuleFactory(Impl).
The client code you inject the MyModuleFactory. The injection chain will be resolved down the path.
Specific point About Model and Services - non Anemic model

Services may seem like an nice idea but it becomes a problem down the line.
Checkout cases against this.
Anemic Domain Model

### item Uunix-740653
Site: unix | Thread title: Does Bourne Shell have a regex validator?
No, but with some tools it's not hard to test whether a regex compiles or not.
For example, with grep: echo | grep -P '[' - the exit code, $?, will be 2, indicating an error occurred (and for this example, grep will print "grep: missing terminating ] for character class" to stderr - you can redirect stderr to /dev/null if you only want the exit code).
An exit code of 1 indicates that the regex compiled OK but didn't match the input.

These exit codes are specific to GNU grep. Other tools, if they even have such a capability, will probably have different exit codes, and different ways of indicating specific kinds of errors.
Note that this is not even remotely close to telling you whether a regex will correctly match what you want it to (and not match what you don't want it to).
In short, try it and test the exit code. And know your tools.

### item Udba-298979
Site: dba | Thread title: Is there a performance or storage space advantage to lowering time/timestamp precision in PostgreSQL?
If you need rounded values, storing them rounded is going to be faster and less error-prone than dynamically rounding each time you access it.
And having less precision means more ties so more opportunity for index duplicate compression (on versions new enough to offer that). It would also offer better compression for the datafiles when they are offline (like in backups) and possibly when online if your FS offers built-in compression.

### item Udevops-2956
Site: devops | Thread title: How do I get Kubernetes to work when I get an error "the server could not find the requested resource"?
As per https://kubernetes.io/docs/tasks/tools/install-kubectl/#before-you-begin:
You must use a kubectl version that is within one minor version difference of your cluster. For example, a v1.2 client should work with v1.1, v1.2, and v1.3 master. Using the latest version of kubectl helps avoid unforeseen issues.
So you need to either downgrade your kubectl version or upgrade your cluster version.

### item Unetworkengineering-6695
Site: networkengineering | Thread title: Cisco callmanager SIP features
The term you are looking for to describe this behavior, is an Outbound Campaign.
There is no built in functionality in Cisco Call Manager (CUCM) itself to do this.
However, both of Cisco's Contact Center products do have this ability. Unified Contact Center Express (UCCX) has a more limited capability for performing a Campaign, but is a much cheaper, much simpler solution to implement. It is still not cheap or simple though!

For more complicated out dialing ability, you'd want to look into Unified Contact Center Enterprise. At that point, due to the cost and complexity of UCCE, I'd recommend involving a Cisco Partner to design and implement the system for you.
With all of that said, if you were controlling a phone via one of the phone control APIs that Cisco provides, you may be able to rig something up yourself to do this. It just won't be as neat or integrated as the Cisco solution.

It might work something like this:
UserA indicates to your software that they're ready to make an outbound call to a customer.
Your software consults the list of customers to call, and sees that CustomerB is up next.
Your software looks up the relevant info of CustomerB in it's database (phone number, account number, etc).
Then, utilizing a Cisco TAPI configuration, your software takes control of UserA's phone.

Your software makes UserA's phone go off-hook, and initiate a call to the retrieved customer number.
UserA hears ringback on their headset and is now on a call to CustomerB, with all of their account info displayed on the screen via your software.
There are many other ways you could go about it, that's just one possibility. This doesn't give you supervisory ability to only connect the call if a customer answers, but that's part of what the UCCX and UCCE solutions provide.

### item Usecurity-5310
Site: security | Thread title: How difficult is it to modify an ISO image and still have the old md5 check sum?
It would be difficult to the point where to seriously suggest it even remotely possible is verging on lunacy.
There have been some demonstrations of theoretical attacks against MD5 wherein the "attacker" could create message data intended to yield a predetermined MD5 hash. But this is miles and miles away from adding a non-jibberish file to an ISO and having it give the same hash.

A much more likely attack scenario would be the MitM altering the page that lists the MD5sums before it gets to you so that you see the attacker's hash rather than the real one. However unlikely this may be, here are the hashes for your comparison:
ubuntu-11.04-desktop-amd64.iso 7de611b50c283c1755b4007a4feb0379
ubuntu-11.04-desktop-i386.iso 8b1085bed498b82ef1485ef19074c281

### item Userverfault-690155
Site: serverfault | Thread title: What's the easiest way to make my old init script work in systemd?
Seriously, a systemd unit file is trivial to write for a service like this...or for most services.
This ought to get you about 95% of the way there. Put this in, for example, /etc/systemd/system/solr.service
[Unit]
Description=Apache Solr
After=syslog.target network.target remote-fs.target nss-lookup.target

[Service]
Type=simple
EnvironmentFile=/etc/courtlistener
WorkingDirectory=/usr/local/solr/example
ExecStart=/usr/bin/java -jar -server -Xmx${CL_SOLR_XMX} start.jar -DINSTALL_ROOT=${INSTALL_ROOT}
Restart=on-failure
LimitNOFILE=10000
[Install]
WantedBy=multi-user.target
Note the stuff that isn't here, like the log file and such; systemd will automatically capture and log the service output under the service's name.

### item Usoftwareengineering-339829
Site: softwareengineering | Thread title: Strategy for avoiding defensive copies while keeping correct encapsulation
Sharing mutable state is not an evil you can fix with documentation. Why? Because programmers are amazing, at ignoring documentation.
What you can do is either defensive copy, which you rejected for performance reasons, keep it immutable, which you claim you can't, invalidate Whatever when it's dependency changes, or don't tell anyone else about this dependency so nothing else can change it.
I know two ways to invalidate Whatever:

Make Whatever an observer. When the dependency changes call Whatever.invalidate() so it knows it can't trust that it's dependency is the same.
Store a state counter. The dependency increments it's state counter every time it changes. When Whatever accepts the dependency it copies the counter. When Whatever uses the dependency it checks that the counter hasn't changed. Once it has Whatever knows not to trust its dependency anymore.
That lets you error out if the dependency has been mutated.

If you don't share this dependency then Whatever can control it's changes it self. Nothing else can change the dependency because nothing else knows about it.
Reference counting doesn't help here. What I think you're trying to do is not make extra clones when you've only stored a reference to it in one place.
That is a doable strategy. One that's easier to pull off if the things accepting the reference aren't responsible for deciding to clone.

Let's say I have an Injector class. Injector holds a reference to a Dependency instance. Might be Injector built it in the first place. Injector will never mutate Dependency so it doesn't count as far as sharing.
Injector can pass this instance once without cloning to anything, Whatever or, heh, whatever. After that it must clone. Now things accepting the Dependency reference don't need to worry about cloning and you only clone when you have to.

### item Uunix-44253
Site: unix | Thread title: How to clone/copy all file/directory attributes onto different file/directory?
After quite a bit of trial and error on the commandline, I think I've found the answer. But it isn't a cp-related answer.
rsync -ptgo -A -X -d --no-recursive --exclude=* first-dir/ second-dir
This does:

-p, --perms preserve permissions
-t, --times preserve modification times
-o, --owner preserve owner (super-user only)
-g, --group preserve group
-d, --dirs transfer directories without recursing
-A, --acls preserve ACLs (implies --perms)
-X, --xattrs preserve extended attributes
 --no-recursive disables recursion
For reference
--no-OPTION turn off an implied OPTION (e.g. --no-D)
-r, --recursive recurse into directories

### item Udba-108575
Site: dba | Thread title: Is an SQL Server trace 'considered harmful' in production?
The latest version of the RML Utilities (09.04.0051 as at today) support Extended Events tracing, so maybe you could work with your DBAs to do some controlled tracing. A screenshot from the help file:

They do however have a point because the default trace template provided with RML includes statement-level events (SQL:StmtStarting, SQL:StmtCompleted, SP:StmtStarting, SP:StmtCompleted), ie every statement in every proc. This could easily bring a server to its knees under the wrong conditions, eg scalar function in a SELECT statement running across a big table.
Extended Events (XE) were a bit limited in versions prior to 2012, but it is more lightweight.

You still need to be careful as SQL statement-level events will still incur overhead for very intensive workloads (sqlserver.sp_statement_starting, sqlserver.sp_statement_completed, sqlserver.sql_statement_starting, sqlserver.sql_statement_completed).
Execution plan capture (sqlserver.query_post_execution_showplan) can also be intensive.
Consider using the XETraceCaptureDefLightWeight.sql template which is provided and includes less events.

In summary I suggest moving to XE and using the lightweight XE definition provided with the latest versions of RML.

### item Udevops-5541
Site: devops | Thread title: How fast does Prometheus data grow?
Prometheus use a timeseries databases with vacuum, the documentation gives some maths to plan your disk consumption:
On average, Prometheus uses only around 1-2 bytes per sample. Thus, to
 plan the capacity of a Prometheus server, you can use the rough
 formula:
needed_disk_space = retention_time_seconds * ingested_samples_per_second * bytes_per_sample

So depending on your retention configuration, 1TB could never be reach or you can keep a very long time. That said it's using prometheus local storage, using another storage system will change the maths depending on the system concerned, influxdb is one of them and has its own documentation about storage.

### item Unetworkengineering-55235
Site: networkengineering | Thread title: Are ICMP Redirect messages really bad?
ICMP re-directs are most often seen when you have a host or router A in the same subnet with two other routers B & C and connectivity to both. Consider the following network:
|__192.168.1.0/24__|
 | | |
 |
 | |___192.168.8.0/24__|
 | | | |
 B C
|____|_____|____|
| | |
 A
A will have a route (most likely a default) pointing to B, and B will have a more specific route to a 192.168.8.0/24 pointing to C.
Without ICMP redirects, all traffic from A to 192.168.8.0/24 will be routed A->B->C

With ICMP re-direct enabled, B will inform A that C is a better next-hop and subsequent traffic will be routed A->C.
Obviously B is an extra hop and depending on what kind of box it is, it may introduce extra latency.
Disabling ICMP-Redirects and redesigning the network to avoid this situation entirely would be the preferred solution eg:
|__192.168.1.0/24__|
 | | |
 |
 | |___192.168.8.0/24__|
 | | | |
 B-----C
|____|__________|
| | |
 A

(or remove C entirely and hang 192.168.8.0/24 directly off B).

### item Usecurity-109471
Site: security | Thread title: Chrome: Watch for modified https-certificates
Is there anything like this for Chrome?
No. Chrome Extensions currently have no way to access information about the TLS certificates being used, and a proposal to add this functionality was rejected back in 2015.
Would this yield a good security layer?
Probably not.

Let's clarify the threat model here: you're concerned about a scenario where "a MITM exchanges the shipped https-certificate and my computer trusts the signing CA". This would require the attacker to obtain a valid certificate from a trusted certificate authority for a domain they do not own.

While CAs have mistakenly issued certificates to the wrong entities in the past (Comodo, WoSign, Symantec), these are pretty rare events, and CAs that consistently fail to uphold the validation requirements in the baseline requirements have their root certificates distrusted by browser vendors. (This happened to WoSign, and is currently happening to Symantec.)

Furthermore, the security benefit that these sort of alerts would provide depends entirely on your response to noticing a modified certificate.
Sites change their certificates all the time (often as frequently as once every other month, such as in the case of Let's Encrypt certs managed by Certbot), so the vast, vast majority of the time this alert appears it's just going to be a false alarm.
How do you plan to distinguish these false alarms from a legitimate attack?

Unless you have some out-of-band way of verifying whether the new certificate you're seeing is legitimate, an alert won't do much.

### item Userverfault-136549
Site: serverfault | Thread title: Rsync over ssh with root access on both sides
Actually you do NOT need to allow root athentication via SSH to run rsync as Antoine suggests. The transport and system authentication can be done entirely over user accounts as long as you can run rsync with sudo on both ends for reading and writing the files.
As a user on your destination server you can suck the data from your source server like this:
sudo rsync -aPe ssh --rsync-path='sudo rsync' boron:/home/fred /home/

The user you run as on both servers will need passwordless* sudo access to the rsync binary, but you do NOT need to enable ssh login as root anywhere. If the user you are using doesn't match on the other end, you can add user@boron: to specify a different remote user.
Good luck.
*or you will need to have entered the password manually inside the timeout window.

### item Usoftwareengineering-121730
Site: softwareengineering | Thread title: How can I make sure my evening project code is mine?
Don't listen to anyone who says "your own time is your own time, just don't tell anyone!" because that's incredibly bad advice that is almost certain to land you in trouble, if not at your current job then at some future one.

Not only do employment contracts vary too widely and significantly for any kind of generic advice to be useful, but different countries (including in the EU) or even different states within a single country (US) have different rules regarding how much of your work an employer owns, and even if you think you're on safe ground you can still get sued regardless, depending on how annoyed your employer is. Who has the deeper pockets for legal fees, you or your employer? I thought so.

Get permission first and get it in writing, so that your butt is covered should it become an issue later (even years later, with some completely different set of management who suddenly freaks out over what the previous management was totally relaxed about - you can't predict the future!)