### item Udba-313984
Site: dba | Thread title: Postgres order by with multiple columns
Simply use order by least(date_one, date_two)
The least function returns the lowest of two values, Coincidentally, you may use greatest(date_one, date_two) to get the highest value. This also works with null, however if both values are null obviously either of these functions will return null since there is nothing to compare.

Keep in mind that using least or greatest will also make any indexes you've created for ordering these 2 columns unusable unless you create it as an index over an immutable function using least/greatest. Although I am not sure that's the best move here in your scenario.

### item Udevops-1782
Site: devops | Thread title: Artifactory vs Git for Infrastructure Version Control / Configuration Management
Version Control (using say Git) and Artifact Management (using Artifactory) are complementary. Version control is useful for easily browsing the historical changes and who made them. Artifact management tools can do this but it's clunky. Also they don't offer a fine grained view of changes, as one version change might involve a large amount of changes.

When integrated with a workflow like feature branches, version control offers some real benefits around collaboration particularly for distributed teams.
Some places use just version control with no artifact management, i.e. Reddit. They deploy to 800 servers 200 times a week using just Git. This may or may not be the best solution for you.

An artifact can be many things, not just a binary. It can be a tar ball of files, an rpm, a virtual machine or a docker container. But I've not really seen artifact tools used to deploy configuration management, you could just deploy straight from Git or bundle it into a tarball or rpm.

### item Unetworkengineering-555
Site: networkengineering | Thread title: Unable to connect via VPN to remote network
I did two things to make the PPTP wireless client work:
1. Added a static NAT on the Buffalo for a wireless device.
2. Added the following to the ASA:
policy-map global_policy
class inspection_default
inspect pptp
After adding the static NAT but before modifying the ASA I saw the following error in the ASA log:
May 20 2013 06:42:05: %ASA-3-305006: regular translation creation failed for protocol 47 src inside:192.168.1.50 dst outside:(vpn-at-work-IP-address)<br>
I had to allow PPTP inspection.

So I am able to connect via IPSec and PPTP through 2 NATs, although evidently that's not a best practice, so I'll be reading up more on that.

### item Usecurity-30310
Site: security | Thread title: Firefox pre-downloading
Technically, the popup does not ask you whether you really want to download the file; that decision, you already took when you clicked on the link which triggered the download. The popup asks you what Firefox should do with the file when it has been fully downloaded.
Potentially hostile files can be a security issue.
Filesystems normally store files as bunch of bytes and are thus nominally immune to the file contents; but modern operating systems are not content with handling files as files.

For instance, if you open a file explorer to see the directory in which downloaded files are stored, and the file has a name which ends in '.jpg' or '.png', then the file explorer will try to interpret the file contents automatically, as a picture, so as to compute and display a miniature view of the said picture.
Any security hole in the JPEG or PNG support library could then be exploited by a malicious file, and it does not require any "opening click" on the file, just opening the directory.

The Web is a harsh place.

### item Userverfault-544340
Site: serverfault | Thread title: Why is crontab file periodically overwritten?
Argh! OK, this was a communication error. We're deploying a Rails app on the server which uses a gem called Whenever:
https://github.com/javan/whenever
This gem was overwriting the changes I made in the crontab file each time I deployed. Solutions are to either remove the gem, or to use it to set up the jobs.

### item Usoftwareengineering-187548
Site: softwareengineering | Thread title: What happens when using address before it's allocated?
No, absolutely not. If that were what invariably happens, we could use that to our advantage and specify it in the standard; known behaviour, even if it is a crash, is virtually always better than unknown behaviour.
But instead, the system response depends on details of the implementation, of the previous actions of the program, on the state of the runtime etc.
in an unpredictable way.

On modern operating systems referencing an address that doesn't belong to you may usually trigger a segmentation violation, but definitely not always.
A segmentation violation might occur, but not until much later.
Even worse, your program might appear to work but silently do the wrong thing.
That's why the language standard has to take the worst possible option and declare that the behaviour is undefined.

(Note that goodness depends on your viewpoint. For the compiler implementor, undefined behaviour is good because it means that whatever you do is, by definition, right. For the application programmer it is bad, because it leads to application errors, and even to the particularly insidious kind of errors where things sometimes work and then fail spectacularly at the least opportune moment.)

