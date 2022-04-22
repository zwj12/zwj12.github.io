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
