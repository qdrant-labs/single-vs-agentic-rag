### item Psecurity-37200-16861
THREAD A
Site: security | Thread title: Login system using authenticated encryption without storing user password
[chunk 868980] Actually your proposal is just a variation of a hashed password. Only in this case it is not the hash which is verified, rather an encrypted/decrypted blob. Hence it has mostly the same advantages and drawbacks of (reasonably implemented) hashed passwords. See PBKDF. When properly designed - like e.g. bcrypt (c.f. Do any security experts recommend bcrypt for password storage?) - it offers rather good security for most scenarios.

[chunk 868981] The question you are referring to (user authentication by decrypting a random blob) actually covers it rather well, I'd say.
As for user's data encrypted by the password - change in the password would of course require re-encrypting anything encrypted with the old one (i.e.
decrypt with old one, encrypt with new one), which is generally performance expensive thing to do.

[chunk 868982] This is usually circumvented in a layered manner: the data itself is encrypted with a randomly generated key, which in turn is encrypted with a password-derived one.
If one decides to change the password, all that is needed is re-encrypting the real encryption key.
It also allows one to use several passwords to access the same data (one example of this very way of encrypting data is LUKS).

[chunk 868983] That said, should you intend to create your own cryptography solutution, read Is my developer's home-brew password security right or wrong, and why? first.

THREAD B
Site: security | Thread title: Verify Login and Encrypt with PBKDF2
[chunk 857111] It depends whether you want to defend against typing mistakes, or attacks.
If you just want to defend against typing mistakes, just include some structure in your configuration file. E.g., define that your configuration file MUST begin, when decrypted, with the string "This is configuration file for application FooBar". If you do not find that string upon decryption, then the key is wrong.

[chunk 857112] If you want to defend against attacks (a bad guy voluntarily alters parts of the encrypted configuration file to make you load an incorrect key), then you need something stronger. The "right" solution is to use an authenticated encryption mode (my favourite is EAX). If your programming framework does not include an implementation of EAX mode, you can do something like this:

[chunk 857113] From the user's passphrase, generate 384 bits of key (PBKDF2 is a "key derivation function", it can be used to produce keys of arbitrary length). Split these into three 128-bit keys K1, K2 and K3.
Encrypt the configuration file with AES-128-CBC, using K1 as key and K2 as IV. Call the result C (the encrypted file).

[chunk 857114] Compute a MAC value over C, using key K3. For the MAC function, use HMAC with SHA-256 (or SHA-1, but SHA-256 is preferred on a general basis). The MAC is stored along C (appended, as header, as a separate file... that's your choice).
When decrypted, to the reverse: obtain the three keys from PBKDF2, verify the MAC, and (only if the MAC was correct) decrypt the file.

[chunk 857115] This scheme would resist both attacks and typing mistakes (however, it does not distinguish between a wrong passphrase and a genuine attack).
Edit: I had left it implicit, but it would be better to state it plainly: since we are using PBKDF2, there is a salt which is used to turn the password into the PBKDF2 output. Each encrypted file SHALL have its own salt. The salt SHALL be encoded in the file header. If a file is "re-encrypted", a new random salt SHALL be generated.

### item Pdba-77664-41743
THREAD A
Site: dba | Thread title: How does SQL Server determine precision / scale?
[chunk 750371] Determining precision and scale resulting from expressions is a rat's nest and I don't think anyone understands the exact rules in every scenario, especially when mixing decimal (or float!) and int. See this answer by gbn.
You can of course tailor the expressions to give you what you want by making much more verbose explicit conversions. This is probably overkill but:

[chunk 750372] SELECT 
 CONVERT(DECIMAL(15,6), CONVERT(DECIMAL(15,6), 0.15) 
 * CONVERT(DECIMAL(15,6), 30) 
 / CONVERT(DECIMAL(15,6), 360)),
 CONVERT(DECIMAL(15,6), CONVERT(DECIMAL(15,6), 0.15) 
 / CONVERT(DECIMAL(15,6), 360) 
 * CONVERT(DECIMAL(15,6), 30));
Neither result is rounded wrongly due to broken floating point math or wildly wrong precision/scale.
0.012500 0.012500

THREAD B
Site: dba | Thread title: Automatic decimal rounding issue
[chunk 734681] tl;dr
Don't do calculations in SQL language
Longer
The result scale and precision is well defined here on MSDN. It isn't intuitive, really.
However, in simple terms, precision is lost when the input scales are high because the result scales need to be dropped to 38 with a matching precision drop.
To confirm things
Your extra CAST in the first example simply add zeroes
The truncation happens as per my MSDN link (2nd example)

[chunk 734682] The 3rd example with constants has implied decimal values that are just enough (5,1) and 18,14).
This means the result scale and precision have no truncation (see blow)
More on the 1st and 3rd cases..
The result scale for a division is max(6, s1 + p2 + 1):
First example, this is 77 which is dropped to 38. Precision is forced down similarly, subject to a minimum of 6 (see this)
Third example, this is 24 so precision does not need adjusted
You have some options
calculate in the client code eg .net

