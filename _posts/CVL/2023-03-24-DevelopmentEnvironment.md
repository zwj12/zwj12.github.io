---
layout: post
title: "Development Environment"
date: 2023-03-24 09:49:00 +0800
author: Michael
categories: CVL
---

# 环境变量 VISION_ROOT
安装CVL库后，会在环境变量中创建一个新的变量VISION_ROOT，该变量存储着CVL库的位置。  
![日志文件夹](/assets/CVL/vision_root.png)  

# CVL库头文件
Visual Studio C++ -> Properties -> C/C++ -> General -> Additional Include Directories -> $(VISION_ROOT)\defs  
![日志文件夹](/assets/CVL/AdditionalIncludeDirectories.png)  

# C++编译预处理宏 NOMINMAX
貌似这个可以不设置，Visual Studio C++ -> Properties -> C/C++ -> Preprocessor -> Preprocessor Definitions -> NOMINMAX  
![日志文件夹](/assets/CVL/PreprocessorDefinitions.png)  

# CVL库lib文件
Visual Studio C++ -> Properties -> Linker -> General -> Additional Library Directories -> $(VISION_ROOT)\lib\win64\cvl  
![日志文件夹](/assets/CVL/AdditionalLibraryDirectories.png)  
