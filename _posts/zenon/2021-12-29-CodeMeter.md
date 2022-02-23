---
layout: post
title: "CodeMeter"
date: 2021-12-29 11:09:00 +0800
author: Michael
categories: zenon
---

# CodeMeter Control Center
如果系统中有多余的dongle，可以通过CodeMeter Control Center删除。如果删除按钮是灰色的，需要修改注册表配置，可能注册表中不存在该项，需要手动添加，也可以新建一个文件，后缀名为“AllowLicenseDelete.reg”，复制下列配置，直接通过文件导入配置参数。  

	Windows Registry Editor Version 5.00
	
	[HKEY_CURRENT_USER\Software\WIBU-SYSTEMS\CodeMeterCC]
	"AllowCmActDelete"=dword:00000001
	

![日志文件夹](/assets/zenon/CodeMeterControlCenter.png)   