[chunk 734683] use CLR functions to do .net calculations
live with the loss of accuracy
use float and live with 15 significant figures as best
FInally, see this on SO https://stackoverflow.com/questions/423925/t-sql-decimal-division-accuracy/424052#424052

### item Punix-339132-1834
THREAD A
Site: unix | Thread title: Reinstall man pages & fix man
[chunk 406383] You need to remove the lines matching /usr/share/man and /usr/share/groff from /etc/dpkg/dpkg.cfg.d/01_nodoc, then reinstall groff, man-db, manpages and any other package whose manpages you want to restore. The cp manpage for example is in the coreutils package.

THREAD B
Site: unix | Thread title: missing man pages of some commands
[chunk 281264] You probably have the man page for echo because most systems have an echo binary in /bin, even though most shells provide a built-in anyway; you're seeing the man page for that binary. The man pages for all the other commands you're missing are in the POSIX Programmer's Manual (man section 1P). How to install it will depend on your distro; on Gentoo they're in the sys-apps/man-pages-posix package

### item Punix-43177-2249
THREAD A
Site: unix | Thread title: Install Compiler, GCC, in SCO
[chunk 302733] gcc-98q2-dist.tar.gz contains a GCC installation image, that is, a tarred-up installation of GCC. All you need to do is untar it to the root directory:
cd /
tar xzvf gcc-98q2-dist.tar.gz
But I hope you won't be using a GCC version from 1998. gcc-2.95.2pl1-dist.tar.gz seems to be a tad newer, but still old (1999). Anyway, if you need a newer version, you can bootstrap it with that compiler.

THREAD B
Site: unix | Thread title: How do I install GCC on a system with no compiler?
[chunk 281505] Cross-compiling may be the solution for you It allows you to compile executables for one architecture on a system of a different architecture. Here's an introduction

### item Punix-120475-60688
THREAD A
Site: unix | Thread title: How can I pass argument stored on a variable to WGET
[chunk 334884] http://mywiki.wooledge.org/BashFAQ/050
user_agent='--user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0"'
cookies_file="/tmp/wget-cookies.txt"
save_cookies_opts=( --save-cookies "$cookies_file" --keep-session-cookies )
load_cookies_opts=( --load-cookies "$cookies_file" --keep-session-cookies )
function mywget {
 log "#!!!!!!!!!# WGET #!!!!!!!!!# wget $quiet $useragent $load_cookies_cmd $@"
 wget "$user_agent" "${load_cookies_opts[@]}" "$@"
}

[chunk 334885] Note that in the wget call , "$user_agent" is quoted. This is crucial.

THREAD B
Site: unix | Thread title: How to defer variable expansion
[chunk 309549] With the kind of input you show, the only way to leverage shell expansion to substitute values into a string is to use eval in some form.
This is safe as long as you control the value of str1 and can ensure that it only references variables that are known as safe (not containing confidential data) and doesn't contain any other unquoted shell special character.

[chunk 309550] You should expand the string inside double quotes or in a here document, that way only "$\` are special (they need to be preceded by a \ in str1).
eval "substituted=\"$str1\""
It would be a lot more robust to define a function instead of a string.
fill_template () {
 sentence1="I went to ${PLACE} and saw ${EVENT}"
 sentence2="If you do ${ACTION} you will ${RESULT}"
}
Set the variables then call the function fill_template to set the output variables.

[chunk 309551] PLACE=Sydney; EVENT=fireworks
ACTION='not learn from history'; RESULT='have to relive history'
fill_template
echo "During my holidays, $sentence1."
echo "Cicero said: \"$sentence2\"."

