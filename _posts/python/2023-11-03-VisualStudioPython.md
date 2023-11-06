---
layout: post
title: "Python in Visual Studio"
date: 2023-11-03 12:54:00 +0800
author: Michael
categories: Python
---

# “调试”>“启动但不调试”
在Visual Studio中运行Python代码时，应选择“调试”>“启动但不调试”运行，如果直接F5或点击运行按钮，会导致运行时间变长。所以应该是使用Ctrl+F5启动运行。但是如果需要创建断点，使程序在断点处停下来，还是需要使用F5启动才能进入调试模式。

# dll to pyd
Python的C++扩展后缀名为pyd，而非dll。  

![日志文件夹](/assets/python/CExtensionConfigurationTypedll.png)  
![日志文件夹](/assets/python/CExtensionFileExtensionpyd.png)  

# Headers and libs
Additional Include Directories:　C:\Program Files\Python312\include
Additional Library Directories:　C:\Program Files\Python312\libs

# Python Version Not Officially Support
当遇到下来情况时，Visual Studio会检测当前的Python版本，并确定是否官方支持，当发现不支持时，会弹出报警框，暂时不清楚如何禁用该报警提示，每次都会打开，很不友好。

- 第一次打开Python项目
- 在Python项目中添加C++扩展项目引用时
- 运行Python项目后

![日志文件夹](/assets/python/PythonVersionNotOfficiallySupport.png)  

# Using CPython debug binaries (python_d.exe) requires different settings.