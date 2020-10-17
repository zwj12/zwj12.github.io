---
layout: post
title: "APROL New"
date: 2020-10-13 08:34:00 +0800
author: Michael
categories: Linux
---

The "AprolInstall" script must be started manually for an update. This must be done in Linux runlevel 3. Marking is done with the [space]. The [Enter] key is used for confirmation.

LoginServer的默认用户名是：Startup，默认密码是：BuR1.admin

其它的用户名和密码还有：aprol（BuR1.aprol）

Aprol系统MariaDB数据库的默认用户名是*buradmin*，默认密码是*.buradmin* 

Aprol系统chronolog数据库的默认用户名是*SqlSystemOperator*，默认密码是*.SqlSystemOperator* 

Aprol系统示例项目位置在/opt/aprol/ENGIN/DEMOPROJECTS/

系统安装完毕后，首先进入root账号，打开AprolConfig配置软件，通过软件创建三个账号：engin，runtime，operator。这三个账号既分别对应Linux系统三个用户，也对应Aprol的三个系统。如果需要删除账号，也需要在root账号下进行，删除的同时，会把目录/home下对应的账号文件夹一同删除。另外runtime和operaotr系统还需要指定对应的engin账号，如果账号错误，那么会拒绝下载。  
![日志文件夹](/assets/aprol/AprolConfig.png)

硬件设置：

1. 新建项目后，首先需要添加运行的工控机设置，主要设置主机名和域名，该工控机是用来运行APROL系统（Runtime，Operator，Gateway系统）的。如果工控机里添加了ARPOL系统后，在APROL systems页面内会显示运行在该工控机上的APROL系统列表。工控机必须要选择Documentation server和Logging server，否则Build时会报错。  
![日志文件夹](/assets/aprol/APC910.png)

2. 有了工控机，就可以添加APROL系统了，通常需要添加Runtime和Operator两个系统。添加后，需要指定运行该APROL系统的工控机，也就是上一条中创建的工控机。在这里还有需要设置需要修改，例如可以修改支持Python模块，自动登录账号等等参数。    
![日志文件夹](/assets/aprol/runtime.png)

3. 以上创建工控机和APROL系统，其含义只是创建了几条配置文件，并不是项目程序会新建两个APROL系统，工控机是硬件，APROL系统在使用AprolConfig配置后，就已经存在了。项目程序中添加runtime和operator项只是为了告示软件，后面编译生成的程序需要下载在这边配置中指定的APROL系统中，所有需要指定APROL系统的计算机名或IP地址。APROL系统中的各种参数，也是在项目中设置的。

SFTP服务器访问：  
![日志文件夹](/assets/aprol/sftp.png)

如果在aprolconfig里对runtime和operator账号的engin账号修改后，那么即使还原会原先的engin账号，也不能正常下载，此时需要修改aprolsys账号下的隐藏文件*.rhosts*，把修改后的engin账号还原为原先的就可以了。  
![日志文件夹](/assets/aprol/rhosts.png)

如果使用自动获取IP地址，那么必须要选中*assign hostname to loopback ip*，否则会出现服务出错问题。 
![日志文件夹](/assets/aprol/loopback.png) 

如果电脑断电意外关机重启后，系统会提示不正常关机报警，此时可以通过删除四个账号下对应的shutdown文件消除该报警。  
![日志文件夹](/assets/aprol/Backupsfound.png)   
![日志文件夹](/assets/aprol/shutdown.png) 

IP设置方法：  
![日志文件夹](/assets/aprol/ip.png)

网关设置方法：  
![日志文件夹](/assets/aprol/gateway.png)

DNS设置方法：  
![日志文件夹](/assets/aprol/dns.png)