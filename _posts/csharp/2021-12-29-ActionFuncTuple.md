---
layout: post
title: "Action & Func & Tuple"
date: 2021-12-29 10:52:00 +0800
author: Michael
categories: CSharp
---

# Action & Func
1. Action用于没有返回值的方法（参数可以根据自己情况进行传递）
1. Func恰恰相反用于有返回值的方法（同样参数根据自己情况情况）
1. 记住无返回就用action，有返回就用Func

# Tuple<T1,T2> Class

    public void NewItemSourceCreated(Tuple<int, string, int> tuple)
    {

    }