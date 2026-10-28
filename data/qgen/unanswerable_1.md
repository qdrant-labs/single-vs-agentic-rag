### item Uunix-315003
Site: unix | Thread title: How do I clean out my /tmp directory upon reboot?
To introduce a 1GB /tmp that sits in tmpfs and therefore clears on boot, add this line to /etc/fstab and then reboot.
tmpfs /tmp tmpfs nodev,nosuid,size=1G 0 0
More info on Arch wiki

### item Udba-13370
Site: dba | Thread title: Primary Key Type's Effect on Performance in Oracle?
From what I know, it depends on whether your table is IOT (Microsoft calls it clustered table, a table with clustered index)or not . Historically, Oracle IOTs performed worse than its heap tables. That seems to change (I believe with Oracle 10), but there is still prejudice against IOT. So the article you mentioned can be applied to some extent if you use IOT in Oracle, but not for heap tables.

Don't misunderstand me, having a PK constraint supported by index on large varchar2 column has impact on performance, but if it's an Oracle heap table, it's the same as having an index on non-PK varchar2 column.

### item Udevops-6559
Site: devops | Thread title: What are some effective questions to ask someone who is considering me as their DevOps person?
In my opinion since the DevOps culture is derived from, or you could say appeared because of, the Agile software development methods
I would ask if the company is following any agile software methods or else you would be just the release guy
Also I would ask how I will be working as part of the dev team like I will be assigned to one project team or I will be working with all the teams

Also it would be great to know the current situation like they are currently facing urgent problem and need fix now , what's their current stack , and also ask about their current workflows in git and in development and try to find a way to solve the issue to make everything go smoothly

Also what really appears on paper is the workflows like git workflows, how often you release cause automating parts like delivery, and integrations,......etc really means less time and better quality and that will appears on paper even for the business guys
But at the end if the day every company is different than any other and every situation is different than the other so it's all back to your judgement to be comfortable in your daily job.

### item Unetworkengineering-1029
Site: networkengineering | Thread title: Difference between Subnet and VLAN?
If they are used interchangeably then they are used incorrectly.
Subnet refers to particular IP network, such as 192.0.2.0/28.
VLAN refers to 802.1Q standard, in which you can essentially give each port unique MAC address table, effectively separating them from each other.

VLAN may transport one or more subnet (but does not have to, it may be transporting something else than IP entirely). 
Subnet may be configured for VLAN, but does not have to be, it could be without 802.1Q or over some completely different L2 technology than ethernet.

### item Usecurity-83263
Site: security | Thread title: Are there / have there ever been viruses that completely evade virus scanners for very long?
Yes, consistently.
Viruses must be used and found before a definition is created.
APT (Advanced Persistent Threats) are a huge deal in recent times where people will spend years developing viruses, called 0 day threats, for specific targets that will remain undetected for very long periods of time.
Viruses like these are usually a product of nation states as most common miscreants won't spend the time or have the sophistication to pull it off.

