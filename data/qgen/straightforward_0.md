### item Tdba-11065
Site: dba | Thread title: How can I profile SQL Azure?
[chunk 718646] I have used the MVC Mini Profiler as part of an application to profile SQL Azure but depending on your application it may or may not work. What kind of tasks are you doing that need profiling?

### item Tdevops-17429
Site: devops | Thread title: How do I find out the attributes of a terraform object?
[chunk 999747] Since local_sensitive_file here is a data source, you can assume that its attributes are the attributes defined by the provider that this data source belongs to, which is hashicorp/local.
At the time of writing the documentation for local_sensitive_file says that it has the following attributes:
filename
content
content_base64
id

[chunk 999748] Provider documentation is typically the best place to find out about attributes of a resource type because it'll also tell you what these attributes represent, in addition to their names.
Not all objects you'll encounter in Terraform will originate in providers though, so a more general answer that will work for any object you can refer to in an expression is to run terraform console and then ask it for the type of the value in question:

[chunk 999749] > type(data.local_sensitive_file.public_key)
object({
 content: string,
 content_base64: string,
 filename: string,
 id: string,
})

[chunk 999750] Unfortunately for a resource (either a resource or data block) it won't yet have a known type until it's been created or read for the first time, and so if your configuration isn't valid then you would need to make it valid enough to run terraform apply successfully before you could use this technique. But for objects that are defined within the Terraform configuration itself, rather than by external operations that haven't run yet, the console is a useful way to inspect data and data types.

### item Tnetworkengineering-239
Site: networkengineering | Thread title: Is TCP maximum segment size (MSS) "clamping" compatible with IPv6?
[chunk 971142] Well technically fragmentation can happen in IPv6; This is the wikipedia article on it.
This Juniper page is a bit old but it shows that you can clamp an MSS for TCP over IPv6 on Junos the same as you would in IPv4 using the same command, tcp mss. The same is shown in this article for Cisco IOS 15, using the traditional ip tcp adjust-mss command.

