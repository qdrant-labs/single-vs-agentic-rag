### item Punix-549-479
THREAD A
Site: unix | Thread title: tmux vs. GNU Screen
[chunk 280498] From their website:
How is tmux different from GNU screen? What else does it offer?
tmux offers several advantages over screen:
a clearly-defined client-server model: windows are independent entities which
 may be attached simultaneously to multiple sessions and viewed from multiple
 clients (terminals), as well as moved freely between sessions within the same
 tmux server;

[chunk 280499] a consistent, well-documented command interface, with the same syntax
 whether used interactively, as a key binding, or from the shell;
easily scriptable from the shell;
multiple paste buffers;
choice of vi or emacs key layouts;
an option to limit the window size;
a more usable status line syntax, with the ability to display the first line
 of output of a specific command;
a cleaner, modern, easily extended, BSD-licensed codebase.
There are still a few features screen includes that tmux omits:

[chunk 280500] builtin serial and telnet support; this is bloat and is unlikely to be added
 to tmux;
wider platform support, for example IRIX and HP-UX, and for odd terminals.

THREAD B
Site: unix | Thread title: Keep processes running after SSH session disconnects
[chunk 280362] Use nohup to make your process ignore the hangup signal:
$ nohup long-running-process &
$ exit
To monitor progress, check nohup's output:
$ tail -f nohup.out

