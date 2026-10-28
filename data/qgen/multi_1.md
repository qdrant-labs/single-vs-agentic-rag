### item Psoftwareengineering-186036-147480
THREAD A
Site: softwareengineering | Thread title: When should pointers be checked for NULL in C?
[chunk 595892] Invalid null pointers can either be caused by programmer error or by runtime error. Runtime errors are something a programmer can't fix, like a malloc failing due to low memory or the network dropping a packet or the user entering something stupid. Programmer errors are caused by a programmer using the function incorrectly.

[chunk 595893] The general rule of thumb I've seen is that runtime errors should always be checked, but programmer errors don't have to be checked every time. Let's say some idiot programmer directly called graph_get_current_column_color(0). It will segfault the first time it's called, but once you fix it, the fix is compiled in permanently. No need to check every single time it's run.

[chunk 595894] Sometimes, especially in third party libraries, you'll see an assert to check for the programmer errors instead of an if statement. That allows you to compile in the checks during development, and leave them out in production code. I've also occasionally seen gratuitous checks where the source of the potential programmer error is far removed from the symptom.

[chunk 595895] Obviously, you can always find someone more pedantic, but most C programmers I know favor less cluttered code over code that is marginally safer. And "safer" is a subjective term. A blatant segfault during development is preferable to a subtle corruption error in the field.

THREAD B
Site: softwareengineering | Thread title: Should one check for null if he does not expect null?
[chunk 579197] The question is not so much whether you should check for null or let the runtime throw an exception; it is how you should respond to such an unexpected situation.
Your options, then, are:
Throw a generic exception (NullReferenceException) and let it bubble up; if you don't do the null check yourself, this is what happens automatically.

[chunk 579198] Throw a custom exception that describes the problem on a higher level; this can be achieved either by throwing in the null check, or by catching a NullReferenceException and throwing the more specific exception.
Recover by substituting a suitable default value.
There is no general rule which one is the best solution. Personally, I would say:

[chunk 579199] The generic exception is best if the error condition would be a sign of a serious bug in your code, that is, the value that is null should never be allowed to get there in the first place. Such an exception may then bubble all the way up into whatever error logging you have set up, so that someone gets notified and fixes the bug.

[chunk 579200] The default value solution is good if providing semi-useful output is more important than correctness, such as a web browser that accepts technically incorrect HTML and makes a best effort to render it sensibly.
Otherwise, I'd go with the specific exception and handle it somewhere suitable.