[chunk 971143] So you can configure MSS clamping if PMTUD isn't working as it should be in a part of your network, otherwise, you should be ensuring that you are aiding the smoothing running of PTMUD across your networking so that MSS clamping isn't required (I understand this isn't always under your control).
Update
Here is a link to a newer Junos article for Junos 10x rather than 9, I can't find one for 11 and I'm not in front of 11 right now, but I expect it will be the same.

### item Tsecurity-36143
Site: security | Thread title: Is it safer to store the XSRF value inside your JavaScript?
[chunk 868209] The problem with this implantation is that the CSRF token is not actually stored within an anonymous function. This token would be stored within text that declares an anonymous function. An XSS payload can request this text from the server using an XHR, the CSRF token can be read and another XHR can be used to send an arbitrary forged request.

[chunk 868210] Related: Sammy worm explanation, which is a good example of how XSS is used to read a CSRF token. Also, XSS is possible without JavaScript. Now keep in mind the following inequality:
HTTP Response Splitting > XSS > CSRF > Clickjacking

### item Tserverfault-12008
Site: serverfault | Thread title: Cheap and easy solution for VPN?
[chunk 5790] You could re-flash your router firmware with a version of dd-wrt that contains openvpn
Configuration can be a bit tricky, but once it's done, it's done - and there are some pretty good howtos out there on doing this.

### item Tsoftwareengineering-36593
Site: softwareengineering | Thread title: How to make audio and video streaming servers work?
[chunk 535701] Most of the internet radios & televisions out there use HTTP protocol to stream. A part of the pie for RTSP (after MMS) and RTMP, but it's marginal. Here are the list of the most popular streaming servers:
SHOUTcast - the legendary streaming server. Supports only HTTP streaming and is very easy to setup.
IceCast - this open source project has been developer to cover limitations of SHOUTcast. It is widely used and as recommandable as SHOUTcast. It also supports HTTP streaming.

[chunk 535702] Windows Media Services - An RTSP based streaming server (before it was MMS). It also supports HTTP streaming, but you need a specific encoder. It is also widely used, but will cost you more in licensing.

[chunk 535703] Wowza Media Server - RTMP based streaming (Flash) but also supports all possible streaming protocols such as HTTP, RTMPE, RTMPT, RTMPTE, RTMPS, MPEG-TS, etc. Not free, but you get what you paid for! Probably the best choice. It has a very well designed API (it has been programmed in Java) and will let you control and extend most things.
There are other solutions that I know less, so I just list them:
Darwin
Flash Media Server (also widely used especially in on-demand video)

[chunk 535704] Red5 (Open Source FMS alternative)
Helix
Here is a comparison of all servers.
I would go for SHOUTcast or IceCast first, the use Wowza Media Server if you are serious about streaming (because of the capabilities and the API).

### item Tunix-39645
Site: unix | Thread title: Can't understand this script. bash <<(curl -s http://xxx.com)
[chunk 301013] There is a << operator (here document) but it is not what is used here.
You have first an input redirection < which says pick the input from the following argument then there is the <(command) known as process substitution which says replace that by a file descriptor containing the output of the command.
This command could have been written
bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
but is just a convoluted way of doing:
curl -s https://rvm.beginrescueend.com/install/rvm | bash

### item Tdba-16052
Site: dba | Thread title: Linked servers: Transaction context in use by another session
[chunk 721353] http://msdn.microsoft.com/en-us/library/ms188716.aspx
Loopback linked servers cannot be used in a distributed transaction.

[chunk 721354] Trying a distributed query against a loopback linked server from within a distributed transaction causes an error, such as error 3910: "[Microsoft][ODBC SQL Server Driver][SQL Server]Transaction context in use by another session." This restriction does not apply when an INSERT...EXECUTE statement, issued by a connection that does not have multiple active result sets (MARS) enabled, executes against a loopback linked server.

[chunk 721355] Note that the restriction still applies when MARS is enabled on a connection.

### item Tdevops-9598
Site: devops | Thread title: Azure DevOps Artifact.zip folder structure for .NET Core 3.0 application
[chunk 997508] I'm looking this fact:
I have an ASP.NET Core 3.0 application for which I have a full CI/CD setup in Azure DevOps. The Application is hosted on a Ubuntu 18.04 server machine.
Therefore I can safely assume that you are developing ASP.NET Core 3.0 app to be hosted in Ubuntu. Any .NET Core 3.0 (or later) application means that you should rely on the dotnet build instead of using VSBuild.

[chunk 997509] Also you had stated that you will host the app on Ubuntu 18.x, then you should also run the build on Azure DevOps agent that runs on Ubuntu. This means you should only use dotnet build in DotNetCoreCLI@2 task, because VSBuild task only runs on Windows based agent, not Ubuntu and it is intended to compile .NET Framework and other platform other than .NET Core.

[chunk 997510] Please consult the official doc of DotNetCoreCLI@2 task at https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/build/dotnet-core-cli?view=azure-devops
After you use dotnet build, use dotnet publish to publish your artifact. It is much easier and it's also the best way to publish .NET Core apps.
I have sample usage of dotnet build and dotnet publish of this on my repo: 
https://github.com/eriawan/dotnetcore-cicd-samples/blob/master/yaml-samples/sample_pipelines_check.yml

### item Tnetworkengineering-1644
Site: networkengineering | Thread title: Does 2504 WLC support LAG?
[chunk 971911] Yes, the 2504 supports LAG in v7.4. Your first guide refers to v7.0.116.0 and the second guide written in 5/2013 implies v7.4. Enabling LAG requires a reboot of the WLC and has limitations similar to the 5500.
When LAG is enabled on a WLC, the WLC forwards data frames on the same port on which they were received. The WLC relies on the neighbor switch to load-balance traffic across the EtherChannel. The WLC does not perform any EtherChannel load-balancing on its own.

[chunk 971912] Limitations/Restrictions, same as 5500 but note 5508 doesn't have ap-manager inf's:
LAG requires the EtherChannel to be configured for 'mode on' on both
 the controller and the Catalyst switch.
The load-balancing method configured on the Catalyst switch must be a
 load-balancing method that terminates all IP datagram fragments on a
 single controller port. Not following this recommendation may result
 in problems with access point association.

[chunk 971913] The recommended load-balancing method for Catalyst switches is src-dst-ip (enter the
 port-channel load-balance src-dst-ip command).

[chunk 971914] With LAG, all of the controller ports need to connect to the same neighbor switch. If the neighbor switch goes down, the controller
 loses connectivity. With multiple AP-manager interfaces, you can
 connect your ports to different neighbor devices. If one of the
 neighbor switches goes down, the controller still has connectivity.
 However, using multiple AP-manager interfaces presents certain
 challenges when port redundancy is a concern.

[chunk 971915] Port mirroring is not supported when link aggregation (LAG) is enabled on the controller.

### item Tsecurity-140034
Site: security | Thread title: Buffer overflow - Print "hello world"
[chunk 918514] If you want to get shellcode quick and dirty, use msfvenom. If you want to learn something and become a wizard, I suggest the following:
1. Write a small assembler program for your platform.
You will realize that you need to code in such way that no NULL bytes will be produced. This can be done by creative use of XOR and other tricks.
;hello.asm
[SECTION .text]
global _start
_start:
jmp short ender
starter:
xor eax, eax ;clean up the registers
 xor ebx, ebx
 xor edx, edx
 xor ecx, ecx

[chunk 918515] mov al, 4 ;syscall write
 mov bl, 1 ;stdout is 1
 pop ecx ;get the address of the string from the stack
 mov dl, 5 ;length of the string
 int 0x80
xor eax, eax
 mov al, 1 ;exit the shellcode
 xor ebx,ebx
 int 0x80
ender:
 call starter ;put the address of the string on the stack
 db 'hello'
2. Use objdump to get the opcodes for the instructions:
hello: file format elf32-i386
Disassembly of section .text:
08048080 <_start>:
 8048080: eb 19 jmp 804809b

[chunk 918516] 08048082 <starter>:
 8048082: 31 c0 xor %eax,%eax
 8048084: 31 db xor %ebx,%ebx
 8048086: 31 d2 xor %edx,%edx
 8048088: 31 c9 xor %ecx,%ecx
 804808a: b0 04 mov $0x4,%al
 804808c: b3 01 mov $0x1,%bl
 804808e: 59 pop %ecx
 804808f: b2 05 mov $0x5,%dl
 8048091: cd 80 int $0x80
 8048093: 31 c0 xor %eax,%eax
 8048095: b0 01 mov $0x1,%al
 8048097: 31 db xor %ebx,%ebx
 8048099: cd 80 int $0x80
0804809b <ender>:
 804809b: e8 e2 ff ff ff call 8048082 
 80480a0: 68 65 6c 6c 6f push $0x6f6c6c65

[chunk 918517] 3. Then your shellcode will be:
char code[] = "\xeb\x19\x31\xc0\x31\xdb\x31\xd2\x31\xc9\xb0\x04\xb3\x01\x59\xb2\x05\xcd"\
 "\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe2\xff\xff\xff\x68\x65\x6c\x6c\x6f";
4. Profit

### item Tserverfault-1276
Site: serverfault | Thread title: Severe write performance problem
[chunk 776] Some good suggestions here from other posters about ruling out the software, and tweaking your RAID performance. It's worth mentioning that if your workload is write-heavy, then going for hardware with a battery-backed write cache is likely to be the right thing to do if you're considering replacing your kit.

### item Tsoftwareengineering-389298
Site: softwareengineering | Thread title: How should I design database, where I have 30 users, each who needs full access to their data?
[chunk 683340] You should not give any client access to the SQL. Give them an API instead.
If you do want to give them access then depending on your database tech there are a number of solutions
One database each.
This is the easiest solution
Row level access restrictions
Duplicate tables into multiple schema and have schema level access restrictions
You also say:
the data is quite private and can't be shared

[chunk 683341] I would go with completely separate databases. This offers the greatest level of separation of the data and is the easiest approach from a access restriction standpoint.
The downside of course is that you have to have multiple databases and presumably multiple application instances, each pointing to its own database.

[chunk 683342] I wouldn't go with a multi-tenant app if you are splitting the database unless there is a specific reason as it is effectively providing a single point of access to all the databases and undermining the separation.

### item Tunix-207369
Site: unix | Thread title: add filename as text in the corner of an image file
[chunk 366022] Indeed you can use ImageMagick to write text into an image. Use the convert utility to transform an image to a new file (or mogrify to transform a file in place, but I don't recommend it, because if you make a mistake, you lose the original). You specify the text with the -annotate option, which can contain escape sequences such as %t for the file name without directory or extension. There are many more options that let you control the position, size, font, color, etc.

[chunk 366023] Suppose your files are in a subdirectory called original of the current directory. Create a directory labeled:
mkdir labeled
To convert the images, call convert like this:
convert original/001abcd.jpg -fill green -pointsize 20 -annotate +0+0 %t -gravity north-east labeled/001abcd.jpg

[chunk 366024] The first parameter after -annotate is the geometry, which indicates the location of the text. +0+0 is the corner; the -gravity north-east says that this is the top right corner. The second parameter is the text, which here is just the escape sequence that says “use the file name”.

[chunk 366025] To convert all the .jpg files in the directory, write a loop. The wildcard pattern *.jpg represents the list of .jpg files, to this loop acts on all the .jpg files in the original directory. In the loop body, "$x" refers to the file name with the directory part; "${x##*/}" refers to the file name without the directory part.
for x in original/*.jpg; do
 convert "$x" original/001abcd.jpg -fill green -pointsize 20 -annotate +0+0 %t -gravity north-east "labeled/${x##*/}"
done

### item Tdba-18228
Site: dba | Thread title: Export multiple tables among servers
[chunk 722644] what you are looking for is to dynamically create tables in the destination.
or in other words Copying tables from Source to destination programmatically
here is a very useful article that transfers tables from access to sql dynamically
but you can take the same concept and apply it on your source as well.
https://stackoverflow.com/questions/6298806/how-do-i-programmatically-get-the-list-of-ms-access-tables-within-an-ssis-packag

### item Tdevops-1269
Site: devops | Thread title: What is the ec2 cli command to modify the minimum number of nodes in a scaling group?
[chunk 994678] I'd go with aws autoscaling set-desired-capacity following the documentation
But if you're up to make a button you should look into the various AWS sdk (on top right is the list of them) to call the related API instead of forking to a system command.

### item Tnetworkengineering-10547
Site: networkengineering | Thread title: Multiple VLANs with same subnet behind single ASA
[chunk 974639] Depending on the ASA and license you have, you could use contexts which create virtual ASAs within the ASA. Each is independent of the other. This would also allow you to test ASA configs before putting them on production. Each vlan interface is assigned to a context. Packets coming in are classified (in your situation, via MAC of the vlan interface) and then sent to their respective context.

[chunk 974640] Another option would be to have 3 routers, one per vlan, performing NAT to a central subnet that the ASA is on.

### item Tsecurity-30961
Site: security | Thread title: How can I protect against email tracking services?
[chunk 864636] It's all in the knowledgebase: https://web.archive.org/web/20140926051535/http://blog.bananatag.com/knowledgebase/how-opens-work/
We use the same technology as mass-email-marketing companies to track our Opens. This is achieved by inserting a small image in the message or Tracking Pixel into the message. When the image is downloaded you get an Open.

[chunk 864637] As a recipient of such a message who does not wish to be tracked you must either block image fetching from the bananatag servers (assuming they are easily identifiable), block images which look like tracking URLs or are smaller than a certain size, or simply block images altogether.

### item Tserverfault-440896
Site: serverfault | Thread title: Separate zone exceptions for each view in BIND
[chunk 138271] Each view have a separate set of zones, so one view will not answer for zones specified only in another view, thus the behavior you have is somewhat expected. But, once all your WAN zones are properly delegated to your server from the parent zone, intranet view will follow the delegation chain, come back to your own server, and query itself for that zone.

[chunk 138272] I guess you problem is either - you testing your server, and did not delegate the zones yet, or BIND's source of your queries falls into lanClients ACL and thus creates infinite loop.
The trick is to use query-source 1.2.3.4;, where 1.2.3.4 is some external interface IP which does not fall into lanClients ACL.
Another option is to add forward only; and forwarders 1.2.3.4; to your intranet view - this way delegation chain does not matter, and this will work also behind NAT.

[chunk 138273] In any case, queries made by bind itself have to be excluded from the lanClients view.

### item Tsoftwareengineering-164999
Site: softwareengineering | Thread title: Stop myself from over-complicating applications
[chunk 587470] I am just wondering if there are any techniques I can utilise to stop myself from turning a "code-behind" style trivial application into a full blown MVVM application?
Yes you can easily stop yourself from over-engineering the application. Always look for the simple solutions over complex, and remember KISS and YAGNI principles.