### item Punix-412900-408617
THREAD A
Site: unix | Thread title: reset the color of the output after my command in bash shell
[chunk 427871] The DEBUG trap runs before each command, so you can abuse it to reset the colors, if you have colored the command line input. ("abuse" since this isn't debugging.)
With this:
$ promptcol="$(tput sgr0)$(tput setaf 3)"
$ cmdcol="$(tput sgr0)$(tput bold)"
$ normalcol="$(tput sgr0)"
$ trap 'echo -n "$normalcol"' DEBUG
$ PS1="\[$promptcol\]\w\$ \[$cmdcol\]"
I get this:

[chunk 427872] Note that you need the \[...\] surrounding the color codes, so that the shell knows how to calculate the width of the prompt properly. Also, note that you can't put the \[...\] within the variables, the shell handles the prompt escapes first, and variable expansions only after that.

THREAD B
Site: unix | Thread title: BASH - customizing PS1 to run a command
[chunk 426601] I'm not sure if this has changed between versions(*), but my man page for Bash says that
Bash allows these prompt strings to be customized by inserting a number of backslash-escaped special characters that are decoded as follows:
(list contains \e, \[, \] etc.)
After the string is decoded, it is expanded via parameter expansion, command substitution, ...
Which means that the \[..\] can't come from the command substitution, but must be there before that.

[chunk 426602] (It also means you could use \u or \w as arguments to a command substitution, and they'd get replaced before the command runs. And I have no idea what putting \[..\] inside a command substitution would do... This would make more sense the other way around.)
So, we'll have to put the color codes in separate expansions and protect them with \[..\] by hand. I'll use variables instead of command substitution, and also the $'...' expansion to get the ESC character:

[chunk 426603] prompt_smile() {
 if [ "$?" = 0 ] ; then
 smile=' :) '
 smilecolor=$'\e[1;32m'
 else
 smile=' :( '
 smilecolor=$'\e[1;31m'
 fi
 normalcolor=$'\e[0m'
}
PROMPT_COMMAND=prompt_smile
PS1='\u@\h \W \$ \[$smilecolor\]$smile\[$normalcolor\]\n'
(* the reason I wonder about that, is that the answers to the older and similar but no so duplicate question seem to output the \[..\] from within an expansion)

### item Punix-60458-3052
THREAD A
Site: unix | Thread title: Awesome: Incorrect timezone
[chunk 309467] Your problem is that you are not defining the environment variable TZ in the right file. ~/.bashrc is the configuration file for interactive shells. It's the place for aliases, key bindings and other things that you want to have in interactive shell. While you can define an environment variable there, this variable will only be set in the programs that are started from an interactive shell. This excluded your window manager and any program started by the window manager.

[chunk 309468] So instead define environment variables in the proper place. For non-graphical logins, the proper place is ~/.profile. When you log in in graphical mode, the proper place depends on your distribution, your display manager and your session or window manager. On Ubuntu, I believe that all display managers are set up to read ~/.profile as well. So define environment variables in ~/.profile.
This topic has come up many times — see Is there a ".bashrc" equivalent file read by all shells?

[chunk 309469] In your situation, an alternative possibility is to define the environment variable in your Awesome configuration file (os.setenv('TZ', 'America/Los_Angeles')). Awesome would be the right place to act if you want to change the timezone without logging out and back in (if you're travelling with your laptop).

THREAD B
Site: unix | Thread title: Is there a ".bashrc" equivalent file read by all shells?
[chunk 282004] The file $HOME/.profile is used by a number of shells, including bash, sh, dash, and possibly others.
From the bash man page:
When bash is invoked as an interactive login shell, ... it first reads and executes commands from the file /etc/profile, if that file exists. After reading that file, it looks for ~/.bash_profile, ~/.bash_login, and ~/.profile, in that order, and reads and executes commands from the first one that exists and is readable.

[chunk 282005] csh and tcsh explicitly don't look at ~/.profile but those shells are kinda antiquated.

### item Psecurity-698-75
THREAD A
Site: security | Thread title: What are the biggest unsolved problems in IT Security?
[chunk 844336] You can't really solve the end user problem. Well, legally or ethically anyway. My vote goes toward the Home Realm Discovery problem.
EDIT:
The end user problem was in reference to previously posted answers.
Home Realm discovery is part of a claims based authentication model, where you can select between multiple services/organizations to provide an identity for a user, much like OpenID/OpenAuth.

[chunk 844337] The problem arises when you need to figure out which provider to get info from since you don't know anything about the user yet.
It's a Chicken/egg thing: how do you figure out who to have authenticate the user when you don't know who the user uses to provide their identity.
The first obvious answer is to use only one provider, but that sort of negates the benefit of the model.

[chunk 844338] The second obvious answer is to ask the user. However, this is openID's downfall. Most people have no idea who their provider is. And what happens when you can authenticate against Google and Facebook, but you don't know which one is tied to the profile of the calling application?

[chunk 844339] This is affectionately referred to as the NASCAR problem with OpenID -- the launching page for OpenID usually has a bajillion logos for providers, so you need to select which provider to use. Which breaks when you have a custom provider.
Remember CardSpace/InfoCard/Information Cards? That attempts to solve the problem. It actually does a pretty good job theoretically. Practically notsomuch.

THREAD B
Site: security | Thread title: What are the best practices for mitigating zero day attacks?
[chunk 843829] Holistic SDL.
By definition, you can't defend against a specific attack that you don't know about beforehand.
However, if you implemented a complete, Secure Development Lifecycle through all the phases, including appropriate Threat Modeling, and you mitigate the threats (not the attacks) - then you should be relatively okay.

### item Psecurity-33824-26647
THREAD A
Site: security | Thread title: SSL Cert Types and Key Usage
[chunk 866570] nsCertType is an old Netscape-specific extension, which was used by the Netscape browser at a time when that browser was still alive. You can forget it nowadays.
The signing CA, by principle, acts in any way as it sees fit.
It can put whatever it wishes in your certificate.
Your certificate request is just a suggestion.

[chunk 866571] You can more or less count on the CA to take the public key from your request and use that public key in the certificate; for everything less (including name, key usages and other extensions) this is completely up to the CA to decide.
Microsoft's Certificate Services uses "certificate templates" for its configuration, and the templates decide what goes in the certificates.

[chunk 866572] According to my own tests, the key usage and extended key usages which you put in the certificate will be completely ignored.
What extensions are needed for client authentication, and/or for server authentication, depends on the involved software. You will find some information in my past prose, e.g. this, this and that.

THREAD B
Site: security | Thread title: Extensions for SSL server certificate
[chunk 863129] No extension is strictly necessary in the SSL server certificate, but some extensions can only help:
An Authority Key Identifier extension will help clients link the certificate with the issuing CA.
A CRL Distribution Points extension (non critical) should be used to point to the URL where the CRL should be found.

[chunk 863130] An Authority Information Access extension can be used to include a pointer (URL) to the certificate for the issuing CA itself; the same extension can point to an OCSP responder, if applicable.

[chunk 863131] If a Key Usage extension is used, it should include some flags: keyAgreement and keyEncipherment for RSA keys to use with TLS_RSA_* cipher suites, digitalSignature for RSA and DSA keys to use with the TLS_DHE_* cipher suites (there is some confusion about whether keyAgreement or keyEncipherment should be used in the case of RSA-based key exchange, so it is safest to include both flags).

[chunk 863132] If you have a formally defined certificate policy, have a pointer to it (OID + download URL) included in all certificates in the path, or at least the SSL server certificate itself: it will give you some legal protection, should disputes arise.

[chunk 863133] The Subject Alt Name extension should be used to indicate the SSL server name. In the absence of such an extension, all browsers will fallback to the CN component of the subjectDN, but this extension is still nominally "preferred" (see RFC 2818 for details).
Of course, all these extensions are supposed to be enforced by the issuing CA, so if you already have the CA, there should be no extra question here.

[chunk 863134] If in doubt, consult the Internet X.509 PKI Profile. The profile defines what you should morally follow. If you fully conform to it, your certificates will work everywhere. Browsers are actually much more lenient than that.

### item Pserverfault-320125-8860
THREAD A
Site: serverfault | Thread title: Moving MySQL users from one db server to another?
[chunk 102579] Dump the mysql.user table (and optionally the mysql.db table) then replace any specific references to the name of the old host with the name of the new host. Import into the new host database and flush the privileges.
That's not hard is it?

THREAD B
Site: serverfault | Thread title: How can I export the privileges from MySQL and then import to a new server?
[chunk 4362] Do not mess with the mysql db. There is a lot more going on there than just the users table. Your best bet is the "SHOW GRANTS FOR" command. I have a lot of CLI maintenance aliases and functions in my .bashrc (actually my .bash_aliases that I source in my .bashrc). This function:

[chunk 4363] mygrants()
{
 mysql -B -N $@ -e "SELECT DISTINCT CONCAT(
 'SHOW GRANTS FOR \'', user, '\'@\'', host, '\';'
 ) AS query FROM mysql.user" | \
 mysql $@ | \
 sed 's/\(GRANT .*\)/\1;/;s/^\(Grants for .*\)/## \1 ##/;/##/{x;p;x;}'
}
The first mysql command uses SQL to generate valid SQL which is piped to the second mysql command. The output is then piped through sed to add pretty comments.
The $@ in the command will allow you to call it as:
mygrants --host=prod-db1 --user=admin --password=secret

[chunk 4364] You can use your full unix tool kit on this like so:
mygrants --host=prod-db1 --user=admin --password=secret | grep rails_admin | mysql --host=staging-db1 --user=admin --password=secret
That is THE right way to move users. Your MySQL ACL is modified with pure SQL.

### item Pdba-7301-4162
THREAD A
Site: dba | Thread title: How to make conditional ordering for two or more columns
[chunk 716440] I'll admit I've never had to do this before so there was a bit of head scratching involved. Simple example table to demonstrate:
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[MyTable]') AND type in (N'U'))
 DROP TABLE [dbo].[MyTable]
GO
CREATE TABLE dbo.MyTable
(
 col1 INT
 , col2 CHAR(1)
)
GO

[chunk 716441] INSERT dbo.MyTable (col1, col2) VALUES (1, 'A')
INSERT dbo.MyTable (col1, col2) VALUES (1, 'B')
INSERT dbo.MyTable (col1, col2) VALUES (1, 'C')
INSERT dbo.MyTable (col1, col2) VALUES (2, 'A')
INSERT dbo.MyTable (col1, col2) VALUES (2, 'B')
INSERT dbo.MyTable (col1, col2) VALUES (2, 'C')
INSERT dbo.MyTable (col1, col2) VALUES (3, 'A')
INSERT dbo.MyTable (col1, col2) VALUES (3, 'B')
INSERT dbo.MyTable (col1, col2) VALUES (3, 'C')

[chunk 716442] Using an @SortStyle parameter to differentiate between sort orders, @SortStyle =1 will sort by col1 ASC, col2 DESC and @SortStyle=2 sort by col2 DESC, col1 ASC.
DECLARE @SortStyle INT
SET @SortStyle = 1
SELECT
 col1
 , col2
FROM
 dbo.MyTable
ORDER BY
 CASE
 WHEN @SortStyle = 1 THEN col1
 END ASC,
 CASE
 WHEN @SortStyle = 1 THEN col2
 END DESC,
 CASE
 WHEN @SortStyle = 2 THEN col2
 END DESC,
 CASE
 WHEN @SortStyle = 2 THEN col1
 END ASC
SET @SortStyle = 2

[chunk 716443] SELECT
 col1
 , col2
FROM
 dbo.MyTable
ORDER BY
 CASE
 WHEN @SortStyle = 1 THEN col1
 END ASC,
 CASE
 WHEN @SortStyle = 1 THEN col2
 END DESC,
 CASE
 WHEN @SortStyle = 2 THEN col2
 END DESC,
 CASE
 WHEN @SortStyle = 2 THEN col1
 END ASC
How do you ORDER BY a parameter covers the simpler case of sorting by just 1 column.

THREAD B
Site: dba | Thread title: 'Conversion failed' error with ORDER BY CASE expression
[chunk 714610] Your CASE expression can only have one datatype. But yours is mixing datatypes and the highest one is being used (as per datatype precedence). So nvarchar is changed to int based on these rules.
You need a case per datatype or per column
Example:

[chunk 714611] CASE WHEN @OrderDirection = 'DESC' THEN
 CASE 
 WHEN @OrderBy = 'JobNumber' THEN J.JobNumber
 WHEN @OrderBy = 'CustID' THEN J.CustID
 WHEN @OrderBy = 'DateIn' THEN J.DateIn
 WHEN @OrderBy = 'DateDue' THEN J.DateDue
 WHEN @OrderBy = 'DateOut' THEN J.DateOut
 WHEN @OrderBy = 'Status' THEN J.MasterJobStatusID 
 ELSE NULL
 END
 END DESC,
CASE WHEN @OrderDirection = 'DESC' THEN
 CASE 
 WHEN @OrderBy = 'OrderNumber' THEN J.OrderNumber
 ELSE NULL
 END
 END DESC

### item Pserverfault-307411-9256
THREAD A
Site: serverfault | Thread title: Monitor traffic by source/destination IP address
[chunk 98733] Netflow is the end all, be all for this type of monitoring.
While there are netflow tools for Windows, my favorite toolset is nfdump+nfsen on Linux/Unix for collection and web-based report generation respectively.
I have found this toolset does everything I want, and they're free.
As for collecting flows for later analysis with one of these tools, your router may support netflow export.

[chunk 98734] If it doesn't, or if you don't have access to the router, you may configure your managed switch (if you have one) to mirror the ports you want to monitor to a dedicated monitoring port.
Then you can use something like fprobe (also on Linux.) I recommend the pcap based fprobe over the ulog one because it was the easiest for me to get working.

THREAD B
Site: serverfault | Thread title: Netflow Collector for Windows Free
[chunk 4570] ntop can act as a NetFlow collector and is available for Win32. You will have to recompile it by yourself though, or find pre-made builds (shouldn't be too hard, it's GPLv3 open source) since the provided build is limited to capturing 1000 packets per session.

### item Psoftwareengineering-193923-174971
THREAD A
Site: softwareengineering | Thread title: Approaches to reduce cyclomatic complexity
[chunk 598954] The first sample is just wrong.
Not wrong in terms of the result, but the style is terrible.
It is repetitive and error prone.
The second sample is actually the step to do to obtain the readable, well written code.
It's not a hack.
It's just badly written code rewritten correctly.

[chunk 598955] The fact that it reduces cyclomatic complexity doesn't surprise me, since there are less operations (at least in source; I'm pretty sure every decent compiler/interpreter will rewrite the first sample into the second one in all cases).

[chunk 598956] The third sample is more complicated to read for beginners who don't have enough practice with arrays, with filtering, with closures, etc. Personally, given the second sample, I would avoid the third one. Still, reduction in cyclomatic complexity is not surprising neither: you are migrating the complexity from your code to the filter method.

THREAD B
Site: softwareengineering | Thread title: Dealing with curly brace soup
[chunk 590855] Put your starting curly brace in the same "rank" as your ending one, like this:
namespace ... 
{
 class ... 
 {
 function ... 
 {
 for ... 
 {
 using ... 
 {
 if ... 
 {
 ...
 }
 if ... 
 {
 ...
 }
 }
 }
 // It's the `function` level!
 }
 }
}

### item Psoftwareengineering-388615-261552
THREAD A
Site: softwareengineering | Thread title: Proper HTTP method for triggering a process
[chunk 683082] What would be a good method of triggering this process to happen in Service B?
First point: if A and B are both under your control, it may not matter very much which method you use, because whether or not your semantics are aligned with the HTTP protocol, both ends are using the same semantics.
But supposing you had to do it "right", because reasons....
RFC 7231 briefly outlines common properties of HTTP methods.

[chunk 683083] Safe is an important one, because it implies that the request can be sent speculatively. For example, a generic client can proactively submit GET requests for links that it sees. Spiders can crawl them. Caches can pre-fetch.
If that's not satisfactory in your domain application protocol, (perhaps because the server is going to react to the request by doing something expensive), then GET and HEAD are not appropriate choices.

[chunk 683084] A thing to keep in mind - if you are trying to use GET/HEAD to propagate a signal, you had best be sure that the metadata in the response does not encourage caching - a cache might short circuit the round trip to your subscriber and return a previously cached response.

[chunk 683085] Idempotent is important on unreliable networks - if two copies of the request are equivalent to a single copy, then idempotent semantics allow generic components to autonomously resend unacknowledged requests. Effectively, you are advertising that at least once delivery strategies can be used.
PUT is unsafe, but idempotent. If you cannot comfortably handle multiple copies of the "same" message, then cross PUT off of the list.

[chunk 683086] POST is neither safe nor idempotent -- the semantics of POST are so broad that they encompass every other use case. This produces the opposite problem: because the semantics are so broad, generic components cannot contribute anything useful to improve the experience.

THREAD B
Site: softwareengineering | Thread title: Which HTTP verb should I use to trigger an action in a REST web service?
[chunk 625290] I don't think there is a proper verb for this action because this transaction isn't really "RESTful." The "s" and "t" stand for "state transfer" and nothing is being transferred here. Or, put another way, by the strictest definition, the verbs like PUT and POST are always used with a noun and "reload" just has the verb.

[chunk 625291] This reload may not be RESTful, but it may still be useful and you'll just have pick a way to do it and live with or explain that it's unusual. GET is probably the simplest. There's a fair amount of skepticism in the comments, though, so you should think about whether or not this reload action is required because something else isn't quite doing what it should be doing.

### item Pserverfault-542230-129953
THREAD A
Site: serverfault | Thread title: Does having too many files on a filesystem significantly impact io performance?
[chunk 162605] Since ext3 the handling of files in the file system is at least as fast as finding an indexed row in a database. This is called the HTree (actually, many indexes in databases still use a BTree.)
http://en.wikipedia.org/wiki/HTree
Older systems would start having problems at 1,000 files because the search was linear (start from the first file, and go through the entire directory to find the file you were interested in.)
Why using a database then?
PRO

[chunk 162606] Then you only need to transport the database from one computer to another (think of a cloud system...), especially if you want to use automatic replication between computers.
CON

[chunk 162607] All the database you send to the database goes through the network! This means a huge bottleneck. If you do not foresee using the replication feature of your database, then that's enough (for me) to avoid using the database. This will have a HUGE impact on your system. Use the file system directly, since anyway the database will be doing the same thing: save the data to a file!
P.S. Your admin seems to be from the past...

[chunk 162608] P.P.S. "ext3 HTree indexes are available in ext3 when the dir_index feature is enabled." -- I use ext4 so I don't worry too much about that, although it can be turned off in ext4; hopefully it is turned ON on your server...

THREAD B
Site: serverfault | Thread title: Maximum number of files in one ext3 directory while still getting acceptable performance?
[chunk 47021] Provided you have a distro that supports the dir_index capability then you can easily have 200,000 files in a single directory. I'd keep it at about 25,000 though, just to be safe. Without dir_index, try to keep it at 5,000.

### item Pdba-16737-14259
THREAD A
Site: dba | Thread title: MySQL Server is Restarting automatically after some minutes
[chunk 721783] I suspect your max_allowed_packet and the presence of a large TEXT/BLOB field.
I answered two questions in the past that involved mysql crashing because of the max_allowed_packet being too small.
MySQL server has gone away obstructing import of large dumps
InnoDB table SELECT returns ERROR 2006 (HY000): MySQL server has gone away (after power outage)
I recommend raising your max_allowed_packet to the max value, which is 1GB

[chunk 721784] If you have TEXT/BLOB fields, you may have entered a TEXT/BLOB field that is too big to pass through a MySQL Packet or through the InnoDB Log Files. You may need to resize your innodb log files to the max value, which is 2047M. Here is what to do:
STEP 01) Add this to /etc/my.cnf
[mysqld]
max_allowed_packet=1G
innodb_log_file_size=2047M
NOTE: In Google Cloud, you can't enter 1G, you must use the value 1073741824
STEP 02) service mysql stop
STEP 03) rm -f /var/lib/mysql/ib_logfile[01]

