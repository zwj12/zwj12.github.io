---
layout: post
title: "CFormView"
date: 2022-10-16 14:12:00 +0800
author: Michael
categories: CPP
---

# PreCreateWindow
通常在PreCreateWindow中设置样式

# OnInitialUpdate
视图窗口完全建立后第一个被框架调用的函数。框架在第一次调用OnDraw前会调用OnInitialUpdate。构造函数生成本类的对象，但没有产生窗口，OnCreate后窗口产生， 然后才是视图的OnInitialUpDate，一般在这里对视图的显示做初始化。简单点,就是ONCREATE只是产生VIEW的基本结构和变量而在OnInitialUpDate()中,主要初始化视图中控件等。对各个变量进行初始化操作。PreCreateWindow在OnCreate之前调用。

    PreCreateWindow -> OnCreate -> OnInitialUpdate
