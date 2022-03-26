---
layout: post
title: "access modifier"
date: 2022-03-18 12:08:00 +0800
author: Michael
categories: CSharp
---

# private set
	 public class Student
	    {
	        public int MyProperty { get; set; }
	
	        public int MyProperty1 { get; private set; }
	
	        public int MyProperty2 { get;  }
	
	        public Student()
	        {
	            this.MyProperty = 1;
	            this.MyProperty1 = 2;
	            this.MyProperty2 = 3;
	        }
	
	        public void TestValue()
	        {
	            this.MyProperty = 4;
	
	            //只能在类内部设置
	            this.MyProperty1 = 5;
	
	            //语法错误，该属性没有set语句，不能在构造函数外设置值
	            this.MyProperty2 = 6;
	        }
	    }