[chunk 721785] STEP 04) service mysql start

THREAD B
Site: dba | Thread title: InnoDB table SELECT returns ERROR 2006 (HY000): MySQL server has gone away (after power outage)
[chunk 720274] This looks oddly familiar.
I have seen this occur with one of my web hosting client's DB servers. There was a particular table that crashed mysqld every single time you accessed it, even with SHOW CREATE TABLE.
The problem stems from a corrupt data dictionary. There is really no way to correct it. You could attempt to alter the tablespace_id within the .ibd file but the headache stems from locating the tablespace_id list internal to ibdata1.

[chunk 720275] Even if you create a MyISAM table with the same name in the same database as the original InnoDB table, you cannot convert it to InnoDB because the tablespace_id is already associated with the table name. This, of course, is a corrupted state. It's like having a pidgeon hole in ibdata1 that you cannot patch up without some exploratory surgery.

[chunk 720276] You may have to mysqldump everything except the database that houses the corrupt table. You would then have to mysqldump every table in that database except the corrupt table. Remember, it is the data dictionary's view of the table that is screwed up, not necessarily the table's data.

[chunk 720277] The only sure way to clean everything up is to perform the mysqldumps as I just specified, shutdown mysql, rm -rf all DB folders except /var/lib/mytsql/mysql, delete ibdata1, delete ib_logfile0, delete ib_logfile1, startup mysql, reload all mysqldumps. See my StackOverflow post about cleaning up your InnoDB infrastructure.
Since you are not using innodb_file_per_table, any tables with this corrupt state of things within ibdata1 are lost as casualities of war. My condolences.

