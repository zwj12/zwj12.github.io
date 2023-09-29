---
layout: post
title: "Preprocessor"
date: 2022-02-28 18:25:00 +0800
author: Michael
categories: CPP
---

# Environment Variable 环境变量 Macro
系统的环境变量`%VISION_ROOT1%`会自动添加到Visual Studio C++的宏变量中`$(VISION_ROOT1)`。  
![日志文件夹](/assets/cpp/EnvironmentVariable.png)  
![日志文件夹](/assets/cpp/EnvironmentVariableMacro.png)  

# 避免同一个头文件被包含（include）多次
为了避免同一个头文件被包含（include）多次，C/C++中有两种宏实现方式：一种是#ifndef方式；另一种是#pragma once方式。

## #pragma once
pragma once可以放置在头文件中任何位置，但是通常推荐放置在开头位置。

	#pragma once

## #ifndef

	#ifndef  __SOMEFILE_H__

	#define   __SOMEFILE_H__

	... ... // 声明、定义语句

	#endif

# pragma comment(lib,“Ws2_32.lib”)
表示链接Ws2_32.lib这个库。

	#pragma comment(lib,"rpcrt4.lib")

# define多个字符串
如果使用define定义宏，如果宏变量后面显示多个字符串，这些字符串会自动被连接起来。

	#define teststring "Hello" "World"
	std::cout << teststring; //output: HelloWorld

# define带参数数据类型的宏
除了基础的define函数宏外，还可以定义带数据类型的函数宏。此时如果在程序中使用该函数时，一定要与宏实现的函数返回值和参数数据类型一致，否则编译报错。数据类型可以在宏定义中定义，也可以在宏函数中定义，也可以返回值数据类型和参数数据类型分别在两个地方定义。神奇的宏。以下四段代码实现了相同的功能。  

	#include "pch.h"	
	using namespace System;	
	#define TESTMACRO(a,b) int test(a, b)
	
	TESTMACRO(int a, int b) {
	    return a + b;
	}
	
	int main(array<System::String ^> ^args)
	{
	    int d=test(1, 1);
	    std::cout << d<<std::endl;
	    return 0;
	}


	#include "pch.h"
	using namespace System;
	#define TESTMACRO(a,b) test( a,  b)
	
	int TESTMACRO(int a, int b) {
	    return a + b;
	}
	
	int main(array<System::String^>^ args)
	{
	    int d = test(1, 2);
	    std::cout << d << std::endl;
	    return 0;
	}


	#include "pch.h"
	using namespace System;
	#define TESTMACRO(a,b) int test(int a, int b)
	
	TESTMACRO(a, b) {
	    return a + b;
	}
	
	int main(array<System::String^>^ args)
	{
	    int d = test(1, 2);
	    std::cout << d << std::endl;
	    return 0;
	}


	#include "pch.h"
	using namespace System;
	#define TESTMACRO(a,b) test(int a, int b)
	
	int TESTMACRO(a, b) {
	    return a + b;
	}
	
	int main(array<System::String^>^ args)
	{
	    int d = test(1, 2);
	    std::cout << d << std::endl;
	    return 0;
	}


# 查看宏展开之后的文件
可以通过设置C/C++ -> Preprocessor -> Preprocess to a File -> Yes，使Visual Studio编译时把宏展开后的代码保存到与.cpp同名的.i文件中。  

![日志文件夹](/assets/cpp/PreprocesstoaFile.png)  

# WIN32宏
在 Win32 配置下，WIN32 在“项目属性-C/C++-预处理器-预处理器定义”里声明了，而在 x64 配置下，这个常量并不在项目预定义列表中。这是否说明可以根据 WIN32 来判断是否在 x64 平台呢？不。在 Windows SDK 的 minwindef.h 下第 37 行有如下定义：

	#ifndef WIN32
	
	#define WIN32
	
	#endif

即是说，只要包含了 Windows.h，那么 WIN32 常量是肯定定义了的，所以不能用于判断平台环境。但是如果在预处理定义里删掉 WIN32，又不包含 Windows.h，那么 WIN32 未定义

# _WIN32，_WIN64
_WIN32 和 _WIN64，这两个比较特别，没有任何显式定义。在 Windows.h 里没有，在“项目属性-C/C++-预处理器-预处理器定义”下也没有。根据 MSDN，这是由编译器（ml.exe/ml64.exe）内部定义的。具体描述是 

	_WIN32：Defined for applications for Win32 and Win64. Always defined.
	_WIN64：Defined for applications for Win64.

WIN32宏   --只要包含了 Windows.h，那么 WIN32 常量是肯定定义了的，所以不能用于判断平台环境

	_WIN32     --32位和64位程序都有，且总是定义的.
	_WIN64    --只有64位程序才有

WIN32/_WIN32 可以用来判断是否 Windows 系统（对于跨平台程序），而 _WIN64 用来判断编译环境是 x86 还是 x64