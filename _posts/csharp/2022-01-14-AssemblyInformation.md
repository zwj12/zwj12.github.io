---
layout: post
title: "Assembly Information"
date: 2022-01-14 08:58:00 +0800
author: Michael
categories: CSharp
---

# Assembly Information
Assembly Information对照如下：  
![日志文件夹](/assets/csharp/AssemblyInformation.png)  

# 获取dll的地址
	System.Reflection.Assembly.GetExecutingAssembly().Location 

# 获取dll版本
	System.Reflection.Assembly.GetExecutingAssembly().GetName().Version.ToString()