[chunk 720278] For future reference, click here to see an artistic conception of InnoDB and its Internals.

### item Punix-33327-21239
THREAD A
Site: unix | Thread title: Toggle border with key combination in xmonad
[chunk 298072] I suppose the XMonad.Actions.NoBorders module (in xmonad-contrib) is helpful here (I've not tried it myself, tough**(a)**). It exports the toggleBorder function, which
[toggles] the border of the currently focused window.
It's rather small and self-explanatory, so if binding toggleBorder doesn't do exactly what you want, you can probably adapt it to your needs.

[chunk 298073] (a) I'm not sure what you're about to achieve, but if you'd prefer not to have to press a key at all, the XMonad.Layout.NoBorders module is great. It exports the smartBorders layout modifier that removes the borders if it is not needed (if there's only one window and only one screen, for example).

THREAD B
Site: unix | Thread title: Change the red border between windows in xmonad
[chunk 292276] To change the colour, you can set normalBorderColor and focusedBorderColor in xmonad.hs. They should be set to #RRGGBB. For example, to set the focused window's border to black, set focusedBorderColor = "#000000". The default color is #FF0000.
To disable the border, set borderWidth = 0 in xmonad.hs, or use XMonad.Layout.NoBorders for specific layouts.

### item Punix-287765-5656
THREAD A
Site: unix | Thread title: How will hibernation work in two Linux installations sharing a swap partition?
[chunk 391257] It will use the swap partition, (especially) if it has an fstab entry for it.
However your problem is not only with the swap partition, but also with all other filesystem partitions. You're not allowed to mount any of them as long as they're still mounted by the hibernated system.

