### item Tsoftwareengineering-312956
Site: softwareengineering | Thread title: What does a load balancer return?
[chunk 645693] The end-IP is not published. The process actually works in a way the client (a user hitting the balancer) believes they are communicating with the balancer, while talking to an actual node.
In a very simple explanation, most transactions work like this:
A user makes request to the load balancer.
The balancer decides which node is the most suitable (based on the strategy you're using for balancing) and choses (changes) the destination IP.

[chunk 645694] (This is where the magic happens.) The node receives a request, accepts the connection and responds back to the balancer.
The balancer changes the response IP back to a virtual one, the one of the balancer and forwards the response to the user.
Voilà, the user receives response with the IP of the initial request, even though it was actually processed somewhere else.

[chunk 645695] Keep in mind the packet rewriting (the change of the IP address in the step 4) is very important. Without it the client, receiving a packet from an IP it does not trust, would simply discard the response.

### item Tunix-14459
Site: unix | Thread title: Vim keybinding to delete up to (but not including) the next period
[chunk 288421] Btw, if you want to delete a sentence you can use the sentence forward motion like this:
d)i.
Meaning, deleting the sentence including the period and then inserting it again.
d/\. is necessary, if you want to delete multiple lines and there is a non-text document context, e.g. empty lines in between text and you really want to delete to the next period.
If the period is on the same line, you can just use the till-before motion: dt.
Typing
:normal d/\.^M
(Ctrl+V + Enter at the end)
works for me.

[chunk 288422] But I have to say that I don't understand the need for :normal.
I mean, using
:map <F10> d/\.<CR>:noh<CR>
the search starts at the position where the cursor is located and ends at the next period.

### item Tdba-233513
Site: dba | Thread title: Non-deterministic sum of floats
[chunk 812709] Actually, the link you're referring to does not say that floating point arithmetic calculations are always deterministic. In fact, in one of the answers it's mentioned that addition is not associative (meaning (a + b) + c does not necessarily equal a + (b + c)), which is also said in this answer.

[chunk 812710] If stream aggregation happens to process rows of each group in different order -- which SQL Server is usually free to do; if there is no ORDER BY in the appropriate clause, then the optimizer will choose whatever scan or seek or other query operator will be fastest, regardless of what order that performs the additions in -- then this could explain the behaviour you observe.

[chunk 812711] Addition is always deterministic: you put in the same two floats, you get the same float out. But adding floats together in a different order can give a different result.

### item Tdevops-261
Site: devops | Thread title: DynamoDB vs RDS for a counter store?
[chunk 993908] Why not something like Redis? (can use it through ElastiCache). Hard to answer this without knowing the operational requirements of this project. Is this data strictly for logging/research, or is it operational (i.e. this "table" is consulted in order to know which lambda to invoke).

[chunk 993909] Dynamo vs. RDS - depends how spiky your traffic is. Dynamo is very scalable and will give you a guaranteed throughput. But if you traffic can grow 10x over hours (spiky) Dynamo might be too expensive, since you'll need the maximum throughput provisioned or else you'll get throttled.
RDS is basically managed RDBMS on an instance type that you choose, so it can handle larger spikes, but ultimately not as scalable as Dynamo.

[chunk 993910] Again, I would consider Redis, for it's simplicity (seems like you just need a KV/counter store), and incredible speed/efficiency. If it's just for logging, it's probably good enough.

### item Tnetworkengineering-83184
Site: networkengineering | Thread title: How PoE interacts LLDP and LLDP-MED?
[chunk 993262] PoE power allocation can happen on the physical layer by signature resistance, or on the data link layer by LLDP TLV (PD→PSE). Which one takes precedence is a matter of configuration in your switches/PoE injectors (PSE).
LLDP can be used for lots of other purposes. LLDP-MED is a mechanism that is mainly used to pass information to an IP phone, like VLAN, DSCP, room, street address (switch→phone). I may also be used as an alternative to native PoE TLVs but may be completely unrelated as well.

[chunk 993263] Is PoE TLV exclusive to LLDP-MED or not?
No - there's native LLDP PoE TLV and there's LLDP-MED, alternatively.
What fields of PoE TLV are mandatory and which are optional for a 802.3at implementation?
LLDP TLV are only mandatory if your PSE is configured to require them. You can use L1 allocation exclusively.
If LLDP PoE TLV includes all the fields from above (as the standard indicates), what additional fields does LLDP-MED brings to PoE?

[chunk 993264] Basically, LLDP MED allows for more granular power allocation (by device/phone type/model) than native PoE TLV (by power class alone). But it all depends on the devices you use and their configuration.

