---
layout: post
title: "Development Environment"
date: 2023-03-24 09:49:00 +0800
author: Michael
categories: CVL
---

# 环境变量 VISION_ROOT
安装CVL库后，会在环境变量中创建一个新的变量VISION_ROOT，该变量存储着CVL库的位置.  
![日志文件夹](/assets/CVL/vision_root.png)  


# DLL路径
安装CVL库后，会在环境变量Path中添加CVL的dll路径：%VISION_ROOT%\bin\win64\cvl  
![日志文件夹](/assets/CVL/CVLPathEnvironment.png)  

# CVL库头文件
Visual Studio C++ -> Properties -> C/C++ -> General -> Additional Include Directories -> $(VISION_ROOT)\defs  
![日志文件夹](/assets/CVL/AdditionalIncludeDirectories.png)  

# C++编译预处理宏 NOMINMAX
貌似这个可以不设置，Visual Studio C++ -> Properties -> C/C++ -> Preprocessor -> Preprocessor Definitions -> NOMINMAX  
![日志文件夹](/assets/CVL/PreprocessorDefinitions.png)  

# CVL库lib文件
Visual Studio C++ -> Properties -> Linker -> General -> Additional Library Directories -> $(VISION_ROOT)\lib\win64\cvl  
![日志文件夹](/assets/CVL/AdditionalLibraryDirectories.png)  

# DLL
Visual Studio C++ -> Properties -> C/C++ -> Preprocessor -> Preprocessor Definitions -> CVL7Library_EXPORTS, cmBuildingDLLs  

## stdafx.h

    #ifdef CVL7Library_EXPORTS
    #define DLLAPI __declspec(dllexport)
    #else
    #define DLLAPI __declspec(dllimport)
    #endif

    //下面这段代码，手册里的代码有错误，需要更正，其目的是使主程序导入静态库cogstds.lib，该静态库包含了CVL库必须的初始化和关闭程序，文件非常小，但是是必须的。
    #ifndef cmBuildingDLLs
    #pragma comment(linker, "/include:_cgLoadHardwareSupport")
    #ifdef _DEBUG
    #ifdef _UNICODE
    #pragma comment(lib, "cogstds10_x64ud.lib")
    #else
    #pragma comment(lib, "cogstds10_x64d.lib")
    #endif
    #else
    #ifdef _UNICODE
    #pragma comment(lib, "cogstds10_x64u.lib")
    #else
    #pragma comment(lib, "cogstds10_x64.lib")
    #endif
    #endif
    #endif

## 主程序stdafx.h

    #include "../CVL7Library/stdafx.h"

## 主程序需要初始化
    //初始化CVL库
    BOOL CWinApp::InitInstance()
    {
        ...
    	cfInitializeDisplayResources();
        ...
    }

# CVL9支持VS2022
需要修改CVL9的头文件, C:\Program Files\Cognex\CVL\defs\ch_cvl\defs.h

    //origin
    #elif cmCompiler == cm_msvc && cmCompilerVer >= 1920
    #  ifdef _M_X64
    #    define cmCompilerChar "142_x64"
    #  else
    #    define cmCompilerChar "142"
    #  endif
    #endif

    //modified
    #elif cmCompiler == cm_msvc && cmCompilerVer >= 1920
    #  ifdef _M_X64
    #    define cmCompilerChar "141_x64"
    #  else
    #    define cmCompilerChar "141"
    #  endif
    #endif