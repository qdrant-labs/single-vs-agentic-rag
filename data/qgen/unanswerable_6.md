### item Usoftwareengineering-287085
Site: softwareengineering | Thread title: Best practice boolean assignment
I prefer 2, but I might go for a small adjustment to it:
obj.NeedsChange = ( obj.Performance <= LOW_PERFORMANCE );

To me the parentheses makes the line easier to parse and makes it clear at a glance that you are assigning the result of a comparison, and not performing a double assignment. I'm not sure why that is (as off-hand I can't think of a language where parentheses would actually prevent a double assignment), but if you must satisfy your reviewer then perhaps this will be an acceptable compromise.

### item Uunix-289477
Site: unix | Thread title: What is the difference between a name and a label in gparted?
A partition name is a name given in the GPT; it's external to the partition itself. A partition label is a label stored inside the filesystem; for example with ext-family filesystems, this is the label you can manipulate with e2label.
You can then use filesystem labels or partition names to mount the filesystems, which helps avoid issues with disk name changes. mount(8) has more information on this (search for "label"). It probably makes sense for the name to match the label...

### item Udba-165189
Site: dba | Thread title: SSAS Tabular: ImpersonationMode that is not supported for processing operations
I agree the documentation on this is a bit terse, but the error message on the other hand is very clear. ImpersonateCurrentUser is not supported for models attached to a SSAS instance.
This is mentioned in the documentation of the ImpersonationMode Enumeration:
ImpersonateCurrentUser: Not supported for tabular model databases attached to an Analysis Services instance.
As well as in the documentation on Impersonation (SSAS Tabular) under the Options header:

When configuring impersonation, or when editing properties for an
 existing data source connection in Analysis Services, you can specify
 one of the following options:
ImpersonateWindowsUserAccount
ImpersonateServiceAccount

### item Udevops-16
Site: devops | Thread title: How can I keep track of my Cloud Resource use?
A judicious usage of one of the cloud "orchestration" tools, such as Terraform or possibly Fugue seems to be the best way.
You can start small, pick a less important and not very extensive environment, carefully decipher it into automatable code and proceed from there.
Broadly this is referred to as infrastructure-as-code, for googling and other buzzword-oriented media applications.

More specifically, say, if you had your environment described in Terraform's HCL files, you would have required ID's exported as "outputs" and could operate on those from scripts/Jenkins jobs/etc

### item Unetworkengineering-37058
Site: networkengineering | Thread title: What do packets look like?
To transmit data you need a media (copper or optical fiber, for example) and each media has its own set of features than make it usable for data transmission.
For example copper is a good electrical transmitter and it's cheap (compared to other elements as silver or gold). Then, the best way to use it is to shape it as a cable and transmit electricity through it.

Now, suppose you need to transmit a jpeg image. The telecommunication protocols divide the whole file in chunks that can be transmitted and verified easily so the transmission is reliable. Those chunks are packets, and inside you will find a stream of bits. Each bit can be represented as a change in voltage of a electrical current.
The following is a simplification of bits traveling the cable:

When we use antennas as wifi or mobile (GPRS, 3G, 4G) we use electromagnetic waves. All around us there are electromagnetic waves (most of them are invisible, but there are other waves that we can see: the light is formed of electromagnetic waves, and the different colors that our eyes can perceive are different frequencies of the waves. Check the following chart):

So, the trick is to choose a range of frequencies and use waves in that range, that is invisble to the human eye. Electromagnetic waves don't depend on air, they can travel on vacuum allowing us to communicate with spaceships, satellites, etc.
How do they look?
Remember how in the copper cable a bit 1 was a high voltage and a bit 0 was a low voltage?

In electromagnetic waves we don't have voltages but we can play with frequencies. A bit 1 can be a frequency and a bit 0 can be a lower frequency than that of the former.
So, sending packets through electromagnetic waves could look like this (this is an oversimplified example):