### item Punix-681422-31947
THREAD A
Site: unix | Thread title: What is this sed doing with the script: `$a\`?
[chunk 500922] As others have said, e.g. in How to add a newline to the end of a file?, with GNU sed (and some other implementations), $a\ adds a newline to the end of a file if it doesn’t have one.
Why it does this isn’t so clear, and the documentation doesn’t explain it. However, examining the source code does...
Let’s start with the documentation. $a\ is a variant of a, exploiting a special case of a GNU extension:

[chunk 500923] As a GNU extension, the a command and text can be separated into two -e parameters, enabling easier scripting:
$ seq 3 | sed -e '2a\' -e hello
1
2
hello
3
$ sed -e '2a\' -e "$VAR"
The way a is implemented in sed is with a queue of text to append, tracked in an append_queue. When the time comes to process this queue, in a function called dump_append_queue, the first step is
output_missing_newline (&output_file);

[chunk 500924] which adds a missing newline if necessary — to ensure that the appended text will be added to separate lines, not to the end of the current line. Then the contents of the queue are appended.
With sed -i '$a\', the missing newline is added if necessary, and then the queue is processed — but the queue is empty, so no additional change is made.

THREAD B
Site: unix | Thread title: How to add a newline to the end of a file?
[chunk 297425] To recursively sanitize a project I use this oneliner:
git ls-files -z | while IFS= read -rd '' f; do if file --mime-encoding "$f" | grep -qv binary; then tail -c1 < "$f" | read -r _ || echo >> "$f"; fi; done
Explanation:

[chunk 297426] git ls-files -z lists files in the repository. It takes an optional pattern as additional parameter which might be useful in some cases if you want to restrict the operation to certain files/directories. As an alternative, you could use find -print0 ... or similar programs to list affected files - just make sure it emits NUL-delimited entries.
while IFS= read -rd '' f; do ... done iterates through the entries, safely handling filenames that include whitespace and/or newlines.

[chunk 297427] if file --mime-encoding "$f" | grep -qv binary checks whether the file is in a binary format (such as images) and skips those.
tail -c1 < "$f" reads the last char from a file.
read -r _ exits with a nonzero exit status if a trailing newline is missing.
|| echo >> "$f" appends a newline to the file if the exit status of the previous command was nonzero.

### item Pserverfault-303151-141386
THREAD A
Site: serverfault | Thread title: Mounting an ISO on Windows Server 2008
[chunk 97580] Why do you need to actually mount the ISO? Instead of installing unnecesasry 3rd party apps on your server, why not just use something like 7-zip to extract the contents of the ISO?

THREAD B
Site: serverfault | Thread title: Mount an ISO Image on Windows 2008 Server
[chunk 50669] Do not mount it?
I mean, seriously. You can't reboot? Ok. This is for software on a server that came with an ISO image? Ok.
So what?
Mount ISO image on your workstation
Copy files to server.
Install.
I do that all the time. Server software (usually) comes without disc based copy protection.

### item Pdba-122582-47266
THREAD A
Site: dba | Thread title: Copying (hundreds of) tables from one server to another (with SSMS)
[chunk 767507] You could use SQL Server Management Studio's "Export Data" task. Right click on the database in SSMS, select Tasks and then "Export Data". It will launch an interactive wizard that will allow to copy tables from one server to another, although you will have to recreate the indices yourself. The wizard creates a temporary SSIS package (although you can also opt to save it) and is relatively fast.

THREAD B
Site: dba | Thread title: overwrite table with data from another table - SQL
[chunk 737405] To combine the answers from @Kin and @DavidSpillett.
First an assumption. DB1 and DB2 are on the same instance. It certainly sounds like they are but it never hurts to state the obvious (particularly since I've been wrong with what I thought was obvious before.)

[chunk 737406] Given that, if the data is large, say multiple millions of rows then use an SSIS package. This has one specific feature that you will want to use. You can specify a batch size. This way your transaction size will be smaller. The downside to the SSIS package is that it adds a level of complexity to your process. It isn't a big one, but if you are working with a smaller table you don't need it.

[chunk 737407] Which leads us to the other option. If however the data is in the several hundred thousand range or smaller then use code like this.
USE D1;
GO
TRUNCATE TABLE dbo.T1;
GO
INSERT INTO D1.dbo.T1
SELECT * 
FROM D2.dbo.T1;
GO
And last but not least it if it is somewhere on the boarder then I would try both and see what works best for you.
NOTE:
You might also consider not using a SELECT * on the INSERT INTO and instead specify a field list.
That structure would look like this

[chunk 737408] INSERT INTO D1.dbo.T1 (Field1, Field2)
SELECT Field1, Field2
FROM D2.dbo.T1;

### item Punix-255843-226164
THREAD A
Site: unix | Thread title: Opening more than 10 file descriptors with ksh
[chunk 381574] In ksh, you can only use single digit for explicit file descriptor. With ksh93r and above, you can open more than 10 file descriptor by using the form:
{var}>filename
(bash and zsh copied this feature later).
ksh will pick available file descriptor greater than or equal to 10, store file descriptor number in variable var:
$ exec {var1}>/tmp/test1
$ echo "$var1"
10
$ exec {var2}>/tmp/test2
$ echo "$var2"
11

THREAD B
Site: unix | Thread title: What does 'exec {fd}</dev/watchdog' do in Bash
[chunk 371996] Rather than having to pick a file descriptor and hope it's available:
exec 4< /dev/watchdog # Was 4 in use? Who knows?
this notation asks the shell to pick a file descriptor that isn't currently in use, open the file for reading on that descriptor, and assign the number to the given variable (fd).
$ exec {fd}< /dev/watchdog
$ echo $fd
10

### item Punix-26805-23130
THREAD A
Site: unix | Thread title: How to silently get an empty string from a glob pattern with no matches
[chunk 294961] Turn on the null_glob option for your pattern with the N glob qualifier.
list_of_files=(*(N))
If you're doing this on all the patterns in a script or function, turn on the null_glob option:
setopt null_glob
This answer has bash and ksh equivalents.
Do not use print or command substitution! That generates a string consisting of the file names with spaces between them, instead of a list of strings. (See What is word splitting? Why is it important in shell programming?)

THREAD B
Site: unix | Thread title: How to report number of files in all subdirectories?
[chunk 293262] This does it in a safe and portable way. It won't get confused by strange filenames.
for f in *; do [ -d ./"$f" ] && find ./"$f" -maxdepth 1 -exec echo \; | wc -l && echo $f; done
Note that it will print the number of files first, then the directory name on a separate line. If you wish to keep OP's format you will need further formatting, e.g.
for f in *; do [ -d ./"$f" ] && find ./"$f" -maxdepth 1 -exec echo \;|wc -l|tr '\n' ' ' && echo $f; done|awk '{print $2"\t"$1}'

[chunk 293263] If you have a specific set of subdirectories you're interested in, you can replace the * with them.
Why is this safe? (and therefore script-worthy)
Filenames can contain any character except /. There are a few characters that are treated specially either by the shell or by the commands. Those include spaces, newlines, and dashes.
Using the for f in * construct is a safe way of getting each filename, no matter what it contains.

[chunk 293264] Once you have the filename in a variable, you still have to avoid things like find $f. If $f contained the filename -test, find would complain about the option you just gave it. The way to avoid that is by using ./ in front of the name; this way it has the same meaning, but it no longer starts with a dash.

[chunk 293265] Newlines and spaces are also a problem. If $f contained "hello, buddy" as a filename, find ./$f, is find ./hello, buddy. You're telling find to look at ./hello, and buddy. If those don't exist, it will complain, and it will never look in ./hello, buddy. This is easy to avoid - use quotes around your variables.

[chunk 293266] Finally, filenames can contain newlines, so counting newlines in a list of filenames will not work; you'll get an extra count for every filename with a newline. To avoid this, don't count newlines in a list of files; instead, count newlines (or any other character) that represent a single file. This is why the find command has simply -exec echo \; and not -exec echo {} \;. I only want to print a single new line for the purpose of tallying the files.

### item Punix-610031-213799
THREAD A
Site: unix | Thread title: How can a shell output affect the typed text after the command prompt?
[chunk 481954] What you are seeing is the attribute string for the terminal. Terminals might respond differently to one or more of these commands.
A quick way to reproduce them:
$ echo -e '\033[c'
In my case, inside Gnome terminal this types 65;1;9c, inside xterm it types 64;1;2;6;9;15;18;21;22c and in the console, after pressing Ctrl-Alt-F1 I get 6c.
The strings are created by the terminal, so you cannot use them to "insert" arbitrary text.
This page tells you more about their meaning:

[chunk 481955] CSI Ps c Send Device Attributes (Primary DA).
Ps = 0 or omitted -> request attributes from terminal.
The
 response depends on the decTerminalID resource setting.
-> CSI ?
1 ; 2 c ("VT100 with Advanced Video Option")
 -> CSI ?
1 ; 0 c ("VT101 with No Options")
 -> CSI ?
6 c ("VT102")
 -> CSI ?
6 2 ; Psc ("VT220")
 -> CSI ?
6 3 ; Psc ("VT320")
 -> CSI ?
6 4 ; Psc ("VT420")
 The VT100-style response parameters do not mean anything by
 themselves.

[chunk 481956] VT220 (and higher) parameters do, telling the
 host what features the terminal supports:
 Ps = 1 -> 132-columns.
Ps = 2 -> Printer.
Ps = 3 -> ReGIS graphics.
Ps = 4 -> Sixel graphics.
Ps = 6 -> Selective erase.
Ps = 8 -> User-defined keys.
Ps = 9 -> National Replacement Character sets.
Ps = 1 5 -> Technical characters.
Ps = 1 8 -> User windows.
Ps = 2 1 -> Horizontal scrolling.
Ps = 2 2 -> ANSI color, e.g., VT525.
Ps = 2 9 -> ANSI text locator (i.e., DEC Locator mode).

[chunk 481957] Some devices will also output identifying information for the device (Request terminal parameters) with the following escape sequence.
$ echo -e '\033[x'

THREAD B
Site: unix | Thread title: Can bash write to its own input stream?
[chunk 368626] With zsh, you can use print -z to place some text into the line editor buffer for the next prompt:
print -z echo test
would prime the line editor with echo test which you can edit at the next prompt.
I don't think bash has a similar feature, however on many systems, you can prime the terminal device input buffer with the TIOCSTI ioctl():
perl -e 'require "sys/ioctl.ph"; ioctl(STDIN, &TIOCSTI, $_)
 for split "", join " ", @ARGV' echo test

[chunk 368627] Would insert echo test into the terminal device input buffer, as if received from the terminal.
A more portable variation on @mike's Terminology approach and that doesn't sacrifice security would be to send the terminal emulator a fairly standard query status report escape sequence: <ESC>[5n which terminals invariably reply (so as input) as <ESC>[0n and bind that to the string you want to insert:
bind '"\e[0n": "echo test"'; printf '\e[5n'
If within GNU screen, you can also do:

[chunk 368628] screen -X stuff 'echo test'
Now, except for the TIOCSTI ioctl approach, we're asking the terminal emulator to send us some string as if typed. If that string comes before readline (bash's line editor) has disabled terminal local echo, then that string will be displayed not at the shell prompt, messing up the display slightly.

[chunk 368629] To work around that, you could either delay the sending of the request to the terminal slightly to make sure the response arrives when the echo has been disabled by readline.
bind '"\e[0n": "echo test"'; ((sleep 0.05; printf '\e[5n') &)
(here assuming your sleep supports sub-second resolution).
Ideally you'd want to do something like:
bind '"\e[0n": "echo test"'
stty -echo
printf '\e[5n'
wait-until-the-response-arrives
stty echo

[chunk 368630] However bash (contrary to zsh) doesn't have support for such a wait-until-the-response-arrives that doesn't read the response.
However it has a has-the-response-arrived-yet feature with read -t0:
bind '"\e[0n": "echo test"'
saved_settings=$(stty -g)
stty -echo -icanon min 1 time 0
printf '\e[5n'
until read -t0; do
 sleep 0.02
done
stty "$saved_settings"
Further reading
See @starfry's answer's that expands on the two solutions given by @mikeserv and myself with a few more detailed information.

### item Punix-323596-244983
THREAD A
Site: unix | Thread title: How to create a persistent USB key of a running system?
[chunk 401693] I think dd is the good way to proceed.
Meanwhile, this solution works out of the box only if there is only one /dev/sd*.
For instance, i would suggest to list all /dev/sd* except usb one then make as many partition (fdisk -n) as required on usb drive and use dd for each /dev/sd* counted.
From the link:
insert the destination USB flash drive in my workstation
delete the existing vfat partition and create a single linux partition using fdisk
create a filesystem and synchronize it:

[chunk 401694] bash# mkfs.ext3 /dev/sdb1
bash# sync ; sync
remove the usb flash drive from the workstation, put it in the target PC
mount the usb drive, move the udev filesystem out of the way, and copy the local filesystem:
bash# cd /
bash# mkdir /mnt/sda1
bash# mount /dev/sda1 /mnt/sda1
bash# mkdir udev
bash# mount --move /dev /udev
bash# cp -ax / /mnt/sda1
That copy command might take awhile. When it is done, get rid of the temporary directory /udev
bash# mount --move /udev /dev
bash# rm -fr /udev

[chunk 401695] Now to make the usb drive bootable. It should still be mounted at /mnt/sda1. First, in file /mnt/sda1/boot/grub/device.map set hd(0) to /dev/sda and in /mnt/sda1/boot/grub/menu.lst set the kernel boot options correctly for each boot configuration, eg:
title Debian GNU/Linux, kernel 2.6.18-6-486
root (hd0,0)
kernel /boot/vmlinuz-2.6.18-6-486 root=/dev/sda1 ro vga=792 
initrd /boot/initrd.img-2.6.18-6-486
savedefault
Finally, install grub on the usb flash drive:

[chunk 401696] bash# grub-install --root-director=/mnt/sda1 /dev/sda
All done! Now you can reboot into the flash drive.

THREAD B
Site: unix | Thread title: Using dd to clone a disk while mounted - risks?
[chunk 378106] If you're lucky, the filesystem corruption will be detected as soon as you try to mount the copy. If you're unlucky, it won't be detected until later.
It's also possible that you'll manage to get a consistent copy of the filesystem except for the files that were modified during the copy. But I wouldn't count on it. It might work with ext4 as long as you don't create, delete or move any file, so that the directories aren't modified.

[chunk 378107] If you copy a filesystem that's mounted read-only, of course, everything will be fine. Except that you shouldn't use dd, use cat instead.
There are several reliable ways to clone a disk. Pick one of these, rather than one that practically guarantees corruption.
Some filesystems offer a clone functionality, for example btrfs. I don't think ext4 does.

[chunk 378108] If the filesystem is on Linux's native partition scheme, i.e. an LVM volume, you can make an LVM snapshot. That requires that you use LVM, rather than putting the filesystem directly on some other partition scheme such as MBR or GPT. You'll be left with a filesystem that wasn't cleanly unmounted, but represents a consistent snapshot of the original at a point in time.

[chunk 378109] If you can get the filesystem onto a RAID-1 array, you can clone it by adding a member to the array, waiting for it to synch, and detaching the new member. Here too you'll have a consistent but not clean snapshot. You can create a RAID-1 volume around an existing filesystem, but that requires an offline step to shrink the filesystem by 128kB.

[chunk 378110] You can make a file-level backup. That won't get you a consistent view of the filesystem, since copying files takes time, but it does guarantee at least that every file that wasn't modified during the backup will be backed up correctly.

### item Pserverfault-900432-171744
THREAD A
Site: serverfault | Thread title: Have a script receive an IP from the DHCP server?
[chunk 237375] In order to test what would happen if a completely new device request your DHCP server for an IP address your Nagios script would need to send DHCP Discover packets with spoofed MAC addresses. You would need to be able to send raw DHCP packets, but before even trying that you should revise what this arrangement would actually require.

[chunk 237376] Let's assume we have a DHCP lease time of 24 hours. If you send a DHCP Discover packet with a new MAC address every 5 minutes and get an DHCP offer from the pool, your Nagios test alone will occupy 288 IP addresses from your pool. If your lease time is even longer, for example a week, you will have up to 2016 dummy reserver IP addresses. You would need to have a /20 DHCP pool in order to have this amount of spare addresses + space for the actual devices.

[chunk 237377] That's why I suggest using the regular test and rely on that for over 99,9% of the cases. The rare condition of pool exhaustion every now and then is worth taking care manually instead of actually causing the situation while testing it.
Secondary approach. Do not test by sending additional DHCP Discover packets, but instead monitor the actual traffic. Create an alert whenever you see:
a DHCP Discovery packet without a corresponding DHCP Offer packet.

[chunk 237378] a DHCP Request packet without a corresponding DHCP Ack packet.
You should be able to recognize any problems pretty fast.

THREAD B
Site: serverfault | Thread title: Command line program to test DHCP service
[chunk 59402] Even if you don't use a Nagios monitoring server, you can grep the check_dhcp binary or compile it from source and use the check to test a DHCP-Server. E.g.
./check_dhcp -v -s <dhcp_server_address> -r <expected_ip_address> -m <mac_address_touse>

### item Punix-166033-159695
THREAD A
Site: unix | Thread title: delete a line if same line exists in the previous line
[chunk 351763] If you can guarantee that the identical lines will be consecutive, you can use
uniq your_file
and cuonglm's answer will work even if they're not.

THREAD B
Site: unix | Thread title: How does awk '!a[$0]++' work?
[chunk 349912] Here is a "intuitive" answer, for a more in depth explanation of awk's mechanism see either @Cuonglm's
In this case, !a[$0]++, the post-increment ++ can be set aside for a moment, it does not change the value of the expression. So, look at only !a[$0]. Here:
a[$0]
uses the current line $0 as key to the array a, taking the value stored there. If this particular key was never referenced before, a[$0] evaluates to the empty string.
!a[$0]

[chunk 349913] The ! negates the value from before. If it was empty or zero (false), we now have a true result. If it was non-zero (true), we have a false result. If the whole expression evaluated to true, meaning that a[$0] was not set to begin with, the whole line is printed as the default action.
Also, regardless of the old value, the post-increment operator adds one to a[$0], so the next time the same value in the array is accessed, it will be positive and the whole condition will fail.

### item Pserverfault-22471-15782
THREAD A
Site: serverfault | Thread title: MMORPG server maintenance
[chunk 9889] I suspect that they're deploying the latest version of their code, which requires that they restart the application (and hopefully running some tests before re-enabling access). From that point of view, it's more of a StackOverflow problem and less of a ServerFault one.
I think it's possible to create a hot-patching system, but it would necessarily be incredibly complicated. From what I understand, an MMO server "application" consists of several different components --

[chunk 9890] Login server -- Handles authentication and acts as a "hub" between gameplay servers. Once a client is in-game they no longer interact with the login server. In such a system you could apply patches and restart the login server without interfering with gameplay (though you'll have a period of time where people won't be able to log in).

[chunk 9891] Gameplay servers -- Clusters of machines grouped into logical independent units ("worlds", etc). It's assumed that the each gameplay cluster uses some kind of internal communication protocol to correspond state to one another; you're probably going to have to patch each cluster all at once. One possible way to do this is to patch a warm-failover. You'd then need to be able to both
Signal the client to connect to the warm failover and disconnect from the old cluster.

[chunk 9892] Keep the state synched between the failover and the out-of-date application server while all of the clients transfer.

[chunk 9893] Database servers -- Some kind of persistent datastore, like an RDBMS. Hopefully you're not making changes to the datastore that often. Presumably each gameplay server/cluster has an independent datastore. You might be able to use the same trick with a warm failover (and tell the gameplay servers to disconnect, wait for the old and failover databases to sync, then reconnect to the failover) but that seems pretty risky to me.

[chunk 9894] All of the above cases add an incredible amount of complexity to an already complex system and introduce a bunch of places where a code failure can cause data loss or corruption.
Another solution is to use a language which is designed for 100% uptime and has built-in capabilties for hotpatching running code. Erlang is a good choice (hotpatching example), and Java has similar functionality.

THREAD B
Site: serverfault | Thread title: How often should I reboot Linux servers?
[chunk 7123] You must reboot after a kernel update (unless you are using KSplice), anything else is optional.
Personally I reboot on a monthly cycle during a maintenance window to make sure the server and all services come back as expected.
This way I can be reasonably certain if I have to do an out of schedule reboot (i.e.
critical kernel update) that the system will come back up properly.
Automated monitoring of servers and services (i.e.

[chunk 7124] Nagios) also goes a long way to helping this process (reboot, watch the lights go red and then hopefully all back to green).

[chunk 7125] P.S. if you do reboot regularily you'll want to make sure you tune your fsck checks (i.e. maximal mount count between checks appropriately, otherwise a quick 2 minute reboot might take 30 minutes if the server starts fsck'ing a couple terabytes of data. I typically set my mount count to 0 (tune2fs -c 0) and the interval between checks to 6 months or so and then manually force an fsck every once in a while and reset the count.

### item Punix-470878-250789
THREAD A
Site: unix | Thread title: Mirror Linux disk writes to secondary disk
[chunk 444704] You can use a MD RAID1 with the option --write-mostly.
subsequent devices listed in a --build, --create, or --add command will be flagged as 'write-mostly'. This is valid for RAID1 only and means that the 'md' driver will avoid reading from these devices if at all possible. This can be useful if mirroring over a slow link.
I use this when I want a fast SSD but have the data on a second, spinning drive.

THREAD B
Site: unix | Thread title: Can I get SSD rw performance while keeing data security if I combine SSD & HDD in btrfs RAID1
[chunk 379904] Assuming your SSD is faster for writes (and not just for reads), then there's an easy way to set this up with Linux's RAID subsystem. Say you're going to replicate /dev/sda1 (HDD) and /dev/sdb1 (SSD):
mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 --write-mostly --write-behind=1024 /dev/sda1

[chunk 379905] --write-mostly means that the preceding device(s) will be preferred for reading, while the following devices will only be written to most of the time. --write-behind means that the write-mostly devices are allowed to lag behind; the parameter determines how large the write buffer is. You may want to tweak the write-behind parameter based on performance on your machine.
If you want to use your existing volume, you can convert it to RAID-1 with superblock format 1.0.

[chunk 379906] Drives already include their own integrity checks, so there's usually not much use for another one on top.
The main problem with drive failure is data that becomes unreadable, not data that becomes corrupted.
I don't know what the relative undetected error rate is for SSD and HDD, but I suspect that it's about the same (and thus not SSD vs HDD but between the particular devices), so there's no reason to assume that the data read back from HDD is more accurate.

[chunk 379907] Btrfs and ZFS have optional filesystem-level integrity verification if you want that.

### item Punix-230692-52131
THREAD A
Site: unix | Thread title: AIX-Need to add lines after identifying the Pattern in the file using Non-GNU - Sed
[chunk 373388] You are escaping the T of TMOUT:
sed 's/.*export.*\TMOUT./&\FGOLD=`echo "\033[1;32m"`/' pro
 ^
 |-----??
That shouldn't make much difference but it's pointless. Then, you are also matching a character after TMOUT but your file has none (sed won't match the final newline). Try this instead:
sed 's/export TMOUT./&\nFGOLD=`echo "\\033[1;32m"`/' file

[chunk 373389] I don't have a non-GNU sed to test this on and I'm not sure if the \n will work in the replacement. If that doesn't work, try adding a \ and then pressing Enter to get the newline:
sed 's/export TMOUT/&\ ## hit enter and continue writing on a new line
FGOLD=`echo "\\033[1;32m"`/' file
So, other options are:
perl -pe 's/export TMOUT/$&\nFGOLD=\`echo "\\033[1;32m"\`/' file
Or awk:
awk '{
 if(/export TMOUT/){a=1}
 {
 print;
 if(a==1){
 print "FGOLD=`echo \"\\033[1;32m\"`";
 a=0
 }}}' file

