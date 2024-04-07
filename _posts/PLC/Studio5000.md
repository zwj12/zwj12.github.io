---
layout: post
title: "Studio 5000"
date: 2024-04-07 12:54:00 +0800
author: Michael
categories: PLC
---

# Studio5000 V32 激活
1. 卸载自带的FactoryTalk Activation Manager 4.03.03
2. 安装FTActivation 4.02.00
3. 进入操作系统安全模式
4. 替换C:\Program Files (x86)\Common Files\Rockwell\FTACommon.dll, C:\Program Files\Common Files\Rockwell\FTACommon.dll
5. 替换C:\Program Files (x86)\Rockwell Software\FactoryTalk Activation\flexsvr.exe
6. 复制eleokstudio31.lic到C:\Users\Public\Documents\Rockwell Automation\Activations\复制eleokstudio31.lic，重启FactoryTalk Activation Manager，

![日志文件夹](/assets/PLC/FactoryTalkActivationNoLicense.png) 
![日志文件夹](/assets/PLC/FactoryTalkActivationLicensed.png) 
