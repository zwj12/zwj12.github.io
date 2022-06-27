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

# 获取程序基目录，非dll目录
	System.AppDomain.CurrentDomain.BaseDirectory //D:\mycode\
	Application.StartupPath //D:\mycode