THREAD B
Site: unix | Thread title: sed on OSX insert at a certain line
[chunk 306452] Strictly speaking, the POSIX specification for sed requires a newline after a\:
[1addr]a\
text
Write text to standard output as described previously.
This makes writing one-liners a bit of a pain, which is probably the reason for the following GNU extension to the a, i, and c commands:

[chunk 306453] As a GNU extension, if between the a and the newline there is other than a whitespace-\ sequence, then the text of this line, starting at the first non-whitespace character after the a, is taken as the first line of the text block. (This enables a simplification in scripting a one-line add.) This extension also works with the i and c commands.
Thus, to be portable with your sed syntax, you will need to include a newline after the a\ somehow. The easiest way is to just insert a quoted newline:

[chunk 306454] $ sed -e 'a\
> text'
(where $ and > are shell prompts). If you find that a pain, bash [1] has the $' ' quoting syntax for inserting C-style escapes, so just use
sed -e 'a\'$'\n''text'
[1] since version 2.0 (1996) and ksh93 (where it comes from), zsh (3.1.5+), mksh (r39b+) and some Almquist shell derivatives (e.g., /bin/sh in FreeBSD 9+)

### item Psecurity-17095-14881
THREAD A
Site: security | Thread title: Security risks of hosting user-supplied images?
[chunk 857266] An image might still be a valid image and still contain malicious material such as embedded comments or other (undefined) attack vectors. One -- albeit old -- example was the GDI JPEG vulnerability in Windows from 2004.
I think your primary concern is to ensure that your image-acceptance mechanism is simple and tight. You'll want to watch for file permission errors, resource exhaustion (running out of space, tying up network resource, etc.) and path attacks (eg. potentially overwriting files).

