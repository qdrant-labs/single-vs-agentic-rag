### item Pdba-199090-12690
THREAD A
Site: dba | Thread title: SQL Server Express Instance Memory vs Memory Limit
[chunk 799930] Community wiki answer:
The 1GB limit is only for the buffer pool, SQL Server uses other memory pools as well so it is possible to see memory usage over 1GB.
Quoting from Memory configuration and sizing considerations in SQL Server 2012 and later versions

[chunk 799931] Starting with SQL Server 2012, these memory limits are enforced only for the database cache (buffer pool). The rest of the caches in the SQL Server memory manager can use much more memory than is specified by these edition limits. For example, a SQL Server 2012 Express edition can use only a maximum size of 1.4 GB for its database cache. Other caches (such as the procedure cache, the metadata cache, and so on) can consume memory up to the size specified by the "max server memory" configuration.

[chunk 799932] For SQL Server 2016 SP1 onward, Express can also use an additional 352MB for columnstore segments per instance and another 352MB for in-memory OLTP (Hekaton) objects per database.
The maximum buffer pool size was also changed in the documentation from 1GB to 1410MB for SQL Server 2016, though this probably applies from SQL Server 2012 (where the big memory management changes were made).

[chunk 799933] Only the buffer pool, columnstore cache, and in-memory OLTP cache sizes are restricted by quota. Other cache stores and memory consumers in Express Edition can push overall memory usage up to the configured limit in the max server memory configuration setting.
See Also:
Why does SQL Server 2012 Express use 9.5GB of RAM on my server?
Does SQL Server 2008R2 Express actually enforce the memory and CPU limit?

THREAD B
Site: dba | Thread title: Does SQL Server 2008R2 Express actually enforce the memory and CPU limit?
[chunk 719473] SQL Server Express does enforce the limits, but the limits are not what you expect:
CPU: SQL Express enforces one socket, not one CPU. Multi-core and hyper-threaded machines will leverage multiple cores on one socket and SQL Express will use 2 or 4 cores on that socket. See Maximum Number of Processors Supported by the Editions of SQL Server:

[chunk 719474] SQL Server supports the specified number of processor sockets multiplied by the number of logical CPUs in each socket. For example, the following is considered a single processor for purposes of this table:
A single-core, hyper-threaded processor with 2 logical CPUs per socket.
A dual-core processor with 2 logical CPUs.
A quad-core processor with 4 logical CPUs.

[chunk 719475] Memory: Express restricts the max size of the buffer pool to only 1GB. The buffer pool accounts only for some of the overall process memory.
See Thread and Task Architecture and Memory Management Architecture

### item Punix-39431-91799
THREAD A
Site: unix | Thread title: dhcpd: any way to check dhcp pool status?
[chunk 300919] On Ubuntu there is the file /var/lib/dhcp/dhcpd.leases, but it is rather verbose and you probably need a little script if you want more high level statistics. I am unaware of existing tools to do this.
There is a separate man page for this file man dhcpd.leases describing the database format.

THREAD B
Site: unix | Thread title: Command to list assigned dhcp addresses
[chunk 323079] No, you can only get this information server side from the DHCP server. This information is contained in the DHCP server's .lease file: /var/lib/dhcpd/dhcpd.leases, if you're using ISC's DHCP server.
Example

[chunk 323080] $ more /var/lib/dhcpd/dhcpd.leases
# All times in this file are in UTC (GMT), not your local timezone. This is
# not a bug, so please don't ask about it. There is no portable way to
# store leases in the local timezone, so please don't request this as a
# feature. If this is inconvenient or confusing to you, we sincerely
# apologize. Seriously, though - don't ask.
# The format of this file is documented in the dhcpd.leases(5) manual page.
# This lease file was written by isc-dhcp-V3.0.5-RedHat

[chunk 323081] lease 192.168.1.100 {
 starts 4 2011/09/22 20:27:28;
 ends 1 2011/09/26 20:27:28;
 tstp 1 2011/09/26 20:27:28;
 binding state free;
 hardware ethernet 00:1b:77:93:a1:69;
 uid "\001\000\033w\223\241i";
}
...
...

### item Punix-13623-106330
THREAD A
Site: unix | Thread title: How much disk space do the files in a list use?
[chunk 287939] Use du -c to get the grand total then pipe through tail to get only the last line (the total):
du -c -- *.sql | tail -n 1
There seems to be no way to make du itself report just the total of a set of files.
The -- is not required but highly recommended if this command is to be used in a script. It marks end of options and protects against some funny filenames. See here for more info What does "--" (double-dash) mean?
Some technical nitpicks:

