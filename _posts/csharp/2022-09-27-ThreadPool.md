---
layout: post
title: "ThreadPool"
date: 2022-09-27 09:01:00 +0800
author: Michael
categories: CSharp
---

# 现场池
    for (int i = 1; i <= 10; i++)
    {
        //ThreadPool执行任务
        ThreadPool.QueueUserWorkItem(new WaitCallback((obj) => {
            Console.WriteLine($"第{obj}个执行任务");
        }), i);
    }
    Console.ReadKey();