[chunk 857267] Furthermore, ensure that any string-handling checks are strictly and precisely defined. There was a recent question on sec.SE regarding attacking ASP upload code that used a less strict string searching mechanism.
Finally, search this site for the term "upload". Some fine examples which can give you a clear picture (no pun intended!) of all of the challenges you may face:
What steps should be taken to validate user uploaded images within an application?

[chunk 857268] What are the security risks of letting the users upload content to my site?

THREAD B
Site: security | Thread title: Is it possible to inject HTML into image to provoke XSS?
[chunk 855636] I'm pretty sure bstpierre was talking about a situation, where you let users upload images to display in a gallery and furthermore you display meta-data about that image taken from EXIF tags.
If the EXIF tags were specifically constructed with malicious html tags, and there was no input sanitation (e.g., escape characters like <, >, &, so they are rendered in the page like < >, &) you could conceivably use them for an XSS attack.

[chunk 855637] Again, it is not a problem if your web app sanitizes all user-input including extracted tags from image files.
bobince was talking about a few totally different things; the closest being that someone uploads a file - say fake_image.jpg but instead of being an image, the content is actually a html file.

[chunk 855638] By content sniffing, he meant that some browsers, when you click to open up a page http://example.com/fake_image.jpg can figure out that fake_image.jpg is not an image but instead a html file and will display the html page in the file.
Thus, the uploaded html file (with an image file name) could be used in an XSS attack.