### item Pserverfault-102948-82039
THREAD A
Site: serverfault | Thread title: Why does a web server's public key certificate have to be signed by a certificate authority?
[chunk 38333] The purpose of SSL when used with HTTP is not just to encrypt the traffic, but also to authenticate who the owner of the website is, and that someone's been willing to invest time and money into proving the authenticity and ownership of their domain.
It's like purchasing a relationship, not just encryption, and the relationship instils, or assumes, a certain level of trust.
That said, I asked a similar question a few months ago, and the basic answer that came back was "SSL is a bit of a scam"

THREAD B
Site: serverfault | Thread title: Difference between SSL products
[chunk 31463] From the typical end-users perspective there is effectively no difference between most certificates. Some even call the SSL system a scam. Even the EV certificates don't really make much to the typical end user over a cheap certificate. As long as the browser doesn't complain, most users are happy.
Unless you are running a bank, or have a large number of highly paranoid security professionals as customers then I suggest you get the cheapest certificate you can.

### item Punix-1168-43713
THREAD A
Site: unix | Thread title: how to glob every hidden file except current and parent directory
[chunk 280911] You can use the GLOBIGNORE variable to hide the . and .. directories. This does automatically also set the dotglob option, so * now matches both hidden and non-hidden files. You can again manually unset dotglob, though, this then gives the behavior you want.
See this example:
$ ls -a
. .. a .a ..a
$ GLOBIGNORE=".:.."
$ shopt -u dotglob
$ echo * # all (only non-hidden)
a
$ echo .* # all (only hidden)
.a ..a
Note the following corner cases shown by numerous users in the comments:

[chunk 280912] . and .. are always ignored as long as GLOBIGNORE has a non-null value. GLOBIGNORE=":" ; echo .*, for instance, would work for the example above, even though it is less readable.
If you want to match hidden directories only (and not all hidden files) and therefore glob with a trailing slash, echo .*/, you need to set GLOBIGNORE='.:..:./:../', because the glob will match ./ and ../, which must be excluded explicitly to prevent them from showing up in the result.

THREAD B
Site: unix | Thread title: What does .??* mean in a shell command?
[chunk 302986] Globs are not regular expressions. In general, the shell will try to interpret anything you type on the command line that you don't quote as a glob. Shells are not required to support regular expressions at all (although in reality many of the fancier more modern ones do, e.g. the =~ regex match operator in the bash [[ construct).

[chunk 302987] The .??* is a glob. It matches any file name that begins with a literal dot ., followed by any two (not necessarily the same) characters, ??, followed by the regular expression equivalent of [^/]*, i.e. 0 or more characters that are not /.
For the full details of shell pathname expansion (the full name for "globbing"), see the POSIX spec.

### item Punix-32851-12195
THREAD A
Site: unix | Thread title: Ssh keeps asking for passphrase several times
[chunk 297824] Try running
eval $(ssh-agent -s)
before ssh-add, to export the environment variables that refer to the just started agent, then run
ssh-agent -k
(without eval) at end of script to kill the agent.

THREAD B
Site: unix | Thread title: How to avoid being asked passphrase each time I push to Bitbucket
[chunk 287132] You need to use an ssh agent. Short answer: try
$ ssh-add
before pushing. Supply your passphrase when asked.
If you aren't already running an ssh agent you will get the following message:
Could not open a connection to your authentication agent.
In that situation, you can start one and set your environment up thusly
eval $(ssh-agent)
Then repeat the ssh-add command.
It's worth taking a look at the ssh agent manpage.

### item Psecurity-45272-8476
THREAD A
Site: security | Thread title: Storing KeePass database in cloud. How safe?
[chunk 874494] It is hard to quantify exactly, but if you have the DB on a mobile device then I wouldn't say this is particularly any less secure. KeePass encrypts the DB because the file remaining secure isn't expected to be a guarantee. It's certainly preferable that the DB file not get in the wild, but if your security depends on the encrypted file remaining confidential, then you have bigger problems than whether to use cloud storage or not.

[chunk 874495] A sufficiently strong master password should prevent brute forcing at least long enough for a breach to be detected and for you to change the passwords within it. In this way, it may even be slightly preferable to having a local copy on a mobile device as someone may compromise the file if you take your eyes off your device even momentarily and it would be much harder to identify that breach occurred.

[chunk 874496] If you want to secure it even further, you can add another layer of security by encrypting the file you store in cloud storage online.
The master password provides pretty good security as long as you choose a difficult to brute force password (long and truly random), but it still can't compete with an actual long encryption key.

[chunk 874497] If you encrypt the file that you store online and then keep that key with you protected by a similar master password, now the online component alone is much, much harder to decrypt (likely impossible if done correctly) and if your key file gets compromised, you simply re-encrypt your online DB immediately with a new key.
You're still in trouble if someone can compromise your cloud account first and get the file, but it requires two points of compromise instead of one.

