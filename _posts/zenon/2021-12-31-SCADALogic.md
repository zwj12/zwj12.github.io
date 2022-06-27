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

1. Profiled variables - STRATON: Logic共享给zenon的数量
2. Profiled variables - ZENONRT: zenonRT共享给Logic的数量
3. <I/Os>: 包含Logic共享给zenon的数量和zenonRT共享给Logic的数量，且还包含Profinet，EtherNet/IP总线的数量，但是不包含modbus变量的数量，不清楚为什么不包含Modbus的变量数量。

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

# SCADA项目字节序
必须为小字节序，否则编译可以通过，但是程序下载不了。原因不明。  
![日志文件夹](/assets/zenon/SCADALittleEndian.png)  

# Offset & Bit number
Offset代表字节的偏移。但是要注意偏移数据结构是大字节序还是小字节序。Bit number代表位偏移。例如PROFINET为大字节序，所以当一个int32的数据，第一个字节是高位字节，第四个字节为低位字节。但设置Offset=1, Bit number=1时，代表的二进制值为00000000 00000010 00000000 00000000=131072，并不是低字节序时的00000000 00000000 00000010 00000000=512。设置时应注意这一点，当然如果数据结构为字符串，则没有这个问题。  
![日志文件夹](/assets/zenon/OffsetBitNumber.png)  

# FieldBus device connection status
it is possible to use each protocol function block to get timeout error bit to show communication break. For example: 

1. Modbus: you can use ERROR output of "MBMasterTCP" function block.
2. EIP scanner: you can use Err output of "eipReadAttr".
3. Profinet IO controller: You can define slave status variable for individual Profinet slave. Refer attached screenshot. 

# FieldBus重复地址映射
当FieldBus配置变量地址时，如果有重复的，貌似后面的变量优先级更高，会自动把签名定义的变量值覆盖掉。如下图所示，字符串和UDINT变量共享一个槽位的地址，此时如果把字符串定义在UDINT签名，则实际输出的数据会按RecipeIDList值确定，如果把str01定义在RecipeIDList后面，则会按str01的值输出。当然如果按RecipeIDList输出，如果中间有某一个byte值为0，那么在接收端如果解析字符串时，会到byte为0这个位置截取字符串。  
![日志文件夹](/assets/zenon/SignalAddressOverLap.png)  
