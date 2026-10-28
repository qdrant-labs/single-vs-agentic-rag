### item Uunix-38162
Site: unix | Thread title: How can I force unzip / zip not to create a subdirectory when I extract it?
Use a FUSE filesystem that allows you to browse archives like directories, such as AVFS. Use cp to extract the files to the directory of your choice.
mountavfs
cp -Rp ~/.avfs/tmp/omeka-1.5.1.zip\#/omeka-1.5.1 omeka
Since we're assuming that there is a single toplevel directory in the archive, you can shorten this to
cp -Rp ~/.avfs/tmp/omeka-1.5.1.zip\#/* omeka

### item Udba-31838
Site: dba | Thread title: How to disable ldf file or limit its size
You cannot disable/remove the LDF file. It has to exist, as it stores database transactions.
What you can do is:
Set the database recovery model to Simple
This should keep your LDF file from growing, and is set via the Options page of the Database Properties dialog.
For additional reducing, which I don't think is necessary, you can:
2 Set Auto Shrink to True
This is also done from the Options page of the Database Properties dialog:
3 Turn auto-grow off

This is done from the Files page of the Database Properties dialog:
Be aware that when a database is in the Simple recovery model, you will not be able to recover to a point in time
Or
Set the database recovery model to Full (I guess it's already set this way)
Create a full database backup
Start creating transaction log backups regularly. It's best to schedule a SQL Server job to do this

The latter scenario provides better disaster recovery as it enables recovery to a point in time
It's up to you to decide how much data you can afford to lose

### item Udevops-11010
Site: devops | Thread title: Custom inventory file failing to parse properly
The keyword hosts is missing. Also colons : are needed after the hostnames. Fix the syntax, for example
all:
 children:
 control:
 hosts:
 moriarty.server.com:
 toby.server.com:
 managed:
 hosts:
 sherlock.server.com:
See How to build your inventory.

### item Unetworkengineering-55017
Site: networkengineering | Thread title: What's the difference between Serial DCE and Serial DTE link?
One side of the link (DCE), has to transmit the clock signal, which controls the data rate, and the other side (DTE) receives the clock signal.
R1 is DCE here:
interface Serial0/0/0
 ip address 10.0.0.1 255.255.255.252
 clock rate 2000000
R2 is DTE here:
interface Serial0/0/0
 ip address 10.0.0.2 255.255.255.252
The difference between the two cables in packet tracer is just which side you click first:

With the DCE cable, (red zigzag with clock) the side you click first will be the DCE, the second will be DTE
With the DTE cable (red zigzag no clock) the side you click first will be DTE, the second will be DCE
Whichever way you do it, you'll see one side of the cable shows the clock symbol: this is the DCE.

### item Usecurity-76945
Site: security | Thread title: How to fake a browser fingerprint?
I just found a open-source extension for firefox RAS since it's open source you can dig into the code and port it to any platform should you want... I've tested this plugin for a time for Firefox and as long you don't spoof mobile browsers on pc, and pc browsers on phones you should be OK.
No problems so far, except when the extension randomly choose to spoof a old browser version but you could just exclude the old browsers versions and only spoof the current version.
This extension can:

Disable Authorization header
Send Spoofed If-None-Match headers
Send Spoofed X-Forwarded-For header
Send Spoofed Via headers
Spoof Referer header
Spoof Accepted Documents
Spoof Accepted Encodings
Spoof Accepted Language
Time zone spoofing (UTC)
Screen size spoofing
Use standard font set

And much more, and i won't tell the details here you can see their documentation Here. Setting plugins to "click to play" by default is also a good idea, but let javascript allowed by default to not break thousand of pages.

### item Userverfault-546342
Site: serverfault | Thread title: Crontab maximum command length
Wow, I found what my problem is and it had nothing to do with line length.
It turns out that my command had a % (percent sign) in it, which has a special meaning in crontab. It is used to input text to STDIN (see Why is my crontab not working, and how can I troubleshoot it?).
So I had to escape it. My command which was:
gzip -c /path/to/a/file > /backup/dir/file-$(date +%F_%T).gz
becomes
gzip -c /path/to/a/file > /backup/dir/file-$(date +\%F_\%T).gz

### item Usoftwareengineering-73342
Site: softwareengineering | Thread title: Is there a defined way to create a commit history for Git
The way you are doing the import is by setting up a git repo anywhere you want on the workstation where you have access to the sources, and point GIT_WORK_TREE to where you can load the successive version of your code base.
From there, you can git add and git commit the different versions of your code base, updating GIT_WORK_TREE to point to the right versions.

Use GIT_AUTHOR_DATE and GIT_AUTHOR_NAME for each import in order to set the right author's name and date. (See Environment Variables in Git)

### item Uunix-89348
Site: unix | Thread title: How to permanently disable the Insert key on Linux?
First, find the keysym which corresponds to Insert
$ xmodmap -pke | grep -i insert
This is probably key 118. To disable it globally run
$ xmodmap -e "keycode 118 ="
which causes that key to map to nothing at all.
Running this command every time your Xserver starts is very dependent upon which distribution and session manager you are using.

### item Udba-142987
Site: dba | Thread title: Access SQL Server Express LocalDB from Local Area Network
LocalDB cannot be accessed remotely, it's by design and documented.
Here is a description of LocalDB.
Here is a list of LocalDB features and limitations.
I don't see how installing SQL Server can be a problem. 120 MB is not that big nowadays even for small applications. You can embed the setup in your application and ship SQL Express with your setup kit. If you need a SQL Server Edition with a small footprint, consider using SQL Server Compact Edition.

### item Udevops-3763
Site: devops | Thread title: Ansible Playbook Localhost Invocation Working Directory
You can use env lookup plugins. Plugins are always evaluated in the context of "parent" ansible process on the control host.
- debug:
 msg: "{{ lookup('env', 'PWD') }}"
More lookup plugins can be found here: http://docs.ansible.com/ansible/latest/user_guide/playbooks_lookups.html

### item Unetworkengineering-5388
Site: networkengineering | Thread title: Auto-QOS configuration for Cisco network
For Cisco IP phones, you've definitely got the right configuration:
!
mls qos
!
interface UPLINK
 ! Unconditionally trust all QoS markings
 auto qos voip trust
!
interface ACCESS
 ! Look for the Cisco Phone's CDP frames, and trust VoIP from the phone...
 auto qos voip cisco-phone
Should I put "auto qos voip trust" on network uplinks for both directions on traffic?

Yes, auto qos voip trust is required on both sides of any uplink for end-to-end QoS functionality (which is what you'd want, of course).
Will there be downtime to be aware of?
There is no downtime associated with QoS settings. I have enabled qos (platform-wide, and on individual links) with no observable impact; even on links that were heavily utilized, there was no perceivable downtime for transit traffic.
For more info, you can reference Cisco's Auto QoS Whitepaper

### item Usecurity-90385
Site: security | Thread title: Obsolete cryptography (SHA1) warning although certificate uses SHA256
The error message is just misleading
You said yourself:
I know that AES_256_CBC isn't considered modern cryptography, so the warning about obsolete cryptography would still appear.
And that is why you get that message.
Now unfortunately the message itself is not very clearly phrased.
SHA-1 is used in several circumstances. And here the "SHA-1" refers to HMAC message authentication and not to its use inside certificates.
From the Chromium TLS page (Archived here.):
Message Authentication

You may see:
“The connection is using [cipher] with SHA1 for message authentication.”
This actually means that the connection is using HMAC-SHA1 for data integrity, rather than as a certificate signing algorithm (e.g. sha1WithRSAEncryption). The HMAC construction is strong enough that it is not broken when used with SHA1 (or even MD5) as the hash function, so this is not currently deprecated.
What to do

Enable and have the server prefer a cipher suite that Chrome likes better. Namely: Something with forward secrecy and either AES-GCM or CHACHA20_POLY1305. (The TLS page recommends TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256.)
Since that is already in your list, all you have to do is change the server's preference for it.

### item Userverfault-178216
Site: serverfault | Thread title: Best way to share a folder between KVM host and guest
You could do this by treating host and guest as completely separate computers. Make the shared folder available on the host, e.g. by exporting it through NFS or by creating a samba share. Then connect to it from the guest just in the normal manner.

Since the guest has its own IP address, this should not present any problems. With NFS you can also easily limit the exported share to only accept connections from the guest (if that is what you want). All the other rules about NFS shares and samba shares still apply.
If either guest or host are Windows machines, then you are probably better of with a samba share.

### item Usoftwareengineering-39499
Site: softwareengineering | Thread title: What should be first - functionality or design?
Functionality
Design can come later, core functionality is key to a deliverable product.
Disregarding design, the key is to get a deliverable functioning product out the door sooner rather then later. Design is a secondary objective. If you can't make it work, then all the flowers and pretty colors won't save you. Having a working product, with minimal design work will.

Perfectly adhering to a pattern or OOP principals are great, but often you will find that for the sake of producing something that works they will have to be ignored in some cases.

### item Uunix-50508
Site: unix | Thread title: Reusing ssh session for repeated rsync commands
Yes, see the ControlMaster and ControlPath options.
You can start the master connection with:
mkdir ~/.ssh/ctl
ssh -nNf -o ControlMaster=yes -o ControlPath="$HOME/.ssh/ctl/%L-%r@%h:%p" user@host
And then use rsync with:
rsync -e "ssh -o 'ControlPath=$HOME/.ssh/ctl/%L-%r@%h:%p'" ...
Then
ssh -O exit -o ControlPath="$HOME/.ssh/ctl/%L-%r@%h:%p" user@host
to terminate the master connection.

(And by the way, some versions of ubuntu have an annoying feature in that they rebuild /etc/motd upon every login (including non-interactive ssh sessions), which can take a long time if part of that involves checking if updates are available for instance. IIRC, you can disable it by removing pam_motd from your pam configuration)

### item Udba-100779
Site: dba | Thread title: How to atomically replace table data in PostgreSQL
Right, the TRUNCATE TABLE command you are performing "... acquires an ACCESS EXCLUSIVE lock on each table it operates on", so in the first SQL block you posted, any other clients attempting to access the table after that time will be blocked until your INSERT finishes and you COMMIT.
You can use the same workaround as in your MySQL-specific code; Postgres supports roughly the same syntax and will have similar locking behavior. To wit:

BEGIN;
-- You probably want to make sure that no one else is
-- INSERT / UPDATE / DELETE'ing from the original table, otherwise
-- those changes may be lost during this switchover process. One way
-- to do that would be via:
-- LOCK TABLE "table" IN SHARE ROW EXCLUSIVE mode;
CREATE TABLE "table_new" (LIKE "table");
INSERT INTO "table_new" ...;

-- The ALTER TABLE ... RENAME TO command takes an Access Exclusive lock on "table",
-- but these final few statements should be fast.
ALTER TABLE "table" RENAME TO "table_old";
ALTER TABLE "table_new" RENAME TO "table";
DROP TABLE "table_old";
COMMIT;
Extra bonus: Postgres actually supports transactional DDL, unlike MySQL, so in case you need to ROLLBACK the above transaction, you may safely do so.

### item Udevops-4847
Site: devops | Thread title: What is ansible-runner about?
This project is to support automation of running ansible playbooks. There is a GUI based project called Ansible Tower or AWX to do that, but ansible-runner seems to be the underlying layer of the automation in essence replacing ansible-playbook command.
There are some really serious issues for automation when trying to use ansible-playbook as part of some scripts.
The output of ansible-playbook is the most awful thing under the sun when it comes to parsing.

So you have to start with writing your own output plugin and then write a parser for that, then you need to figure out how to manage the environment variables and passwords and many other things.
So ansible-runner is the answer to this.
It would preserve the artifacts from running a task or playbook and make encapsulation of ansible in further automation possible.

You can run it from shell, you can run it as python module and there is even a reference container for it and obviously it is used by AWX. Further the project's event emitter will hopefully be much better pluggable to monitoring systems like ELK and to Message Bus type systems.

### item Unetworkengineering-14713
Site: networkengineering | Thread title: After upgrading ASA, client VPN failing from site with active LAN to LAN tunnel
Yes, the device can be instructed to accept the client VPN connections from the peer that it already has an open tunnel with.
This is done by updating the dynamic map to include new entries with a configured peer address.
So, with this existing configuration accepting a dynamic connection from any address:

crypto map vpnmap 10 match address peer_acl
crypto map vpnmap 10 set peer 192.0.2.15
crypto map vpnmap 10 set ikev1 transform-set ESP-AES-SHA1
crypto map vpnmap 65500 ipsec-isakmp dynamic OUTSIDE_DYN_MAP
crypto dynamic-map OUTSIDE_DYN_MAP 100 set ikev1 transform-set ESP-3DES-SHA
crypto dynamic-map OUTSIDE_DYN_MAP 100 set security-association lifetime seconds 86400
crypto dynamic-map OUTSIDE_DYN_MAP 100 set reverse-route

..the dynamic map can be edited to allow client VPN connections from the 192.0.2.15 peer:

crypto map vpnmap 10 match address peer_acl
crypto map vpnmap 10 set peer 192.0.2.15
crypto map vpnmap 10 set ikev1 transform-set ESP-AES-SHA1
crypto map vpnmap 65500 ipsec-isakmp dynamic OUTSIDE_DYN_MAP
crypto dynamic-map OUTSIDE_DYN_MAP 10 set ikev1 transform-set ESP-3DES-SHA
crypto dynamic-map OUTSIDE_DYN_MAP 10 set security-association lifetime seconds 86400
crypto dynamic-map OUTSIDE_DYN_MAP 10 set reverse-route
crypto dynamic-map OUTSIDE_DYN_MAP 10 set peer 192.0.2.15
crypto dynamic-map

OUTSIDE_DYN_MAP 100 set ikev1 transform-set ESP-3DES-SHA
crypto dynamic-map OUTSIDE_DYN_MAP 100 set security-association lifetime seconds 86400
crypto dynamic-map OUTSIDE_DYN_MAP 100 set reverse-route
..and client IPsec connections will now be allowed from 192.0.2.15 despite having an active LAN to LAN tunnel.

### item Usecurity-237131
Site: security | Thread title: How Are Google Chrome Synced Passwords Encrypted If I Can Reset the Password to My Account
I think the text is incorrect. According to the support article (on the upcoming "on-device encryption"), passwords are currently encrypted with a key that Google has access to:
How standard password encryption works
Today, your saved passwords are encrypted while they’re sent over any network and when they’re saved to Google. The encryption key, used to access your passwords, is safely stored in your Google Account. Google then uses this key to access (decrypt) your passwords when:

You access them on passwords.google.com, on your eligible devices, or in Chrome settings.
Your passwords get checked for security issues in the Password Checkup.

The article goes on to describe "on-device encryption". The description is incredibly unclear, but it sounds like "on-device encryption" might handle password resets by having you enter your new password on an existing device so it can re-encrypt the passwords under the new key (or equivalent). It's still not that secure (Google has access to your password every time you enter it), but it may make it harder for mass compromise via e.g. a court order from an unfriendly government.

So why does it say "Google username and password"?
It looks like the progression was
~2014: "Encrypt synced passwords with your Google credentials"
(slightly misleading, since your username/password are not actually used)
~2017: "Encrypt synced passwords with your Google username and password"
(the support article changes between May and July)
Current (2022): "Encrypt synced passwords with your Google Account"

(Unclear when this happens; the text of the "credentials/username and password/Account" option was removed from the support article in Oct-Dec 2017).
My guess? Someone thought "credentials" was unclear and changed it to "username and password" (making it even more misleading!), and then someone else noticed and changed it to "Google Account".

### item Userverfault-39537
Site: serverfault | Thread title: How to stop Outlook 2007 asking for credentials when using RPC over HTTPS
This blog entry provides a solution:
Get Outlook 2003 RPC Over HTTP To Remember Your Password
On your client, you need to go into
 your Mail settings, then check your
 Exchange Proxy Settings.
Ensure that Connect using SSL only and Mutually authenticate the session
 when connecting with SSL are both
 checked on.
Enter in the Principal name for proxy server: in the
 msstd:frontend.domain.com format.
Select both the Fast and Slow settings.

Make sure the Proxy authentication settings is set to NTLM
 Authentication.
Now the real trick. Outlook will, when
 you select Remember my Password, store
 your password for the Back-end Mailbox
 server. But it does not save your
 password for the Front-end Proxy
 server.
Go into your Control Panel > User Accounts > Advanced > Manage
 Passwords.

Click Add, then type out the name of your Front-end server. This should be
 the same name as your SSL certificate
 on the default web site that contains
 the RPC virtual directory, put in your
 username and password.
It's for Outlook 2003, but I guess it should work for Outlook 2007 too.