[chunk 287940] If any *.sql files are "hidden" (filename start with a dot) then they will not be included. This is because by default the glob does not include hidden files.
For *.sql that are directories du will include all files in those directories recursively.
Using zsh you can write *.sql(^/) to exclude directories. Or *.sql(D) to include hidden files. For more info look up zsh glob qualifiers.

[chunk 287941] For *.sql that are symlinks du will count the size of the link itself instead of the target it points to. Use du -H to get the size of the target of the link.
Beware that in any case most du implementations including GNU du will only count the disk usage of unique files. So if foo.sql is a hard link to bar.sql (or a symlink and -H is used) its disk usage will only be counted once.

[chunk 287942] This might cause confusion if you plan to copy the files to a filesystem that does not support hardlinks. In most cases the hardlinked files will be copied twice and you will end up needing more disk space on the target system than shown by du.
With the GNU implementation of du the -l option can be used to skip the deduplication.

THREAD B
Site: unix | Thread title: Sort all directories based on their size
[chunk 328851] With GNU sort and GNU du (which it appears you have, since you state you are using du's -h option):
du -sh -- * | sort -rh # Files and directories, or
du -sh -- */ | sort -rh # Directories only
The output looks something like this:
22G foo/
21G bar/
5.4G baz/
2.1G qux/
1021M wibble/
4.0K wobble/

### item Psoftwareengineering-126095-110740
THREAD A
Site: softwareengineering | Thread title: Resources on learning to program in machine code? 
[chunk 569066] People don't program in machine code (unless they are masochistic). They use (or develop) tools to generate machine code (compiler or assembler, including cross-development tools), or perhaps libraries generating machine code (LLVM, libjit, GNU lightning, ....). So resources about machine code generation, compilation, optimizers, and micro-architectures are also relevant.

[chunk 569067] And very often, a good optimizing compiler generates better machine code than you could do. You'll probably don't be able to write a 200 line assembler code better than a good optimizer.

[chunk 569068] If you want to understand machine code, learn assembly first. It is very close to machine code. Use it wisely, only for things you cannot code in C (or in some higher-level language, like Ocaml, Haskell, Common Lisp, Scala). A good way is often to use asm instructions (notably GCC extended assembly feature) inside a C function. Reading the assembly code (generated by gcc -S -O2 -fverbose-asm) can also be helpful.
The Linux Assembly HowTo is a good thing to read.

[chunk 569069] Current processor's instruction set architecture (i.e. the set of instructions understood by the chip) are quite complex. Common ones are x86 (a typical PC in 32 bits mode), X86-64 (a desktop PC in 64 bits mode), ARM (smartphones, ...), PowerPC etc. They are all quite complex (because of historical and economical reasons). Perhaps learning first an hypothetical instruction set like e.g. Knuth's MMIX is simpler.

THREAD B
Site: softwareengineering | Thread title: How exactly do we go from Binary/Hex to Assembly Instruction sets?
[chunk 561481] The heart of a CPU is the ALU. It's responsible for taking an instruction (like MOV) which is just some pre-defined series of binary digits, and also taking 0, 1, or 2 operands, and performing the applicable operation on them. The simplest instruction could be a NOP (no operation) which essentially does nothing. Another typical operation is ADD (adds two values).
The ALU reads and writes data from and to "registers".
These are small memory locations internal to the CPU.

[chunk 561482] Part of the instruction (2 to 3 bits for each input depending on how many registers you have) indicates which register to read from.
There are units in the CPU external to the ALU that handle loading required data (and the instruction) from memory into registers, and writing the result from registers back into memory.
The location to write the result will also be encoded into another 2 or 3 bits.
The choice of "op codes", which is the binary number that represents an operation, is not arbitrary.

[chunk 561483] Well-chosen opcodes reduce the complexity of the ALU.
Each bit or group of bits tends to enable and disable certain logic gate in the ALU.
For instance, an ADD instruction would have to enable the output stage to choose the result of the internal adding logic.
Likewise, a MUL instruction would choose the result of the multiply logic.

[chunk 561484] Depending on the design, it's quite likely that both the adder and multiply circuits both actually perform their operation on the input operands, and it's just the output selection (what gets written to the output bits of the ALU) that changes.

### item Punix-50372-45120
THREAD A
Site: unix | Thread title: How do I know which kernel version will have a bug fix I need?
[chunk 306163] Duplicate of Given a git patch id, how to find out which kernel release contains it?
In short: from your "fix" link, click "commitdiff" at the top, click "raw", and look at the X-Git-Tag header.

THREAD B
Site: unix | Thread title: Given a git commit hash, how to find out which kernel release contains it?
[chunk 303626] In GitHub kernel repository, you can check all tags/kernel versions.
Example for dc0827c128c0ee5a58b822b99d662b59f4b8e970 provided by Jim Paris:
If three-dots are clicked, full list of tags/kernel versions can be seen.

### item Punix-429521-228558
THREAD A
Site: unix | Thread title: How to translate Unicode characters?
[chunk 433021] Both GNU and BSD sed are multibyte-aware in appropriate locales, and the y command is analogous to tr:
$ echo hello | sed -e 'y/abcdefghijklmnopqrstuvwxyz/ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ/'
ｈｅｌｌｏ
This should work most places you're likely to run it, as long as your locale is a UTF-8 one.
The Perl issue isn't quite as simple as treating multibyte characters as bytes. It's understanding your input just fine, and even encoding the output, it's the source code it doesn't understand:

[chunk 433022] $ echo abc | perl -C -pe 'tr/abcdefghijklmnopqrstuvwxyz/ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ/'|hexdump -C
00000000 c3 af c2 bd c2 81 0a |.......|
The UTF-8 encoding of "ａ" is ef bd 81, so you can see that it's treating "b" as that second byte and then mangling it trying to encode it on the way out, and the same for "c". You need to use utf8 to have your Perl (5) source itself encoded in that way; -C only controls IO the program does when it's running.

[chunk 433023] You can put use utf8; into your -e string, or use -Mutf8 on the command line:
$ echo abc | perl -C -Mutf8 -pe 'tr/abcdefghijklmnopqrstuvwxyz/ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ/'
ａｂｃ
Perl 6 does solve this issue, as so many, but...

THREAD B
Site: unix | Thread title: How to make tr aware of non-ascii(unicode) characters?
[chunk 372636] That's a known (1, 2, 3, 4, 5, 6) limitation of the GNU implementation of tr.
It's not as much that it doesn't support foreign, non-English or non-ASCII characters, but that it doesn't support multi-byte characters.
Those Cyrillic characters would be treated OK, if written in the iso8859-5 (single-byte per character) character set (and your locale was using that charset), but your problem is that you're using UTF-8 where non-ASCII characters are encoded in 2 or more bytes.

[chunk 372637] GNU's got a plan (see also) to fix that and work is under way but not there yet.
FreeBSD or Solaris tr don't have the problem.
In the mean time, for most use cases of tr, you can use GNU sed or GNU awk which do support multi-byte characters.
For instance, your:
tr -cs '[[:alpha:][:space:]]' ' '
could be written:
gsed -E 's/( |[^[:space:][:alpha:]])+/ /'
or:
gawk -v RS='( |[^[:space:][:alpha:]])+' '{printf "%s", sep $0; sep=" "}'

[chunk 372638] To convert between lower and upper case (tr '[:upper:]' '[:lower:]'):
gsed 's/[[:upper:]]/\l&/g'
(that l is a lowercase L, not the 1 digit).
or:
gawk '{print tolower($0)}'
For portability, perl is another alternative:
perl -Mopen=locale -pe 's/([^[:space:][:alpha:]]| )+/ /g'
perl -Mopen=locale -pe '$_=lc$_'
If you know the data can be represented in a single-byte character set, then you can process it in that charset:

[chunk 372639] (export LC_ALL=ru_RU.iso88595
 iconv -f utf-8 |
 tr -cs '[:alpha:][:space:]' ' ' |
 iconv -t utf-8) < Russian-file.utf8

### item Punix-628231-56444
THREAD A
Site: unix | Thread title: Command-line variable assignment and command execution
[chunk 486647] This is a standard feature. You can set the variable when launching the command and then the variable will be set for the command. It also works in the example you show, foo='hello' echo $foo. The problem is that you are testing the wrong way. When you run this:
foo='hello' echo $foo
The shell will expand the variable before running the command. Since foo is not actually set when you launch it, that becomes echo (echo nothing). You can see this with set -x:

[chunk 486648] $ set -x
$ foo='hello' echo $foo
+ foo=hello
+ echo
Now, compare that to what happens if you instead use a little script so that the variable is not seen by your shell:
$ cat ~/scripts/foo.sh
+ cat /home/terdon/scripts/foo.sh
#!/bin/bash
echo "The value of foo is:$foo"
Use that to echo the variable and you get:
$ foo='hello' ~/scripts/foo.sh
+ foo=hello
+ /home/terdon/scripts/foo.sh
The value of foo is:hello

[chunk 486649] You can do the same thing if you call bash -c and enclose the command you give it in single quotes so the variable will be protected and not expanded by your current shell before calling bash -c:
$ foo='hello' bash -c 'echo $foo'
hello
While this fails because the double quotes mean that $foo is being expanded before bash -c ever sees it:
$ foo='hello' bash -c "echo $foo"
$
The behavior is documented in man bash in the "ENVIRONMENT" section:

[chunk 486650] The environment for any simple command or function may be augmented
 temporarily by prefixing it with parameter assignments, as described
 above in PARAMETERS. These assignment statements affect only the envi‐
 ronment seen by that command.
It's also described in detail in the manual: 3.7.1 Simple Command Expansion

THREAD B
Site: unix | Thread title: How do I set an environment variable on the command line and have it appear in commands?
[chunk 307787] This is because the shell expands the variable in the command line before it actually runs the command and at that time the variable doesn't exist. If you use
TEST=foo; echo $TEST
it will work.
export will make the variable appear in the environment of subsequently executed commands (for on how this works in bash see help export). If you only need the variable to appear in the environment of one command, use what you have tried, i.e.:
TEST=foo your-application

[chunk 307788] The shell syntax describes this as being functionally equivalent to:
export TEST=foo
your-application
unset TEST
See the specification for details.
Interesting part is, that the export command switches the export flag for the variable name. Thus if you do:
unset TEST
export TEST
TEST="foo"
TEST will be exported even though it was not defined at the time when it was exported. However further unset should remove the export attribute from it.

### item Pserverfault-110127-5958
THREAD A
Site: serverfault | Thread title: Which FileSystem is best for CentOS 5 on SSD?
[chunk 40709] ssd has much larger 'physical data allocation unit' - so regardless of the fileystem you choose remember to align your partitions with size of sector on your ssd drive. if you don't - your write performance will suffer a lot.

[chunk 40710] this is even true for newest desktop disks with 4kB sector instead of 512B sector - just yesterday i did empirical experiment that gave me 29MB/s write speed with default alignment [ from 63rd logical 512B sector ] vs 70MB/s with proper alignment [ starting from 128rd sector ].
regarding the file system - ext4 is supposed to support trim, but i never really tested it. take a look here and here.

THREAD B
Site: serverfault | Thread title: Most Appropriate log-structured file system to use with Linux / SSD?
[chunk 2741] NILFS2 has been merged into the current development kernel, and will be available in kernel 2.6.30 (You can run a -rc kernel if you're impatient). It apparently performs very well on SSDs.
As with anything recently merged into the kernel, you'll have to make your own decision regarding stability and maturity.

### item Psoftwareengineering-96524-107288
THREAD A
Site: softwareengineering | Thread title: Why do people use programming books?
[chunk 555197] Here's how I learn, generally speaking:
Buy a book
Don't read it cover to cover but know where everything can be found
Find a pet project to work on
Learn from experience, but use the book as a reference
Where the book fails, there is always google
Note: the third point sometimes comes first.
Edit: To answer the question "Why?"

[chunk 555198] Google is great to find out how to do something, but it's not great for finding out what you don't know. Why would you ever google "C# delegates," if you didn't first know that C# has a concept called delegates and that it might be useful to solve a problem you're working on?

[chunk 555199] Also, the signal-to-noise ratio can be a bit high sometimes. If you have a rough idea in your head how something is done then you can easily confirm whether the article you are reading is correct. But if you've no clue... you can end up in a bigger mess.

THREAD B
Site: softwareengineering | Thread title: Could spending time on Programmers.SE or Stack Overflow be substitute of good programming books for a non-beginner?
[chunk 559843] No, it is not a substitute, but a perfect complement. I feel a combination of the two holds a lot of power.
Why is it that a good lecture teaches you more than just reading a book? Interaction and the ability to ask questions.
By just reading a book, some questions might pop up to which you can't find any answers. Look for those questions here, or ask them if they haven't been discussed before.

### item Punix-336909-199935
THREAD A
Site: unix | Thread title: BTRFS balance completed, but still shows data stored in "single" mode
[chunk 405626] With the help of a user on the btrfs irc, I was able to answer question (1).
It seems unrelated to the reboot and unsuccessful mount attempt (still not sure what that was about).
Instead, it seems the 645GB of data stored as "single" was data that was added to the btrfs volume after the raid1 conversion had been initiated.
Therefore, it seems good practice to check the output of btrfs fi usage before you assume all your data is stored as raid1 after a conversion.

[chunk 405627] Furthermore, the "soft" filter will allow you to rebalance data which is not being stored according to the target profile, so for example I ran:
btrfs balance start --bg -mconvert=raid1,soft /mnt/btrfs
btrfs balance start --bg -dconvert=raid1,soft /mnt/btrfs
(following a suggestion by the user on the btrfs irc forum to perform the balance on the metadata first, and then on the data) and this is in the process of converting the remaining data to raid1.

[chunk 405628] Furthermore, to answer question (2), the answer is that it is possible to end up with some "single" chunks in a raid1 filesystem, but they should have 0 usage. If this happens, you can clean them up by running
btrfs balance start -dusage=0 -musage=0 /mnt/btrfs
(see the btrfs FAQ)

THREAD B
Site: unix | Thread title: Why does btrfs refuse to convert metadata to RAID1
[chunk 363779] This is a regression in kernel 4.0, causing conversion filters in balance to have no effect; it looks like all conversions are affected (not just single->raid1 or raid1->raid5). See a recent mailing list thread, where there's currently no official fix. If you're up to patching your kernel, there's an easy patch to apply as a temporary fix.

[chunk 363780] This is a known bug in v4.0. I sent in a patch [1] to revert the commit
 that caused the regression, but it didn't get any response. You
 could apply that or just revert 2f0810880f08 ("btrfs: delete chunk
 allocation attemp when setting block group ro") to fix your problem for
 now.
[1]: https://patchwork.kernel.org/patch/6238111/

### item Pdba-12337-11101
THREAD A
Site: dba | Thread title: Is it more secure to go through a 3rd database to connect two databases using the same login?
[chunk 719217] One thing jumps out here:
The entire process uses the same set of login credentials
Problem
So hypothetical userX (whether some meatsack using Excel, or IIS AppPool Identity) can see some views and code. It doesn't matter what database these views and code are in because userX is setup in 3 databases anyway.
However, you lose ownership chaining like this.

[chunk 719218] Let's say WebDB.dbo.SomeProc calls PrivateDB.dbo.SomeTable. UserX requires permissions on both objects. If this was OneDB.WebGUI.SomeProc using OneDB.dbo.SomeTable then only the OneDB.WebGUI.SomeProc needs permissions. Permissions on referenced objects with the same owner are not checked.
Note: I haven't looked too deeply at cross database ownership chaining. I only know plain old "ownership chaining" well

[chunk 719219] Now, as per comments you really have 2 databases that can be combined. Not 3 which was originally implied. However, the intermediate and web can be combined.
The other "private" databases can perhaps be combined, but that'll be a separate issue. See the bottom link for a fuller discussion of "one database or many"
Solution?
If the extra databases are code containers only, then schemas are a better idea.

[chunk 719220] This sounds like you've used "Database" where you should use "Schema" (in the SQL Server sense, not MySQL sense). I'd have a WebGUI schema, a Helper or Common schema (to replace Intermediate database) and Desktop schema. This way you separate permissions based on clients and just have one database
With one database (in addition to "ownership chaining") you can also start to consider indexed views, SCHEMABINDING (I use it always) and such that can't be done with seperate databases

[chunk 719221] For more on schemas, see these questions:
Schema design - best practices?
Over use/correct use of schemas?
Finally, there appears no reason to have separate databases based on "transactional integrity not required". See this question to explain this:
 Decision criteria on when to use a non-dbo schema vs a new Database

THREAD B
Site: dba | Thread title: Decision criteria on when to use a non-dbo schema vs a new Database
[chunk 718668] I'll start by saying don't consider schemas as namespaces or object domains in the OO sense. Schemas are essentially permission containers with some added value (see below)
Also, "separate schemas" or "separate databases" are 2 different concepts. Data that needs to be transactionally and referentially consistent needs to be in the same database. See One Database or Ten? blog article for more.
In that database, you may or may not use schemas for organising your objects.

[chunk 718669] Personally, I'm a fan of schemas and always use them but for things like permissions and logical grouping. For that, I'll refer you to previous questions where you can see the general opinion is in favour of them:
Schema design - best practices?
What standard should I follow when naming tables and views?
Over use/correct use of schemas?
For the case for separate databases, see Aaron's answer, but this all hinge on the "transactionally and referentially consistent" requirement.

### item Punix-379398-364047
THREAD A
Site: unix | Thread title: Using middle mouse click to paste text enters insert mode
[chunk 417426] This is fully answered here. See the excellent linked answer for details and alternative solution.
Short answer: 
put :set t_BE= in your .vimrc file.

THREAD B
Site: unix | Thread title: Stop vim pasting selections as text!
[chunk 413440] Well after going through a LOT of web pages, many giving some hints that did not seem to work, I found a hint (extra text around a paste) that lead me to the cause and the solution to the problem.
It seems that vim has built into it a number of 'fake' termcap entries which it uses when it recognises specific terminals (and sometimes gets wrong, though it wasn't wrong in this case).

[chunk 413441] Termcap settings in vim are numerious add as such DOES NOT show up in a normal ":set all" setting list. To see them you need to use ":set termcap". The specific 'non-standard' termcap setting is "t_BE" (see vim ":help t_BE"). The built-in help "xterm-bracketed-paste" explains this internal-to-vim termcap setting.

[chunk 413442] Basically if this setting is defined (in this case by Vim not termcap/terminfo) then vim will send it to the xterm when it starts up, which tells xterm to add special codes around any text the user pastes from an external source. When vim sees these it automatically goes not only into insert-mode but also sets 'paste-mode' so as not to format the text.
The later (paste-mode) is I think VERY useful! The former is what has been giving me all the trouble.

[chunk 413443] The brute force solution is disable bracketed-paste by adding this to the ".vimrc"
:set t_BE=
An Alternative Solution....
Instead of disabling bracketed-paste completely, stop vim taking action when it sees the starting sequence of a terminal paste (from the mouse), while in command or normal-mode.
:nmap <PasteStart> <NOP>
:nmap <PasteEnd> <NOP>
:cmap <PasteStart> <NOP>
:cmap <PasteEnd> <NOP>

[chunk 413444] Using this means that if you do paste text while in insert-mode vim will not try to format (indent) text that is more than likely already indented.
This does not mean I no longer need to toggle paste-mode, as I also use the paste-mode toggle (mapped to F2) to disable "showbreak" and "listchars" (displaying wrapped lines, tabs, no-break spaces, and extra spaces at the end of lines). I would still need to put vim in that mode when I want to make mouse selections to paste elsewhere.

[chunk 413445] Comments and Suggestions on the solutions are welcome.

### item Pserverfault-628441-238563
THREAD A
Site: serverfault | Thread title: ufw cancel port forward
[chunk 182653] By flushing the chains in the NAT table and removing any sub-chains:
ufw disable
iptables --table nat --flush
iptables --table nat --delete-chain
ufw enable
Short options: --table|-t, --delete-chain|-X

THREAD B
Site: serverfault | Thread title: Can I use ufw to setup a port forward?
[chunk 78753] Let's say you want to forward requests going to 80 to a server listening on port 8080.
Note that you will need to make sure port 8080 is allowed, otherwise ufw will block the requests that are redirected to 8080.
sudo ufw allow 8080/tcp
There are no ufw commands for setting up the port forwards, so it must be done via configuraton files. Add the lines below to /etc/ufw/before.rules, before the filter section, right at the top of the file:

[chunk 78754] *nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
COMMIT
Then restart and enable ufw to start on boot:
sudo ufw enable

### item Punix-131592-50692
THREAD A
Site: unix | Thread title: Blank lines when executing "grep | xargs" in a "find -exec"
[chunk 339700] It's failing because when the grep doesn't match, you're not passing anything to xargs.
For example:
find gets ./.htaccess and calls your -exec.
The grep doesn't match anything in the file, so it outputs nothing
xargs launches dirname without any arguments, and so dirname thinks it was just misused and displays its help message.
The proper way to do this:
find . -type f -name .htaccess -exec grep -iq '^deny from all$' {} \; -printf '%h\n'

THREAD B
Site: unix | Thread title: Executing user defined function in a find -exec call
[chunk 306255] A function is local to a shell, so you'd need find -exec to spawn a shell and have that function defined in that shell before being able to use it. Something like:
find ... -exec ksh -c '
 function foo {
 echo blan: "$@"
 }
 foo "$@"' ksh {} +
bash allows one to export functions via the environment with export -f, so you can do (in bash):
foo() { ...; }
export -f foo
find ... -exec bash -c 'foo "$@"' bash {} +

[chunk 306256] ksh88 has typeset -fx to export function (not via the environment), but that can only be used by she-bang less scripts executed by ksh, so not with ksh -c.
Another option is to do:
find ... -exec ksh -c "
 $(typeset -f foo)"'
 foo "$@"' ksh {} +
That is, use typeset -f to dump the definition of the foo function inside the inline script. Note that if foo uses other functions, you'll also need to dump them as well.

[chunk 306257] Or instead of passing the function definition on the command line (which would be visible in the output of ps -f for instance), you can pass it via an environment variable:
FUNCDEFS=$(typeset -f foo) find ... -exec ksh -c '
 eval "$FUNCDEFS" &&
 unset -v FUNCDEFS &&
 foo "$@"' ksh {} +
(the unset -v FUNCDEFS to avoid polluting the environment of commands started by that foo function if any).

### item Psoftwareengineering-387269-235909
THREAD A
Site: softwareengineering | Thread title: Unit testing abstract classes with Google mock (gmock/gtest) (C++)
[chunk 682328] You are asking quite a few things here, but let me share my opinion on the things you describe.
The typical use of mock classes is when you need them for testing another class, and need to check if the state of the mock class is changed (instead of more heavy implementations of the interface).

[chunk 682329] The case that you describe is valid of course, but I would like to argue that the test in itself is not useful. In a typical example I would expect pureFunc to be private, but it does not matter too much. What you are actually testing now is implementation, and not the behavior. What you should test is what func does (i.e., by returning something or changing the state of the class).

[chunk 682330] To be more explicit. In your example I can have the for-loop in func run to count/2 and run the code in pureFunc itself twice (doesn't work for odd numbers, but consider it for the sake of the argument. The unit test fails, however, the state of your object is the same. You want to be able to change your class and implementation, without unit tests starting to fail. If you need to modify the unit test everytime you change the implementation, you have done something wrong.

[chunk 682331] So what can you do instead? Well, you have implementations of your abstract class. You can test func for that, to check if it does what you expect. (And pureFunc if it is really public).

THREAD B
Site: softwareengineering | Thread title: Testing abstract class' behavior
[chunk 616693] As long as the functionality you'd like to test doesn't invoke any pure virtual methods and isn't overridden in subclasses, I'd stick with your bullet point number 1 - creating a test-specific subclass. You could name it Sub<ClassName> or any generic name reflecting that the subclass itself is not important.
Now if what you want to test can be altered in any way by the final concrete class, you might want to consider this :

[chunk 616694] I don't know if there's an equivalent in the C++ test framework you're using, but NUnit (and I believe JUnit) let you implement the Abstract Test pattern.
In short, you have
An abstract base test class. It contains a abstract factory method used to generate the object under test, and the test methods per se. These methods verify things that must stay true regardless of the concrete object underneath.

[chunk 616695] As many derived test classes as there are derivatives of the abstract class under test. You just have to implement the factory method here to return an instance of the derived class.
When the test runner sees a derived test class, it will automatically execute all test methods inherited from the base test class against the factory method-generated object.

### item Psoftwareengineering-327622-278285
THREAD A
Site: softwareengineering | Thread title: What are the licensing requirements for a program I compile using GCC?
[chunk 651731] This would be covered by the GCC Runtime Library Exception.
If you use GCC as-is to compile your program, the resulting binary is not covered by the GPLv3 and you can license it under any terms you wish.

[chunk 651732] Your source code is not subject to the GPLv3 merely because you use GCC to compile it to a binary, the only way GCC's license would impact your source code is if you directly copy portions of the GCC code into your source code itself (which, of course, would mean some of the source code isn't yours).

THREAD B
Site: softwareengineering | Thread title: Licensing of content created by licensed code
[chunk 632308] The GPL describes rules about the use of the source code, not rules about the use of products of the application itself. The most obvious example is the GNU compiler. The compiler is released under the GPL. It is perfectly fine to use that to compile programs that are not released under the GPL. What you are restricted from is modifying the GNU compiler itself and not putting those modifications under the GPL. Lots of very proprietary code is compiled with the GNU compiler.

[chunk 632309] This is generally true of most open source licenses, however, I suppose it might not be the case for every single one. If you run into some weird license, read the license and perhaps consult a lawyer. But for the GPL and trianglify, you would not be restricted from using generated svg files in any way.
That said, pointing to the code that generated the file in your own .readme is a nice thing to do, and has no real downsides, so you might as well do it. But you aren't required to.

### item Punix-312590-2976
THREAD A
Site: unix | Thread title: Setting up environment variables with .sh file
[chunk 398602] You need to source (.) the file, not execute:
. env.sh
When you execute the script, it is run in a subshell, and all the parameters exported will go out of scope once the (sub)shell exits, not affecting the parent shell.
When you source it, the parameters will be available on the calling session. And also on the child processes as you are export-ing them.

[chunk 398603] Note that, the default system shell (sh) for Ubuntu is dash, not bash and gnome-terminal spawns bash as the interactive shell. While executing, make sure the shebang is correct, and desired one. Also while source-ing, no need for the shebang, you can drop it.

THREAD B
Site: unix | Thread title: Different ways to execute a shell script
[chunk 281955] Another way is by calling the interpreter and passing the path to the script to it:
/bin/sh /path/to/script

[chunk 281956] The dot and source are equivalent. (EDIT: no, they're not: as KeithB points out in a comment on another answer, "." only works in bash related shells, where "source" works in both bash and csh related shells.) It executes the script in-place (as if you copied and pasted the script right there). This means that any functions and non-local variables in the script remain. It also means if the script does a cd into a directory, you'll still be there when its done.

[chunk 281957] The other ways of running a script will run it in its own subshell. Variables in the script are not still alive when it's done. If the script changed directories, then it doesn't affect the calling environment.
/path/to/script and /bin/sh script are slightly different. Typically, a script has a "shebang" at the beginning that looks like this:
#! /bin/bash

[chunk 281958] This is the path to the script interpreter. If it specifies a different interpreter than you do when you execute it, then it may behave differently (or may not work at all).
For example, Perl scripts and Ruby scripts begin with (respectively):
#! /bin/perl
and
#! /bin/ruby
If you execute one of those scripts by running /bin/sh script, then they will not work at all.

[chunk 281959] Ubuntu actually doesn't use the bash shell, but a very similar one called dash. Scripts that require bash may work slightly wrong when called by doing /bin/sh script because you've just called a bash script using the dash interpreter.
Another small difference between calling the script directly and passing the script path to the interpreter is that the script must be marked executable to run it directly, but not to run it by passing the path to the interpreter.

[chunk 281960] Another minor variation: you can prefix any of these ways to execute a script with eval, so, you can have
eval sh script
eval script
eval . script
and so on. It doesn't actually change anything, but I thought I'd include it for thoroughness.

### item Pserverfault-38318-432322
THREAD A
Site: serverfault | Thread title: Better way to wait a few seconds in a bat file?
[chunk 15746] You can use the "default choice" and "timeout" options of the built-in choice command to create a delay.
@echo off
echo Hi, I'm doing some stuff
echo OK, now I need to take a breather for 5 seconds...
choice /d y /t 5 > nul
echo Times up! Here I go again...

THREAD B
Site: serverfault | Thread title: How to sleep in a batch file?
[chunk 135987] The correct way to sleep in a batch file is to use the timeout command, introduced in Windows 2000.
To wait somewhere between 29 and 30 seconds:
timeout /t 30
The timeout would get interrupted if the user hits any key; however, the command also accepts the optional switch /nobreak, which effectively ignores anything the user may press, except an explicit CTRL-C:
timeout /t 30 /nobreak

[chunk 135988] Additionally, if you don't want the command to print its countdown on the screen, you can redirect its output to NUL:
timeout /t 30 /nobreak > NUL

### item Punix-131653-114795
THREAD A
Site: unix | Thread title: Repackaging proprietary software
[chunk 339723] I try to maintain the PHP App Engine package on AUR and I'm installing it in /opt which was where you should put a self-contained Matlab package (in something like /opt/matlab) and sym-link the executable back to /usr/bin and other stuff back to /usr/share/applications and what not.

[chunk 339724] I would take a look at a few other packages that re-package binaries for arch. Like the Dropbox or Google Chrome packages. The Chrome package in particular depends on the Debian binary so they drop the Debian specifics when installing on arch.
On the other hand, if you drop everything into /opt/matlab as-is rather than strip common libraries and the JRE you're much more likely to have a working Matlab that doesn't break or have to be re-tested and re-packaged every time a dependency changes.

[chunk 339725] You could offer two flavours: a Matlab-complete package and a Matlab-minimal package.

THREAD B
Site: unix | Thread title: Add multiple subdirectories under the same parent directory to PATH
[chunk 332294] Adding a directory to PATH only makes the executables in this directory available as bare command names. This does not extend to subdirectories.
You can put a loop in your .profile (not .bashrc) to add multiple directories, for example:
for d in ~/tools/*/bin; do
 PATH="$PATH:$d"
done
(You don't need to repeat export: when a variable is exported, it stays exported, and modifications are reflected in the environment).

[chunk 332295] If you create new directories under tools, this will not be reflected in your ongoing session, only the next time .profile is read. If this is not satisfactory, you can use a different approach: put a single directory such as ~/bin in your PATH, and when you install software, create symbolic links in ~/bin. Stow (or its alternative XStow) is a good way of doing this; see Keeping track of programs for an overview of how this works.

### item Punix-397529-1459
THREAD A
Site: unix | Thread title: grep with variable using ssh
[chunk 422817] Since the default shell is tcsh on the remote host, you may want to explicitly start a sh shell:
ssh username@servername sh -c 'for FILE in pathToDirectory/*.txt; do grep -q "word1" "$FILE" && grep -q "word2" "$FILE" && echo "$FILE"; done'
Note also that you should double quote the $FILE variable expansion to cope with filenames that have exotic characters in them.

[chunk 422818] Also note that although you use word1 and word2 with grep, these are regular expressions and not words. To look for words in a file, use grep -wF "word".
It seems as if ssh will always run the login shell to execute the given command on the remote host, and if this is tcsh it is really difficult to get the quoting right in the command line script.
Two solutions (and I'm not fond of either):

[chunk 422819] Change the login shell on the remote host to a sh-like shell like bash, ksh, or zsh. Do this by logging in on the host and run chsh.
Put the script in a script file and execute it through ssh with
ssh username@servername sh ./script.sh

THREAD B
Site: unix | Thread title: Remote for-loop over SSH
[chunk 281042] Your local shell interpretes the ${i} within double quotes ("), so the command works out to
ssh user@some.serv.er "for i in /tmp/foo* ; do echo; done"
Simply use single quotes (') instead and your problem will disappear:
ssh user@${server} 'for i in /tmp/foo* ; do echo $i; done'