### item Usecurity-242876
Site: security | Thread title: Is there any hope of getting my pictures back after an iPhone factory reset some day in the future?
Modern encryption is strong enough that there is no way to retrieve the lost data without the key. Although it's possible that it could be doable in the future in theory, consider that even the cipher 3DES, a trivial modification to a cipher designed nearly half a century ago in the 1970s, cannot be broken in the manner you want, and that was cryptography in its infancy. Modern iPhones use AES which has held up to 20 years of analysis and is showing no signs of meaningfully weakening.

Ciphers are never secure one day and fatally broken the next.
There is virtually never a massive breakthrough that renders a cipher useless, as attacks are improved incrementally.
If AES ever gets broken badly enough that you would be able to recover the encrypted data without the key, there would have been decades of slow improvements to the attack and we would all have known for years that it's too weak to even consider using.

If that were the case now, I'd tell you to wait a few decades and maybe, just maybe, a key recovery attack would be released, but that's not the case.
The data is gone. Plan for keeping backups in the future to avoid a repeat of this issue.

### item Userverfault-173977
Site: serverfault | Thread title: Inconsistent trailing slash in DOCUMENT_ROOT variable in PHP when using Apache
I have no idea why the slash is changing between your virtual hosts. By the way, is it important ? Just add a new slash to your programs (remove if a double slash is present) and the problem is solved.
I use
$realpath = realpath ($_SERVER['DOCUMENT_ROOT']."/");
$realpath = str_replace ("//", "/", $realpath);

### item Usoftwareengineering-306634
Site: softwareengineering | Thread title: Name of design pattern for single-observer
There are two cases:
The observer is specified (passed or otherwise injected) at construction time.
The observer is registered and unregistered after construction time.
If the observer is specified at construction time, it could be thought of as a peer.

If the observer is registered and unregistered after construction time, then the fact that only one observer is supported is best considered to be an implementation detail, and not exposed in any way, shape, or form. Pretend that you support multiple observers, assert that only one ever gets registered. This way, if you ever decide to allow multiple observers in the future, nothing but the implementation needs to change.

### item Uunix-138669
Site: unix | Thread title: Login site using cURL
Well, you'll need to store the session data in a cookie. You can use -c cookie_filename to create the cookie (add this to your login command). And then, for the other requests, you can read from the cookie with -b cookie_filename.
In example:
curl -s loginpage -c cookiefile -d "user=myself&pass=secure"
curl -s secretpage -b cookiefile
EDIT:

Notice many times loginpage is not the page you open with your web browser where you introduce your user and password. You'll have to check where the form is posting that data to (search the <form> tag in the source code and the action=... attribute). So, for example, if you want to log in to https://criticker.com, loginpage is https://www.criticker.com/authenticate.php and not https://www.criticker.com/signin.php, which is the one you open with your browser.

A tampering plugin/extension for your browser may help you find the correct loginpage and all the data that is being posted to it (like hidden input fields in the form).

### item Udba-246421
Site: dba | Thread title: Bad execution plan when having partial index and big In-clause in Postgres
This will be fixed in version 12, which will be released soon.
I think the summary here is that we are only willing to do so much work to try to prove a partial index can be used, because all queries have to go through that work even if they don't end up using the partial index. In this change, they just found a more efficient way to do that work in this particular case, and so no longer impose the 100-element limit to it.

### item Udevops-3253
Site: devops | Thread title: Nginx reverse proxy setup issues with Docker containers
Thanks to this question and answer here, I was able realize that I had two issues going on:
the containers have different default Docker networks because I am using two different docker-compose.yml files, I had envisioned my Ngnix proxy working independently from any of my API containers entirely, including the docker-compose, more on that issue below

the second issue is simply when I tried to proxy to 127.0.0.1:5023 that is localhost inside the Ngnix container, not the network outside of the Nginx proxy container

