### item Tserverfault-896535
Site: serverfault | Thread title: Possible to see btrfs defrag progress?
[chunk 236634] You can use -f to flush, otherwise it works in batches and may stall. If it's printed the file then it's done, subject to caching / locking (hopefully not any filesystem errors).
-f flush data for each file before going to the next file.
-r defragment files recursively in given directories.

[chunk 236635] Note: Directory arguments without -r do not defragment files recursively but will defragment certain internal trees (extent tree and the subvolume tree). This has been confusing and could be removed in the future.
-v be verbose.
$ btrfs filesystem defrag -v -r dir/

[chunk 236636] Recursively defragment files under dir/, print files as they are processed. The file names will be printed in batches, similarly the amount of data triggered by defragmentation will be proportional to last N printed files. The system dirty memory throttling will slow down the defragmentation but there can still be a lot of IO load and the system may stall for a moment.
$ btrfs filesystem defrag -v -r -f dir/

[chunk 236637] Recursively defragment files under dir/, be verbose and wait until all blocks are flushed before processing next file. You can note slower progress of the output and lower IO load (proportional to currently defragmented file).

### item Tsoftwareengineering-83064
Site: softwareengineering | Thread title: GUI, BLL, DAL Organization In A Project
[chunk 550380] Yes. And also assemblies.
I'd separate by layers, then components.
Yes.
There are different approaches to this, but I'd have an IDatabaseService (abstracting the various manners in which the database is called -- this can almost be a direct mapping of the ExecuteScalar/ExecuteNonQuery/ExecuteReader), and then various data access classes that partition by type of data.
For example, you could have a UserDataAccess class that would have simple CRUD methods that create/modify/delete User objects.

[chunk 550381] Another approach would be to have a User object that has the CRUD built right in.
No. That makes it much harder to unit test. You should use dependency injection to pass in dependencies to the constructor of each data access class (such as an IDatabaseService). You would then pass the data access objects into the business objects, like this:
BusinessObject businessObject = new BusinessObject(new DataAccessObject(new DatabaseService()));
businessObject.PerformOperation();

[chunk 550382] Each business object may need multiple data access objects. Your GUI code would also use one or more business objects. Some business objects may not need any data access objects but should never use the IDatabaseService directly.

### item Tunix-18701
Site: unix | Thread title: Share the clipboard between bash and X11
[chunk 290843] Bash's clipboard is internal to bash, bash doesn't connect to the X server.
What you could do is change the meaning of M-w to copy the selection to the X clipboard¹ in addition to bash's internal clipboard. However bash's integration is pretty loose, and I don't think there's a way to access the region information or the clipboard from bash code. You can make a key binding to copy the whole line to the X clipboard.²

[chunk 290844] if [[ -n $DISPLAY ]]; then
 copy_line_to_x_clipboard () {
 printf %s "$READLINE_LINE" | xsel -ib
 }
 bind -x '"\eW": copy_line_to_x_clipboard'
fi
If you want to do fancy things in the shell, switch to zsh, which (amongst other advantages) has far better integration between the line editor and the scripting language.

[chunk 290845] if [[ -n $DISPLAY ]]; then
 x-copy-region-as-kill () {
 zle copy-region-as-kill
 print -rn -- "$CUTBUFFER" | xsel -ib
 }
 x-kill-region () {
 zle kill-region
 print -rn -- "$CUTBUFFER" | xsel -ib
 }
 zle -N x-copy-region-as-kill
 zle -N x-kill-region
 bindkey '\C-w' x-kill-region
 bindkey '\ew' x-copy-region-as-kill
fi
¹ 
Gnome doesn't specifically have a clipboard, this is general to X.

[chunk 290846] ² 
As of bash 4.1, there is a bug in the key parsing code: key sequences bound with bind -x may not be more than two characters long. I think bash 4.2 fixes some cases of longer prefixes but not all of them; I haven't researched the details.

### item Tdba-5528
Site: dba | Thread title: Rebooting a MySQL Replication Slave
[chunk 715401] This looks right. The slave will pick up where it left off when it starts back up.
I will note that unless you supply the --skip-slave-start option, the slave should start automatically.

### item Tdevops-8253
Site: devops | Thread title: What artifact managers are available in GCP?
[chunk 997150] If the artifacts in question are docker images then the recommended artifact management solution is the Container Registry, well integrated with other GCP products producing and/or using such images.
AFAIK they don't have a real artifact manager for other kinds of artifacts, they suggest the rather general purpose Cloud Storage for that. You can find an example of such use in the Quickstart for Go guide. Most likely not what you're looking for:

[chunk 997151] artifacts:
 objects:
 location: 'gs://[BUCKET_NAME]/'
 paths: ['hello']

### item Tnetworkengineering-50916
Site: networkengineering | Thread title: Destination device disconnects while packet was in transit
[chunk 985522] As they say, timing is everything. Because a packet can travel around the world in just a few tens of milliseconds, what happens depends on exact timing.

[chunk 985523] Assuming the new device is on the same network, the last hop router will forward the packet according to its ARP table. If the router has not been able to update its ARP table with the new host MAC address in time, it will forward the packet to a non existent MAC address, and no one will respond. If there is a switch, it will either forward the packet to the old port, or it will flood the packet on all ports. In either case, no one will respond to the packet.

[chunk 985524] If the router and switch have had enough time to update their tables, the packet will be delivered to the new host.

### item Tsecurity-34258
Site: security | Thread title: Secure login system - using sessions?
[chunk 866930] A more secure way? Use https along with this. There are two vulnerabilities here:
When the user logs in, the password that is sent over can be easily read by anyone snooping on your connection. This can't happen on an https connection.
If a user is already logged in, someone snooping on your connection can just copy over the session cookies. In HTTPS, cookies are transmitted securely, so there isn't much of an issue.

[chunk 866931] You may also want to log the user IP address and not let them switch, though this may get annoying (for a user like me who is behind a university proxy with rotating external IPs, I'll never be able to log in).

[chunk 866932] A final observation: Don't use GET for the log out bit.. Try not to use GET for anything which triggers a change -- it's fine for navigation, but not for anything which will lead to something changing on the server (a logout, or anything that writes to a database). See the prescribed usage of GET and POST for more details.

[chunk 866933] If you implement the above, then also make sure that the referrer of a POST request is your site and not some other site. (This, along with the above, will help prevent CSRF attacks).
To prevent clickjacking, disable framing via javascript and the X-Frame-Options: deny header.

### item Tserverfault-800174
Site: serverfault | Thread title: proxmox install on ubuntu
[chunk 217832] They both use apt as a package manager, but Ubuntu diverges greatly in tis package offering from Debian. Proxmox installs and runs on Debian, so you'll have to explicitly install some Debian packages to get it to work.
However, what you'll find is that the dependency chain runs straight to crazy town, and that you'll be replacing almost every package on your Ubuntu system with Debian repository packages. Then you get a super broken Ubuntu install that is for the most part Debian.

[chunk 217833] I can't think of any great reasons to use Ubuntu over Debian for this task anyways. On top of that, Proxmox is a distribution. While it's possible to install all of its relevant packages on an existing server (as I hastily described above), that would be a very silly thing to do.

### item Tsoftwareengineering-118064
Site: softwareengineering | Thread title: Is it necessary to know and understand design patterns in order to be a professional programmer?
[chunk 565047] No. I only say that to be pedantic though. The term "professional programmer" really just means you get paid to program. I assure you that you can be paid to program without knowing any design patterns (I certainly did, for a few years).
However, knowing design patterns has some benefits:
It's a way that other programmers tell us about general ways that they've solved general classes of problems.

[chunk 565048] It's a name that you can apply to a specific pattern, and other programmers who know that pattern will understand what you mean. You can even put it into the name of the methods and classes (XyzSingleton, for instance).

[chunk 565049] In many ways it's a good way to learn the shortcomings of programming languages and paradigms. For instance the Visitor pattern exists because in object-oriented programming you typically have to make a choice between an architecture where it's easier to add new types that exhibit the same interface, or easy to add new behaviors to existing types, but doing both gets complicated. Thinking about these problems informs your design decisions.

### item Tunix-8813
Site: unix | Thread title: Should the usage message go to stderr or stdout?
[chunk 285276] It should go to stdout, so you can type:
command --help | less
This is also recommended by the Gnu Coding Standards on --help.
On the other hand, the usage message that you get when you use an invalid option or omit a required argument should go to stderr, because it's an error message, and you don't want it to feed into the next command in a pipeline.

[chunk 285277] When you use --help, the usage message is the normal and expected output of the command. Therefore, it goes to stdout, so it can be piped to another command, like less or grep.

[chunk 285278] When you say command --bogus-option | other-command, you don't want the usage message going to stdout, because it's now unexpected output that should not be processed by other-command. Also, if the output of --help is more than a handful of lines, then the usage error message should only contain a summary of the --help output, and refer the user to --help for additional details.

### item Tdba-230043
Site: dba | Thread title: SELECT very slow when JOIN and LIMIT are specified but no/few results found
[chunk 811359] There are several things that you can try:
Add the status in sessionlatest table. Since this table is like a "cache" of the latest session, it makes absolute sense to do so (@jjanus suggestion). The WHERE - ORDER BY - LIMIT would all involve columns from the same (and smaller) table, so a suitable index could be used effectively (and then the join to the big table would only have to find the relevant 500 rows).

[chunk 811360] I don't understand why you are joining on update_id and not session_id. This has not a good effect on the execution plan. You want to ORDER BY and LIMIT by session_id but the join is on another column. Perhaps you do that in order to get a single entry per session. The query could be rewritten to use session_id instead.
I would try to use LATERAL JOIN starting from the smaller table.
See this (using update_id or session_id or both):

[chunk 811361] select gs.*, gsl.*
from sessionlatest gsl
 join lateral
 ( select s.*
 from session s
 where s.session_id = gsl.session_id
 and s.update_id = gsl.update_id
 order by s.update_id desc
 LIMIT 1
 ) as gs
 on gs.status = 'STARTED'
order by gsl.session_id desc
limit 500 ;
I think the above would result in a better execution plan, if you had an index on session (session_id, update_id) but it's better if you tested with your tables (sizes, distribution, several things matter for performance).

[chunk 811362] See the dbfiddle.uk.

### item Tdevops-49
Site: devops | Thread title: What are the pro and cons of SnowFlakes Servers, Phoenix Servers and Immutable Servers?
[chunk 993695] The term Phoenix Server was coined by a fellow of Martin Fowler, and all three terms described in short articles on Martin's bliki.
Snowflake Server
Phoenix Server
Immutable Server
The pros and cons of each such server are described in the articles. The main difference being in the way the server is managed.

[chunk 993696] Servers exist to fulfill the role of a container for some application(s). Since applications change often, it is often required to change some attributes of the container - such as packages, configuration, etc. It is also sometimes required to change attributes of the container itself because of external reasons, such as security vulnerabilities that require patches to be installed.
There are several ways to change an existing server:

[chunk 993697] Manually create the server initially, then keep changing its content (mutating) each time a change is required.
"Bake" an image for a server based on a recipe, usually in an automated way (not manually). Then create servers from that image. And repeat this process on every change.

[chunk 993698] The former is called Snowflake, while the latter is a practice that allows Phoenix and Immutable server types. Where Immutable states that no changes are made to an existing server once it was created, and Phoenix means that a server is destroyed completely and a new one is used to replace it during the change process.

### item Tnetworkengineering-3754
Site: networkengineering | Thread title: Plexiglass and 2.4GHz wifi signal
[chunk 972822] Robert Wilson, a graduate student at USC, prepared an analysis of 2.4GHz and 5GHz propagation through common materials, with a useful Table 3. It looks like Plexiglas incurs about a .36dB loss at 2.3GHz and about a .93dB loss at 5.25GHz, in addition to the slowdown caused by the slower speed inside the material.
You probably wouldn't notice any decline in connection quality through walls of a normal thickness, though for a mouse, there might be enough lag to interfere with gaming.

### item Tsecurity-29796
Site: security | Thread title: Is Chrome giving out information about me?
[chunk 863954] I've been looking into this recently and, yes, Google are collecting information as you use Chrome but Google claim to collect this data anonymously.
Be aware that 'anonymously' in this context means it is difficult for Google to personally identify you but they can combine some pieces of information to identify the collective activities of an anonymised user through the use of a unique ID. Not all of the telemetry from Chrome uses the unique ID though, some of it is completely anonymous.

[chunk 863955] There is a a very good description here:
https://www.google.com/intl/en/chrome/browser/privacy/whitepaper.html
Obviously this is a biased source but I came across it while I was looking at Chrome's privacy controls.
Regards.

### item Tserverfault-121766
Site: serverfault | Thread title: WebDav rename fails on an Apache mod_dav install behind NginX
[chunk 44550] (Back to the days when I used Subversion) I had similar problem with proxying to Apache SVN from Nginx SSL frontend. Suppose Nginx SSL frontend is https ://host and we'd like to proxy connections to the internal Apache SVN server http ://svn
The problem occurs when you try to copy a resource is with Destination header:
COPY /path HTTP/1.1
Host: host
Destination: https://host/another_path
As you can see Destination header still contains https schema. The fix is pretty evident --

[chunk 44551] location / {
 # to avoid 502 Bad Gateway:
 # http://vanderwijk.info/Members/ivo/articles/ComplexSVNSetupFix
 set $destination $http_destination;
if ($destination ~* ^https(.+)$) {
 set $destination http$1;
 }
proxy_set_header Destination $destination;
 proxy_set_header Host $host;
 proxy_set_header X-Forwarded-For $remote_addr;
proxy_pass http://svn;
}

### item Tsoftwareengineering-350058
Site: softwareengineering | Thread title: Using partial classes hide controller complexity
[chunk 663001] Your approach is not common practice and may raise a few issues, since Visual Studio is optimized to work a different way.
easy to find the controller method in solution explorer
 one file ( one partial class ) contains only a single method and its internal utility methods (if there is any).
Visual Studio provided dropdowns in the top of the code pane that allow you to quickly find a method. Also, VS supports regions that can be named, nested, hidden, and shown as needed.

[chunk 663002] If a utility method is used by multiple controller methods, then I organize them in a common place
What about a utility method that was previously defined in one of your method files, but later you discover you need to call it from a new method? You'd have to move it. Not only is that a PITA, but it will break history in your code repository.
a method is never longer than a common screen size for two reasons

[chunk 663003] No reasons necessary; short methods are a good practice in general. One way to keep methods short is to break them into smaller methods. But-- using your approach, there is actually a disincentive to break up longer methods, because the developer will have to add a new file each time. God help a developer who is restructuring code and wants to to be able to add/remove/restructure a whole lot of methods at once.

[chunk 663004] The only advantage I can think of is this: in the "one file" approach, if a developer decides to move a method around (e.g. move it from the bottom to the top) it can cause code merges to get confused. If there is only one method per file, this is a non-issue. But-- on the other hand, if a method name changes, under your system the file name would change as well, and merges might get skipped entirely.

### item Tunix-420594
Site: unix | Thread title: Why process killed with nohup
[chunk 430253] As far as I know, there are two situations that can cause a process to be killed after being protected by nohup, and each situation has a different workaround.
One possibility, which does not appear to be the case here, is that the system uses systemd where logind.conf is configured with KillUserProcesses=yes. In this case, closing the terminal will not cause problems, but logging out of the system will. The workaround in this case is to use
$ systemd-run --scope --user [command]

[chunk 430254] This basically just tells systemd that it should not kill the process.
The other possibility is that the spawned process implements its own handler for SIGHUP which overrides the protection of nohup. In this case, problems will occur as soon as the shell is closed, even if you remain logged in. You can check for this with:
$ nohup [command] &
$ grep Sig /proc/$!/status
You should see a line
SigIgn: 0000000000000001

[chunk 430255] (or some other string of hexadecimal digits). SIGHUP is signal number 1, so if this big-endian hexadecimal number has its first (least-significant) bit set (that is, the final digit is one of 1, 3, 5, 7, 9, B, D, or F), then SIGHUP is ignored. Otherwise, the program has installed its own handler overriding the protection of nohup.
In this case, the solution is to use disown:
nohup [command] & disown

[chunk 430256] This removes the process from the shell's job list, preventing SIGHUP from being sent in the first place.

### item Tdba-64896
Site: dba | Thread title: Determining the tables and impact of a large number of SPs
[chunk 745862] If you know for sure that these 35 programmables are the culprits a combination of Profile/Events for elapsed time and cached plans, plus sys.dm_exec_query_stats should get you a long way to understanding where about the pain lies.
@Paul's comment about recording a baseline is important, though.

### item Tdevops-12398
Site: devops | Thread title: Properly shutdown k3s on local machine
[chunk 998493] There is a systemd shutdown task (/etc/systemd/system/k3s.service) which stops the server, but not the k8s resources (pods, networks, etc). For this there is a utility script k3s-killall.sh which should be at /usr/local/bin/k3s-killall.sh

### item Tnetworkengineering-2665
Site: networkengineering | Thread title: What OSI layer do Access Points operate on?
[chunk 972323] Strictly speaking, access points are a L2 device. Their primary function is to bridge 802.11 WLAN traffic to 802.3 Ethernet traffic.
However, in the real world, enterprise wireless vendors often push more functionality to either the AP itself and/or tie them into a controller, with the end result that they often incorporate functionality from higher layers as well.

[chunk 972324] I don't entirely follow #1, but neither the connection to a switch or router nor the use of CSMA-CA has anything to do with their function as a L2 device. It is a L2 device because that is the layer of the network where it is designed to function. It doesn't care nor need L3 or above to operate and allow devices to communicate (again strictly speaking).

[chunk 972325] As for #2, yes, an AP (or any bridge) needs to keep track of which interface any individual device is connected. In general (and simply), they work on the principle of frames destined to an associated station gets forwarded out the wireless interface and any other frames get forwarded out the wired interface (or sent to the controller).