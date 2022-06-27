---
layout: post
title: "TemplateBinding"
date: 2022-05-31 09:55:00 +0800
author: Michael
categories: WPF
---

# TemplateBinding是Binding的一个轻量级版本
需要把ControlTemplate里面的某个Property绑定到应用该ControlTemplate的控件的对应Property上。

	<TextBlock Text="{TemplateBinding MyText}"/>
	<TextBlock Text="{Binding Path=MyText, Mode=OneWay, RelativeSource={RelativeSource TemplatedParent}}"/>