So the different default networks being created by docker-compose for my Nginx proxy docker container and my api docker container are because I am using two different docker-compose.yml files. This is because I have Jenkins builds for many API microservices so the have independent docker-compose files and I needed a Nginx proxy to forward requests on port 80 to each microservice.
To test this out, created a docker-compose.yml for both containers, the API and the Nginx proxy:
version: '3'

services:
 reverseproxy:
 build: 
 context: ./
 dockerfile: docker/nginxproxy/docker/Dockerfile
 image: tsl.devops.reverseproxy.image
 container_name: tsl.devops.reverseproxy.container
 ports:
 - "80:80"
 apistaging:
 build: 
 context: ./
 dockerfile: docker/staging/Dockerfile
 image: tsl.api.example.image
 container_name: tsl.api.example.container
 ports:
 - "5023:5023"
 environment: 
 ASPNETCORE_URLS: http://+:5023

Yes there was still an issue, the proxy pass to http//:127.0.0.1:5023, that forward remains in the Nginx Docker container and never finds the API running on the Docker host, I simply needed to use the docker-compose.yml service name to get to it:
upstream accountstaging {
 server apistaging:5023;
}
server {
listen 80;
 server_name account.staging.mysite.com;

location / {
 proxy_pass http://accountstaging;
 proxy_redirect off;
 proxy_set_header Host $host;
 proxy_set_header X-Real-IP $remote_addr;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header X-Forwarded-Host $server_name;
 }
}

### item Unetworkengineering-9292
Site: networkengineering | Thread title: Why do some common traceroute implementations default to using UDP probes?
The first version of traceroute was written by Van Jacobson and it used ICMP but it didn't work very well.
The vendor interpretation of ICMP in RFC792 was that routers should not send an ICMP error message in response to an ICMP packet (see edit notes below).
Therefore most routers would not send a "time exceeded" message in response to an echo request with a TTL of 1 or 0.
So he changed it to use UDP and lo and behold it worked great and there was much rejoicing (and adoption).

The traceroute tool on Linux and FreeBSD (and I assume Cisco) is based on Van Jacobson's work.

The spec was later changed to "in response to an ICMP error packet." The world progressed, vendors made changes to their stacks allowing ICMP error messages in response to echo requests, and with the rise of firewalls and ACLs, stray UDP packets sometimes get blocked, but ICMP echo request could get through. Of course, your success on that today varies wildly. I would expect the tracert and other tools were written at a time when using ICMP echo responses wasn't so problematic.

These days you can't really say UDP is better than ICMP. Or that either of those is better than TCP. It completely depends on the path you are traversing and the security policies in place. You may need to try one, both, or all three implementations.
Sources:
http://ftp.arl.army.mil/~mike/ping.html
http://www.inetdaemon.com/tutorials/troubleshooting/tools/traceroute/definition.shtml
Edit:
Changed RFC from IP (RFC791) to ICMP (RFC792) that says in the intro:

To avoid the infinite regress of messages about messages etc., no ICMP
 messages are sent about ICMP messages.
That's the bit that caused vendors to not send "Time Exceeded" errors for echo requests.
RFC1122, Requirements for Internet Hosts, in section 3.2.2. is the update that says hosts shouldn't respond to ICMP error messages.

### item Usecurity-214891
Site: security | Thread title: What is this user-friendly device registration process called?
It's the OAuth 2.0 device code flow. It goes something like this:
The device makes a request to the authorization server's device code endpoint
The authorization server responds with a code to show to the user and a URL where they should enter that code
The device displays the code and URL to the user
The device begins periodically polling the authorization server's token endpoint
The user visits the provided URL and provides their credentials along with the code given to them

The next time the device polls the authorization server's token endpoint the authorization server responds with an access token that the device can use to authenticate to the protected resource
Here's a diagram from the current draft RFC describing the flow:

+----------+ +----------------+
 | |>---(A)-- Client Identifier --->| |
 | | | |
 | |<---(B)-- Device Code, ---<| |
 | | User Code, | |
 | Device | & Verification URI | |
 | Client | | |
 | | [polling] | |
 | |>---(E)-- Device Code, --->| |
 | | & Client Identifier | |
 | | | Authorization |
 | |<---(F)-- Access Token ---<| Server |
 +----------+ (& Optional Refresh Token) | |
 v | |
 : | |
 (C) User Code & Verification URI | |
 : | |
 v | |
 +----------+ | |
 | End user | | |
 | at |<---(D)--

End user reviews --->| |
 | Browser | authorization request | |
 +----------+ +----------------+
Figure 1: Device Authorization Flow

Since the device code flow is still just a draft, not a lot of OAuth 2.0 libraries have support for it, nor do all OAuth 2.0 identity providers. Luckily the protocol is pretty straightforward, so it shouldn't be too hard to build from scratch given a decent HTTP library. There's also a proxy server out there that can implement the device code flow on top of an existing OAuth 2.0 authorization server.

### item Userverfault-136753
Site: serverfault | Thread title: Giving SSH access to a user, and security issues
As a normal user your friend won't be able to do too much harm to your server (sure they could spawn off a fork bomb or fill your disk, but if they're really a friend they probably wouldn't pull a dick move like that). My friends get actual login shells on my machine if they ask for an account, and a stern lecture that if they do anything that pisses me off they'll get booted off the machine.

It sounds like you don't trust your "friend" very much, so in addition to The Rook's answer I'll also say that a halfway competent person with the ability to run a PHP script can be almost as dangerous as a user with unrestricted (login-able) SSH access, and I assume your server allows PHP.

Remember that the user can run untrusted code via PHP, up to and including downloading, compiling and running other arbitrary programs on your system (albeit within the limitations of the web server user's privileges).
Generally speaking unless you are chrooting/jailing your webserver anything your friend could have seen with his login shell he can see with some not-terribly-creative PHP scripting.

Bottom line: giving someone an account on your system and then locking out their shell in /etc/passwd & setting the SFTP chroot option helps, but you should really consider the security implications of any access, and your level of trust in this person.

### item Usoftwareengineering-288616
Site: softwareengineering | Thread title: Creating two-way object references and keeping data integrity
First and foremost, determine what is more common in your system - to list groups of a specific player or to list players of a specific group. Depending on which case is more common, implement it accordingly. If you try to implement both equally, you will take a performance hit for both.
So, assumption goes Player belongs to a group, so:
public class Group {
 public void AddPlayer(Player player) {
}
public void AddPlayers(IEnumerable<Player> player) {
}
}
Now that we got that out of the way.

public class Player {
 public Ienumerable<Group> GetRelevantGroups() {
 // Assuming you have some groups provider in this class. You should anyways.
 return this._groupsService.GetGroupsWithPlayer(this.Id);
 }
}
Using both:
// Adding a bunch of players to a group.
myGroup.Add(players);
// Getting all groups for specific player.
var playerGroups = player.GetRelevantGroups();

### item Uunix-187905
Site: unix | Thread title: 'Pass' password manager - does it require public key?
The pass password manager requires a public key for encrypting its files (where the managed passwords are stored) - and it requires a private key to decrypt its files.
It isn't possible to configure pass to use gpg's 'pure' symmetric file encryption (cf. the -c or --symmetric GPG options).

This is due to the design of pass - using GPG's public key cryptography for file encryption/decryption allows for flexibility, e.g. for configuring multiple keys - say - such that a group of users has access to the managed passwords.

Also note that GPG uses a hybrid scheme when encrypting a file for one or many recipients (i.e. using one or many public keys): it randomly generates a session key for the symmetric encryption of the file and then just uses the public key/keys to encrypt the session key.

### item Udba-27315
Site: dba | Thread title: Disabling logging on certain tables
Is it possible to disable logging on certain tables within the database?
Can I place the two tables in the same schema, then disable logging on the schema?
Is the only option to move the two tables to a separate database, and disable logging there?
Logging of user operations cannot be disabled.

There is a class of operations called minimally-logged operations that only allows a transaction to be rolled back (as opposed to also being able to roll forward). However, it doesn't sound like what you're doing would meet the criteria for that to apply, nor do I think this would solve the problem anyway.

The SQL Server solution would be to land the staging tables in a new database in SIMPLE recovery, separate from the aggregation results database, which I assume is in FULL recovery. While this wouldn't decrease the volume of logging, it would eliminate the need to back up the log generated by the data loads. (See my blog post here about logging, and some of the factors involved in choosing a database's recovery model.)