### item Tsecurity-266377
Site: security | Thread title: Does ISO27001 require to use Github Enterprise Single Sign on?
[chunk 968104] We've just gone through ISO27001 Certification (and achieved it) and were not required to change to GitHub Enterprise - although it was an option.
As long as we had the right controls in place to manage the risks, there was no mandate to use a particular technical solution.
From what we can tell as long as you've got the processes documented and they are being followed - that is the important thing.

[chunk 968105] We did have to do the following (some of which we'd already started before our ISO journey kicked off):
Protect main branches
Require PRs into main
Create PR templates (.github/pull_request_template.md) with checklists of items for developers to check off when creating/updating PRs
Ensure we had the correct approvals in place (in our case managed with GitHub teams)

[chunk 968106] We did have some disagreements with our assessor around the detail required in the policies, but in the end as long as the policies are approved by the appropriate person, then that is generally enough (at least in our experience).

### item Tserverfault-342530
Site: serverfault | Thread title: How to download public key from Amazon AWS?
[chunk 109270] Nice puzzle, thanks! Here's one answer:
Start a new, temporary EBS boot t1.micro instance A, specifying keypair p2. Specify an availability zone where you have another instance B already running and to which you have access. (Start a temporary one if needed).
Stop (not terminate) the instance A after it has been in the running state for a few minutes, so it has a chance to save the public key to its authorized_keys file.

[chunk 109271] Detach the root EBS volume from the stopped instance A. Attach and mount it to your running instance B.
Copy the public key from the mounted file system.
Detach and delete the EBS volume. Terminate the temporary instance A.

### item Tsoftwareengineering-241583
Site: softwareengineering | Thread title: What license is the GPL License licensed under?
[chunk 619036] The terms under which the text of the various versions of the GPL may be distributed are quite clearly given in the opening lines of the licences:
GNU General Public License, Version 3:
Copyright © 2007 Free Software Foundation, Inc. http://fsf.org/
Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
GNU General Public License, Version 2:
Copyright (C) 1989, 1991 Free Software Foundation, Inc.

[chunk 619037] 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
GNU General Public License, Version 1:
Copyright (C) 1989 Free Software Foundation, Inc.
51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

### item Tunix-483701
Site: unix | Thread title: Why do commands starting with a space, not show up in bash history?
[chunk 448265] Check the value of your HISTCONTROL environment variable. If the value contains ignorespace or ignoreboth, any command starting with a space will not be added to command history.
From man bash:
HISTCONTROL:
 A colon-separated list of values controlling how commands are saved on the history list.
If the list of
 values includes ignorespace, lines which begin with a space character are not saved in the history list.

[chunk 448266] A value of ignoredups causes lines matching the previous history entry to not be saved.
A value of
 ignoreboth is shorthand for ignorespace and ignoredups.
A value of erasedups causes all previous lines
 matching the current line to be removed from the history list before that line is saved.
Any value not
 in the above list is ignored.
If HISTCONTROL is unset, or does not include a valid value, all lines
 read by the shell parser are saved on the history list, subject to the value of HISTIGNORE.

[chunk 448267] The second
 and subsequent lines of a multi-line compound command are not tested, and are added to the history
 regardless of the value of HISTCONTROL.

### item Tdba-254655
Site: dba | Thread title: RDS MySQL 8.0.16 has empty "INFORMATION_SCHEMA.ST_SPATIAL_REFERENCE_SYSTEMS" table
[chunk 819819] The new MySQL v8.0.16 image on RDS (as of writing this) is missing spatial references other than SRID 0.
As a workaround, you can create a new instance with v8.0.15 and then perform the minor upgrade (requires reboot).
select count(*) from INFORMATION_SCHEMA.ST_SPATIAL_REFERENCE_SYSTEMS
...returns:
5152

### item Tdevops-2909
Site: devops | Thread title: Pause/Suspend guest in KVM without virsh and libvirtd
[chunk 995510] After long searching and experiments, the best option for me became qemu monitor. See https://nico.schottelius.org/blog/control-and-shutdown-qemu-kvm-vm-via-unix-socket/ for more details regarding flexible management guest by using qemu monitor.

### item Tnetworkengineering-23229
Site: networkengineering | Thread title: Network design question
[chunk 977439] First of all, as they mentioned above it is a poor design. No security engineer would consider exposing their servers directly to public without having any defenses (IPS, Firewall DMZ or host based firewalls)...
Still to answer your questions technically,

[chunk 977440] There is no need to do NAT at the firewall for your public server since you may already have default route towards outside to facilitate the public Internet traffic so this public server IP also would be reachable (or adding a route for this public server will work).
It is fine, if you could add route in the public server for the complete private subnet towards firewall outside to reach internal network (because, it make no sense to route private subnet towards Internet).

[chunk 977441] With NAT exempt in the firewall, it will work.
BTW, can you share more details on your firewall model, memory & CPU utilization, Interface types, max used connection when you had your public servers traffic through this firewall?

### item Tsecurity-123764
Site: security | Thread title: How are DNS requests sent when using OpenVPN? Are they encrypted?
[chunk 911191] In a default configuration, all traffic (including DNS) should be routed through an OpenVPN tunnel.
However OpenVPN in itself does not provide mechanisms to enforce all traffic being routed via its tunnel and if an application or the operating system decides to route traffic via unencrypted interface, it is free to do so (as was the case with Windows 10 Smart Multi-Homed Name Resolution).

[chunk 911192] As for your intention—protection against snooping on DNS queries by ISPs—you would be better off by configuring and using dnsmasq with DNScrypt even for your non-VPN connections.
By adding an outbound firewall (e.g. iptables in Linux) rules to block all DNS traffic you could ensure that even in case of OpenVPN failure or misconfiguration, you would get a fallback to an encrypted DNS channel (or no connection at all because of FW).

### item Tserverfault-663778
Site: serverfault | Thread title: AWS Override VPC DHCP - Additional Option Sets for RRAS VPN Clients
[chunk 190558] As far as I'm aware, this is simply not possible within an Amazon VPC, as they use DHCP for all of their IP assignments within a VPC subnet, static IP addresses are assigned by using Elastic Network Interfaces, which work in the same way as a DHCP reservation. Amazon Support will be able to confirm this though, so I'd suggest you contact them.

[chunk 190559] Your next-best solution is to create a virtual network on the Windows box, using the Loopback Adapter. You can then create a DHCP scope on this network, and essentially dual-home the box.
To create a NIC using the loopback driver (from the link above):

[chunk 190560] Start -> Computer -> Right-click, Properties -> Device Manager -> Computer Name, Right-click, Add Legacy Hardware -> Next -> Install the hardware I manually select from a list -> Next -> Network Adapters -> Microsoft on the right, Loopback adapter on the left -> Next
Once you have two functioning networks, it should be relatively straightforward to configure your RRAS clients to receive a DHCP address from the virtual scope and route to the Internet via your Amazon VPC's default gateway.

### item Tsoftwareengineering-330626
Site: softwareengineering | Thread title: Why does the call stack have a static maximum size?
[chunk 653250] It's possible to write an operating system that doesn't require stacks to be contiguous in address space. Basically you need some extra messing about in the calling convention, to ensure that:
if there isn't enough space in the current stack extent for the function you're calling, then you create a new stack extent and move the stack pointer to point to the start of it as part of making the call.

[chunk 653251] when you return from that call you transfer back to the original stack extent. Most likely you retain the one created at (1) for future use by the same thread. In principle you could release it, but that way lie rather inefficient cases where you keep hopping back and forth across the boundary in a loop, and every call requires memory allocation.

[chunk 653252] setjmp and longjmp, or whatever equivalent your OS has for non-local transfer of control, are in on the act and can correctly move back to the old stack extent when required.
I say "calling convention" -- to be specific I think it's probably best done in a function prologue rather than by the caller, but my memory of this is hazy.
The reason that quite a few languages specify a fixed stack size for a thread, is that they want to work using the native stack, on OSes that don't do this.

[chunk 653253] As everyone else's answers say, under the assumption that each stack needs to be contiguous in address space, and cannot be moved, you need to reserve a specific address range for use by each thread.
That means choosing a size up front.
Even if your address space is massive and the size you choose is really large, you still have to choose it as soon as you have two threads.

[chunk 653254] "Aha" you say, "what are these supposed OSes that use non-contiguous stacks? I bet it's some obscure academic system of no use to me!". Well, that's another question that fortunately is already asked and answered.

### item Tunix-50093
Site: unix | Thread title: Ctrl-C does not work with pppd non-detached session
[chunk 306046] Turned out it was a bug in the particular version of pppd that was being used in the distro. I checked and previous and later versions of pppd do not have this problem. Also the problem is not specific to this arch and platform or tmux. If pppd is being run inside a shell script, It does not handle Ctrl-C, while outside shell, it has no problem.

### item Tdba-130220
Site: dba | Thread title: Will replication commands build up if the distribution agent is stopped?
[chunk 770875] Yes, the transactional replication data will build up while waiting for distribution to start again. Of course, if not tracked it is possible that a long delayed set of transactional replication data can fill the log space that you have available, thus causing you problems.
Replication is hostage to the resources available, including the log space since the replication data is read from the transaction log.

[chunk 770876] For what it is worth, we once kept a replication open for a couple of days until a network problem could be resolved. (Plenty of log space at that time.)
If the replication process fails (for any reason) that would cause loss of data then you need to redo the steps to establish the replication landscape.

### item Tdevops-468
Site: devops | Thread title: How do I hire a good DevOps, fitting my company?
[chunk 994155] It is a common misbelief that “DevOps” is a role in a company. The word merely denotes an organisational shift in software companies, this shift can be shortly described by the “You build it, you run it!” coined by Werner Vogels:
There is no need to distinguish between building and running, and according to Werner Vogels, it is much better than that:

[chunk 994156] Giving developers operational responsibilities has greatly enhanced the quality of the services, both from a customer and a technology point of view.
The traditional model is that you take your software to the wall that separates development and operations, and throw it over and then forget about it.
Not at Amazon.
You build it, you run it.
This brings developers into contact with the day-to-day operation of their software.
It also brings them into day-to-day contact with the customer.

[chunk 994157] This customer feedback loop is essential for improving the quality of the service.
This lesson is interesting, but this particular change in an organization is not always easy to implement.

[chunk 994158] This shift is concomitant of an increasing importance of continuous integration and deliveries methods. Please note that these ideas are much older than the formalisation of “agile” methodologies, some of them are already present in the NATO Scientific Committee report about software engineering published in … 1968!
While the wording can be overlooked, the short description of the DevOps proposal (this site) mentions “software engineers”:

[chunk 994159] Beta Q&A site for software Engineers working on automated testing, continuous delivery, service integration and monitoring, and building SDLC infrastructure.

[chunk 994160] Now if you are looking for a software engineer that can help your team getting started with these methodologies, engage them on this topic. Even if you are not familiar with this topic, following the “You build it! You run it!” slogan you can start from a programming problem and lead the interview towards question about deployment and maintenance of the application.

### item Tnetworkengineering-18857
Site: networkengineering | Thread title: SonicWall : Bandwidth Management Per User
[chunk 976307] Set user for guaranteed speed of 1Mb and max speed of 2Mb.
This is absolutely possible. Dell has an article outlining this specifically; How To Configure Bandwidth Management with limits Per IP (SW12385).
Enable Advanced Bandwidth Management
Activate bandwidth management on WAN interface and declare the interface speed
Generate a new bandwidth object and configure it for Per-IP Bandwidth Management.

[chunk 976308] Edit your default any -> any firewall rule and enable the bandwidth object you created earlier for both ingress and egress.
Also I would like to know if I can set a user for 1Mb of speed with
 maximum of 2 GB of download per day then have it reduced automatically
 to 256Kb after consuming his 2 GB for the day.

[chunk 976309] I can't find any documentation that says you can do this, so I would imagine per-ip based bandwidth management is about as close as you can get to evening the playing field for everyone. This is usually sufficient as you wouldn't stand to benefit much from limiting someone who has reached this limit if they aren't effecting anyone else (because you're already guaranteeing bandwidth evenly).
Also I would like to know if I can put such rules on applications
 instead of users.