[chunk 391258] Only one OS is allowed to mount a filesystem at a time, and with Hibernation, the system is "still running". If you Hibernate, then boot in another OS, change filesystems, then reboot and resume the Hibernated OS that still remembers the old state of those modified filesystem... it all goes ka-boom.
* BIG FAT WARNING
********************************************************* 
* 
* If you touch anything on disk between suspend and resume... 
* ...kiss your data goodbye.

[chunk 391259] Source: https://www.kernel.org/doc/Documentation/power/swsusp.txt
If you cannot guarantee that the disks won't be touched, best to avoid Hibernation altogether.

THREAD B
Site: unix | Thread title: Are there any side effects when two distros share a swap partition?
[chunk 283521] It's possible. In fact, you can share the swap space between completely different operating systems, as long as you initialize the swap space when you boot. It used to be relatively common to share swap space between Linux and Windows, back when it represented a significant portion of your hard disk.
Two restrictions come to mind:
The OSes cannot be running concurrently (which you might want to do with virtual machines).
You can't hibernate one of the OSes while you run another.

### item Psecurity-212062-163152
THREAD A
Site: security | Thread title: Why does WhatsApp not encrypt Google Drive backups?
[chunk 948947] 'Why does Google not encrypt your Whatsapp messages'?
As mentioned briefly in the comment above, it is something that we will never really know, unless privy to the agreements between FB and Google.
We can speculate though:
Google makes it's money from data and information. The more information it gathers, the more opportunities it has to make money. Very similar business model to FB in that respect.