### item Uunix-135000
Site: unix | Thread title: Is there a command line method by which I can check whether a downloaded file is complete or broken?
The most common way to verify the integrity of downloaded files is to use MD5 checksums. This assumes that the site you are downloading from actually published MD5 checksums of their files. You can verify a MD5 checksum by creating your own checksum of the downloaded file and comparing it to the published checksum. If they are identical the file you have downloaded is complete and not tampered with.

If you don't expect the file you are downloading to change you can precompute a checksum and hard code it into the script, but if the file is ever updated the verification will fail.
To create a MD5 checksum of a file run md5sum myFile. In the case of wget you might find this command useful, especially if the file you are downloading is large:
wget -O - http://example.com/myFile | tee myFile | md5sum > MD5SUM.

This will create a checksum of "myFile" while downloading and save it to the file MD5SUM, possibly saving you some time.
In the case of a dropped connection I think the best way would be to check the exit codes of wget. If the download is successful without any errors wget will return 0. Anything else indicates something went wrong. Take a look at the "Exit status" section of man wget.

### item Udba-290210
Site: dba | Thread title: Is OPTION (RECOMPILE) used in production environments?
OPTION(RECOMPILE) is used in real word production scenarios. I've employed it to address parameter sniffing and optimize kitchen sink queries. It might be the answer for your issue but the symptoms suggest OPTIMIZE FOR UNKNOWN (same as local variables) may address the problem as well.
I certainly would not avoid an option just because a bug once existed, and it was fixed several years ago. The main risk with OPTION(RECOMPILE) is when it's used inappropriately, such as high-frequency queries.

### item Udevops-8722
Site: devops | Thread title: What are some reasons for using an Ansible role for Certbot vs. Ansible's native `acme_certificate` module?
Thanks for linking your question. Here's the github thread for reference: https://github.com/geerlingguy/ansible-role-certbot/issues/87
There are many different ways to get certs from a CA. certbot (what this repo uses) is just one of the ways which uses letsencrypt as a certificate authority. acme_certificate is more generic and if you can't use letsencrypt then it might be a good tool to check out for http-01, dns-01 and tls-alpn-01 challenges.

Certbot is a great way to manage certs from letsencrypt, so if you're needs are fairly standard this is a good choice. It's a higher level package and will also handle auto renewal (assuming you enable it).
it is possible to do renewals with acme_certificate. You could do something similar with letsencrypt https://docs.ansible.com/ansible/2.5/modules/letsencrypt_module.html . certbot just handles a lot of this for you, specifically for letsencrypt.

Personally I think using certbot to help manage certificates is simpler, but that's up to you. certbot is an application that handles the verification process for with the certificate authority, which is very handy. With acme_certificate you'll essentially be doing that yourself. It also automatically can set up automatic renewals which is very nice.

### item Unetworkengineering-53993
Site: networkengineering | Thread title: PoE losses: Cat5e vs Cat6
The cable category defines the high-frequency parameters of the cable (mostly attenuation and crosstalk). For PoE, the serial resistance of the cable matters which isn't defined by category.
Good plenum cable grew somewhat thicker by custom from Cat-3 over Cat-5 to Cat-6(A), patch cables vary greatly down to 30 AWG.

Essentially, the thicker the cable (lower AWG) the better the PoE performance. The initial IEEE 802.3af-2003 defined a maximum loop resistance between pairs (thx jonathanjo) of 20 Ω, 802.3at-2009 lowered that to 12.5 Ω and the new 802.3bt-2018 to 6.25 Ω. Accordingly, the maximum current increased from 350 mA (af) to 600 mA (at) to 1860 mA (bt 4-pair), enabling the power increase.

The loop resistance limits the maximum power due to the induced voltage drop: at 600 mA current and 6 Ω cable resistance, the voltage drop is (U = R*I) 3.6 V - from the perhaps 48 V you start with at the PSE you've got 44.4 V left at the PD. Multiplied by .6 A, that's 26.6 W with 3.6 * .6 = 2.2 W lost in the cable. (Note that the 25.5 W maximum 802.3at power is worst case.)

