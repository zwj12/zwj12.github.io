---
layout: post
title: "WindowChrome"
date: 2022-10-11 10:09:00 +0800
author: Michael
categories: CSharp
---

# 无边框
WPF中自定义的界面的方式可以分为两种，尽量使用 WindowChrome 而不要使用 AllowsTransparency=True： 

1. 使用 AllowsTransparency="True"和WindowStyle="None"，这种呢就相当于直接把原生非客户区给干掉了，然后我们在内容区域自己去实现非客户区，就会导致窗口自定的行为如：缩放，拖动，停靠边界放大。。。这些功能全都没有了，如果需要的话，是需要自己手动代码添加的。
2. 使用我们的WindowChrome来自定义界面， 这种方式保留了一个窗口基本的行为，只需要我们重新规划一下客户区和非客户区就行了。


    <WindowChrome.WindowChrome>
        <WindowChrome />
    </WindowChrome.WindowChrome>