---
layout: post
title: "User Administration"
date: 2022-03-28 13:01:00 +0800
author: Michael
categories: zenon
---

# Editor添加的user自动编译到Runtime
默认情况下，Editor添加和修改的user数据是不会自动编译到Runtime中去的，需要在project -> properties -> General -> Runtime changeable data -> User Administration -> Do not generate and transfer中取消该设置才行。  
![日志文件夹](/assets/zenon/UserAdministrationTransferToRuntime.png) 

# Password protection for dynamic elements 
All dynamic screen elements that either allow a function execution or the Write set value function can be linked to an authorization group for the Runtime.

# Login User
当没有用户登录时，系统变量的值为：
	
	[User Administration] User name: SYSTEM
	[User Administration] User full name: 0000
	[User Administration] Current authorization group 1: 0

当有用户登陆时，[User Administration] Current authorization group 1至少大于0，这是创建用户时强制设置level时定义的。

# 自动打开login窗口
可以使用Reaction Matrix，关联[User Administration] Current authorization group 1变量，当等于0时，自动打开login窗口。

# 设置多次输错密码后，自动锁定账号功能
通过设置Project -> Properies -> User Administration可以设置用户密码输错后锁定账号和系统的功能，锁定后，需要管理员账号才能解锁，所以该限制对管理员账号没有效果：  

1. Max. user error: 用户名输错最大次数后，系统锁定
2. Max. password error: 密码输错最大次数后，该账号锁定。

![日志文件夹](/assets/zenon/MaxUserPasswordError.png)  

# AdministratorLevel和Interlocking配合使用禁用或隐藏没有权限的按钮
通过Project -> Properies -> User Administration -> Login and sigature和Project -> Properies -> Graphical design -> Locked/Interlocked elements可以设置禁用按钮时的外观或是否隐藏等参数。

![日志文件夹](/assets/zenon/LockedbuttonsInvisble.png)   
![日志文件夹](/assets/zenon/AdministratorLevel_Interlocking.png)   


