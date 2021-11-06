---
layout: post
title: "C#原始类型扩展方法"
date: 2021-10-28 13:00:00 +0800
author: Michael
categories: CSharp
---

# C#原始类型扩展方法—this参数修饰符
扩展方法使您能够向现有类型“添加”方法，而无需创建新的派生类型、重新编译或以其他方式修改原始类型。扩展方法是一种特殊的静态方法，但可以像扩展类型上的实例方法一样进行调用。对于用 C# 和 Visual Basic 编写的客户端代码，调用扩展方法与调用在类型中实际定义的方法之间没有明显的差异。

	using System.Linq;
	using System.Text;
	using System;
	
	namespace CustomExtensions
	{
		//Extension methods must be defined in a static class
		public static class StringExtension
		{
		   // This is the extension method.
		   // The first parameter takes the "this" modifier
		   // and specifies the type for which the method is defined.
		   public static int WordCount(this String str)
		   {
		    	return str.Split(new char[] {' ', '.','?'}, StringSplitOptions.RemoveEmptyEntries).Length;
		   }
		}
	}

	namespace Extension_Methods_Simple
	{
		//Import the extension method namespace.
		using CustomExtensions;
		class Program
		{
		   static void Main(string[] args)
		   {
				string s = "The quick brown fox jumped over the lazy dog.";
				// Call the method as if it were an 
				// instance method on the type. Note that the first
				// parameter is not specified by the calling code.
				int i = s.WordCount();
				System.Console.WriteLine("Word count of s is {0}", i);
		   }
		}
	}
