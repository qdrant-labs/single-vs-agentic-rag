### item Punix-43617-3961
THREAD A
Site: unix | Thread title: Tools to visualize file size distributions
[chunk 302948] I am using Disk Usage Analyser (aka Baobab), its output looks like this. (It's a png, couldn't paste it here). I believe it's part of the regular Ubuntu installation.
Also, there's KDirStat, of which WinDirStat is a clone. Here's a screenshot:
Check out this page 6 Great Apps to View Disk Usage in Linux for a collection of other tools.

THREAD B
Site: unix | Thread title: How to understand what's taking up disk space?
[chunk 282530] Based on your issues in installing ncdu my recommendation would be to use du and sort on together.
For instance:
du /home | sort -rn (will search all files/directories under /home and sort them by largest to smallest.
du -h /home | sort -rh (same but will show it in MB/KB/etc) - Note this requires coreutils 7.5 or newer (sort --version to check)
You can replace /home with any directory of your choice.

### item Punix-596276-164704
THREAD A
Site: unix | Thread title: How to tell if a Linux machine supports io_uring?
[chunk 478321] io_uring doesn’t expose any user-visible features, e.g. as a sysctl; it only exposes new system calls. It is available since kernel 5.1, but support for it can be compiled out, and it might be backported to older kernels in some systems.
The safest way to check for support is therefore to check whether the io_uring system calls are available. If you have /proc/kallsyms, you can look there:
grep io_uring_setup /proc/kallsyms

[chunk 478322] Another way to check for the system call is to attempt a safe but malformed call, and check whether the resulting error is ENOSYS, for example:
#include <errno.h>
#include <linux/io_uring.h>
#include <stddef.h>
#include <sys/syscall.h>
#include <unistd.h>
int main(int argc, char **argv) {
 if (syscall(__NR_io_uring_register, 0, IORING_UNREGISTER_BUFFERS, NULL, 0) && errno == ENOSYS) {
 // No io_uring
 } else {
 // io_uring
 }
}

[chunk 478323] On a kernel supporting io_uring, the available operations vary as new features are introduced with new kernel versions; to determine the supported operations, use io_uring_get_probe.

THREAD B
Site: unix | Thread title: System calls supported in running Kernel
[chunk 351368] The file /proc/kallsyms lists all the symbols of the running kernel. By convention, system calls have a name that begin with sys_. On a 64-bit system, system calls for 32-bit programs have a name that begin with sys32_. Strictly speaking, this lists internal kernel functions, not system call, but I think that the correspondence does work (every system call invokes an internal kernel function to do the job, and I think the name is always the name of the system call with sys_ prepended).

[chunk 351369] </proc/kallsyms sed -n 's/.* sys_//p'
This is usually not useful information, because system calls change very slowly.
Optional components provide functionality in terms of existing system calls, using general features such as devices (with ioctl when read and write doesn't cut it), filesystems, sockets, etc.
Determining the list of supported syscalls won't tell you anything about the features that the system supports.

[chunk 351370] Other internal function names won't help either because these change very quickly: the name of the function that implements some feature on one kernel version may change on the next version.

### item Psoftwareengineering-135910-43948
THREAD A
Site: softwareengineering | Thread title: How to explain your non-programmer boss you need to refactor a whole site?
[chunk 573836] The amount of change one should effect is contentious. What happens if you decide on a 'big bang' approach, estimate that it should take two months to refactor completely, and end up taking six? I'm not questioning your competence - it's just that projects like these can easily spiral out of control.

[chunk 573837] You could make a case for a gentle, iterative refactoring. So maybe you take a day to centralise the configuration files, and then move to other projects. Then two weeks later, you add autoloading. Get small changes live each time, and then wait for a bit for them to bed in. This way you remain productive on new projects, whilst slowly improving your codebase.

[chunk 573838] You should do these things on a separate branch, and if there are other tech people that your changes will touch (programmers, dbas, etc) then get them to buy into your changes before you do them.

THREAD B
Site: softwareengineering | Thread title: How can I convince management to deal with technical debt?
[chunk 537899] When I met with my boss to discuss this, he said I should include refactoring in all my estimates. He said it's not a problem he wants to think about. Instead, I should handle it.
This isn't a problem that management in general wants to think about. They aren't the engineers, you are. Just make this an unspoken part of all of your estimates, and you'll find that the technical debt decreases.

[chunk 537900] It will never be perfect though. Technical debt, like credit card debt, is an investment in getting customers faster and gaining market share over your competitors faster. Like credit, if managed properly, it can make you quite successful.

### item Punix-455137-359989
THREAD A
Site: unix | Thread title: Firmware packages: What do they actually do?
[chunk 440346] Loadable firmware is typically not "one-shot" installs that are written to flash on the device.
The firmware is loaded into volatile storage on the device and needs to be done each time the host computer is turned on.
The device does not function before the firmware is loaded.

[chunk 440347] The firmware can be written to RAM on the device, in which case it contains code and data for the processor on the device, but it can also be a bit stream defining the logic of a field-programmable logic array (FPGA), or some combination of both.

[chunk 440348] On the other hand, firmware in flash memory is typically pre-programmed on the devices, and only needs to be rewritten if there is an update to the firmware from the manufacturer. This is typically done via other mechanisms, like a separate executable that is run by the user.
There are a few reasons why manufacturers want to use RAM instead of flash memory.

[chunk 440349] First of all, it makes it possible to design a single version of the hardware, but at the same time deliver several versions of the product (for different market areas, for example).
If the product is expected to be field-upgraded frequently, it may be easier to handle the firmware upgrades this way than go through the trouble of creating a program for upgrading the flash memory on the device.

[chunk 440350] This program should have a nice user interface and be designed to be as user friendly as possible, since it is typically intended run by the end user of the product.
Some devices with flash storage often run code from RAM anyway, and they just copy the contents of the flash to RAM when the device is started, in which case the flash chip just sits idle most of the time and is an extra expense.

THREAD B
Site: unix | Thread title: What is "firmware" in Linux terminology?
[chunk 412120] In the Linux kernel context, firmware is software which runs on another processor in the system, e.g. a wireless controller, a GPU, a SCSI controller... This software used to be stored in ROM (of various types) attached to the relevant controller, but to reduce costs and make upgrades simpler, controllers now tend to rely on the host operating system to load their firmware for them.

[chunk 412121] So firmware files aren’t used by the kernel, they’re loaded by the kernel onto other pieces of hardware. This is also what makes it vaguely acceptable to have software without source code in FLOSS systems: the argument goes that it’s not running on the main CPU but on another device.

### item Punix-8788-8807
THREAD A
Site: unix | Thread title: Installed Fedora in dual boot Windows desktop. Now I can't get full monitor resolution with my AMD Radeon HD 6450
[chunk 285262] So, this appears to be a really new graphics card. You'll need both an up-to-date X driver and a really recent kernel — in fact, you need the not-yet-released (as of early March 2011) 2.6.38 kernel. (See this article for more on the upcoming kernel release.)
The good news is that the pre-release 2.6.38 kernel is already in the tree for Fedora 15, and the Fedora 15 Alpha release is scheduled for tomorrow today (March 8th, 2011). Get the release from http://torrent.fedoraproject.org/.

[chunk 285263] I can't promise that that'll make the card work, but the signs look positive. I'm not sure if the needed driver code is in the F15 X.org drivers yet, but the quickest way to find out is to try it.
You can even get the Live Desktop CD option, which will let you test if it works without even reinstalling.
It's possible (likely even) that the required bits will make it into Fedora 14 in a few months. So just waiting is another option.

[chunk 285264] (Honestly, I think either of those will be a better option than the proprietary binary driver. I've had no end of trouble from that. It's faster at 3D, so if top 3D performance is your main need, it might be worth it, but for general use, eh.)
Update: So, Fedora 15 (final release) is out today. I'm curious — did it work?

THREAD B
Site: unix | Thread title: Fedora won't boot. The startup progress bar goes all the way to the right and then everything just freezes
[chunk 285275] Sounds very much like there is a problem starting X, especially if you were messing around with xorg.conf.
Deleting xorg.conf should solve the problem, also you should check /var/log/Xorg.0.log for errors.

### item Pserverfault-721523-562574
THREAD A
Site: serverfault | Thread title: Install CentOS 7 on HP dl120 gen9 server with b140i raid controller
[chunk 202361] Ok, so after countless hours spent searching for the B140i Dynamic Storage Array drivers, I managed to find the driver by downloading the HP service pack for Proliant, mounting the iso locally and finding the hpdsa driver inside a folder named DUD.
The steps I did in order to successfully install CentOS 7 on my HP Proliant DL120 gen 9 are the following:
Download CentOS Image and write it on a USB;

[chunk 202362] Download HP
Proliant Service Pack and locate the hpds driver inside it
(download only the b140i drivers from here);
Use dd to write the appropriate driver (u0 or u1) on a separate USB drive;
Insert the CentOS USB in the server, boot from it but at the
install menu, press e in case of an UEFI system and add on the
linuxefi line the following inst.dd modprobe.blacklist=ahci;
Press Ctrl+x or the keys needed to continue the installation;
Insert the usb drive with the driver;

[chunk 202363] Press r to refresh the drive list and choose the appropriate drive;
After it unpacks, continue with the installation as usual;
Special thanks to @ewwhite and @michael-hampton :)
Hope this helps someone else who is facing this problem and is not experienced with servers.

THREAD B
Site: serverfault | Thread title: Install Oracle Linux 6.4 on HP ProLiant DL380e Gen8 server
[chunk 167261] I blame HP for convincing people to buy the ProLiant DL360e/DL380e series of servers. The storage controller is a big compromise on those servers. Here, you basically installed onto one of the two disks.
The HP Dynamic Smart Array needs a binary driver to really function... See this Red Hat knowledge base article. You'll have to slipstream it into the installation.

[chunk 167262] In order to install onto your server model, you'll require a driver disk for use during the installation process. The driver you need is the hp-vsa module. The install will need to be performed with a USB key.
Here's the link to the driver. Choose the right binary driver for your EL version (6.4)
Here are the installation instructions.

### item Psoftwareengineering-141854-70877
THREAD A
Site: softwareengineering | Thread title: Design patterns - do you use them?
[chunk 576673] When I was a novice programmer, I loved design patterns. I didn't just use design patterns. I inflicted them. Wherever and whenever I could. I was merciless. Aha! Observer pattern! Take that! Use a listener! Proxy! AbstractFactory! Why use one layer of abstraction when five will do? I've spoken to many experienced programmers and found that just about everyone who reads the GoF Book goes through this stage.
Novice programmers don't use design patterns. They abuse design patterns.

[chunk 576674] More recently, I find that keeping principles like the Single Responsibility Principle in mind, and writing tests first, help the patterns to emerge in a more pragmatic way.
When I recognise the patterns, I can continue to progress them more easily.
I recognise them, but I no longer try to force them on code.

[chunk 576675] If a Visitor pattern emerges it's probably because I've refactored out duplication, not because I thought ahead of time about the similarities of rendering a tree versus adding up its values.
Experienced programmers don't use design patterns. Design patterns use them.

THREAD B
Site: softwareengineering | Thread title: Are design patterns really essential nowadays?
[chunk 546170] For my money, I think everyone's missing the point of design patterns. It's rare that I sit wondering which pattern I should use in a given situation. Also, I was using most of those patterns long before I knew they had names.

[chunk 546171] The power of design patterns is in communication. It is much quicker for me to say "use a Strategy for that" than to describe in detail what I am suggesting. It is much easier for us to debate the benefits of fat domain models vs. transaction scripts if we all know what those two terms mean. And so on.
And most powerfully of all, if I have named a class FooBuilder then you know that I'm using the Builder pattern to generate my Foo.

[chunk 546172] Even if you don't know what I'm talking about when I say "Observer pattern is ideal for that," you will be able to go off and google it pretty easily.
In that sense, the power of design patterns will never fade.

### item Pdba-112011-11299
THREAD A
Site: dba | Thread title: "Specify SQL Server administrators" - unusual default value
[chunk 762827] You're right: system administrators can gain sysadmin access, but you will find entries in the default trace for that action. Moreover, it requires restarting the service at least twice, which would hardly go unnoticed.
Not granting sysadmin privileges to BUILTIN\Administrators is a change introduced in SQL Server 2008. In my opinion it's a good idea: it allows the separation of duties between server administrators and SQL Server administrators.

[chunk 762828] The main undesired effect of having BUILTIN\Administrators in your sysadmin role is the loss of control, which can manifest with one or more of the following annoying things:
New databases appearing on your servers
Unwanted connections from windows admins that end up competing with legitimate connections
Implied permissions to windows admins on databases with sensitive
data

[chunk 762829] Seemingly innocuous but disrupting "self service" operations,
such as taking full "one-off" backups on databases with differential
backup strategies.
Long story short, windows admins have a different skill set and a different mindset, not to mention different responsibilities: letting them manage your SQL Server instances is not a good idea.
My suggestion is to create a windows group for your DBAs and add that group to the sysadmin role upon each new SQL Server installation.

THREAD B
Site: dba | Thread title: How to add new sysadmin account when no sysadmin accounts exist
[chunk 718758] The details presented in this answer are correct - however other answers do provide workarounds that exist to allow SQL Server to be started in a special mode that allows the server administrator to access SQL Server as a member of the sysadmin role.

[chunk 718759] Even the most uber-admin type of connection option Dedicated Administrator Connection (DAC), which can only be used as a local connection, and lets you undo all kinds of evil, still requires login credentials. So I don't think there's an official way to do this.

[chunk 718760] The quickest way to resurrect this system may be to shut down SQL Server, copy the user database files somewhere safe, uninstall, reinstall (making sure to service pack up to at least the level you were previously at), copy the files back and attach the databases. (Not sure the copying out/back is required, but just to be safe...).
You'll still need to manually recover server level objects (e.g. logins)

### item Punix-126433-36388
THREAD A
Site: unix | Thread title: Automatically update GCC to a later release without upgrading distribution
[chunk 337804] The package management gives you a set of packages that "belong together". Trying to trick it to install a new set of software that doesn't belong in your distro is likely to "not work out great". What typically happens is that you get a huge daisy-chain of follow-on packages that you also need to upgrade (e.g. "gcc needs a new glibc, new glibc needs new binutils, new binutils breaks your gdb, so you need to update that", etc).

[chunk 337805] I find it a better solution to retain the existing installed tools where they are, and then build my own version of gcc, llvm+clang, gdb, lldb or whatever it is I feel I need a later version of.
Typically, this works without trouble, because it installs in /usr/local/{bin,lib,include,...}, where the distros tools install in /usr/{bin,lib,include,...} - so if you ever need to use the older ones (and sometimes that turns out to be the case, e.g.

[chunk 337806] you got a newer gcc that unfortunately isn't capable of compiling project A - or even itself) - you use use /usr/bin/gcc or edit your $PATH to not use /usr/local.

[chunk 337807] I have a Fedora-16 install, but I use gcc 4.8.2 (the latest as of end of March) and clang 3.5 - the default compilers that the system comes with are gcc 4.6.3 and clang 2.9. Clang 3.5 requires a C++11 compatible compiler, so 4.7 or 4.8 is required for that project. It works just fine. (but the new gcc and clang breaks older gdb such that symbols don't work as expected, so I either need to rebuild gdb or upgrade it).

THREAD B
Site: unix | Thread title: Get newest gcc for debian?
[chunk 299420] Debian 6.0 is Squeeze (currently stable); Lenny was 5.0 (currently oldstable). I'll assume you meant Squeeze.
Use apt-pinning to safely add Wheezy (currently testing) to your sources.list, then install gcc-4.7/wheezy.
In other words, your /etc/apt/sources.list should look something like this:
deb local.debian.mirror squeeze main
deb local.debian.mirror wheezy main
while your /etc/apt/preferences should look something like this:
Package: *
Pin: release n=squeeze
Pin-Priority: 900

[chunk 299421] Package: *
Pin: release n=wheezy
Pin-Priority: 200
(The exact numbers don't matter too much; see man 5 apt_preferences for details on what various ranges mean.)
This will prevent testing packages from being unintentionally installed. (Of course, you could just upgrade your whole system to testing.)

[chunk 299422] You may get some resolution errors with apt-get install gcc-4.7/testing as it will have dependencies that require versions greater than stable; apt-get --target-release testing install gcc-4.7 will set testing to priority 990 for the duration of the command.

### item Punix-44364-152258
THREAD A
Site: unix | Thread title: How to maximise a window horizontal or vertically?
[chunk 303228] By default there is no such key binding (in 3.5.1, see other answer for 4.1). But you can create one. Use this snippet (or better add the key binding to your existing configuration) for your rc.lua file:
clientkeys = awful.util.table.join(
 awful.key({ modkey }, "F7",
 function(c) c.maximized_horizontal = not c.maximized_horizontal end),
 awful.key({ modkey }, "F8",
 function(c) c.maximized_vertical = not c.maximized_vertical end),
)

[chunk 303229] It assigns horizontal and vertical maximization to mod-F7 and mod-F8, respectively.

THREAD B
Site: unix | Thread title: Using Awesome window manager on CentOS 7
[chunk 347174] ⚠ All the answers here are OUTDATED and SHOULD NOT BE USED!!!
Awesome can be installed from source with a little tweaking.
; cat /etc/centos-release 
CentOS Linux release 7.6.1810 (Core) 
; awesome --version 
awesome v4.2-dirty (Human after all) 
 • Compiled against Lua 5.1.4 (running with Lua 5.1) 
 • D-Bus support: ✔ 
 • execinfo support: ✔ 
 • xcb-randr version: 1.6 
 • LGI version: 0.9.2