[chunk 948948] Google can also comply with court orders to turn over information if asked. If they used zero-knowledge encryption, they would not be able to do that. I imagine that would make LE very unhappy.
An actual answer is impossible, I'm afraid. If you want to be sure your messages are not copied, or used for marketing or whatever, install Signal and encourage all of your friends to do so. Good luck. It's an uphill battle to fight the inertia of WhatsApp!

THREAD B
Site: security | Thread title: Does backing up WhatsApp on Google Drive expose messages?
[chunk 928227] You're confusing message integrity and security with secrecy. WhatsApp provides end to end encryption, meaning the message you send can only be read by the recipient and vice versa. This protects you from third parties trying to eavesdrop on your conversation, and even prevents WhatsApp themselves from reading the messages. You can't demand WhatsApp to allow you to wiretap a conversation if WhatsApp themselves have no idea what's being sent.

[chunk 928228] However once the message is in the hands of the recipient, it's a different story.
In order for it to appear in their chat history, it has to be saved on the phone.
If a persons device is compromised, so is your chat history with that person.
The person could also screenshot your conversation, or even use another phone to take a picture of your conversation.

[chunk 928229] Backup to Google Drive is simply a way of backing up your chat history so if you change devices or reset your phone all your messages aren't gone.

[chunk 928230] Once the conversation is in Google Drive however, if a valid law enforcement request is made for your files, your conversation is now compromised, as Google only provides server side encryption, which allows them to decrypt your files. This even opens you up to further compromise if the recipients Google account was ever hacked, as the hackers would have access to your message history with that person.

[chunk 928231] In short, no, the warning is accurate. It's not ambiguous, it tells you exactly what it means, if you save the messages to Google Drive, anyone with access to that account can retrieve the messages. This all boils down to the level of trust you have in your recipient. If you're not 100% sure that the person you're talking to isn't going to rat you out, best not to voice your dissent of your government to them.

### item Psecurity-3306-778
THREAD A
Site: security | Thread title: Why re-verify with CAPTCHA on failed form entry?
[chunk 846362] If the site has a means of knowing it's the same user in the same session, then no. So for example given a cookie or an ssl session then it seems OK to assume it's still a human user (within the limits of captcha).
If it's just a cookie that establishes the session (i.e. this is over http without SSL) then make sure to time it out tho. And you should be using SSL anyhow :-)