[chunk 874498] Personally, I'd probably end up using my OwnCloud (which is self hosted), but I have the advantage of having my own personal web server and I realize that's not an option everyone can take advantage of. (The only reason I haven't is that I don't have a particular need to coordinate a key database in that manner.) A public cloud based solution should work as a fine second option though.

THREAD B
Site: security | Thread title: How difficult to crack keepass master password?
[chunk 850903] KeePass uses a custom password derivation process which includes multiple iterations of symmetric encryption with a random key (which then serves as salt), as explained there.
The default number of iterations is 6000, so that's 12000 AES invocations for processing one password (encryption is done on a 256-bit value, AES uses 128-bit blocks, so there must be two AES invocations at least for each round).

[chunk 850904] With a quad-core recent PC (those with the spiffy AES instructions), you should be able to test about 32000 potential passwords per second.
With ten random characters chosen uniformly among the hundred-of-so of characters which can be typed on a keyboard, there are 1020 potential passwords, and brute force will, on average, try half of them. You're in for 1020*0.5/32000 seconds, also known as 50 million years. But with two PC that's only 25 million years.

[chunk 850905] This assumes that the password derivation process is not flawed in some way. In "custom password derivation process", the "custom" is a scary word. Also, the number of iterations is configurable (6000 is only the default value).

### item Punix-440082-350625
THREAD A
Site: unix | Thread title: Does execution of a file need read permission?
[chunk 435787] When you execute a file, in many cases you don’t need to read it, so you don’t need read permission. You’re right, the system needs to read it on your behalf, but that’s not defined as requiring the read permission (because nothing running as you ever needs access to the file’s contents).

[chunk 435788] The exception is any circumstance where executing a file involves reading it, by a process running with your credentials. So shell scripts, in fact scripts in general, require read permission, as would any executable handled by binfmt_misc.

[chunk 435789] Likewise, accessing a directory doesn’t involve reading it: you can enter a directory without listing its contents. Think of this as exploring a building with a blindfold: execute/search permission allows you to unlock doors to change rooms (as long as you already know where the doors are), read permission allows you to remove the blindfold to see what’s in the room.

THREAD B
Site: unix | Thread title: What is a valid use case for an "execute only" file permission?
[chunk 409724] Shell scripts require the read permission to be executed, but binary files do not:
$ cat hello.cpp
#include<iostream>
int main() {
 std::cout << "Hello, world!" << std::endl;
 return 0;
}
$ g++ -o hello hello.cpp
$ chmod 100 hello
$ ./hello
Hello, world!
$ file hello
hello: executable, regular file, no read permission

[chunk 409725] Displaying the contents of a file and executing them are two different things. With shell scripts, these things are related because they are "executed" by "reading" them into a new shell (or the current one), if you'll forgive the simplification. This is why you need to be able to read them. Binaries don't use that mechanism.
For directories, the execute permission is a little different; it means you can do things to files within that directory (e.
g.
read or execute them).

[chunk 409726] So let's say you have a set of tools in /tools that you want people to be able to use, but only if they know about them.
chmod 711 /tools.
Then executable things in /tools can be run explicitly (e.
g.
/tools/mytool), but ls /tools/ will be denied.
Similarly, documents could be stored in /private-docs which could be read if and only if the file names are known.

### item Punix-345036-122170
THREAD A
Site: unix | Thread title: Alternative of rsync --delete to move files to another directory instead of deleting
[chunk 408054] You can use --backup
-b, --backup
 With this option, preexisting destination files are renamed as each file is transferred or deleted.
in combination with --backup-dir
--backup-dir=DIR
 In combination with the --backup option, this tells rsync to store all backups in the specified directory on the receiving side. This can be used for incremental backups.
to keep a copy of any modified and removed files in a separate directory, on a receiving side.

[chunk 408055] If you want to only keep the deleted files in the backup, you can separately purge the updated files after the sync (e.g. like this).

THREAD B
Site: unix | Thread title: remove duplicate files in 2 directories
[chunk 335701] The code below will search through not just the old directory but also its subdirectories and delete files from the new directory that have the same name and path. This will work with all manor of hostile file names (spaces, newlines, etc.):
cd /folder/files/data/old || { echo "Failed to get in correct directory" ; exit 1 ; }
find . -type f -exec rm -f ../new/{} \;

