---
layout: post
title: "Assembly Information"
date: 2022-01-14 08:58:00 +0800
author: Michael
categories: CSharp
---

# Assembly Information
Assembly Information对照如下：  
![日志文件夹](/assets/csharp/AssemblyInformation.png)  

# 获取dll的地址
	System.Reflection.Assembly.GetExecutingAssembly().Location 

# 获取dll版本
	System.Reflection.Assembly.GetExecutingAssembly().GetName().Version.ToString()

# 获取程序基目录，或dll所在目录
	System.AppDomain.CurrentDomain.BaseDirectory //D:\mycode\
	Application.StartupPath //D:\mycode

# 获取当前工作目录current working directory
如果把快捷方式挂载在Windows 10操作系统的Start页面，且没有设置快捷方式的Start in属性，这个页面的默认当前工作目录是C:\WINDOWS\System32。如果在文件夹中搜索程序，在搜索页面启动程序的默认当前工作目录也是C:\WINDOWS\System32。

	System.Environment.CurrentDirectory

![日志文件夹](/assets/windows/ShortcutStartIn.png) 

# 友元程序集
通过设置友元程序集可以让另一个项目访问本项目的internal对象，方便单元测试。

	using System;
	using System.Collections.Generic;
	using System.Linq;
	using System.Text;
	using System.Threading.Tasks;
	
	using System.Runtime.CompilerServices;

	[assembly: InternalsVisibleTo("UnitTestProject1")]	
	namespace Project1
	{
	    internal class Calendar
	    {
	        static void Main(string[] args)
	        {
	            DateTime now = GetCurrentDate();
	            Console.WriteLine($"Today's date is {now}");
	            Console.ReadLine();
	        }
	
	        internal static DateTime GetCurrentDate()
	        {
	            return DateTime.Now.Date;
	        }
	    }
	}