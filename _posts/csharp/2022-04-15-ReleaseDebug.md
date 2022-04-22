---
layout: post
title: "Release Debug"
date: 2022-04-15 10:02:00 +0800
author: Michael
categories: CSharp
---

# Release配置下F5进行Debug
在Release配置下，因为代码会默认被优化，所以此时Visual Stuido会认为代码和运行的程序不是同一个，此时需要禁用Just My Code功能才能正常调试。  

![日志文件夹](/assets/csharp/JustMyCodeWarning.png)   
![日志文件夹](/assets/csharp/EnableJustMyCode.png)   