THREAD B
Site: security | Thread title: Anyone using Asirra in production? Are there similar alternatives?
[chunk 844396] Not relating specifically to Asirra, but wrt CAPTCHA in general, I will elaborate on @Graham's point and direct you to the following links:
"Has reCaptcha been cracked / hacked / OCR'd / defeated / broken?" on SO
My answer to "Practical non-image based CAPTCHA approaches?" on SO
Presentation I gave on this topic at OWASP in 2008
Best idea yet (obligatory XKCD)
RSnake's opinion of another "new" type of CAPTCHA (but mostly still applies to Asirra)
Bruce Schneier, but mostly the comments

[chunk 844397] In case you're lazy here are the highlights...
The 3 general ways of breaking CAPTCHAs are:
Broken implementation (e.g. wrong configuration, wrong settings, static images, exposing the answer, etc) - but probably does not apply to Asirra, unless its configuration-dependant
Inherent reverse-computability - If you can build a program to blur something that is still readable, I can build one to unblur it. I.e OCR is pretty darn good, at least if the image is readable by a human.

[chunk 844398] Putting a human in the mix, either by:
CAPTCHA farms: paying someone small amount of money, there is a MARKET for this: I've seen advertised on Ebay packages of 1000 CAPTCHAs "solved" for 4$, with a matching reliability % SLA
CAPTCHA Proxies, e.g. you can access pr0n if you solve this CAPTCHA... or even make a game out of it.
To sum up (as I've often done on this topic):

[chunk 844399] CAPTCHA tries to solve the wrong problem, and it does it badly: even if it worked perfectly, the problem is not "I want to identify who is a computer and who is a human and allow only humans to use my site however they want", but rather "I want to prevent misuse and flooding on my site".
We shouldnt be trying to turing-test the users, we should be limiting what they could do.
Or even better:
Authentication (or identification) is a poor replacement for authorization.

### item Punix-94318-47407
THREAD A
Site: unix | Thread title: Efficient way to print lines from a massive file using awk, sed, or something else?
[chunk 324422] Neither, use tail or head instead:
$ time tail -n 4000001 foo | head -n 11
real 0m0.039s
user 0m0.032s
sys 0m0.004s
$ time head -n 4000010 foo | tail -n 11
real 0m0.055s
user 0m0.064s
sys 0m0.036s
tail is in fact consistently faster. I ran both commands 100 times and calculated their average:
tail:
real 0.03962
user 0.02956
sys 0.01456
head:
real 0.06284
user 0.07356
sys 0.07244

[chunk 324423] I imagine tail is faster because though it has to seek all the way to line 4e10, it does not actually print anything until it gets there while head will print everything until line 4e10 + 10.
Compare to some other methods sorted in order of time:
sed:
$ time sed -n 4000000,4000011p;q foo
real 0m0.312s
user 0m0.236s
sys 0m0.072s
Perl:
$ time perl -ne 'next if $.<4000000; print; exit if $.>=4000010' foo 
real 0m1.000s
user 0m0.936s
sys 0m0.064s
awk:

[chunk 324424] $ time awk '(NR>=4000000 && NR<=4000010){print} (NR==4000010){exit}' foo 
real 0m0.955s
user 0m0.868s
sys 0m0.080s
Basically, the rule is the less you parse, the faster you are. Treating the input as a stream of data which only needs to be printed to the screen (as tail does) will always be the fastest way.

THREAD B
Site: unix | Thread title: cat line X to line Y on a huge file
[chunk 304801] I suggest the sed solution, but for the sake of completeness,
awk 'NR >= 57890000 && NR <= 57890010' /path/to/file
To cut out after the last line:
awk 'NR < 57890000 { next } { print } NR == 57890010 { exit }' /path/to/file
Speed test (here on macOS, YMMV on other systems):
100,000,000-line file generated by seq 100000000 > test.in
Reading lines 50,000,000-50,000,010
Tests in no particular order
real time as reported by bash's builtin time

[chunk 304802] 4.373 4.418 4.395 tail -n+50000000 test.in | head -n10
 5.210 5.179 6.181 sed -n '50000000,50000010p;57890010q' test.in
 5.525 5.475 5.488 head -n50000010 test.in | tail -n10
 8.497 8.352 8.438 sed -n '50000000,50000010p' test.in
22.826 23.154 23.195 tail -n50000001 test.in | head -n10
25.694 25.908 27.638 ed -s test.in <<<"50000000,50000010p"
31.348 28.140 30.574 awk 'NR<57890000{next}1;NR==57890010{exit}' test.in
51.359 50.919 51.127 awk 'NR >= 57890000 && NR <= 57890010' test.in

[chunk 304803] These are by no means precise benchmarks, but the difference is clear and repeatable enough* to give a good sense of the relative speed of each of these commands.
*: Except between the first two, sed -n p;q and head|tail, which seem to be essentially the same.

### item Punix-79684-50752
THREAD A
Site: unix | Thread title: Fix terminal after displaying a binary file
[chunk 317384] Often times when in a Unix/Linux terminal (Bash) for example you'll use the commands more or less or cat to view a file. When you do this and the file isn't meant to be viewed (such as /bin/ls) you'll get output like this:
What's going on here is that you just tried to view a file that's a program. An executable which aren't meant to be viewed with standard viewers as I mentioned above.
method #1 - reset
To fix this issue you can do the following:
Hit Control + C a couple of times (Ctrl+C)

[chunk 317385] Type the command reset and hit return
This should usually put your terminal back into a more normal mode. I'll mention one more thing, when you do the steps above, you'll by typing them blind into your terminal. So just make sure you're typing it correctly.
method #2 - stty sane
As suggested in the comments by @sendmoreinfo you might have better luck using the following commands instead if the above doesn't work:
$ stty sane
$ tput rs1
determining a files' type

[chunk 317386] Incidentally, if you come across a file and aren't sure if it's going to mess up your terminal you can inspect the file using the command file which will report back the type of file it is.
For example, with /bin/ls that file shows the following output:
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, stripped

THREAD B
Site: unix | Thread title: How to fix a terminal after a binary file has been dumped inside it?
[chunk 306302] I think reset would definitely fix it.
Consider looking into man page.
Example:
[m0nhawk@terra:~]> cat /dev/urandom
êIÉè;┤Ü)MåÇ▐¿÷¢§ôWdO┘&!π¡
[└█┼░▒┬┐@├err▒:·]> c▒├ /de┴/┤r▒┼do└
And resetfixes this.

