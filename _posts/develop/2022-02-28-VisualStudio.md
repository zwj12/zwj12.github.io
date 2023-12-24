---
layout: post
title: "Visual Studio"
date: 2022-02-28 14:49:00 +0800
author: Michael
categories: Develop
---

# Active Configuration Manager 生成配置和生产平台
Visual Studio通过Configuration Manager管理Build程序时的配置，在Configuration Manager中新建配置时，会在每个项目中添加对应的配置和平台，Soluiton的配置名称可以随意设置，并不一定需要和项目中保持一致，在添加时可以选择是否需要用相同的名字在每个项目中创建配置，如果选中，则会在每个项目中新建同名的配置，如果不选中，则只会在solution中创建一个配置，然后在Configuration Manager需要配置每个项目的配置和平台。这种设置也就意味着Solution（Visual Studio工具栏的设置）中的配置比如Debug，其实是可以通过修改Configuration Manager中的属性让当个项目生产Release版本的程序。项目的平台是固定的，不能添加和修改，但是Solution的平台是可以随便命名的，然后把Solution的平台与项目的平台关联即可。项目在Build时，一定是按Solution当前的配置和平台编译的，即使项目中属性选择的配置和平台不一样，也是按Solution的配置编译。项目中Build页面的下拉框其实只是让你修改配置而已，除非选择Active，否则配置只是用来修改，不适用于当前编译环境。  

1. 每个项目可以有多个配置和平台设置，但是项目不能添加配置和平台，配置可以添加，但是平台的类别是锁定的。
2. 在Solution中添加配置，可以自动在项目中同名创建，在Solution中添加平台不会在项目中创建。
3. Solution中的配置和平台对应每个项目的一组配置和平台参数，虽然可以随便配置，但是建议名称对应，否则会容易引起困扰。
4. 项目中的配置下拉框只用于修改，并不代表当前编译使用该配置，当前编译还是有Solution的配置和平台决定的。
5. 当项目中选择Active时，在Solution中切换配置和平台时，会自动切换。
6. C#的平台有AnyCPU, x86, x64, C++的平台有Arm, Win32, x64


![日志文件夹](/assets/develop/VSActiveConfigurationManager.png)  
![日志文件夹](/assets/develop/JustCreateSolutionConfiguration.png)  
![日志文件夹](/assets/develop/ConfigurationManager.png)  


# C#编译设置
1. x86： 将程序集编译为由兼容 x86 的 32 位公共语言运行库运行。
1. x64： 将程序集编译为由支持 AMD64 或 EM64T 指令集的计算机上的 64 位公共语言运行库运行。
1. anycpu：（默认值）将程序集编译为在任意平台上运行。
1. Itanium： 将程序集编译为由采用 Itanium 处理器的计算机上的 64 位公共语言运行库运行。

具体行为如下：

1. 在 64 位 Windows 操作系统上：
	- 用 x86 编译的程序集将在 WOW64 下运行的 32 位 CLR 上执行。
	- 用 x64 编译的程序集将在 64 位 CLR 上执行。
	- 用 anycpu 编译的可执行文件将在 64 位 CLR 上执行。
	- 用 anycpu 编译的 DLL 将在与加载它的进程相同的 CLR 上执行。 
2. 在 32 位 Windows 操作系统上：
	- 用 x86或anycpu 编译的程序集将在 32 位 CLR 上执行。
	- 用 x64 编译的程序集无法运行。

# 多线程断点调试
通过断点的条件筛选器可以限制断点在某一个线程中启用。  
 ![日志文件夹](/assets/develop/DebugByThreadID.png)  

# Extensions
1. ResXManager
2. GitHub Copilot
3. GitHub Copilot Chat
4. COPA-DATA Developer Tools