### item Usecurity-201289
Site: security | Thread title: How does full disk encryption cater for overprovisoned disk space in flash devices and can this result in data leakage?
If you encrypt the disk from the start, when you first start using it, then this isn't a problem. All data you write is encrypted and remapped sectors just lead to encrypted data being remanent on the over-provisioned area. Since the data is encrypted, you can't do anything with it even if you recover it using direct flash reads on a disassembled SSD.

Furthermore, identifying where that data came from in the encrypted stream is particularly difficult, and since most FDE block cipher modes (e.g. XTS) include the sector number (or some other position value) as part of the initialisation vector it becomes exceedingly difficult to recover plaintext from those remanent sectors even if you are in possession of the FDE master key.
On top of that, most SSDs implement the ATA Secure Erase feature.

This feature allows you to send a single command to safely erase the disk without needing to write over every sector.
Overwriting sectors is costly as flash cells have limited write cycles.
This feature works by transparently encrypting all sectors using a randomly generated key which is stored in the disk controller's nonvolatile memory.
When you run the ATA Secure Erase command, the disk controller discards the old key and generates a new one.

This instantly makes all data on the disk unreadable.
As a side-effect, all over-provisioned areas are also encrypted this way, meaning that even without using your own FDE on the SSD the over-provisioned areas are still encrypted and difficult to recover even if you extract the Secure Erase master key from the controller's nonvolatile memory.
If you later do a Secure Erase command, the overprovisioned areas become unreadable too.

### item Userverfault-271070
Site: serverfault | Thread title: How to open port 555 on Linux / Debian
Since that appears to be an Apache config I suspect you also need to add a Listen directive to the /etc/apache2/ports.conf (for Debian).
It should be Listen 555.

### item Usoftwareengineering-11802
Site: softwareengineering | Thread title: GIT branch model for derivative work
If each brand has independent assets then you can create each customer branch from develop and then pull future changes in as required. Individual assets can be created, edited and committed on the appropriate customer branch.
A nice side-effect of this is that you could have common assets on develop if that makes sense.

Depending on how distributed your development is, you might consider pulling from master rather than rebaseing. You don't want to rebase if commits are being pushed around to other repositories.
To summarise: code changes on develop; asset changes on customer-X; occasionally pull from develop to customer-X. Sorted.

### item Uunix-57232
Site: unix | Thread title: Difference between system calls and library functions
Conceptually, a library function is part of your process.
At run-time, your executable code and the code of any libraries (such as libc.so) it depends on, get linked into a single process. So, when you call a function in such a library, it executes as part of your process, with the same resources and privileges. It's the same idea as calling a function you wrote yourself (with possible exceptions like PLT and/or trampoline functions, which you can look up if you care).

Conceptually, a system call is a special interface used to make a call from your code (which is generally unprivileged) to the kernel (which has the right to escalate privileges as necessary).
For example, see the Linux man brk.
When a C program calls malloc to allocate memory, it is calling a library function in glibc.
If there is already enough space for the allocation inside the process, it can do any necessary heap management and return the memory to the caller.

If not, glibc needs to request more memory from the kernel: it (probably) calls the brk glibc function, which in turn calls the brk syscall. Only once control has passed to the kernel, via the syscall, can the global virtual memory state be modified to reserve more memory, and map it into your process' address space.

### item Udba-87040
Site: dba | Thread title: Rollback on \include error in psql
Finally I've got an answer at pgsql-general mailing list by Adrian Klaver (link)
There is some kind of unexpected behavior with using both --set ON_ERROR_STOP=on and --single-transaction options. The ON_ERROR_STOP stops the processing, but does not rollback current transaction in case of \include error.
So, the solution for my initial problem will be removing the single-transaction option and wrapping explicit BEGIN/COMMIT statements around my main script.

### item Udevops-1626
Site: devops | Thread title: How to provide a user to access only a particular bucket in AWS S3?
Amazon's IAM roles generally grant a role access to a particular ARN (Amazon Resource Name). Amazon notes on their pages that for S3 a resource
...can be a bucket-name or a bucket-name/object-key.
They also provide a helpful example for doing just this which appears as follows:

