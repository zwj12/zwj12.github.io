---
layout: post
title: "Multi Thread"
date: 2021-12-01 15:24:00 +0800
author: Michael
categories: CSharp
---

# 背景线程VS前台线程
如果把线程的背景模式设置为false（默认），那么主线程和创建的线程是处于同一级别的，主线程关闭后，创建的线程还是在运行的，只有等全部线程都执行完，操作系统才会认为它执行完。但是如果把线程的背景模式设置为true，那么当主线程执行完后，创建的线程会被自动关闭掉，哪怕创建的线程没有执行完，也会被关闭掉。可以使用下列代码测试两者的区别。

    ThreadTest threadTest = new ThreadTest();
    threadTest.TestMultiThread();
    Console.WriteLine("thread End {0}", Thread.CurrentThread.ManagedThreadId);

    threadTest.TestMultiThread();
    Console.WriteLine("thread End {0}", Thread.CurrentThread.ManagedThreadId);


	public class ThreadTest
    {
        public void TestMultiThread()
        {
            Thread thread_A=new Thread(new ThreadStart(ThreadProc_A));
            thread_A.IsBackground = true;
            thread_A.Start();

        }

        public void ThreadProc_A()
        {
            Console.WriteLine("thread_A Start {0}", Thread.CurrentThread.ManagedThreadId);
            Thread thread_B = new Thread(new ThreadStart(ThreadProc_B));
            thread_B.IsBackground = true;
            thread_B.Start();
            Thread.Sleep(10000);
            Console.WriteLine("thread_A End {0}", Thread.CurrentThread.ManagedThreadId);
        }

        public void ThreadProc_B()
        {
            Console.WriteLine("thread_B Start {0}", Thread.CurrentThread.ManagedThreadId);
            Thread.Sleep(50000);
            Console.WriteLine("thread_B End {0}", Thread.CurrentThread.ManagedThreadId);
        }

    }
