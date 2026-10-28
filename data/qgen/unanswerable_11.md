### item Uunix-245746
Site: unix | Thread title: How to change theme with zsh
when you're done editing your ~/.zshrc, in a shell prompt run the command source ~/.zshrc.
it will read the config from ~/.zshrc and it will apply it, it's like reload your config.

### item Udba-7537
Site: dba | Thread title: Query best possible matches and order them
SELECT col1, 
 col2,
 col3, 
 col4, 
 col5, 
 col6
FROM TableX 
WHERE col1 = 1 
 OR col2 = 2 
 OR col3 = 3 
ORDER BY (CASE WHEN col1 = 1 THEN 1 ELSE 0 END) +
 (CASE WHEN col2 = 2 THEN 1 ELSE 0 END) +
 (CASE WHEN col3 = 3 THEN 1 ELSE 0 END) DESC,
 col4, col5, col6
or, for MS-Access:
ORDER BY IIF(col1 = 1,1,0) +
 IIF(col2 = 2,1,0) +
 IIF(col3 = 3,1,0) DESC,
 col4, col5, col6

### item Udevops-1221
Site: devops | Thread title: How to get the ARN for an arbitrary Amazon Resource?
https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html lists the schema for (I believe) all of the ARNs that Amazon supports. Text in italic red indicates where you should substitute in your own value, rather than the literal string, and there are examples in each section to help figure this out.
Be warned that IAM is less usefully restrictive than it appears on first glance.
To start with, most services have only partial IAM support.

Secondly, often the things that are supported at a resource level are supported only in very specific ways; for instance, granting all permissions on a subnet ARN does not grant the attached users the ability to fully manage instances in that subnet, as AttachVolume only supports restricting by volume id, etc.

Thirdly, if the users are going to use the Amazon web console at all, they must have broad viewing permissions, as the console was not written with PoLP in mind and issues non-resource-restricted API calls (and often merely dumps errors in the javascript console!).

### item Unetworkengineering-85358
Site: networkengineering | Thread title: Can ARP tables store addresses for other networks?
"It doesn't work like that."
Nothing in network A will even attempt to find network B via layer-2 (ARP), because it's not a local ("on-link") network. They will forward that traffic according to their route table -- without a more specific route (192.168.2.0/24 via 192.168.1.5) the default route applies. You could attempt to "poison" the arp tables, but (a) they won't be consulted, and (b) any sane host will ignore such martians.
Your options are:

add a route to the router for network A (which you said is not available to you)
add a route on every node in network A
send an ICMP redirect for network B hosts (but modern security is to ignore redirects)

### item Usecurity-159756
Site: security | Thread title: Dangers of one step email subscription
I see one of the possible inconveniences in a situation when company's newsletter can't be unsubscribed. An attacker programmatically subscribes many real users. The company sends its newsletter to subscribed users as usual. Some of the users who did not subscribe themselves might unsubscribe using the proper link included in the newsletter. Some might just move the message to spam. The attacker could then (periodically) make sure all the targeted users have subscribed again.

But I'm not sure about the efficiency of such attack and how likely it could cause real legal consequences for the attacked company. Nevertheless, the company could end up sending quite a lot of spam.

### item Userverfault-904756
Site: serverfault | Thread title: Why the Sequence number in an ACK packet is incremented?
In TCP, the protocol keeps track of what has been sent by using a Sequence number. Effectively it's a counter of everything that was sent+1.
More details on https://www.rfc-editor.org/rfc/rfc793#section-3.3
ACK is incremented by 1 because the packet is carrying a SYN, it's not empty.
SYNs contribute to incrementing the SEG.LEN, as explained in the rfc:
SEG.LEN = the number of octets occupied by the data in the segment
(counting SYN and FIN)

Had the packet been empty and without SYN/FIN, the counter would have not been incremented.
This is also contemplated in the rfc where it states that the next sequence number to be sent must be greater or equal than the one indicated in the ACK:
A new acknowledgment (called an "acceptable ack"), is one for which the inequality below holds:
SND.UNA < SEG.ACK =< SND.NXT
where SND.UNA is the oldest unacknowledged sequence number and SND.NXT is the next sequence number to be sent.

