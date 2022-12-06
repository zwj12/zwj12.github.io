---
layout: post
title: "Class Library"
date: 2022-10-31 08:09:00 +0800
author: Michael
categories: CSharp
---

# 在Class Library中添加WPF窗口
默认C#类库中是不能添加WPF窗口的，可以在项目的csproj文件中添加如下配置信息，即可突破这个限制，如不清楚该配置添加的位置，可以打开一个正常的WPF应用程序的csproj文件，即可知道设置位置。如果项目编译提示缺少基础库System.Xaml等，可以先添加一个WPF的User Control即可自动引用相关类库。  

	<ProjectTypeGuids>{60dc8134-eba5-43b8-bcc9-bb4bc16c2548};{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}</ProjectTypeGuids>
    <WarningLevel>4</WarningLevel>
    <AutoGenerateBindingRedirects>true</AutoGenerateBindingRedirects>

