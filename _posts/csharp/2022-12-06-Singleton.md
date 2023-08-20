---
layout: post
title: "Pipe"
date: 2022-12-06 10:36:00 +0800
author: Michael
categories: CSharp
---

# No Thread Safe Singleton
	public sealed class Singleton1 {  
	    private Singleton1() {}  
	    private static Singleton1 instance = null;  
	    public static Singleton1 Instance {  
	        get {  
	            if (instance == null) {  
	                instance = new Singleton1();  
	            }  
	            return instance;  
	        }  
	    }  
	}  

# Thread Safety Singleton
性能欠佳，不推荐，因为每次获取对象都需要锁资源

	public sealed class Singleton2 {  
	    Singleton2() {}  
	    private static readonly object lock = new object();  
	    private static Singleton2 instance = null;  
	    public static Singleton2 Instance {  
	        get {  
	            lock(lock) {  
	                if (instance == null) {  
	                    instance = new Singleton2();  
	                }  
	                return instance;  
	            }  
	        }  
	    }  
	}  

# Thread Safety Singleton using Double-Check Locking
如果使用锁，推荐用这个

	public sealed class Singleton3 {  
	    Singleton3() {}  
	    private static readonly object lock = new object();  
	    private static Singleton3 instance = null;  
	    public static Singleton3 Instance {  
	        get {  
	            if (instance == null) {  
	                lock(lock) {  
	                    if (instance == null) {  
	                        instance = new Singleton3();  
	                    }  
	                }  
	            }  
	            return instance;  
	        }  
	    }  
	}  

# Thread Safe Singleton without using locks and no lazy instantiation
推荐使用Lazy

	public sealed class Singleton4    
	{    
	    private static readonly Singleton4 instance = new Singleton4();    
	    static Singleton4()    
	    {    
	    }    
	    private Singleton4()    
	    {    
	    }    
	    public static Singleton4 Instance    
	    {    
	        get    
	        {    
	            return instance;    
	        }    
	    }    
	}   

# Using .NET 4's Lazy<T> type
推荐使用这个，Lazy的默认构造函数是线程安全的。由于单例的构造函数是私有的，所以初始化Lazy时，必须传入一个匿名函数用于实例化这个单例类对象。记住类一定要是封闭的sealed。

	public sealed class Singleton5    
	{    
	    private Singleton5()    
	    {    
	    }    
	    private static readonly Lazy<Singleton5> lazy = new Lazy<Singleton5>(()=>new Singleton5());    
	    public static Singleton5 Instance    
	    {    
	        get    
	        {    
	            return lazy.Value;    
	        }    
	    }    
	}    