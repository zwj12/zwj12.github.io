---
layout: post
title: "DataTemplate"
date: 2022-05-30 16:38:00 +0800
author: Michael
categories: WPF
---

# 数据模板
需要为一种不可见的数据类型提供外观. 比如如果你把一个DateTime的对象作为Button的内容, 因为DateTime并不是一个可视的元素(UIElement), WPF会默认把其渲染成string; 为了提供更好的用户体验, 我们可以给它添加一个模板, 以控制WPF对DateTime对象的渲染。通过ContentTemplate属性设置的DT不会影响外部Button的渲染。

数据模板常用在3种类型的控件:

![日志文件夹](/assets/wpf/DataTemplate.jpg)   

# DataTemplate & ControlTemplate
通过ContentTemplate属性设置的DT不会影响外部Button的渲染, 而通过CT则会影响Button的渲染, 如Button的边框, 高亮都不见了，就好像CT会影响外部的Container(在这里是一个Button)的渲染, 而DT则会影响Containner里的Content的渲染; 所以在有些地方, 如ItemsControl中, CT是通过ItemContainerStyle设置, 而DT是通过ItemTemplate设置的.DataTemplate用于为底层数据提供可视结构，而ControlTemplate与底层数据无关，仅为控件本身提供可视化布局。ControlTemplate通常只包含TemplateBinding表达式，绑定回控件本身的属性，而DataTemplate将包含标准绑定表达式，并绑定到其DataContext（业务/域对象或视图模型）的属性，它们面对的绑定对象类型不一致。

# ContentControl.ContentTemplate

	public System.Windows.DataTemplate ContentTemplate { get; set; }
	
	<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
	        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
	        xmlns:sys="clr-namespace:System;assembly=mscorlib"
	        Title="Window1" Height="300" Width="300">
	    <Button>
	        <Button.ContentTemplate>
	            <DataTemplate>
	                <StackPanel Orientation="Horizontal">
	                    <Button Content="{Binding Year}" />
	                    <Button Content="{Binding Month}" />
	                    <Button Content="{Binding Day}" />
	                </StackPanel>
	            </DataTemplate>
	        </Button.ContentTemplate>
	        <sys:DateTime>3/1/2008</sys:DateTime>
	    </Button>
	</Window>