Separating the tables into another database would provide the flexibility to land the log file on a faster I/O subsystem, probably a small array of locally-attached solid-state drives.

Also, consider that SQL Server alone may not be the best solution to solve the problem. There are other RDBMS solutions that offer the ability to completely disable logging for certain tables. The data could be staged and aggregated in another system, and the results merged into the existing SQL Server database, which is well-protected by full logging and backups.

### item Udevops-1002
Site: devops | Thread title: How can I experiment with Cloud (Azure, AWS, Google, etc) without going broke?
The three major cloud platforms you mentioned have either free trials or a free tier; these all include spending and resource caps which prevent you from spending more than your free trial allows:
Azure
Azure offer £150/$200/€170 for the first one month of usage, in addition many of Azure's services have a free or low cost tier:
App Service Free Tier
SQL Azure Basic Instance @ £0.005/hour
Azure Machine Learning Free Tier
Azure Service Bus @ £0.04/million operations

Azure Functions @ £0.15 per million executions
If you have a MSDN or Visual Stuido Online account you can also get £100/$150/€130 per month of credit just because you are a subscriber to one of these services.
If you are a startup you may qualify for $120,000 of Azure Credits to host your application through Microsoft's BizSpark programme.
Amazon Web Services
Amazon have a Free Tier which includes:
750 Hours of EC2 which equates to about a month of a t2.micro instance
750 Amazon RDS
5GB S3

250,000 AWS IoT Messages
... and more
In addition there perpetually free usage allowances on most services:
AWS Lambda: 1 million free requests a month
DynamoDB: 25GB Storage
Amazon SNS: 1 million publishes
... and more
Google Compute Platform
Google offer a $300 free trial for 12 months in a similar deal to Amazon. In addition they have free usage tiers for many of their core offerings:
Google App Engine: 28 instance hours / day
Google Cloud Database: 1GB Storage

Google Compute Engine: 1 f1-micro instance / month
Google Pub/Sub: 10GB messages / month
Google Cloud Functions: 10 million executions / month
... and more

If all of that wasn't enough for you most of the cloud providers will compensate you in credits if you blog about their services in detail, you do have to put in a substantial effort up front and "appear" on their radar by writing blog posts, presenting at meetup and conferences but once they see you they will gladly put $100 a month towards your further learning.

### item Unetworkengineering-47114
Site: networkengineering | Thread title: Better throughput with 100 Mb NIC setting
This is a buffering issue. I had the same problem with a new Level 3 circuit. Their NID apparently has no measurable buffers, so feeding it at a rate 10x the circuit rate (1000 vs. 100) leads to all manner of poor performance.
(They had the customer side set to auto (1000) but manually set the network side to 100. After a week of arguing, they set both sides to auto and the problem went away -- Charter/Spectrum, the actual carrier for the circuit, actually has a clue. Shocking, I know.)

Note: Cisco has no mechanism to control the autonegotiation process. There's no way to tell it to advertise 100/full. And autoneg is the only way to get full duplex -- unless you control both sides.

### item Usecurity-108104
Site: security | Thread title: Why would the government collect Wi-Fi SSIDs via manual door-to-door questioning of citizens?
I had a chance to ask an insider, and they said that at that time there was a group of reactionary changing the Wi-Fi names to antigovernment statements, so they had to collect them to stop this. But I think if they really wanted to do this they could use other means, couldn't they? So this might be a way to remind people about their existence?