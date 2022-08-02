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