{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["s3:ListBucket"],
 "Resource": ["arn:aws:s3:::test"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": ["arn:aws:s3:::test/*"]
 }
 ]
}

### item Unetworkengineering-83028
Site: networkengineering | Thread title: Two switches, double connection, no LACP: how does it work?
Most likely, the rapid or the multiple spanning tree protocol RSTP/MSTP has been activated on the 1910 switch.
With the unmanaged 1410 switch forwarding STP BPDUs (most do), the 1910 notices a loop to self and blocks one of the ports to the 1410. Not a really reliable state (as you're currently seeing) but mostly good to go.
if we replace the 1910 with a newer device, and connect the 1410 with one (or two cables, with LACP configured), the LAN becomes unstable/unusable.

That is to be expected. If you replace the 1910 with a switch without STP, a bridge loop forms, causing a broadcast storm to bring down the network. By default, all HPE switches I've seen come with STP turned off.
Trying to configure a LACP LAG on the new switch won't work. Lacking configuration on its 1910 partner, LACP fails and both ports are just switch ports. Again, without proper STP, a loop forms.

Creating a static LAG would work better but due to potential MAC address instabilities that's not a proper operational mode either.
In a nutshell: using anything but simple, single links between switches or more than one VLAN requires both sides to be configured in the same way: STP/RSTP/MSTP or LACP or static LAG.

If you replace any network device make sure you've examined and understood its configuration. That's where a decent documentation including the operational concept comes into play as well.
Since a device can also simply fail at any given time, make sure you've backed up its current config somewhere.

### item Usecurity-99554
Site: security | Thread title: Are case-insensitive passwords a bad idea?
Whether you should be worried or not depends on the sensitivity of what you're protecting. The lock protecting my filing cabinet holding my taxes and medical information doesn't need to be that secure, and I don't worry that the lock is cheaply designed. But I want the locks protecting my money to be extremely secure. It does show that they may not be thinking very clearly about security when designing the system.

Making passwords not case sensitive reduces the number of possibilities dramatically. A 6 non case sensitive character alphabet only password has 2^28 possible passwords,while a 6 character case sensitive password has 2^34 possible passwords. This reduced search space makes an attack on a leaked hash database more feasible.

As Jeff Ferland points out below, having caps lock on doesn't mean the site isn't case sensitive. If I type Password, then hit caps lock, it comes out pASSWORD. The case is merely inverted. If the site is doing this, then the password is still case sensitive, but merely tries the original, and inverted password. This merely halves the search space. That's simply a usability/security tradeoff since people commonly have caps lock on and don't know it, and (at least IMO) a good one.

It's impossible to tell if the service is storing your password in plaintext from this one fact. It's trivial to just change everything to one case before the hashing is done.

### item Userverfault-28868
Site: serverfault | Thread title: How to restore/import an Oracle database from dmp file?
It depends what you are trying to do but one short answer is:
imp system/password@sid file=(filename) log=imp.log fromuser=(existing user) touser=(new user)
The last 3 here: log, fromuser, touser are optional. You might give some more details about what you are doing if that doesn't help...

### item Usoftwareengineering-218823
Site: softwareengineering | Thread title: What does "testing surface" mean in the context of programming?
The testing surface of an object is the collective area that is encompassed by the public properties, methods and constructors of that object (its Application Programming Interface, or API). The term "testing surface" is essentially a proxy term for how much programming effort will be required to unit test an object.
Things that can increase the testing surface of an object:

Objects that have a greater number of public members have a greater testing surface, because there are more end-points to test.
Members that have more complex logic in them have a greater testing surface, because a test is required for each "bifurcation" (e.g. the two sides of an if statement).
Members that have a greater number of parameters in them increase the testing surface, because it increases the number of different combinations of parameter values that the member uses.

Boundary conditions (such as nulls, transition between positive and negative numbers, and off-by-one conditions) increase the testing surface, because a greater number of tests are required to indentify and test those boundary conditions).
Exceptions to normal control flow (such as thrown exceptions) increase the testing surface, because you need tests to insure that those exceptions are accounted for, and that they are working properly under the right conditions.

Things that can decrease the testing surface of an object:
Good design practices.
A simpler API design
The practice of TDD (Test-Driven Design), which makes your code more testable in the first place, and decreases the need for exotic tests.
Design by Contract, if the programming language supports it directly, reduces the testing surface, because it already accounts for incorrect input or contract violations (assuming that the contract conditions are correctly specified).