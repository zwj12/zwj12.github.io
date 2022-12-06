---
layout: post
title: "Delegate Event"
date: 2022-10-15 14:35:00 +0800
author: Michael
categories: CSharp
---

# Action<T> Delegate
封装一个方法，该方法有0个或多个参数并且不返回值。

	public delegate void Action<in T>(T obj);
	public delegate void Action<in T1,in T2>(T1 arg1, T2 arg2);

# Func<TResult> Delegate
封装一个方法，该方法具有0个或多个参数，且返回由 TResult 参数指定的类型的值。

	public delegate TResult Func<out TResult>();
	public delegate TResult Func<in T,out TResult>(T arg);
	public delegate TResult Func<in T1,in T2,out TResult>(T1 arg1, T2 arg2);

# 事件 EventHandler 委托
表示将用于处理不具有事件数据的事件的方法。

	public delegate void EventHandler(object sender, EventArgs e);
	public delegate void EventHandler<TEventArgs>(object sender, TEventArgs e);

    public static event EventHandler<uint> OnFound;
    public static event EventHandler<uint> OnLost;
