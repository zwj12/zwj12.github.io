---
layout: post
title: "Installation"
date: 2023-11-03 12:54:00 +0800
author: Michael
categories: Python
---

# CPython
The canonical implementation of the Python programming language, as distributed on python.org. The term “CPython” is used when necessary to distinguish this implementation from others such as Jython or IronPython.

# 安装选项
-- Download debugging symbols: *.pdb
-- Download debug binaries: *_d.pdb, *_d.pyd, *_d.lib, *_d.dll, *_d.exe

![日志文件夹](/assets/python/PythonOptions.png)  
![日志文件夹](/assets/python/WithoutDebug.png)  
![日志文件夹](/assets/python/DebuggingSymbols.png)  
![日志文件夹](/assets/python/DebugBinariesVisualStudio.png) 
![日志文件夹](/assets/python/DebuggingSymbolsAndBinariesVisualStudio.png) 

# Precompile standard library
python的编译有两层优化，-O和-OO，编译出.pyo文件分别为.opt-1.pyc和.opt-2.pyc, 当选中了Precompile standard library就会把这层优化的pyc文件在安装的时候编译出来。

1. -O 参数表明要生成更加紧凑的优化后的字节码；
2. -OO 会进一步移除-O选项生成的优化后的字节码文件中的文档字符串。

![日志文件夹](/assets/python/opt-1_opt-2_pyc.png) 

# 静默安装
可以通过命令行的不同参数打开安装界面测试每个选项对应的安装界面的功能。

    //弹出安装窗口，没有交互，显示安装进程，安装在C:\Program Files目录中，所有用户可用，同时安装Python Launcher，同时把路径添加到环境变量中，PrependPath代表把路径插入到Path的最前面，优先级最高，AppendPath代表把路径插入到Path的最后面，优先级最低。
    python-3.12.0-amd64.exe /passive InstallAllUsers=1 PrependPath=1
    python-3.12.0-amd64.exe /passive InstallAllUsers=1 AppendPath=1

    ////弹出安装窗口，没有交互，显示安装进程，安装在C:\Users\Michael\AppData\Local\Programs\Python，不安装安装Python Launcher，不添加环境变量
    python-3.12.0-amd64.exe /passive Include_launcher=0

    //弹出卸载界面，没有交互，显示卸载进程
    python-3.12.0-amd64.exe /uninstall

    python-3.12.0-amd64.exe /passive TargetDir=C:\test InstallAllUsers=0 Include_launcher=0 Shortcuts=0
    python-3.12.0-amd64.exe TargetDir=C:\test InstallAllUsers=0 Include_launcher=0 Shortcuts=0

# Python Environment Path
每一个版本安装后，都可以把路径添加到环境变量中，通过调整Path中的顺序，可以控制默认优先使用哪个Python的版本启动。在安装python时，如果发现已经存在该大版本的较低版本，会默认升级该大版本，例如从3.11.5升级到3.11.6。但是当系统已经有3.11.6时，此时再安装3.11.5会导致失败，Python不会自动降级安装，需要用户手动删除较高版本后，再安装低版本的Python。
![日志文件夹](/assets/python/PythonEnvironmentPath.png) 
![日志文件夹](/assets/python/MultiPythonVersion.png) 
![日志文件夹](/assets/python/UpgradePython.png) 
![日志文件夹](/assets/python/InstallFailed.png) 

    

    