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

# 预编译器常量
__FILE__为预编译器常量，返回当前编译的文件名，标准C++推荐编译器实现时预定义的宏, 是由编译器定义的宏，表示当前文件名, 常用于调试。报告错误时，我们可以方便地知道是哪个文件出错。
__LINE__编译器在编译的文件的第几行；
__DATE__返回当前的日期Jul-20-2004；
__TIME__返回当前的时间hh:mm:ss；   
__TIMESTAMP__的预定义的编译器宏始终返回时间戳信息在太平洋标准的时间内无论本地时间和CL.EXE 的运行位置在计算机上的时区。     
__STDC__条件编译，意思是：如果定义了标准C或c++，那么编译这句话后面直到#endif 以前的源代码。
_STDC__cplusplus这两个都是标准宏，_STDC_表示是是否符合标准C
_cplusplus表示是否是C++

	#ifdef _DEBUG //如果定义了_DEBUG
	#define new DEBUG_NEW //则定义new为DEBUG_NEW
	#undef THIS_FILE //反定义，即清除THIS_FILE的宏定义
	static char THIS_FILE[] = __FILE__;
	#endif//结束宏定义     

# C语言宏定义中 # 和 ## 符号的用法
## 一个#的作用
一个#的作用就是把后面的参数当做一个字符串，也就是说等同于把后面的宏变量加上双引号,  #define  PRINT(NAME)  printf(#NAME)这个宏，等同于把NAME加上了双引号“”，即替换成了“NAME”，所以，第一个PRINT可以直接把括号内的内容打印出来。

	#define PRINT(NAME) printf(#NAME)

	PRINT(Hello world);  //printf("Hello world");

## 两个##的作用
两个##是连接符，即把两个宏变量拼接到一起。定义了两个宏LINK和POWER，LINK直接把两个宏变量拼接起来，所以n等于1234；POWER把两个宏变量和e顺次拼接，所以n2等于2e3，也就是等于2000。

	#define LINK(AA,BB) AA##BB
	#define POWER(AA,BB) AA##e##BB

	int n = LINK(12,34)
	int n2 = POWER(2,3)