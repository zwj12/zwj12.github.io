---
layout: post
title: "App.config"
date: 2022-06-12 16:15:00 +0800
author: Michael
categories: CSharp
---

# App.config
.NET 4.8的WPF程序在新建时，会自动添加App.config配置文件，但是.NET Core不会自动添加，需要右击 -> Add New Item -> General -> Application Configuration File手动添加。

# 转义字符
XML只有5个转义符: `&lt; &gt; &amp; &quot; &apos;` 他们分别时：< > & " '
