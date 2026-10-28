### item Punix-334364-21638
THREAD A
Site: unix | Thread title: Why does "ls .*" show the contents of hidden directories?
[chunk 404870] Short answer: shell glob expansion.
The shell takes your input and expands the .* part before passing it to ls, so effectively you're doing:
$ ls .bash_history .bash_profile .bashrc .coin_history .emacs ...
So it lists each entry. When it sees a directory entry, it lists the contents of that directory, just as you would expect ls to do. To see only the files/directories in your working directory, use the -d option to ls:
$ ls -d .*

[chunk 404871] The -d option tells ls to "list directories themselves, not their contents" (taken from the lsman page).

THREAD B
Site: unix | Thread title: Show only hidden files (dot files) in ls alias
[chunk 292476] Either make the inner pair of quotes double quotes:
alias hidden='ls -a | grep "^\."'
Or make the outer pair of quotes double quotes:
alias hidden="ls -a | grep '^\.'"
Or make all quotes double quotes and escape the inner pair:
alias hidden="ls -a | grep \"^\.\""
Or make it a function, so you can pass some arguments when calling:
hidden() { ls -a "$@" | grep '^\.'; }

### item Punix-405798-158289
THREAD A
Site: unix | Thread title: Quickest way to find the largest file in a directory and subdirectories
[chunk 425621] GNU find + sort + head solution (for any directory depth level), assuming file paths don't contain newline characters:
find . -type f -printf "%s %p\n" | sort -nr | head -1
%s - format specificator pointing to file size (in bytes)
%p - format specificator pointing to file name
sort -nr - sort records numerically in reversed order
head -1 - print the TOP first line/record
To get a human-readable file size value - extend the pipeline with GNU numfmt command (if supported):

[chunk 425622] find . -type f -printf "%s %p\n" | sort -nr | head -1 | numfmt --to=si

THREAD B
Site: unix | Thread title: Finding largest file recursively
[chunk 349319] use find (here assuming GNU find) to output file names with the file size. sort. print out the largest one.
find . -type f -printf "%s\t%p\n" | sort -n | tail -1
That assumes file paths don't contain newline characters.
Using a loop in bash with the GNU implementation of stat:
shopt -s globstar
max_s=0
for f in **; do
 if [[ -f "$f" && ! -L "$f" ]]; then
 size=$( stat -c %s -- "$f" )
 if (( size > max_s )); then
 max_s=$size
 max_f=$f
 fi
 fi
done
echo "$max_s $max_f"

[chunk 349320] This will be significantly slower than the find solution. That also assumes that file names don't end in newline characters and will skip hidden files and not descend into hidden directories.
If there's a file called - in the current directory, the size of the file open on stdin will be considered.
Beware that versions of bash prior to 4.3 followed symbolic links when descending the directory tree.

### item Punix-338945-48805
THREAD A
Site: unix | Thread title: Are `if` and `then` actually programs
[chunk 406305] The ; separates statements (loosely speaking). It is (almost) always possible to replace a ; by a newline.
To say that ; separates two programs, therefore if and then must be "programs" is a bit too simplistic as a statement may be made of reserved words, shell functions, built-in utilities and external utilities, and combinations of these using pipes and boolean operators etc. etc.