[chunk 855639] For this attack to be useful, you have to have a browser that allows this sort of content-sniffing, and then you have to go to the URL of the image (not just have <img src='fake_image.jpg'> embedded in the page).

### item Pserverfault-9766-8981
THREAD A
Site: serverfault | Thread title: What a beginner should know/learn for sysadmin job?
[chunk 4766] There is a lot of overlap with existing questions, I am creating a wiki here with links. Please feel free to update.
How to make (and restore) backups!
Customer service skills
Troubleshooting
Your troubleshooting rules, approach to troubleshooting?
Etiquette of Troubleshooting Problems In The Workspaces Of Others
How to respond when there is a crisis
What’s your checklist for when everything blows up?
The OSI Model, and IP networking.

[chunk 4767] What is the OSI model and how does it apply to todays networks?
Practical implications of OSI vs TCP/IP networking.
How does Subnetting Work?
What is the difference between a port and a socket?
What are routers, hubs, and switches?
What is the difference between UDP and TCP?
How to document their network
How are you documenting your work, processes and environment?
How to ask for help in a way that will get you useful results.
How To Ask Questions The Smart Way
How to ask a question
Security

[chunk 4768] How to respond to a compromised system
How to use the CLI
Useful Commandline Commands on Windows
Useful Commandline Commands on Linux
Useful Commandline Commands on Mac OS
How to monitor the systems you will be responsible for
Also see
What makes a “Good” or “Great” Administrator?
Cheat Sheets for System Administrators?
What tools should you absolutely know as a Windows/Linux Sysadmin?
What should every sysadmin know before administrating a public server?

