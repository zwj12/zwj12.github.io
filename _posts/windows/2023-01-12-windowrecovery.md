---
layout: post
title: "Windows Recovery"
date: 2023-01-12 16:17:00 +0800
author: Michael
categories: Windows
---


# 修复Recovery
	reagentc /info
	//dir这条语句可能需要多次运行，才会把Winre.wim复制到c:\Windows\System32\Recovery目录下，不清楚原因
	dir /a /s c:\winre.wim
	attrib -h -s c:\Windows\System32\Recovery\Winre.wim
	reagentc /enable
	reagentc /info

## Method 2
从win10 iso的光盘镜像中，复制/sources/install.wim/windows/system32/recovery/winRE.wim到c:\Windows\System32\Recovery\Winre.wim, 运行reagentc /enable

![日志文件夹](/assets/windows/winre.wim.iso.png)