### item Pserverfault-352431-49222
THREAD A
Site: serverfault | Thread title: Should I completely turn off swap for linux webserver?
[chunk 112457] I would say it depends on your use case and the rest of the answers have covered this pretty well. 4G of swap are after all a cheap way to buy some safety. And I feel that this cheapness is what is making people not want to turn it off.

[chunk 112458] But let me answer with a rhetorical question. If money is not an issue, and you have a choice between two systems - one with 12G of RAM and 4G of swap, and another with 16G of RAM and no swap - which one would you choose? Unfortunately most people would still answer that they'd choose 16G of RAM and still add 4G of swap, which is missing my point.

[chunk 112459] And on another note, I personally find a swappy system worse than a crashed system. A crashed system would trigger a standby backup server to take over much sooner. And in an active-active (or load balanced setup) a crashed system would be taken out of rotation much sooner. A win for the no-swap system again.

THREAD B
Site: serverfault | Thread title: CentOS How Much SWAP for 16GB of RAM?
[chunk 19830] Not more than a gig or two -- you want a little bit of swap available, just in case and because it helps things work a bit better, but if you ever get to the point where you're heavily swapping, the machine is going to be useless -- and in a real catastrophic situation, you're actually better off with a smaller swap space, because then you'll trigger the OOM killer sooner rather than later.

### item Psoftwareengineering-256380-141005
THREAD A
Site: softwareengineering | Thread title: Does it make sense to split up an existing multi-method interface into several single method interfaces just to take advantage of lambdas?
[chunk 623712] Instead of building a facade wouldn't it make sense to do something more like this?
public interface SuccessListener<T> {
default void onSuccess(T data) {
 // Completely ignore it.
 }
}
public interface AuthFailureListener {
default void onAuthFailure() {
 // Completely ignore it.
 }
}
public interface ErrorListener {
default void onError() {
 // Completely ignore it.
 }
}

[chunk 623713] // Retain the old API
public interface GetCallback<T> extends SuccessListener<T>, AuthFailureListener, ErrorListener {
 // Now empty - we are a conglmerate.
}
public static <T> void issueRequest(String url, SuccessListener<T> successListener, AuthFailureListener failureListener, ErrorListener errorListener) {
 // Implementation ...
}
public static <T> void issueRequest(String url, GetCallback<T> callback) {
 // Ensures backwards compatability.
 issueRequest(url, callback, callback, callback);
}

[chunk 623714] public void getData() {
 issueRequest("http://programmers.stackexchange.com", new GetCallback<String>() {
@Override
 public void onSuccess(String data) {
 }
@Override
 public void onAuthFailure() {
 }
//@Override
 //public void onError() {
 // Can now leave out the ones you don't want.
 //}
 });
}

[chunk 623715] It is still compatible with your earlier API and internally who cares that the same object is a listener for all three events. It also opens up the possibilities of adding default implementations and allowing the chance to issue a request with only a SuccessListener.
Note: I tweaked the code to use default for even more niceness.

THREAD B
Site: softwareengineering | Thread title: How would you know if you've written readable and easily maintainable code?
[chunk 576313] Your peer tells you after reviewing the code.
You cannot determine this yourself easily because as the author, you know more than the code says by itself. A computer cannot tell you, for the same reasons that it cannot tell if a painting is art or not. Hence, you need another human - capable of maintaining the software - to look at what you have written and give his or her opinion. The formal name of said process is peer review.