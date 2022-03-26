---
layout: post
title: "SCADALogic"
date: 2021-12-31 14:53:00 +0800
author: Michael
categories: zenon
---

# Cycle time
如果SCADALogic runtime运行时持续报cycle time错误，可以从下图分析当前的程序平均cycle time是多少，然后在project setting里设置合理的cycle time参数。  
![日志文件夹](/assets/zenon/Cycletimeoverflow.png)   

# Profiled IO Variables
代码编译时，会计算程序中变量的总数量，zenonRT共享给Logic的数量，Logic共享给zenon的数量。  
![日志文件夹](/assets/zenon/ProfiledIOVariables.png)   

# Structure Variable
如果UDFB定义的输入变量是结构体，那么在调用它时，传入的结构体变量并不是整个复制进来，而是传入了这个结构体的地址引用，也就意味着如果在UDFB中修改传入的变量值，会直接修改UDFB外面传入的原始变量。在FBD程序中，变量会有一个**@**前缀符号标识。  
![日志文件夹](/assets/zenon/UDFBInputStructureVariable.png)  

# Log
可以使用printf函数在SCADA Logic页面打印日志信息。

	printf ('zModeRequestCmd=%ld; zModeCurrent=%ld;', zModeRequestCmd, zModeCurrent);

![日志文件夹](/assets/zenon/LogPrintf.png)  

# 导出Fieldbus变量CSV文件分隔符修改
需要把List separator修改为分号;  
![日志文件夹](/assets/zenon/FieldbusImportCSVListSeparator.png)  
