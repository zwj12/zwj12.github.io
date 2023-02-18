---
layout: post
title: "WPF Resource"
date: 2022-05-17 13:29:00 +0800
author: Michael
categories: WPF
---

# 资源
资源是保存在可执行文件中的一种不可执行数据。在WPF的资源中，几乎可以包含图像、字符串等所有的任意CLR对象，只要对象有一个**默认的构造函数**和独立的属性。也就是说，应用程序中非程序代码的内容，比如点阵图、颜色、字型、动画/影片档以及字符串常量值，可将它们从程序中独立出来，单独包装成"资源(Resource)"。

# 图片资源编译
1. Build Action = Resource, 不能错误的设置为Embedded Resource, 因为Embedded Resource生成操作会在另一个更难访问的位置放置二进制数据。
2. 不要再Project Properties窗口中使用Resource选项卡。WPF不支持这种类型的资源URI。
3. 单独的资源流使用以下格式命名：AssemblyName.g.resources, 该资源目录下，还有WPF xaml文件的数据。
4. pack URI, WPF使用pack URI语法寻址，地址分为相对URI和绝对URI，相对地址如：`images/winter.jpg`，绝对地址如：`pack://application:,,,/images/winter.jpg`。三个逗号实际上是三个转义的斜杠。所以pack URI实际是以`application:///`开头的。

![日志文件夹](/assets/wpf/buildactionresource.png)   

# WPF资源
每个元素都提供了Resource属性，为了找到期望的资源，WPF在元素树中进行递归搜索。

# 资源字典
资源字典只是XAML文档，除了存储希望使用的资源外，不做其他任何事情。Build Action = Page, 也可以设置为Resource，这样会被嵌入到程序集中，但是不会被编译，如果设置为Page，会被编译为BAML，可以获得最佳性能。资源字典中的每个资源都必须具有唯一键。 在标记中定义资源时，可通过 x:Key 指令来分配唯一键。 

# 资源字典集合
MergedDictionaries是ResourceDictionary对象的一个集合，可使用该集合提供自己希望使用的资源集合。

    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="pack://application:,,,/Fluent;Component/Themes/Generic.xaml" />
                <ResourceDictionary>
                    <vm:ViewModelLocator x:Key="Locator" d:IsDataSource="True" xmlns:vm="clr-namespace:PickMasterUtility.ViewModel" />
                </ResourceDictionary>
				<ResourceDictionary Source="Resources/ConverterDictionary.xaml" />
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>

# pack URI
1. 相对地址：images/winter.jpg, "ImageLibrary;component/images/winter.jpg", "ImageLibrary;v1.25;dc642a7f5bd64912;component/images/winter.jpg"
2. 绝对地址：pack://application:,,,/images/winter.jpg, pack://application:,,,/ImageLibrary;component/images/winter.jpg
3. 对于“页”或“资源”生成操作(**Build Action=page**)，可以将指定程序集名称的 Source 属性指定为详细形式，并使用 component; 关键字引用程序集中的资源。例如，如果已编译的应用程序 DLL 命名为 MyApplication，并且要合并的资源 XAML 命名为 MergedDictionary.xaml，则为 Source 指定的正确值为：/MyApplication;component/MergedDictionary.xaml

		<ResourceDictionary Source="/PickMasterUtility;component/Resources/StringResources.xaml"/>

# 资源数据类型
在设置控件属性为资源时，资源的数据类型一定要和控件属性正确匹配，例如如果字体的数据类型为FontFamily，那么就一定要用FontFamily设置资源，不能使用String类型设置资源。XAML解析器只会在元素解析时使用转换器，即在设置WPF元素属性时可以使用字符串（此时XAML解析器会使用默认Converter转换器解析），但是如果使用资源绑定时，此时不会调用转换器，如果数据类型不一致，会直接抛出异常。

	<Window x:Class="WpfApp1.MainWindow"
	        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
	        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
	        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
	        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
	        xmlns:local="clr-namespace:WpfApp1"
	        xmlns:sys="clr-namespace:System;assembly=mscorlib"
	        mc:Ignorable="d"
	        Title="MainWindow" Height="450" Width="800">
	
	    <Window.Resources>
	        <FontFamily x:Key="ButtonFontFamily">Times New Roman</FontFamily>
	        <sys:Double x:Key="ButtonFontSize">18</sys:Double>
	        <FontWeight x:Key="ButonFontWeight">Bold</FontWeight>
	        <sys:String x:Key="ButtonFontFamilyString">Times New Roman</sys:String>
	    </Window.Resources>
	    <Grid>
	        <Button Name="cmd"
	                FontFamily="{StaticResource ButtonFontFamily}"
	                FontWeight="{StaticResource ButonFontWeight}"
	                FontSize="{StaticResource ButtonFontSize}">
	            Button
	        </Button>
	    </Grid>
	</Window>
