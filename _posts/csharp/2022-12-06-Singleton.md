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