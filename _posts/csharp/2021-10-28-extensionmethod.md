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

# 扩展方法
扩展方法可以将方法写入最初没有提供该方法的类中。扩展方法在静态类中声明，定义为一个静态方法，其中第一个参数定义了它扩展的类型。为了区分扩展方法和一般的静态方法，扩展方法还需要给第一个参数使用this关键字。扩展方法不能访问它扩展的类型的私有成员。调用扩展方法只是调用静态方法的一种新语法。

    public static class StringExtension
    {
        public static void Foo(this string s)
        {
            Console.WriteLine("Foo invoked for {0}", s);
        }
    }

	string s = "Hello";
	s.Foo();

	//调用扩展方法只是调用静态方法的一种新语法
	string s= "Hello";
	StringExtension.Foo(s);

# LINQ扩展方法
定义LINQ扩展方法的一个类是System.Linq命名空间中的Enumerable。只需导入这个命名空间，就打开了这个类的扩展方法的作用域。

# LINQ中的查询语法和方法语法
编译代码时，查询语法必须转换为针对 .NET 公共语言运行时 (CLR) 的方法调用。 这些方法调用会调用标准查询运算符（名称为 Where、Select、GroupBy、Join、Max 和 Average 等）。 可以使用方法语法（而不查询语法）来直接调用它们。查询语法和方法语法在语义上是相同的，但是查询语法更简单且更易于阅读。

# yield return
使用yield return 语句可一次返回一个元素。返回类型必须为 IEnumerable、IEnumerable<T>、IEnumerator 或 IEnumerator<T>。

    public static IEnumerable<T> Where<T>(this IEnumerable<T> source, Func<T, bool> predicate)
    {
        foreach (T item in source)
        {
            if (predicate(item))
                yield return item;
        }
    }