[chunk 976310] Yes this is certainly possible, but is accomplished in a couple different areas. It's slightly more involved, too, since you setup everything manually versus the per-IP based solution which works across the board. Dell has another write-up for that, as well; UTM: Configuring Bandwidth Management for HTTP Websites using App Rules feature (SW11515).
Create Bandwidth object
Create Action object
Match that Action object to the sites you want (or don't want)

[chunk 976311] Map the Bandwidth object to the Action object with an App Rule
Since this is all performed under the Firewall section, it should just begin working across the board.
Good luck!

### item Tsecurity-22903
Site: security | Thread title: Why refresh CSRF token per form request?
[chunk 860790] For the reasons already discussed, it is not necessary to generate a new token per request.
It brings almost zero security advantage, and it costs you in terms of usability: with only one token valid at once, the user will not be able to navigate the webapp normally.
For example if they hit the 'back' button and submit the form with new values, the submission will fail, and likely greet them with some hostile error message.

[chunk 860791] If they try to open a resource in a second tab, they'll find the session randomly breaks in one or both tabs.
It is usually not worth maiming your application's usability to satisfy this pointless requirement.
There is one place where it is worth issuing a new CSRF token, though: on principal-change inside a session. That is, primarily, at login. This is to prevent a session fixation attack leading to a CSRF attack possibility.

[chunk 860792] For example: attacker accesses the site and generates a new session. They take the session ID and inject it into a victim's browser (eg via writing cookie from a vulnerable neighbour domain, or using another vulnerability like jsessionid URLs), and also inject the CSRF token into a form in the victim's browser. They wait for the victim to log in with that form, and then use another form post to get the victim to perform an action with the still-live CSRF token.

[chunk 860793] To prevent this, invalidate the CSRF token and issue a new one in the places (like login) that you're already doing the same to the session ID to prevent session fixation attacks.