[chunk 4769] What sysadmin things should every programmer know?
What is the single most influential book every sysadmin should read?

THREAD B
Site: serverfault | Thread title: What is the difference between UDP and TCP?
[chunk 4400] TCP is backed by acks and retries to make sure you data gets where it's going. UDP is connectionless and "fire and forget". UDP is mostly used for streaming type applications, where if you lose some data you don't need to try to send it again.
Which one you use depends on the application. For example, a web server uses TCP.

### item Psoftwareengineering-316195-157526
THREAD A
Site: softwareengineering | Thread title: Should unit tests always overlap
[chunk 647421] It should be pointless. But you should be making sure handler calls what validator needs called.
For unit testing you should be testing in isolation. That means you'll need a stub (or mock) validator to hand to handler when you test handler. You don't check validator business logic when testing handler. You test that handler calls validator (in this case ValidatorStub) when, and with what, it should.

THREAD B
Site: softwareengineering | Thread title: Explanation on how "Tell, Don't Ask" is considered good OO
[chunk 583902] Asking the object about its state, and then calling methods on that object based on decisions made outside of the object, means that the object is now a leaky abstraction; some of its behavior is located outside of the object, and internal state is exposed (perhaps unnecessarily) to the outside world.
You should endeavor to tell objects what you want them to do; do not
ask them questions about their state, make a decision, and then tell
them what to do.

