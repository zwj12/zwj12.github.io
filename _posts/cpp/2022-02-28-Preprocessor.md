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

# pragma once
pragma once可以放置在头文件中任何位置，但是通常推荐放置在开头位置。

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