By incrementing the seq. number the packet is basically asking the other party "I expect you to send me the first byte of data now"

### item Usoftwareengineering-165164
Site: softwareengineering | Thread title: Should I be using a JavaScript SPA designed when security is important
I wouldnt rely on the client side javascript to tell you if the user is logged in. That can easily be changed.
The couple of times I've made 'single page' type web interfaces, I did it with two 'pages'.
The first page encountered was a login page.
When submitted, that allowed for the creation of a traditional web session on the server, and then returned back the 'application' page, which then immediately loaded everything by ajax requests.

For all subsequent ajax calls the cookie was sent with the request, so authentication worked the same way as it does in traditional applications.
So there's nothing particular you have to do differently in your javascript to support this.
Every server side response must, of course, validate the session.

I say two 'pages', but they were really the same 'index.php' - it just returned either a login page or the main application page depending on whether a valid 'login' was set in the server-side session. In your case, you'd just have node return two different page templates.

### item Uunix-487052
Site: unix | Thread title: Where is page table stored in Linux?
Yes, the page tables are stored in the kernel address space. Each process has its own page table structure, which is set up so that the kernel portion of the address space is shared between processes. The kernel address space is not accessible from user space, however. The user space code communicates with the kernel in a controlled manner using system calls. After a successful system call the processor enters a privileged state in which the kernel address space is available.

### item Udba-150329
Site: dba | Thread title: Is it possible to do this math in a view?
this sorts on PlanCode - if you have duplicates then use a row_number()
if you need a particular order then you need to have that order in the table
select PersonID, PlanCode, Deduction, [sum]
 , case when [sum] < 400 then 0 else [sum] - 400 end as oop
 from
 ( select p1.PersonID, p1.PlanCode, p1.Deduction 
 , ( select sum(p2.Deduction) 
 from payroll p2 
 where p2.PersonID = p1.PersonID 
 and p2.PlanCode <= p1.PlanCode ) as [sum] 
 from payroll p1 
 ) tt
 order by tt.PersonID, tt.PlanCode
or

select p1.PersonID, p1.PlanCode, p1.Deduction 
 , case when sum(p2.Deduction) < 400 then 0 else sum(p2.Deduction) - 400 end as OOP
 from payroll p1 
 join payroll p2 
 on p2.PersonID = p1.PersonID 
 and p2.PlanCode <= p1.PlanCode 
 group by p1.PersonID, p1.PlanCode, p1.Deduction

### item Udevops-2310
Site: devops | Thread title: Get all change logs of since last successful build in Jenkins Pipeline
You may try something like this:
node('my_kubernetes_pod') {
 passedBuilds = []
lastSuccessfulBuild(passedBuilds, currentBuild);
def changeLog = getChangeLog(passedBuilds)
 echo "changeLog ${changeLog}"
}
def lastSuccessfulBuild(passedBuilds, build) {
 if ((build != null) && (build.result != 'SUCCESS')) {
 passedBuilds.add(build)
 lastSuccessfulBuild(passedBuilds, build.getPreviousBuild())
 }
}

@NonCPS
def getChangeLog(passedBuilds) {
 def log = ""
 for (int x = 0; x < passedBuilds.size(); x++) {
 def currentBuild = passedBuilds[x];
 def changeLogSets = currentBuild.rawBuild.changeSets
 for (int i = 0; i < changeLogSets.size(); i++) {
 def entries = changeLogSets[i].items
 for (int j = 0; j < entries.length; j++) {
 def entry = entries[j]
 log += "* ${entry.msg} by ${entry.author} \n"
 }
 }
 }
 return log;
}

Additionally, you may try out "Changes Since Last Success Plugin":
https://wiki.jenkins.io/display/JENKINS/Changes+Since+Last+Success+Plugin
But it will not work together with pipeline, this is a separate approach.