[chunk 406306] Both if and then are reserved words in the shell grammar, not "programs". Here they are used to build up what's technically called a compound command.
echo is likely a built-in utility in the shell (but doesn't need to be), and ls is probably an external utility (or "program" as you say).

THREAD B
Site: unix | Thread title: Semicolon in conditional structures
[chunk 305455] The semicolon is needed only when the end of line is missing:
if [ "a" == "a" ] ; then echo "true" ; fi
Without semicolons, you get Syntax error.
I do not understand your question about quotes. Can you be more specific?
(And by the way, using = instead of == is more portable and POSIX compliant).

### item Punix-299618-182882
THREAD A
Site: unix | Thread title: An official standard / convention for a file extension for shell scripts to source
[chunk 395032] I'd use .sh (for files in the POSIX sh language, .bash for non-sh-compatible bash files, that is the extension identifies the language the script is written in) for files intended to be sourced (or more generally not intended to be executed), and no extension for files that are meant to be executed.
You can also add a:
#! /bin/echo Please-source

[chunk 395033] she-bang, so that when executed by mistake (though I'd expect those files should not be given execution permissions, which would already prevent execution), you get a notice that it should be sourced instead.

THREAD B
Site: unix | Thread title: Use .sh or .bash extension for Bash scripts?
[chunk 357547] does using the .bash extension actually invoke bash or does it depend
on system config / 1st shebang line.
If you do not use an interpreter explicitly, then the interpreter being invoked is determined by the "shebang" used in the script (the #!-line, which must be the first line of the script file).

[chunk 357548] On the other hand, if you use an interpreter explicitly, then the interpreter doesn't care what extension you gave your script. However, the extension exists to make it very obvious for others what kind of script it is.
[sreeraj@server ~]$ cat ./ext.py
#!/bin/bash
echo "Hi. I am a Bash script"
See, the .py extension to the Bash script does not make it a Python script.
[sreeraj@server ~]$ python ./ext.py
 File "./ext.py", line 2
 echo "Hi. I am a Bash script"
 ^
SyntaxError: invalid syntax

[chunk 357549] It's always a Bash script.
[sreeraj@server ~]$ ./ext.py
Hi. I am a Bash script

### item Psecurity-4574-3390
THREAD A
Site: security | Thread title: Why is it always `HASH( salt + password )` that we recommend?
[chunk 847629] Actually, "we" are not recommending any of what you show. The usual recommendations are PBKDF2, bcrypt or the SHA-2 based Unix crypt currently used in Linux.
If the hash function you use is a perfect random oracle then it does not really matter which way you input the salt and the password; only matters the time it takes to process the salt and password, and we want that time to be long, so as to deter dictionary searches; hence the use of multiple iterations.

[chunk 847630] However, being a perfect random oracle is a difficult property for a hash function; it is not implied by the usual security properties that secure hash functions must provide (resistance to collisions and to preimages) and it is known that some widely used hash functions are not random oracles; e.g.
the SHA-2 functions suffer from the so-called "length extension attack", which does not make them less secure, but implies some care when using the function in funky password-hashing schemes.

[chunk 847631] PBKDF2 is often used with HMAC for that reason.
You are warmly encouraged not to feel creative with password hashing schemes or cryptography in general. Security relies on details which are subtle and which you cannot test by yourself (during tests, an insecure function works just as well than a secure one).

THREAD B
Site: security | Thread title: Stretching a hash, many iterations versus longer input string
[chunk 846500] The main reason why concatenating the salt and password many times is not used is a combination of tradition and laziness.
Namely, since password size is not fixed, the number of copies would have to be adjusted so that the "much longer string" size reaches a given goal.

[chunk 846501] It seems that some initial implementers of such schemes found it cumbersome, possibly because it implies using a "streamed" hash function implementation (which accepts data by successive chunks) instead of a one-function-call implementation.
Most ulterior designers simply copied the previous designs for no real good (neither bad) reason.

[chunk 846502] On a theoretical point of view, multiple concatenations of the salt and password are better, because multiple iterations reduce the space of possible hash values (a hash function is not a permutation). But the reduction does not go below a 2128 space of a 256-bit hash function, so no worry here.

### item Psecurity-91109-8303
THREAD A
Site: security | Thread title: What do I do if I find XSS on my website?
[chunk 895833] What should I do to mitigate the damage?
Usually, it is the user's browser that is compromised by XSS vulnerabilities on web sites. You probably won't see any damage done to your site, especially since it was reflected XSS. The attacker would need to target each user separately and convince them to click a malicious link in an email or visit a malicious domain that could launch the attack.

[chunk 895834] That said, reflected XSS is sneaky and can be combined with other attacks (like CSRF) and that CAN damage a web site. Let's say I achieve a reflected XSS attack where it rewrites all the links on the page to links that can change things on your site. For example, rewrite links to www.example.com/records?record_id=3&action=delete. Now you have a script that can delete records under the authority of whatever user has had their browser compromised by XSS.

[chunk 895835] I don't believe too many web site owners do a lot of investigation when they find and fix an XSS problem unless there is evidence of an actual exploit.
How to Find out What was Compromised:
If your application writes detailed logs, you might have records of http requests with malicious scripts in the parameters.
If any users have complained that that their stuff has been altered or deleted without their consent, that might also be a clue that someone has taken advantage of the XSS.

[chunk 895836] For more information, please describe what your web application does and what technologies it uses. You could even post a link to it if you don't mind the attention. That would give the people here more to go on.

THREAD B
Site: security | Thread title: How serious are XSS attacks
[chunk 850758] Anything you can do with javascript as the site owner can be done with an XSS attack. That includes modifying the DOM. You could replace an entire page and thus have control of all data into and out of the website. Relatively simple scripts can read cookies and forward session information. That would be like Firesheep at a distance -- impersonating a user by grabbing their access credentials.
Further, this may introduce visitors to your site any sort of attack that affects browsers.

### item Pserverfault-326493-326837
THREAD A
Site: serverfault | Thread title: Basic iptables NAT port forwarding
[chunk 104528] PC ----- Ubuntu 10 Server ----- Slashdot 
(1.2.3.4) (5.6.7.8) (216.34.181.45)
Enable the IP forwarding on Ubuntu:
echo 1 > /proc/sys/net/ipv4/ip_forward
and add the following rules:
iptables -t nat -A PREROUTING -i eth0 -p tcp -m tcp --dport 8080 -j DNAT \
 --to-destination 216.34.181.45:80 
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 5.6.7.8
No.
You should use MASQUERADE if the Ubuntu has a dynamic IP:
iptables -t nat -A POSTROUTING -j MASQUERADE

[chunk 104529] You can also use SSH local port forwarding in this case by executing the below command on the Ubuntu:
$ ssh -L 5.6.7.8:8080:216.34.181.45:80 -N user@216.34.181.45
There's still another (or more) way to do this. Take a look at the rinetd:

[chunk 104530] Name : rinetd
Arch : i386
Version : 0.62
Release : 6.el5.art
Size : 41 k
Repo : installed
Summary : TCP redirection server
URL : http://www.boutell.com/rinetd
License : GPL
Description: rinetd is a daemon which redirects TCP connections from one IP address
 : and port to another IP address and port. This daemon is often used to
 : access services behind a firewall.
The configuration is very simple. Add the belows line into /etc/rinetd.conf:
5.6.7.8 8080 216.34.181.45 80
and start:

[chunk 104531] # /etc/init.d/rinetd start
Starting rinetd: [ OK ]
It will do everything for you.

THREAD B
Site: serverfault | Thread title: iptables NAT port fowarding and Apache log IPs
[chunk 104623] You need a Layer 4 device (such as squid, apache in proxy mode, or a dedicated load balancer such as an F5 or Netscaler) if you want information about the original host making the request. If you do a straight NAT translation, then all requests will appear (correctly) to be from the host with the public IP address that is connecting to the server.

[chunk 104624] A Layer 4 device or server can add either a Via:, X-Forwarded-For:, or other arbitrary header to the HTTP request to the server. The server can then (if it desires) use that information about the original client. Netscaler(Citrix) publishes an Apache plugin which allows you to rewrite the apache request with the value of said arbitrary HTTP header, for example.

[chunk 104625] See http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html for more information about the Via: header and what actual information is attached.

### item Punix-524254-39291
THREAD A
Site: unix | Thread title: Why are backslashes included in this shell script?
[chunk 459778] Backslash will suppress alias expansion, ie it executes the original command and makes sure that alias version does not run. Scripts can unknowingly run with alias expansion when the system has set shopt -s expand_aliases (BASH only) or if it is executed using source.
./conda.sh # usually no alias expansion (unless `shopt -s expand_aliases` in BASH)
source ./conda.sh # alias expansion
. ./conda.sh # alias expansion

[chunk 459779] Some sysadmins like to put backslash in everything as a preventive measure against side-effects of aliases, just in case it was aliased unintentionally somewhere else and the alias gets expanded as explained previously. For example, if the system has set this alias dirname='dirname -z' somewhere and the condition allows the alias to be expanded, then a script that tries to call dirname will unfortunately call dirname -z instead, which was not the script intended.

[chunk 459780] If there's certainty that such alias do not exist, we can remove all the backslash and it should work fine.
Alternatively, one can use command instead of backslash version to suppress alias. Thus, instead of \dirname, one can use command dirname, which might look more readable. (For built-in commands like cd, one should use builtin instead). I prefer this instead, as it also bypasses function with same name as well as any aliases.

THREAD B
Site: unix | Thread title: Run a command that is shadowed by an alias
[chunk 300847] You can also prefix a back slash to disable the alias: \ls
Edit: Other ways of doing the same include:
Use "command": command ls as per Mikel.
Use the full path: /bin/ls as per uther.
Quote the command: "ls" or 'ls' as per Mikel comment.
You can remove the alias temporarily for that terminal session with unalias command_name.

### item Pserverfault-905093-233962
THREAD A
Site: serverfault | Thread title: "Server refused to allocate pty" - how to mount devpts automatically?
[chunk 238133] The /dev/pts filesystem is usually mounted by the initrd (a.k.a. initramfs) in Ubuntu.
The initramfs is a small filesystem that is loaded in memory when the kernel boots and sets up the system to switch into the real root filesystem, after setting up the basics and loading any kernel drivers needed to mount the real root.
You can find it under /boot, named initrd.img-* where the last part matches the kernel version.
It's an xz-compressed cpio archive.

[chunk 238134] You can look inside the "init" script that is first run when it's mounted by using the following command. The "grep" at the end of it looks at the line that mounts devpts:
$ xz -dc /boot/initrd.img-$(uname -r) | cpio -i --quiet --to-stdout init | grep devpts
mount -t devpts -o noexec,nosuid,gid=5,mode=0620 devpts /dev/pts || true

[chunk 238135] That devpts is actually mounted in the root of the initramfs, so later on there's another step that moves it to the real root before switching to it. You can look at it here:
$ xz -dc /boot/initrd.img-$(uname -r) | cpio -i --quiet --to-stdout scripts/init-bottom/udev | grep move
# move the /dev tmpfs to the rootfs
mount -n -o move /dev ${rootmnt}/dev
If you want to extract the whole contents of the initrd, you can use:

[chunk 238136] # First go to an empty directory
$ mkdir -p /tmp/extract_initrd
$ cd /tmp/extract_initrd
$ xz -dc /boot/initrd.img-$(uname -r) | cpio -id
And then explore that tree...
If it seems something is wrong with your initramfs, you can try to re-generate it using the update-initramfs command, like so:
$ sudo update-initramfs -c -k $(uname -r)
Watch out for any errors in the output of this command, they might give you a clue of something that might be going wrong...

[chunk 238137] Another possibility is to enable debug logging in the initrd. To do that, add "debug" to the kernel command-line and reboot. Then look at the file /run/initramfs/initramfs.debug after the system boots, that will contain the messages printed by the initrd scripts. See here for more details on initramfs debugging.

THREAD B
Site: serverfault | Thread title: Failing to connect to server via SSH - "Server refused to allocate pty"
[chunk 77441] Did you tried to re-create pty and tty devices ?
root@mydomain.de:~# /sbin/MAKEDEV tty
root@mydomain.de:~# /sbin/MAKEDEV pty
It seems to be a known issue on virtual servers...
If you don't have access to any shell, you could try sending the command via ssh :
florian@localmachine:~$ ssh root@mydomain.de "/sbin/MAKEDEV tty"
florian@localmachine:~$ ssh root@mydomain.de "/sbin/MAKEDEV pty"
Edited to reflect your comment :
If you use a chroot, you also have to mount /proc, /dev and /sys :

[chunk 77442] root@h1696522:/# mount -o bind /proc /repair/proc
root@h1696522:/# mount -o bind /dev /repair/dev
root@h1696522:/# mount -o bind /sys /repair/sys
It should work now.

### item Punix-513926-164987
THREAD A
Site: unix | Thread title: What controls the buffering of stdout stderr?
[chunk 457189] Your programming language
This behaviour is an artefact of the C runtime library, and a requirement of the C programming language. Other programming languages have historically been built on top of the C runtime library, and gain this behaviour from it. This is true for C++ programs, for example. Chapter and verse of the C and C++ language standards is quoted fairly often over on Stack Overflow (q.v.).

[chunk 457190] Most notably, programs written in Python have the same behaviour, and are asked about fairly frequently, sometimes with the blame for the behaviour of the programming language runtime being wildly mis-placed.

[chunk 457191] Tools to change this behaviour of programs which use the default language semantics (without modifying and recompiling the programs) come in two forms: language-dependent (and sometimes runtime-library-specific) tools that insert themselves into the runtime and change the buffering, and tools that make standard I/O into files that the runtime libraries decide to be interactive devices. Tools in the latter class are language-independent and include Bernstein ptybandage.
Further reading

[chunk 457192] https://unix.stackexchange.com/a/407472/5132
https://unix.stackexchange.com/a/249801/5132
http://git.musl-libc.org/cgit/musl/tree/src/stdio/__stdout_write.c#n8
Just a few instances of the buffering question:
Write Python stdout to file immediately
Getting systemd service logs faster from my service
Systemd Python service not sending all output to syslog
Output of a python script running as unit is out of order while shells seems unnafected

[chunk 457193] Daemontools multilog loses log line time information. How to fix it?
stderr gets flushed before stdout, when using file logger
Output of a python script running as unit is out of order while shells seems unnafected
systemd: process with fork() only shows logs after child exits

THREAD B
Site: unix | Thread title: Output of a python script running as unit is out of order while shells seems unnafected
[chunk 351450] Stdout is being buffered, probably because of systemd redirect
Adding sys.stdout.flush() after write or PYTHONUNBUFFERED environment will solve this problem
See also the Stack Overflow question Python output buffering.

### item Punix-372627-38205
THREAD A
Site: unix | Thread title: Is it possible to pass environment variables from child to parent in user space?
[chunk 415866] No, it's not possible
Not without some kind of workaround.
Environment variables can only be passed from parent to child (as part of environment export/inheritance), not the other way around.

THREAD B
Site: unix | Thread title: change environment of a running process
[chunk 300274] You can't do this without a nasty hacks - there's no API for this, no way to notify the process that its environment has changed (since that's not really possible anyway).
Even if you do manage to do that, there is no way to be sure that it will have any effect - the process could very well have cached the environment variable you're trying to poke (since nothing is supposed to be able to change it).

[chunk 300275] If you really do want to do this, and are prepared to pick up the pieces if things go wrong, you can use a debugger. See for instance this Stack Overflow question:
Is there a way to change another process's environment variables?
Essentially:
(gdb) attach process_id
(gdb) call putenv ("DISPLAY=your.new:value")
(gdb) detach
Other possible functions you could try to call are setenv or unsetenv.

[chunk 300276] Please do really keep in mind that this may not work, or have dire consequences if the process you target does "interesting" things with its environment block. Do test it out on non-critical processes first, but make sure these test processes mirror as close as possible the one you're trying to poke.

### item Punix-231530-13349
THREAD A
Site: unix | Thread title: Comparing directories using diff
[chunk 373715] There's a limit to how much portable code you can write without having conditionals to execute different things on different systems. Don't feel bad about using dircmp if available or GNU diff if available.
if type dircmp >/dev/null 2>/dev/null; then
 dircmp dir1 dir2
else
 diff -r dir1 dir2
fi

[chunk 373716] If you only want to know which files have changed and you don't care about listing contents, you can filter the diff output to retain only header lines. (Warning: if you have file names with newlines, the output may be unparseable.)
diff -r dir1 dir2 | grep -v '^[<>0-9]'
Make that grep -v '[^<>]' to keep information about the range of changed lines, but still filter out the content of the changed lines.

THREAD B
Site: unix | Thread title: Directory "diff"?
[chunk 287784] You should use rsync instead. Something like rsync -rv $old/ $new/ should do the trick: this will print the files it's going to copy over.
Run with additional -n for a dry-run before actually modifying the new directory.

### item Psoftwareengineering-190090-190120
THREAD A
Site: softwareengineering | Thread title: When to use DI and when to create yourself in Java
[chunk 597690] In .Net (which is similar in this regard that everything is an object), I use DI mostly with my domain objects (entities, repositories and services) and application objects (controllers, view models), so repos/services get injected into controller/view models and similar. This means my business and application logic is fully testable, which is the primary reason I use DI.

[chunk 597691] Basically the objects that you inject and inject stuff into, are mostly objects that are specific to the solution you are building.
If some object is "native" to the language or framework (like .Net), there's probably no need to inject it.
A lot of objects need string to represent data, and a string is basically a "language feature" that is not specific to your domain.

[chunk 597692] The same thing applies to enumerables, lists, arrays and a whole lot of other stuff that does not need to change when you want to run your class in isolation from the rest of the system.

[chunk 597693] The most important thing to look at is coupling between your domain/application classes. If an object does not introduce tight coupling, then it's usually safe to just create it.
One of the ways to check for coupling is to try to run the methods in a class in isolation (which is basically unit testing). What needs to be DI-ed are all dependencies that you need to mock out, in order to make sure that the class you're testing is really running in isolation from the system.

THREAD B
Site: softwareengineering | Thread title: Should I use Dependency Injection or static factories?
[chunk 597736] Use dependency injection, but whenever your constructor argument lists become too big, refactor it using a Facade Service. The idea is to group some of the constructor arguments together, introducing a new abstraction.
For example, you could introduce a new type SessionEnvironment encapsulating a DBSessionProvider, the UserSession and the loaded Descriptions. To know which abstractions make sense most, however, one has to know the details of your program.

[chunk 597737] A similar question was already asked here on SO.

### item Pserverfault-631771-631257
THREAD A
Site: serverfault | Thread title: Why are some CentOS 5 boxes still vulnerable to ShellShock after upgrading Bash?
[chunk 183321] Could be a false positive - Make sure the 'echo' file does not exist from an earlier test on your bad machine, then retest.
Failing that, could also be a false negative - Check you can touch a file on your good machine, then retest.

THREAD B
Site: serverfault | Thread title: How to test if my server is vulnerable to the ShellShock bug?
[chunk 183239] To check for the CVE-2014-6271 vulnerability
env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
it should NOT echo back the word vulnerable.
To check for the CVE-2014-7169 vulnerability
(warning: if yours fails it will make or overwrite a file called /tmp/echo that you can delete after, and need to delete before testing again )
cd /tmp; env X='() { (a)=>\' bash -c "echo date"; cat echo

[chunk 183240] it should say the word date then complain with a message like cat: echo: No such file or directory. If instead it tells you what the current datetime is then your system is vulnerable.
To check for CVE-2014-7186
bash -c 'true <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF' || echo "CVE-2014-7186 vulnerable, redir_stack"
it should NOT echo back the text CVE-2014-7186 vulnerable, redir_stack.
To check for CVE-2014-7187

[chunk 183241] (for x in {1..200} ; do echo "for x$x in ; do :"; done; for x in {1..200} ; do echo done ; done) | bash || echo "CVE-2014-7187 vulnerable, word_lineno"
it should NOT echo back the text CVE-2014-7187 vulnerable, word_lineno.
To check for CVE-2014-6277. I'm not 100% sure on this one as it seems to rely on a partially patched system that I no longer have access to.
env HTTP_COOKIE="() { x() { _; }; x() { _; } <<`perl -e '{print "A"x1000}'`; }" bash -c "echo testing CVE-2014-6277"

[chunk 183242] A pass result on this one is it ONLY echoing back the text testing CVE-2014-6277. If it runs perl or if it complains that perl is not installed that is definitely a fail. I'm not sure on any other failure characteristics as I no longer have any unpatched systems.
To check for CVE-2014-6278. Again, I'm not 100% sure on if this test as I no longer have any unpatched systems.
env HTTP_COOKIE='() { _; } >_[$($())] { echo hi mom; id; }' bash -c "echo testing CVE-2014-6278"

[chunk 183243] A pass for this test is that it should ONLY echo back the text testing CVE-2014-6278. If yours echoes back hi mom anywhere that is definitely a fail.

### item Punix-118244-94041
THREAD A
Site: unix | Thread title: Fastest way to concatenate files
[chunk 333888] Nope, cat is surely the best way to do this. Why use python when there is a program already written in C for this purpose? However, you might want to consider using xargs in case the command line length exceeds ARG_MAX and you need more than one cat. Using GNU tools, this is equivalent to what you already have:
find . -maxdepth 1 -type f -name 'input_file*' -print0 |
 sort -z |
 xargs -0 cat -- >>out

THREAD B
Site: unix | Thread title: A virtual file containing the concatenation of other files
[chunk 324319] On Linux-based operating systems, that can be done with network block devices or device mapper devices. The file you obtain is a block device.
With nbd:
ln -s /path/to/first-file file.0
...
ln -s /path/to/last-file file.19
nbd-server -C /dev/null -m 127.0.0.1:12345 file
sudo nbd-client localhost 12345 /dev/nbd0
(the concatenation is /dev/nbd0).
With device mapper (file sizes have to be multiple of 512):

[chunk 324320] sudo losetup /dev/loop0 file1
sudo losetup /dev/loop1 file2
s0=$(sudo blockdev --getsize /dev/loop0)
s1=$(sudo blockdev --getsize /dev/loop1)
printf '%s\n' "0 $s0 linear /dev/loop0 0" "$s0 $s1 linear /dev/loop1 0" |
 sudo dmsetup create mybundle
(the concatenation is /dev/mapper/mybundle).

### item Psecurity-82057-51648
THREAD A
Site: security | Thread title: Is it secure to have source code for website public?
[chunk 891578] If your website is secure, even the source code wouldn't help an attacker in a perfect world. But we do not live in this world.
By making the source code public you are simultaneously holding yourself to a higher standard coding wise, and introducing more risk. Since you're giving away your code to anybody who asks, you'd better make it rock-solid. (In fact, you should be doing this anyway, but I'm sure you know that!)

[chunk 891579] Releasing your source will allow for good, helpful people to point out bad things, and it gives a motivation for you to write solid code at all times. I'd say it's a good idea. However, you should talk about the risk with the website owner. Private repos do exist on GitHub and you can stand up your own Git server/local Git repo for private version control.
Suggested Reading:
Pros and Cons of Open Source implementation
Kerckhoffs's principle

THREAD B
Site: security | Thread title: Security related code in Open Source projects?
[chunk 877655] I have recently heard that most of the PHP code is confidential, because if attackers know your database structure or the hash function used to encrypt the passwords, there is higher chances of a breach.

[chunk 877656] That's only when designers don't use the correct hash function or protect the webapp from SQL injection. But these things can be easily detected, there eve are automated tools these days that can look for SQL injection vulnerabilities via the source code (instead of pointing sqlmap at the webapp)
If you use something like scrypt, you're perfectly safe in telling everyone that you use it.

[chunk 877657] MediaWiki used to use a salted MD5 hash. The salt is installation specific and not part of the open source code (it gets generated on install). This isn't as secure as it can be (per-user salts and using a better hashing algorithm would be better), but it's still secure as long as the LocalSettings file isn't exposed. (Admittedly, that's not a great level of security). I think Drupal does this too, but with sha512.

[chunk 877658] I was wondering, if it's so, then what about open source projects where everything is wide out in the open?
Security by obscurity is not security. If putting the code out in the open impacts security, then you don't have any security in the first place.
Besides, if there are security holes in the code, these get caught by contributors too. I recently caught and patched a security-related bug in the Bugzilla software, for example.

### item Punix-160527-115631
THREAD A
Site: unix | Thread title: Is there a way to prevent git from changing permissions and ownership on pull?
[chunk 350187] This sounds like the user you're running has the default group set to yuri. You can confirm this like so:
$ id -a
uid=1000(saml) gid=1000(saml) groups=1000(saml),10(wheel),989(wireshark)
The UID of your account is this: uid=1000(saml) whereas the default group is git=1000(saml) and any secondary groups are thereafter.
NOTE: If you want the git clone to have specific ownership, then you have at least 2 options.
Option #1
Set a parent directory with the permissions as you want like so:

[chunk 350188] $ mkdir topdir
$ chgrp http topdir
$ chmod g+s topdir
$ cd topdir
$ git clone ....
This forced the directory topdir to enforce any child directories underneath it to have the group http applied. This will work by in large but can lead to problems, since if you move files into this git clone workspace, those files will not have their groups enforced by the changes made above.
Option #2
Prior to doing work, change your default group to http like so:
$ newgrp http
$ git clone ...

[chunk 350189] This method will force any new files created to have their group set to http instead of your normal default group of yuri, but this will only work so long as you remember to do a newgrp prior to working in this workspace.
Other options
If neither of these seem acceptable you can try using ACLs instead on the git workspace directory. These are discussed in multiple Q&A's on this site, such as in this Q&A titled: Getting new files to inherit group permissions on Linux.

THREAD B
Site: unix | Thread title: Getting new files to inherit group permissions on Linux
[chunk 332626] It sounds like you're describing the setgid bit functionality where when a directory that has it set, will force any new files created within it to have their group set to the same group that's set on the parent directory.
Example
$ whoami
saml
$ groups
saml wheel wireshark
setup a directory with perms + ownerships
$ sudo mkdir --mode=u+rwx,g+rs,g-w,o-rwx somedir
$ sudo chown saml.apache somedir
$ ll -d somedir/
drwxr-s---. 2 saml apache 4096 Feb 17 20:10 somedir/

[chunk 332627] touch a file as saml in this dir
$ whoami
saml
$ touch somedir/afile
$ ll somedir/afile 
-rw-rw-r--. 1 saml apache 0 Feb 17 20:11 somedir/afile
This will give you approximately what it sounds like you want. If you truly want exactly what you've described though, I think you'll need to resort to Access Control Lists functionality to get that (ACLs).
ACLs

[chunk 332628] If you want to get a bit more control over the permissions on the files that get created under the directory, somedir, you can add the following ACL rule to set the default permissions like so.
before
$ ll -d somedir
drwxr-s---. 2 saml apache 4096 Feb 17 20:46 somedir
set permissions
$ sudo setfacl -Rdm g:apache:rx somedir
$ ll -d somedir/
drwxr-s---+ 2 saml apache 4096 Feb 17 20:46 somedir/
Notice the + at the end, that means this directory has ACLs applied to it.

[chunk 332629] $ getfacl somedir
# file: somedir
# owner: saml
# group: apache
# flags: -s-
user::rwx
group::r-x
other::---
default:user::rwx
default:group::r-x
default:group:apache:r-x
default:mask::r-x
default:other::---
after
$ touch somedir/afile
$ ll somedir/afile 
-rw-r-----+ 1 saml apache 0 Feb 17 21:27 somedir/afile
$
$ getfacl somedir/afile
# file: somedir/afile
# owner: saml
# group: apache
user::rw-
group::r-x #effective:r--
group:apache:r-x #effective:r--
mask::r--
other::---

[chunk 332630] Notice with the default permissions (setfacl -Rdm) set so that the permissions are (r-x) by default (g:apache:rx). This forces any new files to only have their r bit enabled.

### item Psecurity-139738-136900
THREAD A
Site: security | Thread title: Company can tell if new and old passwords are too similar. Is there a security problem?
[chunk 918407] Usually, when users change their password on a system, they're required to input their old password as well, along with the new password.
Now, this old password is hashed and checked against the hash stored in the machine(password is not stored in cleartext). If the hashes match, then the system proceeds to compare the old password and new password. If it finds that the 2 passwords are too similar, then it throws an error, informing the user about the same.

[chunk 918408] In case the passwords are sufficiently different according to the system logic, then the new password is hashed and this new hash value is stored in the system, hence successfully changing the user's password.
In case the users are NOT required to input their old password, I'd recommend you better check with your IT support team, and raise a concern with the system owner...

[chunk 918409] UPDATE:
As pointed out in the comments, there's one more way to get around this issue without asking for user's old password. When the user enters the new password, the system generates the variations of the new password entered, hashes each one of them, and compares each hash against the old password's hash. If any of the hash matches, it throws an error. Else, it successfully changes the password.

THREAD B
Site: security | Thread title: Can one tell if a password guess was close by the hash result?
[chunk 916940] No, you cannot determine how close you guessed looking at the hash. A hash function is designed with this in mind: one single changed bit on the input must change a lot of bits on the output. Its called Avalanche Effect.
Bellow are SHA1 hashes for some of your example passwords:
cbfdac6008f9cab4083784cbd1874f76618d2a97 - password123
b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb1 - Password123
2b4bfcc447c3c8726d26c22927a68f511d5e01cc - password124

[chunk 916941] 115b55dcc1cd9a0dfdd60c120e83eaf658c45fc6 - right horse battery staple
abf7aad6438836dbe526aa231abde2d0eef74d42 - correct horse battery staple
A single bit change will completely change the hashing result. In fact, in an ideal case for every bit of input change every bit of output will be changed with a 50% probability.

### item Punix-394015-170493
THREAD A
Site: unix | Thread title: Confused about the meaning of an interactive and non-interactive shell when running a script
[chunk 421686] A shell running a script is a non-interactive shell.
A non-interactive shell can still use e.g. read to read data from standard input.
If standard input is a terminal, this may provide a level of "interaction", but it does not make the shell executing the script an interactive shell. Thu script will be "interactive" though.
The text is confusing because it uses the word "interactive" to mean two things:

[chunk 421687] A shell that was started in order to execute a shell script is non-interactive (in the sense that it does not have job control, it does not provide a prompt by itself by default etc. etc.). This is a technical term for the type of a shell, just like "login shell" and "interactive shell".

[chunk 421688] The action of acquiring data by this same script may be "interactive" (if not reading from e.g. a pipe or a file). But then again, any command that takes data from standard input may be said to be interactive. tr 'a-z' 'A-Z' will, by itself, "interactively" turn all lowercase ASCII characters to uppercase.

THREAD B
Site: unix | Thread title: login/non-login and interactive/non-interactive shells
[chunk 353429] login shell: A login shell logs you into the system as a specific user. Necessary for this is a username and password. When you hit ctrl+alt+F1 to login into a virtual terminal you get after successful login: a login shell (that is interactive). Sourced files:
/etc/profile and ~/.profile for Bourne compatible shells (and /etc/profile.d/*)
~/.bash_profile for bash
/etc/zprofile and ~/.zprofile for zsh
/etc/csh.login and ~/.login for csh

[chunk 353430] non-login shell: A shell that is executed without logging in. Necessary for this is a current logged in user. When you open a graphic terminal in gnome, it is a non-login (interactive) shell. Sourced files:
/etc/bashrc and ~/.bashrc for bash
interactive shell: A shell (login or non-login) where you can interactively type or interrupt commands, for example, a gnome terminal (non-login) or a virtual terminal (login). In an interactive shell the prompt variable must be set ($PS1). Sourced files:

[chunk 353431] /etc/profile and ~/.profile
/etc/bashrc or /etc/bash.bashrc for bash
non-interactive shell: A (sub)shell that is probably run from an automated process. You will see neither input nor output when the calling process doesn't handle it. That shell is normally a non-login shell, because the calling user has logged in already. A shell running a script is always a non-interactive shell, but the script can emulate an interactive shell by prompting the user to input values. Sourced files:

[chunk 353432] /etc/bashrc or /etc/bash.bashrc for bash (but, mostly you see this at the beginning of the script: [ -z "$PS1" ] && return. That means don't do anything if it's a non-interactive shell).
depending on shell; some of them read the file in the $ENV variable.

### item Pdba-15030-3375
THREAD A
Site: dba | Thread title: MySql recommended hardware
[chunk 720750] You should invest in both.
As for MySQL, if you are using InnoDB as your default storage engine, you must upgrade to MySQL 5.5 in order to use more cores. Here are some of my past posts on this subject
Multi cores and MySQL Performance
Possible to make MySQL use more than one core?
About single threaded versus multithreaded databases performance
16 Cores 12 GB RAM server MySql Configuration - my.cnf

[chunk 720751] As a point of reference, I have a client at my employer's web hosting company that has three DB Servers in Circular Replication. Each DB server has the following:
MySQL 5.5.9
192 GB RAM
162 GB InnoDB Buffer Pool
dual hexacore (that's right, 12 CPUs)
1.8TB Disk Volume
978 multitenant databases
892 GB of InnoDB Data
innodb_file_per_table enabled

[chunk 720752] They have had this setup for a whole year. I personally configured my.cnf for multicore engagement. All 12 CPUs are in use. The InnoDB Buffer Pool is full to capacity. There have been no complaints from the client on the DB Performance since this layout was setup for them.
Tuning InnoDB is very important because if you don't, MySQL 5.5 will perform worse than MySQL 5.1. In some cases, it can be worse than MySQL 4.1.
Query runs a long time in some newer MySQL versions

[chunk 720753] Why mysql 5.5 slower than 5.1 (linux,using mysqlslap)
As for RAM, tuning connection usage, the number of connections and InnoDB caches is the most important thing
Cache MySQL database in memory
What are the main differences between InnoDB and MyISAM?
How do I properly perform a MySQL bake-off?

THREAD B
Site: dba | Thread title: How do I properly perform a MySQL bake-off?
[chunk 714056] Here is the first thing I thought about
Setup 3 DB servers (identical HW/OS configs) each installed with
MySQL
Percona
MariaDB
Get a Fourth Server installed with MONyog (eval version lasts 30 days)
Register the 3 DB servers in MONyog
Use the Performance Metrics Charts in MONyog or Set Up Your Own Charts in MONyog
Use SysBench against all 3 DB Servers at your discretion

[chunk 714057] This is just a basic outline. Believe me, you can use Monyog right out of the box. Check out my testimonial at MonYog's Website (Look for my name on the page). I eventaully convinced my company to purchase the Utlimate Version outright after my testimonial, which they watched with me as it happened.
Caveat : Do no get Monyog until you have the 3 DB servers and Sysbench Ready to get the best 30-day usage of MonYog.
UPDATE 2011-06-20 13:18 EDT

[chunk 714058] If you keep the InnoDB Buffer Pool Small (default for innodb_buffer_pool_size is 8M) and keep the binary logs disabled (do no include log-bin in my.cnf), then these metrics should be measured
Innodb_buffer_pool_pages_flushed
Innodb_buffer_pool_write_requests
Innodb_row_lock_time_avg
Innodb_os_log_fsyncs
Queries, Questions
SELECTs ((Com_select + Qcache_hits) / Questions)
INSERTs ((Com_insert + Com_replace) / Questions)
UPDATEs (Com_update / Questions)
DELETEs (Com_delete / Questions)

[chunk 714059] Many of these are default graphs in MONyog's Monitors/Advisors Section, and more graphs can be created to check other desired MySQL metrics. MONyog also lets you export the graphs as CSV data.
UPDATE 2011-10-12 14:17 EDT
Percona performed a bake-off among multiple releases of MySQL
MySQL 4.1
MySQL 5.0
MySQL 5.1 (with built-in InnoDB)
MySQL 5.1 with InnoDB-plugin
MySQL 5.5
MySQL 5.6
All tests were performed with MySQL unconfigured. The results?
MySQL 4.1 performs the best single-threaded

[chunk 714060] MySQL 5.1 with InnoDB plug-in scales on multiple cores better than 5.1 InnoDB built, 5.5 and 5.6
What do I get out of this? Your must configure MySQL 5.5/5.6 to get multicore enhancements engaged.