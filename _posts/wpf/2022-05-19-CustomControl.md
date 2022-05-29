---
layout: post
title: "Custom Control"
date: 2022-05-19 11:37:00 +0800
author: Michael
categories: WPF
---

# 自定义控件
1. 自定义控件可以继承自System.Windows.Controls.Control
2. 默认样式需要放在Themes文件夹的generic.xaml资源字典中
3. 通知WPF提供新样式，再静态构造函数中调用`DefaultStyleKeyProperty.OverrideMetadata(typeof(ColorPicker), new FrameworkPropertyMetadata(typeof(ColorPicker)));`该函数会自动识别Themes文件夹的generic.xaml资源字典中的控件样式。