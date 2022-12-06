---
layout: post
title: "SynchronizationContext"
date: 2022-10-31 09:09:00 +0800
author: Michael
categories: CSharp
---

# 同步上下文 SynchronizationContext
非UI线程需要将对UI元素的所有更改安排到UI线程。这就是同步上下文提供的内容。它允许将一个工作单元（执行某些方法）发布到不同的上下文 - 在这种情况下是UI线程。无论使用哪种平台（ASP.NET 、WinForm 、WPF 等），所有.NET程序都包含同步上下文的概念。Microsoft .NET Framework提供了同步上下文的SynchronizationContext类。但是该类并不仅仅用于UI线程，理论上任何线程都可以使用。


	public static SynchronizationContext UiSynchronizationContext { get; set; }
	if (UiSynchronizationContext == null)
    {
        UiSynchronizationContext = SynchronizationContext.Current;
    }


# SynchronizationContext.Send(SendOrPostCallback d,object state);


# SynchronizationContext.Post(SendOrPostCallback d,object state);

        private SynchronizationContext context;

        private void Form1_Load(object sender, EventArgs e)
        {
            //此处就是之前提的在主线程获得SynchronizationContext
            context = SynchronizationContext.Current;
            //之后可以开线程了
            Thread thread = new Thread(new ThreadStart(Start));
            thread.IsBackground = true;
            thread.Start();
        }

        private void Start()
        { 
            for(int i=0;i<100;++i)
            {
                //这边即可正常调用主界面的控件了
                context.Send(operation, i);//正确
                //按原先直接应用，因为使用到控件会报错
                operation(i);//报错
                Thread.Sleep(100);
            }
        }

        private void operation(object obj)
        {
            textBox1.AppendText(obj.ToString() + "\r\n"); 
        }

# SynchronizationContext.Current 
此属性可用于将同步上下文从一个线程传播到另一个线程。