[chunk 335702] The argument -type f tells find to look for files, not directories. The -exec ... \; argument tells find that, once it finds a file in old, it should run the command rm -f on its counterpart in the new subdirectory.

[chunk 335703] Because rm is given the -f option, it will silently ignore files that don't exist. This eliminates the need for testing for the existence of the file in new before attempting to delete it. Also, it will not prompt before deleting files. This is very handy when deleting a large number of files. However, be sure that you really want to delete the files before running this script. For protection, the script will exit with an error with an error if the cd command fails.

### item Pdba-48408-11614
THREAD A
Site: dba | Thread title: EF Code First uses nvarchar(max) for all strings. Will this hurt query performance?
[chunk 737998] Larger nvarchar (max) data items (over 8000 bytes or so) will spill over into text storage and require additional I/O. Smaller items will be stored in-row. There are options that control this behaviour - see this MSDN article for more details.
If stored in-row there is no significant I/O performance overhead; there may be additional CPU overhead on processing the data type but this is likely to be minor.

[chunk 737999] However, leaving nvarchar (max) columns lying around the database where they are not needed is rather poor form.
It does have some performance overhead and often data sizes are quite helpful in understanding a data table - for example, a varchar column 50 or 100 chars wide is likely to be a description or a free-text field where one that's (say) 10-20 chars ling is likely to be a code.

[chunk 738000] You would be surprised how much meaning that one often has to infer from a database through assumptions like this.
Working in data warehousing, as often as not on poorly supported or documented legacy systems, having a database schema that's easy to understand is quite valuable. If you think of the database as the application's legacy, try to be nice to the people who are going to inherit it from you.

THREAD B
Site: dba | Thread title: SQL Server VARCHAR Column Width
[chunk 718871] The question might be better stated as:
"What is the advantage of over-specifying the maximum length of a variable-length column?"

[chunk 718872] In general, there is little advantage, and several disadvantages as the various linked answers point out. Aside from any other concerns, consider that SQL Server is not open-source: there are many 'magic numbers' and heuristics applied based on the information provided to the system. Without source code access, we could never be entirely sure what the impact of this practice might be.

[chunk 718873] In some cases, where the average length of a column is significantly higher than the 50% assumed by SQL Server when calculating sort/hash memory grants, you may see a performance improvement by over-specifying the maximum length. This is a dubious workaround, and should probably only be applied by an explicit CAST or CONVERT (with comments!) rather than changing the base column definition. Sometimes, it will be preferable to rewrite the query to sort keys instead of whole rows anyway.

[chunk 718874] Where the maximum row size might exceed the in-row limit (even if no rows actually do), deleting rows can cause unexpected page-splitting if a trigger is present. Updates may also lead to fragmentation via the same mechanism.

[chunk 718875] SQL Server does a pretty good job in most cases where it is provided with good, accurate information from metadata. Compromising this principle for 'convenience' seems unwise to me. A sensible approach is to choose a maximum length value that is reasonable according to the actual data to be stored, and any foreseeable changes.

### item Pserverfault-232763-189046
THREAD A
Site: serverfault | Thread title: How to disable ETag headers in Tomcat
[chunk 77095] No way disable out of the box. But ETags are set by the DefaultServlet via request.setHeader(). So an easy workaround to disable them is to create a filter for DefaultServlet which swallows the tag. For example:
void doFilter(ServletRequest request, ServletRequest reponse) {
 chain.doFilter(request, new HttpServletResponseWrapper(response) {
 public void setHeader(String name, String value) {
 if (!"etag".equalsIgnoreCase(name)) {
 super.setHeader(name, value);
 }
 }
 });
}
And in web.xml:

[chunk 77096] <filter>
 <filter-name>noetag</filter-name>
 <filter-class>foo.NoEtagFilter</filter-class>
 </filter>
 <filter-mapping>
 <filter-name>noetag</filter-name>
 <servlet-name>default</servlet-name>
 <dispatcher>REQUEST</dispatcher>
 <dispatcher>FORWARD</dispatcher>
 </filter-mapping>

THREAD B
Site: serverfault | Thread title: When should you use and not use Etags?
[chunk 64235] The main argument I have seen against them is that files that are common to many servers will have to be grabbed over and over again by the client. Better is to include a version string in the name of the file itself.
So for example, if you round robin load balance your web servers each server will generate its own ETag causing the client to grab it multiple times.

[chunk 64236] You can read more on the yahoo high performance website blog. The summary of this is that you can make it work but you have spend the time to configure it right.