[chunk 583903] The problem is that, as the caller, you should not be making decisions
based on the state of the called object that result in you then
changing the state of the object. The logic you are implementing is
probably the called object’s responsibility, not yours. For you to
make decisions outside the object violates its encapsulation.

[chunk 583904] Sure, you may say, that’s obvious. I’d never write code like that.
Still, it’s very easy to get lulled into examining some referenced
object and then calling different methods based on the results. But
that may not be the best way to go about doing it. Tell the object
what you want. Let it figure out how to do it. Think declaratively
instead of procedurally!

[chunk 583905] It is easier to stay out of this trap if you start by designing
classes based on their responsibilities; you can then progress
naturally to specifying commands that the class may execute, as
opposed to queries that inform you as to the state of the object.
https://web.archive.org/web/20160204103129/https://pragprog.com/articles/tell-dont-ask

### item Pdba-13662-2918
THREAD A
Site: dba | Thread title: MariaDB XtraDB Performance Tuning
[chunk 719959] InnoDB in Percona Server 5.0.91 and MySQL 5.5.x has three options
innodb_read_io_threads
innodb_write_io_threads
innodb_io_capacity
These options were introduced in MySQL 5.1.38 InnoDB Plugin
Tuning these will engage more CPUs within InnoDB/XtraDB
I have discussed this in past posts in the DBA StackExchange along with other InnoDB tuning suggestions
Multi cores and MySQL Performance
About single threaded versus multithreaded databases performance
Possible to make MySQL use more than one core?

[chunk 719960] Query runs a long time in some newer MySQL versions
Click here for the XtraDB features that the InnoDB Plugin does not have.

THREAD B
Site: dba | Thread title: About single threaded versus multithreaded databases performance
[chunk 713751] Here is my opinion:

[chunk 713752] Usually the bottleneck (or slowest part) of a DB system is the disk. The CPU only spikes during arithmetic operations, processing, or any other task that the CPU does. With proper architecture, multithreading can help to offset the load of a query onto the CPU instead of doing the slow disk reads/writes. There are cases where it is faster to calculate a value using the CPU cycles rather than to create a computed column (that was previously saved to disk) and read this column from disk.

[chunk 713753] In some RDBMS there is a temporary DB (tempdb) that is used by all the DBs on that instance for sorting, hashing, temporary variables, etc... Multithreading and splitting up this tempdb files can be used to improve the throughput of the tempdb, thereby improving overall server performance.

[chunk 713754] Using multithreading (parallelism), the result set of a query can be split up to be processed on the different cores of the server, rather than using one core alone. This feature does not always improve the performance, but there are cases where it does, and hence the feature is available.
The threads available to the DB are used for many purposes: reading/writing to disk, user connections, background jobs, locking/latching, network IO, etc...

[chunk 713755] Depending on the OS architecture the threads are preemptively fed to the CPU and are managed using waits and queues.
If the CPU can crunch these threads pretty quickly then the wait times will be low.
A multi-threaded DB will be faster than a single-threaded DB, as in a single-threaded DB there will be the overhead of recycling only one thread rather than having other treads readily available.

[chunk 713756] Scalability also becomes an issue, as more threads will be required to manage and execute the scaled DB system.

### item Punix-251847-251726
THREAD A
Site: unix | Thread title: Clear to end of line uses the wrong background color in tmux
[chunk 380278] Unlike screen, tmux does not have switchable background colour erase capability in its terminal emulator. Erasure is always with the default background colour, never the current background colour.
Nicholas Marriott added it to the to-do list in September 2015, but stated at the time that neither he nor anyone else cares enough about it to implement it.
He later implemented it in October 2016, nearly a year after this answer was originally written.
Further reading

[chunk 380279] Nicholas Marriott (2015-09-15). Support background color erase (bce). tmux/tmux. Bug #109. GitHub.
Nicholas Marriott (2015-09-15). Add BCE to TODO.. tmux/tmux. 54bd7612868341c47bd3bd237c9598d5860b3ef3. GitHub.
vim colorscheme completely wrong inside screen or tmux sessions:
t_ut turns off BCE. tmux should support BCE but it depends on the tmux version, I think 2.1 is too old.

THREAD B
Site: unix | Thread title: Clear to end of line uses the wrong background color in screen
[chunk 380245] When you send one of the ECMA-48 erase control sequences, whether the erasure uses the current background colour or the default background colour varies amongst different terminal types.
(In the terminfo database, there is a capability that allows programs to determine what the terminal that they are talking to will do.
It is named bce.

[chunk 380246] The termcap equivalent name is ut.) You are setting the current background colour, and then erasing to the end of the line, expecting the erasure to always use that current colour.