### item Unetworkengineering-868
Site: networkengineering | Thread title: Which is the Preferred location of an IPS within a network?
Use google to check/translate the following blog post (in portuguese, from the author of the book Cisco Firewalls):
http://alexandremspmoraes.wordpress.com/2012/07/03/multiplas-camadas-de-defesa-a-complementaridade-do-firewall-e-do-ips
For me this is the best explanation I've seen on where to place IDS and IPS (and their complementarity).

### item Usecurity-192943
Site: security | Thread title: Are EU cookie consent forms safe?
It increases dialog box fatigue. By overflowing the user with mundane dialog boxes, they are more likely to get into the habit of just clicking OK to remove the dialog box from their screen. This increases the risk of a user clicking OK on some important security decision presented in a dialog window.

### item Userverfault-656753
Site: serverfault | Thread title: Configuring Chroot for SFTP Users
Internal-sftp require chrooted user home to reside inside root-owned dir:
/some/path/root-owned/user-dir1
 /user-dir2
Root-owned dir should have 555 permissions and user-dirs should be created by root and owned by specific user. Inside subdirs user can do anything, but he can't delete or rename user-dir[12].
This is internal-sftp restrictions.

### item Usoftwareengineering-19851
Site: softwareengineering | Thread title: How to handle conflicts between developers in your team?
I have had a team of 10 people for two years without a conflict(touch wood) I could be lucky or may be doing something right. The best way to handle conflict is never to let one exist for a longer time. There are several core values that you can preach.
Team Spirit
Fairness in everything (compensation/rewards)
Being appreciative
Give recognition, responsibility
Give freedom
Let people know they are not greater than the team
Personal success means nothing if the team fails

attach personally to people
never show a carrot you dont intend to give
never hire(no matter how good) who could ruin the team
communicate more often etc etc.
Appreciate whenever someone goes beyond the job
Give regular feedback on performance and set expectations preferrably monthly.
Let people know when they behave like children.
All these take guarded effort from some one.
Software is pretty much a team game individual brilliance is generally short lived. If I go by your examples :

We have decided decided to go with dependency injection. Period. We will see if it is the best way or not. If it is not, you get a chocolate :-) till than cooperate and let's make this thing happen
If the rest of the team is slowing you down you help them to make it faster they are your teammates you are the elder guy, help them. I know you are good.
Talk to both of them tell them they are spoiling the environment. If nothing works get rid of one of them or both of them.

One thing I find very effective is to repeat "we are a good team" and repeat "we are a team to the lonely one's".

### item Uunix-372505
Site: unix | Thread title: How to select the mq-deadline scheduler?
You also need to enable CONFIG_SCSI_MQ_DEFAULT
Symbol: SCSI_MQ_DEFAULT [=y]
Type : boolean
Prompt: SCSI: use blk-mq I/O path by default
 Location:
 -> Device Drivers
 -> SCSI device support
 Defined at drivers/scsi/Kconfig:50
 Depends on: SCSI [=y]
And voila
$ cat /sys/block/sda/queue/scheduler
[mq-deadline] none

### item Udba-23487
Site: dba | Thread title: Page setup and print layout in SSRS Report
The page setup in the print options does not control your report parameters. You will need to use the Height/Width property of the report inside BIDS. Orientation in SSRS is controlled by setting these values. We have a report at our office that is similar to what you describe and there are two ways of (semi) achieving what you want to get done.

The first is to use a separate report for each page that you want. This gives you complete control over all elements of each page such as height/width etc but may be more work for you to do and possibly more maintenance in the long run. It does however mean that should you change elements of the report later you only have to retest the bits you have changed, not the entire report.

The second one is to you expressions to force page breaks. This will work for reports that need the same orientation (as they inherit the properties set on the report container) but will not work for a report that has a different orientation. A link to an example of page breaks is below:
http://msdn.microsoft.com/en-us/library/ms157328.aspx#AppearanceofReportData
I hope this makes sense and that it helps you in what you want to achieve.