I believe Stuxnet is one of these viruses (http://en.wikipedia.org/wiki/Stuxnet) that went a year or longer before being found out and once it was, other miscreants altered the code to do what they wanted the virus to do.
It's likely more common than anyone would like to believe.
Red October:
http://www.kaspersky.com/about/news/virus/2013/Kaspersky_Lab_Identifies_Operation_Red_October_an_Advanced_Cyber_Espionage_Campaign_Targeting_Diplomatic_and_Government_Institutions_Worldwide

### item Userverfault-577342
Site: serverfault | Thread title: NFSv4 through portforward
My colleague spotted the solution in the tcpdump, that the only other difference between the good and bad connection attempts is the source port.
Then Google told me that I need the insecure option to the export, because after the forward the source port is above 1024 and in the normal case it is below 1024 and insecure tells to the server that it can accept clients with source port above 1024.

### item Usoftwareengineering-232562
Site: softwareengineering | Thread title: Why do most sites require email activation
Activation confirms the email is yours. It's not so much about being bogus or non-existent, as it is about being yours and they need it for an alternative/plan-b way of authentication, in first place.

### item Uunix-115129
Site: unix | Thread title: Why does root not have /usr/local in path?
Because it isn't set up in the relevant shell startup files for root.

Traditionally, /usr/local has been used for unofficial, locally installed software (often to override buggy/broken/limited "official" versions; a friend quipped that the first step when a new Sun arrived was GNU > /usr/local). As root is all-powerful, any mistake or misdesign in the programs it runs can be fatal. It stands to reason that running e.g. a local, experimental version of make by root should be treated with caution. Better have it go the extra step of giving an explicit path.

### item Udba-33533
Site: dba | Thread title: Query optimization with extreme statistic
At the risk of stating the obvious, you have a cardinality problem with col1.
Looking at the two queries you posted in the question:
SELECT * FROM table_1 WHERE col1 = 1
AND id NOT IN (79869) ORDER BY date DESC LIMIT 0, 10;
SELECT * FROM table_1 WHERE col1 = 1 AND id <> 18983
AND date > '2012-10-26' AND (col2 LIKE '%word1%' OR col2 LIKE '%word2%')
ORDER BY date DESC LIMIT 5;
you need good indexes that will accommodate these two queries. In your particular case, you will need just one index.

If the table is MyISAM, here is that index
ALTER TABLE table_1 ADD INDEX col1_date_ndx (col1,date,col2,id);
If the table is InnoDB, here is that index
ALTER TABLE table_1 ADD INDEX col1_date_ndx (col1,date,col2);
How will this index help? Although you have to live with the lopsided cardinality of col1, you improve each query's chances of being effectively searched.
You could also take a chance on refactoring the queries. How ???

Perhaps you could collect the ids only then join the ids back to the original table.
QUERY #1
Here is the first query
SELECT * FROM table_1 WHERE col1 = 1
AND id NOT IN (79869) ORDER BY date DESC LIMIT 0, 10;
Collect the ids and join back to table_1
SELECT B.* FROM
(SELECT id FROM table_1 WHERE col1 = 1
AND id NOT IN (79869) ORDER BY date DESC LIMIT 0, 10) A
LEFT JOIN table_1 B USING (id);
QUERY #2
Here is the second query

SELECT * FROM table_1 WHERE col1 = 1 AND id <> 18983
AND date > '2012-10-26' AND (col2 LIKE '%word1%' OR col2 LIKE '%word2%')
ORDER BY date DESC LIMIT 5;
Collect the ids and join back to table_1
SELECT B* FROM
(SELECT * FROM table_1 WHERE col1 = 1 AND id <> 18983
AND date > '2012-10-26' AND (col2 LIKE '%word1%' OR col2 LIKE '%word2%')
ORDER BY date DESC LIMIT 5) A
LEFT JOIN table_1 B USING (id);
I cannot make promises on the queries, but, at the very least, the index suggestion should help.

Give it a Try !!!

### item Udevops-740
Site: devops | Thread title: How to remove directories and files in another layer using Docker?
A solution is to remove the not empty directory using find:
Dockerfile
FROM alpine
RUN mkdir dir && cd dir && wget http://google.com && cd / && echo -e "BEFORE\n" && ls && find /dir -delete && echo -e "\nAFTER\n" && ls
Outcome

Sending build context to Docker daemon 2.048kB
Step 1/2 : FROM alpine
 ---> 4a415e366388
Step 2/2 : RUN mkdir dir && cd dir && wget http://google.com && cd / && echo -e "BEFORE\n" && ls && find /dir -delete && echo -e "\nAFTER\n" && ls
 ---> Running in ba93a1742a76
Connecting to google.com (172.217.20.110:80)
Connecting to www.google.nl (172.217.20.99:80)
index.html 100% |*******************************| 11092 0:00:00 ETA
BEFORE

bin
dev
dir
etc
home
lib
media
mnt
proc
root
run
sbin
srv
sys
tmp
usr
var
AFTER
bin
dev
etc
home
lib
media
mnt
proc
root
run
sbin
srv
sys
tmp
usr
var
 ---> 2e3109285a2d
Removing intermediate container ba93a1742a76
Successfully built 2e3109285a2d

### item Unetworkengineering-17722
Site: networkengineering | Thread title: How to detect port changes in real time on Cisco 4506
From configuration mode, type
logging monitor info
end
then from enable mode type
term[inal] mon[itor]
this will send console messages to your vty session.

### item Usecurity-60769
Site: security | Thread title: Transferring of keys from key servers to recipients
If you use the signatures on the key to validate it (such as the web of trust model), then you only depend on the key material you have, and not the key served to you. In fact, if you know the fingerprint of the key you want (with certainty) you can just verify the fingerprint after retrieving it.
If you want to avoid a MITM, you can use the hkps protocol described on the SKS Keyserver page here: https://sks-keyservers.net/overview-of-pools.php.

Keep in mind that anyone can upload any key to the keyserver, so just because it has the email you want doesn't mean it's the right key. Only the signatures on the key (and the trustworthiness of the signatures) can help determine if the key you have is the legitimate one.

### item Userverfault-559834
Site: serverfault | Thread title: How to limit connection speed
I figured this out using LargeFileLimit:
<IfModule mod_bw.c>
BandwidthModule On
ForceBandWidthModule On
Bandwidth all "52428800"
MaxConnection all "400"
LargeFileLimit * 1024 204800
BandWidthError 510
</IfModule>
This will mean that the domain is limited to 50mb bandwidth (52428800), that it can only have 400 connections at once and that any files over 1mb will be limited to 200kb/s (204800).

For anyone reading this later you can also put an extension instead of * to limit just zips,rars,avis or whatever.

### item Usoftwareengineering-234530
Site: softwareengineering | Thread title: Utilising Promises, Closures and Recursion in Node.js
The nesting is a little hard to read. If you write it as follows, it's easier to tell what's happening.
function queryDatabase() {
 query.getResult({query: resourceQuery}, queryDone);
}
function queryDone(err, result) {
 if (result.length !== 0) {
 q.resolve(result);
 }
 else if (timeoutCounter++ > timeoutLimit) {
 q.reject();
 }
 else {
 queryDatabase();
 }
}

Since query.getResult() is asynchronous (I'm assuming, or else you wouldn't need a promise), that means queryDatabase() will return before queryDone() is called. When queryDatabase() is called inside queryDone(), it will return, causing queryDone() also to return, before it's called again. So while it's recursive in a semantic sense, the function calls themselves are never nested. So you shouldn't have issues like keeping 100 copies of a result object in memory at once.

As far as style goes, I don't see how it could be expressed without recursion without adding complexity. If this pattern is repeated frequently in your code, you could make a more general solution, used something like:
var promise = 
 repeatQueryUntil(resourceQuery, function(err, result) {return result.length !== 0;})

### item Uunix-359773
Site: unix | Thread title: How does history work in fish shell?
The history command in the fish shell isn't bash-compatible, it's just displaying it in a pager (e.g. less).
To select an old command, you'll probably want to enter the part you remember right into the commandline, press up-arrow until you have found what you want and then press enter to execute.
E.g. on my system I enter mes, press up and rm -I meson.build appears (with the "mes" part highlighted). I then press enter and it executes.

### item Udba-45642
Site: dba | Thread title: Bulk update of all columns
If you only want to update data, I'm not sure what the INSERT statement is for in your question.
If you just want to update several rows with a single statement, you might be looking for this:

with update_values (ID,PARENT_ID,BOUGHT_IN_FORM_TYPE_ID,PRIORITY,NAME,HEADING,DESCRIPTION,ICON,BOUGHT_IN_CONTROL_PANEL_FILE_ID) as 
(
 VALUES
 (109,1,28,100,'Tooling','Tooling','Enter your Machine Tools here','tooling.png',null), 
 (1,0,1,200,'Bought In','Bought In','','boughtin.png',null)
)
update bought_in_control_panel
 set parent_id = ud.parent_id, 
 bought_in_form_type_id = ud.bought_in_form_type_id,
 ....
from update_values ud
where ud.id = bought_in_control_panel.id;

### item Udevops-5848
Site: devops | Thread title: How to see when an AWS IAM role was last used?
I've been meaning to come back to this.
After consulting with AWS support it would seem that this is possible using some functions of the AWS CLI, that I was not aware of.
Specifically they recommended using 
aws iam generate-service-last-accessed-details and aws iam get-service-last-accessed-details-with-entities, and they referred me to https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html#access_policies_access-advisor-viewing-cli.

For completion's sake here's how I used it:
#! /bin/bash

ROLES=$(aws iam list-roles | jq -r .Roles[].Arn)
for ROLE in $ROLES
do 
 echo $ROLE
 JOBID=$(aws iam generate-service-last-accessed-details --arn $ROLE | jq -r .JobId)
 echo $JOBID
 NAMESPACES=$(aws iam get-service-last-accessed-details --job-id $JOBID | jq -r .ServicesLastAccessed[].ServiceNamespace)
 for NAMESPACE in $NAMESPACES
 do 
 echo $NAMESPACE
 aws iam get-service-last-accessed-details-with-entities --job-id $JOBID --service-namespace $NAMESPACE | jq

'.JobCompletionDate,.EntityDetailsList[].EntityInfo.Name,.EntityDetailsList[].EntityInfo.Id'
 done 
done

### item Unetworkengineering-49502
Site: networkengineering | Thread title: Can we run Linux guest OS in Cisco Packet Tracer?
Packet tracer is fairly limited. It is designed to let someone practice for the CCNA exams. It doesn't include all the IOS features, only a subset of commands that are useful for CCNA-level exercises.
Packet Tracer is not going to give you what you seem to want.

### item Usecurity-135967
Site: security | Thread title: Strange response body in burp suite
The response of the server reply is Brotli encoded:
Content-Encoding: br
I think that the Burp Suite doesn't decode this, so you're seeing the compressed version of your response.
For more information about Brotli you can look here.
Update:
Until the Burp Suite supports Brotli, you can override the Accept-Encoding-Header as a workaround. Go to Proxy -> Options -> Match and Replace. There is allready a template named "Require non-compressed responses" that you can simply activate:

### item Userverfault-387219
Site: serverfault | Thread title: Centos - fstab - mount keeps changing
If your BIOS is detecting devices in a different order you can mount by label or by UUID. (You can see your /boot mount is already doing this.)
LABEL=filesystemlabel /mnt/directory type options
-or-
UUID=uuidhere /mnt/directory type options
You can get the UUID with the blkid command or the label with e2label. (Assuming ext2/ext3.) If it has no label, you can set it e2label also, or tune2fs.