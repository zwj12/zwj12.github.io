---
layout: post
title: "Visual C++ Configuration"
date: 2022-06-29 13:50:00 +0800
author: Michael
categories: CPP
---

# 设置项目工作目录和命令行参数
可以通过Configuration Properties -> Debugging -> Working Directory / Command Arguments 设置C++程序运行时的工作目录和命令行参数。  

	Working Directory: $(OutDir)

![日志文件夹](/assets/cpp/DebuggingCommandArguments.png)  

# CustomBuildStep
可以设置项目的自定义事件，这样可以在Build时自动运行一些脚本。如可以提前把.h文件复制到某一个文件夹下。    

	cd .
	if not exist "$(ObjDir)" md "$(ObjDir)"
	if not exist "$(BinDir)" md "$(BinDir)"
	if not exist "$(IncDir)" md "$(IncDir)"
	if not exist "$(IncDir)\me.h" copy "..\appweb-windows-default-me.h" "$(IncDir)\me.h"
	copy /Y /B ..\..\src\appweb.h $(IncDir)
	copy /Y /B ..\..\src\server\windows\appwebMonitor.h $(IncDir)
	copy /Y /B ..\..\src\customize.h $(IncDir)
	copy /Y /B ..\..\src\mbedtls\embedtls.h $(IncDir)
	copy /Y /B ..\..\src\esp\esp.h $(IncDir)
	copy /Y /B ..\..\src\http\http.h $(IncDir)
	copy /Y /B ..\..\src\mbedtls\mbedtls.h $(IncDir)
	copy /Y /B ..\..\src\server\windows\monitorResources.h $(IncDir)
	copy /Y /B ..\..\src\mpr-version\mpr-version.h $(IncDir)
	copy /Y /B ..\..\src\mpr\mpr.h $(IncDir)
	copy /Y /B ..\..\src\osdep\osdep.h $(IncDir)
	copy /Y /B ..\..\src\pcre\pcre.h $(IncDir)
	cd .

![日志文件夹](/assets/cpp/CustomBuildStep.png)  

# Project Manager
项目中的自定义宏在Project Manager中管理。  

1. Project Property：又称项目属性，是你当前项目的属性配制，保存在你工程的配制文件中，ProjectName.vcxproj中。
2. Property Sheet：又称属性表，可用于多个工程的属性配制，可以自己创建添加属性配制，也可以使用系统默认的属性表，保存在.props为拓展名的文件中。而属性表(Property Sheet)的添加和管理就是在Property Manager中进行设置的。
3. Microsoft.Cpp.Win32.user是当
前系统用户默认的属性表，保存在C:\Users\Administrator\AppData\Local\Microsoft\MSBuild\v4.0\Microsoft.Cpp.Win32.user.props中
4. 项目的属性是分层的。 每一层会继承前一层的值，通过调整顺序在同一层中确认继承关系。  

![日志文件夹](/assets/cpp/ProjectManager.png)  
![日志文件夹](/assets/cpp/CustomizedProjectMacros.png)  