[chunk 380247] screen is a terminal emulator itself. But unlike most hardware terminals its behaviour in this regard is switchable. By default, background colour erase is switched off, and the control sequence causes erasure with the default colour. One switches it on with the bce command. One sets the default for the bce setting in all new screens with the defbce command.
(I say most, because late model DEC VTs provide DEC Private Mode 117 for switching the behaviour.

[chunk 380248] The default for these terminals was the "new" PC-compatible behaviour of erasing with the current colour, and switching Private Mode 117 off would revert back to the "old" VT-compatible behaviour of erasing with the default colour.
DEC VT 52x terminals were switchable like screen, except that the host could do the switching and the default was the "new" behaviour, the opposite of screen's default.
These terminals were actually newer than screen, by several years.)

[chunk 380249] So switch it on. It's as simple as that.
Further reading
"Character Processing", Screen Users' Manual. GNU Project.
"DECECM". VT520/VT525 Video Terminal Programmer Information. EK-VT520-RM. July 1994. DEC.
https://unix.stackexchange.com/a/252078/5132

### item Pdba-144744-16725
THREAD A
Site: dba | Thread title: Joining Tables in the FROM vs. the WHERE clause
[chunk 777432] Both queries are exactly the same, should return exactly the same result set and should produce exactly the same Execution plan.
BUT the second query is using ANSI-92 SQL syntax . The first one is using the older (very old) version of SQL Joins.
I can think of a few reasons why you should use the ANSI-92 SQL Syntax.
It separates the Join Conditions and the actual filters in the WHERE clause if you have any.

[chunk 777433] With the old syntax, you can only have the equivalent of INNER and CROSS joins. Outer joins were not possible except with complicated UNION queries. Some DBMS had added proprietary syntaxes for outer joins, (+) in Oracle, *= and =* in SQL Server, but these are being or have been deprecated. The explicit LEFT, RIGHT and FULL outer joins were added in the standard and have been adopted from almost all DBMS.
It make query much more readable hence easier to debug.

[chunk 777434] Now days most of the developers, DBAs and also ORMs use the Join syntax.
When using ANSI-92 SQL Syntax for joins if you miss out a join condition you get a compile time error, hence it forces you to provide a valid join condition whereas in older version it doesn't throw any error but it simply returns a CROSS JOIN, in my experience this is one of the worst cons of the older approach.

[chunk 777435] When using older version of joins and your query is mixing inner join and outer joins the result set may always not what you expect it to be.

THREAD B
Site: dba | Thread title: SQL JOIN Syntax in MS SQL
[chunk 721779] Queries of the second type fall under what some call a SQL antipattern (check out the nice book written by Bill Karwin). The second query almost resembles a Cartesian JOIN whose WHERE clause has to be evaluated on the fly.
The first is cleaner and the order of execution can be better managed.
You could compare both ways by
getting the EXPLAIN plan for each and seeing if execution time is the same
creating a third type that refactors the query and get its EXPLAIN plan and running time

[chunk 721780] see if all indexes are being evaulated the same for the three query styles
You are better off going for the JOIN syntax because you can generate result sets with LEFT JOINs and RIGHT JOINs that may be far different from (maybe more desirable than) INNER JOINs.

### item Punix-580613-67678
THREAD A
Site: unix | Thread title: Mount a PV image as a readonly loop device (again - it used to work)
[chunk 473837] Below is a workaround: given LVM wants a read-write block device, we create one with an overlay block device based on the read-only block device (see this other question).
As root:
Create a sparse file with the same size as the read-only block device
truncate -s`blockdev --getsize64 /dev/loop1` '/tmp/overlay.bin'
(even if larger than the current filesystem)
Create the overlay block device

[chunk 473838] loop=`losetup -f --show -- '/tmp/overlay.bin'`
size=`blockdev --getsz /dev/loop1`
printf '%s\n' "0 $size snapshot /dev/loop1 $loop P 8" | dmsetup create 'overlayloop1'
To avoid LVM to complain about duplicate PV with the same UUID, edit /etc/lvm/lvm.conf to exclude the original /dev/loop1: either devices { scan = [ "/dev/mapper" ] } either devices { filter = [ "r|/dev/loop1|" ] } (see this FAQ on LVM wiki)
Now vgchange -a y fw works.

[chunk 473839] During the use, the file /tmp/overlay.bin should be monitored, although it should not increase particularly if the filesystem of the LV is mounted read-only.
To close the loop device:
vgchange -a n fw
dmsetup remove /dev/mapper/overlayloop1
rm /tmp/overlay.bin
losetup -d /dev/loop1

THREAD B
Site: unix | Thread title: GNU/Linux: overlay block device / stackable block device
[chunk 312594] You can do that with the device mapper and its snapshot target.
Basically, you'd do the same as what LVM does when you create a writable snapshot.
dev=/dev/read-only-device
ovl=/path/to/overlay.file
newdevname=newdevice
size=$(blockdev --getsz "$dev")
loop=$(losetup -f --show -- "$ovl")
printf '%s\n' "0 $size snapshot $dev $loop P 8" |
 dmsetup create "$newdevname"
Then you can access the overlayed device as /dev/mapper/newdevice.

[chunk 312595] If you also need access to the original device at the same time, you can do:
printf '%s\n' "0 $size snapshot-origin $dev" |
 dmsetup create originaldevice
And access it over /dev/mapper/originaldevice.
You can write to that device, then in addition to the chunks written to the snapshot device, the overlay file will contain a copy of the chunks that have been overwritten when writing to the snapshot-origin.

[chunk 312596] The overlay file can be a sparse file. (for instance, create it as truncate -s10G the-file), and doesn't have to be as large as the original device. You can tell how full it is with dmsetup status "$newdevname".
Note: There are size and contents reqirements on a snapshot device.