### item Udevops-3510
Site: devops | Thread title: What are Design Patterns for creating images?
The general design pattern is one container = one running service - see the initial comment at https://docs.docker.com/config/containers/multi-service_container/
Now, after spending about a year developing a multi-service application relying heavily on docker this is what works for me:
Avoid creating files inside the container unless it is your storage engine - in which case use volumes (recommended by Docker and also common sense) - we use Elasticsearch for that.

If I need multiple custom configurations I am trying to either load it from somewhere (DB, Environment) or I mount the configuration as a volume like
-v config.yml:/usr/src/app/config.yml
In general, we have one service = one repository, but sometimes you have to copy all the dependencies in order to just create one script. So we have one repository where these scripts are aggregated and I change the CMD with an environment variable like this:
CMD cd /usr/src/app && python -u $RUN_SCRIPT

It can be probably improved with a combination of ENTRYPOINT and CMD as described here http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/
Then we use various docker-compose.yml files for getting the setup we need.
For some operations (like DB setup) we either run one container like
docker run --network ournetwork init-profiling
or I can run a command inside that container
docker run -it --network ournetwork init-profiling bash
# run_command.sh
^D

We spent some time minimizing the footprint of containers, they can quickly get bloated. For example, we use a common base image for our python containers. Also, things like pip freeze do make sense only if you use a separate virtual environment for each repository/container.
We do not use swarm/kubernetes for now, so I cannot add any additional guidelines for that.

### item Unetworkengineering-28373
Site: networkengineering | Thread title: Why do we use VLAN?
According to my understanding, the network switch will look out for the specific MAC address and then it will forward the frame so basically it doesn't broadcast the frames then why do we make VLANs?

While VLAN is a tool often used to reduce the size of the broadcast domain, its major underlying goal was to partition a physical LAN device (switch, bridge) into multiple logical portions (VLANs). Think of a single physical device offering Ethernet LAN services for multiple departments within an organization. Every department would get a piece of that single physical device -- that is, some ports restricted into a VLAN. Thus one would not need to buy dedicated LAN hardware for every department.

### item Usecurity-220828
Site: security | Thread title: Does injecting my own key material into the authenticator undermine authenticator's attestation?
The argument is that, if you supply your own key material, the key manufacturer has no way to verify that the key material is sufficiently random, not stored elsewhere, etc.
Imagine if you are the victim of a sophisticated targeted attack, and you generate the key material on a computer that has malware on it which exfiltrates it to the attacker.

Or perhaps a supply chain attack, Alice sets the key material then hands the authenticator to Eve to deliver it to Bob, but by the time Bob receives it Eve has changed the key material to a value she knows.
This would be fixed by Bob setting his own key material, but then Alice has to trust Bob to do that correctly.

It sounds like Yubico wants to be able to say "if an attestation is verified up to our root cert, we guarantee that the associated keypair comes from a Yubikey, and the key material used to create the keypair was generated securely by us and is stored only on the authenticator." If they allowed you to set your own key material they would no longer be able to make that guarantee.

Now this doesn't really matter for public websites, and most (or all) public websites that allow U2F or WebAuthn for 2nd factor don't bother checking attestation at all. But for something like a high security intranet, there could be value in auditing a small number of authenticator manufacturers and using attestation to only allow authenticators from those manufacturers. In that scenario not being able to modify the key material could be seen as an advantage.

Also, it looks a bit ironic since these days financial institutions tend to trust SMS and not U2F, even though SMS is anything but secure.
I imagine he's talking about employees of a financial institution rather than clients.

### item Userverfault-965716
Site: serverfault | Thread title: AWS S3 bucket size has exploded, but I can't figure out how
It was aborted multipart uploads. S3 keeps every uploaded part of every failed multipart upload indefinitely by default! A process had been failing and retrying multipart uploads without explicitly cleaning up the failed transfers.
We remedied this by temporarily enabling versioning, setting a lifecycle rule to remove aborted multipart upload chunks after 1 day, then waited a day, disabling versioning again once the chunklets were cleared.