### item Punix-463913-28983
THREAD A
Site: unix | Thread title: Delete files with names that appear to begin with '?' in command line
[chunk 442747] The character is not a question mark. The ls utility will replace non printable characters with ?. It is further unclear whether the non printable character really is the first character in the filename or whether there may be one or several spaces before that.
Would you want to delete both those files, you could match the "bad part" with * and then specify the rest of the visible filename more closely:
rm -i ./*ssolve*

[chunk 442748] This would first expand the given pattern to all the filenames matching it, and then rm would remove them. Be more specific and specify a longer part of the filename if there are files that you don't want to delete that matches the above short pattern, e.g. with
rm -i ./*ssolveIncpUL46pK*
This is assuming that you are located in the same directory as the files that you want to delete.
The -i option to rm makes it ask for confirmation before actually deleting anything.

THREAD B
Site: unix | Thread title: How can I delete a file which filename has non-printing characters
[chunk 296012] The file has a name, but it's made of non-printable characters. If you use ksh93, bash, zsh, mksh or FreeBSD sh, you can try to remove it by specifying its non-printable name. First ensure that the name is right with: ls -ld $'\177'
If it shows the right file, then use rm: rm $'\177'
Another (a bit more risky) approach is to use rm -i -- * . With the -i option rm requires confirmation before removing a file, so you can skip all files you want to keep but the one.
Good luck!

### item Psecurity-112672-38845
THREAD A
Site: security | Thread title: Verify password hashed with nonce when the password is already hashed on the server?
[chunk 906575] Am I right to say that this won't work if the password is not stored in plain text on the server? I fail to see how the server could verify the hash if the password is already hashed (with salt and pepper) on the server.
This scheme does require the password to be stored in clear-text. Very bad.
Can this scheme be extended to work with hashed passwords somehow?

[chunk 906576] I'm sure it can, but there's no need. The scheme you've referenced is the HTTP digest authentication protocol. It was written in a day when SSL was considered to expensive to implement in many systems. Digest authn provided a way to login over clear-text channels without exposing the password. There's absolutely no reason to do that anymore. SSL is now effectively free.

[chunk 906577] In general, the risk of storing passwords on the server is considered to outweigh the benefit of having the server not having your password in memory for a short period of time (time from reception of password message until hashing begins and the cleart-text password's memory can be erased).

[chunk 906578] There are some situations where client-side hashing can make sense. For example, LastPass implements a unique authentication mechanism that involves both client and server hashing. They do this because they use your password as the basis for creating your encryption key and they never want the server to know your encryption key. So what they do is:
Many rounds of PBKDF2 on client to create a strong encryption key.

[chunk 906579] One round of SHA-256 to turn encryption key into what is effectively your password.
Send password to server. Note that the properties of SHA-256 make it computationally impossible to reverse the password back to your encryption key.
Server performs standard server-side hashing using PBKDF2 and salt.
Basically, the LastPass server does standard password storage but what it gets as a "password" is the result of client-side hashing.

THREAD B
Site: security | Thread title: How can salted, hashed password storage be combined with a plaintext, nonce and hash based authentication?
[chunk 870223] Yes, this is possible. There are two algorithms described here which both avoids the need to store plaintext-equivalents on the server (while making it possible to authenticate without the need to send plaintext password over the wire).

### item Pdba-203934-203975
THREAD A
Site: dba | Thread title: PostgreSQL alternative to SQL Server’s `try_cast` function
[chunk 801555] If casting from one specific type to one other specific type is enough, you can do this with a PL/pgSQL function:
create function try_cast_int(p_in text, p_default int default null)
 returns int
as
$$
begin
 begin
 return $1::int;
 exception 
 when others then
 return p_default;
 end;
end;
$$
language plpgsql;
Then
select try_cast_int('42'), try_cast_int('foo', -1), try_cast_int('bar')
Returns
try_cast_int | try_cast_int | try_cast_int
-------------+--------------+-------------
 42 | -1 |

[chunk 801556] If this is only for numbers, another approach would be to use a regular expression to check if the input string is a valid number. That would probably be faster than catching exceptions when you expect many incorrect values.

THREAD B
Site: dba | Thread title: Safely quoting type names to protect against SQL-injection
[chunk 801573] How would I quote the type name to protect against SQL Injection.
You do not need format_type() for the purpose. You may have misunderstood Andrew there. All you need is the cast to regtype:
SELECT format('SELECT cast(%L AS %s);', '5.42', 'int'::regtype);
The text representation of the regtype value is the standard SQL name and quoted automatically where needed - and the value is cast to text implicitly for the concatenation. Demo:

[chunk 801574] SELECT 'varchar(20)'::regtype, 'int'::regtype, '"char"'::regtype;
regtype | regtype | regtype
------------------+---------+---------
character varying | integer | "char"
format_type() would only serve to add type modifiers (which are lost in the cast), an orthogonal matter. Related:
PL/pgSQL regclass quoting of table named like keyword
How to introspect materialized views
PostgreSQL syntax error in parameterized query on “date $1”
Table name as a PostgreSQL function parameter

### item Pserverfault-912094-840996
THREAD A
Site: serverfault | Thread title: apache2: Saves files on /tmp in a 'system-private-[hash]' instead of just saving folders as defined in the code
[chunk 239518] That is a systemd security setting that creates a service specific private temp directory.
Your apache systemd unit will file have a setting:
...
[Service]
ExecStart=...
PrivateTmp=yes
...

[chunk 239519] This option will ensure that the /tmp directory the service will see is private and isolated from the host system's /tmp. /tmp traditionally has been a shared space for all local services and users. Over the years it has been a major source of security problems for a multitude of services. Symlink attacks and DoS vulnerabilities due to guessable /tmp temporary files are common. By isolating the service's /tmpfrom the rest of the host, such vulnerabilities become moot.

[chunk 239520] Source: http://0pointer.de/blog/projects/security.html
You can configure multiple services to share a PrivateTmp with JoinsNamespaceOf= which may be desirable to setting PrivateTmp=no

THREAD B
Site: serverfault | Thread title: Modify systemd unit file without altering upstream unit file
[chunk 226185] You have two options:
Copy the unit file from /lib/systemd/system/ to /etc/systemd/system/.
And then make your modifications in /etc/systemd/system/pimd.service to completely override the unit file(s) supplied by the package maintainer.
The command systemctl edit --full <service-name> automates this for you.

[chunk 226186] You can alter or add specific configuration settings for a unit, without having to modify unit files by creating .conf files in a drop-in directory /etc/systemd/system/<unit-name>.<unit-type>.d/
i.e. create a /etc/systemd/system/pimd.service.d/restart.conf
The command systemctl edit <service-name> performs these steps for you.
See man systemd.unit

### item Punix-721364-672996
THREAD A
Site: unix | Thread title: Searching for a missing number in a sequence of numbers
[chunk 511912] Using Raku (formerly known as Perl_6)
~$ raku -e 'my @a; for lines() {@a.push: $/.Int if .match(/<?after \"index\"\: \s > \d+ /) }; \
 put ((1..10) (-) @a.Set).keys.sort;' index.txt
#OR
~$ raku -e 'my @a; for lines() {@a.push: $0.Int if .match(/<?after \"index\"\: \s > (\d+) /) }; \
 put ((1..10) (-) @a.Set).keys.sort;' index.txt
Raku is a programming language in the Perl-family. It was released in 2015 as Perl_6, and renamed Raku in 2019. Consequently, you'll find many "Perl-isms" in Raku.

[chunk 511913] One interesting feature of Raku is Set semantics. Unicode as well as ASCII operators are available. In the code above, ASCII (-) stands for Set difference (non-symmetric). You can also use Unicode:
∖
SET MINUS
Unicode: U+2216, UTF-8: E2 88 96
Sample Input (note max value is 100):
"index": 1
"index": 2
"index": 3
"index": 5
"index": 100
Sample Output (both code examples):
4 6 7 8 9 10

[chunk 511914] Caveat: It can be easy to confuse symmetric and non-symmetric Set operations. For example, with the code above if you reverse the order of sets and try the ASCII (^) or Unicode ⊖ symmetric Set difference operator instead, you'll see a big difference (using 1..99 as the test range):

[chunk 511915] ~$ cat index.txt | perl6 -e 'my @a = do for lines() {$/.Int if .match(/<?after \"index\"\: \s > \d+ /) }; put (@a.Set (-) (1..99)).keys.sort;'
100
~$ cat index.txt | perl6 -e 'my @a = do for lines() {$/.Int if .match(/<?after \"index\"\: \s > \d+ /) }; put (@a.Set (^) (1..99)).keys.sort;'
4 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75

[chunk 511916] 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
https://docs.raku.org/language/setbagmix
https://raku.org

THREAD B
Site: unix | Thread title: How can I see if a consecutive number name file is missing some file?
[chunk 498539] You could use Awk to filter out the missing ones. On GNU Awk, with support for multi-char FS, you could pipe your result to
awk -F'[_.]' ' $2 != prev+1 { print "file " prev+1 " missing" }{ prev = $2 }'
Or using perl
perl -F'[_.]' -ane 'if ($F[1] != $prev+1) {printf "file %d missing\n",$prev+1}; $prev=$F[1]'
If there are more gaps anticipated, you could have awk print out the range of file numbers missing. Modifying the above

[chunk 498540] awk -F'[_.]' ' $2 != prev+1 { print "file(s) " prev+1 "-" $2-1 " missing" }{ prev = $2 }' file

### item Punix-345975-137842
THREAD A
Site: unix | Thread title: Configure shortcut on Vim to save file
[chunk 408335] Vim comes with a file providing some mappings intended to match Windows files. This is usually in $VIMRUNTIME/mswin.vim (run :echo $VIMRUNTIME to see what it is for you). You can just do:
:source $VIMRUNTIME/mswin.vim
And get a bunch of shortcuts, including CtrlS. See :h mswin.vim for more.
Note that your terminal emulator might use CtrlS for other purposes, but that's outside Vim.
To just create a mapping to test, do:
nnoremap <c-s> :w<cr>

THREAD B
Site: unix | Thread title: What is the point of Ctrl-S?
[chunk 341697] Long before there were computers, there were teleprinters (a.k.a. teletypewriters, a.k.a. teletypes). Think of them as roughly the same technology as a telegraph, but with some type of keyboard and some type of printer attached to them.

[chunk 341698] Because teletypes already existed when computers were first being built, and because computers at the time were room-sized, teletypes became a convenient user interface to the first computers – type in a command, hit the send button, wait for a while, and the output of the command is printed to a sheet of paper in front of you.

[chunk 341699] Software flow control originated around this era – if the printer couldn't print as fast as the teletype was receiving data, for instance, the teletype could send an XOFF flow control command (Ctrl+S) to the remote side saying "Stop transmitting for now", and then could send the XON flow control command (Ctrl+Q) to the remote side saying "I've caught up, please continue".

[chunk 341700] And this usage survives in Unix because modern terminal emulators are emulating physical terminals (like the vt100) which themselves were (in some ways) emulating teletypes.

### item Psecurity-249274-82596
THREAD A
Site: security | Thread title: Concerning GET request in logs
[chunk 962493] Can anyone help me determine if this is something I should be concerned about?
Someone is trying to exploit a vulnerability on your server. References to cmd.exe, System.Net.WebClient and %SystemRoot% indicates this exploit is intended to a Windows server.
It shows your server returning HTTP 404, with 2111 bytes on the response (those last 2 values on your log). That means your server does not have the vulnerable /public/index.php file, so no damage was done on this case.

[chunk 962494] Your websocket probably is dying because you aren't properly processing unexpected input, and this is a MASSIVE SECURITY ISSUE (bold capitals because I cannot use blinking red text font). Failing to detect malformed input and reacting to that is the source of countless exploits.

[chunk 962495] If you don't know much about security, you can be sure that your server will be hacked sooner or later. Take your server offline, install a Linux VM on your desktop, and train on your VM first. Read articles on Linux hardening, on securing Nginx and Django, on secure coding. Your server can be a threat to anyone on the internet as soon as someone hacks it and turns it into a hacking platform to launch attacks.
nobody else is using this server currently

[chunk 962496] As soon as your server is reachable from the internet, that statement is not true anymore.

THREAD B
Site: security | Thread title: Why am I getting strange HTTP requests for non-existing pages?
[chunk 891869] These types of spurious requests are very, very common. They are either looking to see if you are already compromised, or looking to get your server to throw an error to gather info about your server (from error messages).
You aren't the only one:
http://shadow.wolvesincalifornia.org/awstats/data/awstats092014.shadow.wolvesincalifornia.org.txt

[chunk 891870] # URL with 404 errors - Hits - Last URL referer
BEGIN_SIDER_404 193
/admin.php 1 -
/root/back.css 1 -
/drdr/drd/dr.php 2 -
/hkhk/hkh/hk.php 1 -
/wp/2011/07/19/& 6 -
/ahah/aha/ah.php 1 -
/andro/back.css 1 -
/wp/comments/feed/ 1 -
/wjwj/wjw/wj.php 1 -
We all get spammed by these requests.