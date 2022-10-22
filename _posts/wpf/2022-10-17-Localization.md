---
layout: post
title: "Localization"
date: 2022-10-17 16:09:00 +0800
author: Michael
categories: CSharp
---

# 方案一：使用Resources文件实现
这个方案也不支持动态切换语言，只支持直接使用字符串，不支持TypeConverter，甚至也不支持除字符串以外的其它XAML内置类型（即Boolea,Char,Decimal,Single,Double,Int16,Int32,Int64,TimeSpan,Uri,Byte,Array等类型）。例如使用Label.resx中名为Background值为 #880000FF 的字符串为Grid.Background实现本地化。但是非常简单。

## 智能感应
使用方案一基础版，支持全部智能感应。但是如果使用方案一的增强版，智能感应不支持XAML，但是支持语法检查，如果没有该字段，会有波浪线出现，支持在代码中感应。

## 添加多语言字符串
在程序的Resources文件中添加所有的字符串，然后复制并命名为Resources.xx-xx.resx，其中xx-xx为语言标识。Culture names follow the standard defined by BCP 47. 这边新的Resources.xx-xx.resx文件有一个Custom Tool属性：PublicResXFileCodeGenerator，从测试看，可以删除，如果保留会自动生成一个Resources.xx-xx.Designer.cs空文件，貌似没啥作用。

![日志文件夹](/assets/wpf/Resources.zh-CN.resx.png)  
![日志文件夹](/assets/wpf/PublicResXFileCodeGenerator.png)  

## 重载Application.OnStartup函数，并设置当前线程的CurrentUICulture或者直接设置当前项目的Properties.Resources.Culture就可以了。

    public partial class App : Application
    {

        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

			PickMasterUtility.Properties.Resources.Culture = new System.Globalization.CultureInfo("zh-CN");

            Thread.CurrentThread.CurrentUICulture = new System.Globalization.CultureInfo("zh-CN");
            //Thread.CurrentThread.CurrentUICulture= new System.Globalization.CultureInfo("fr-FR");
        }
    }

## 使用x:Static引用多语言字符串

<Window x:Class="WpfApp2.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:WpfApp2"
        xmlns:localResources="clr-namespace:WpfApp2.Properties"
        mc:Ignorable="d"
        Title="MainWindow" Height="450" Width="800">
    <Grid>
        <StackPanel Loaded="StackPanel_Loaded">
            <Button Content="{x:Static localResources:Resources.button1}"></Button>
            <Button Content="{x:Static localResources:Resources.button2}"></Button>
        </StackPanel>
    </Grid>
</Window>

## 编译
使用Resources文件方案编译程序后，会自动生成所添加的多语言的xx-xx/yyyy.resources.dll资源dll文件。其中xx-xx为语言字符串，yyyy是程序名称。

## 增强版
基础的Resources文件实现多语言方案不支持动态切换，但是可以使用Binding的方式突破这个限制。

### 新建一个具有默认的构造函数的ApplicationResources类，用于创建应用程序级别的资源

    public class ApplicationResources :INotifyPropertyChanged
    {
        public static ApplicationResources Current { get; private set; }

        public Resources Labels { get; set; }

        private string language;
        public string Language
        {
            get { return language; }
            set
            {
                if (language == value)
                    return;

                language = value;
                var cultureInfo = new CultureInfo(value);
                Thread.CurrentThread.CurrentUICulture = cultureInfo;
                Thread.CurrentThread.CurrentCulture = cultureInfo;
                Resources.Culture = cultureInfo;

                RaiseProoertyChanged();
            }
        }

        public ApplicationResources()
        {
            Current = this;
            Labels = new Resources();
        }

        public event PropertyChangedEventHandler PropertyChanged;

        public void ChangeCulture(System.Globalization.CultureInfo cultureInfo)
        {
            Thread.CurrentThread.CurrentUICulture = cultureInfo;
            Thread.CurrentThread.CurrentCulture = cultureInfo;
            Resources.Culture = cultureInfo;

            if (Current != null)
                Current.RaiseProoertyChanged();
        }

        public void RaiseProoertyChanged()
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(""));
        }
    }

### 在App.xaml文件中创建一个应用程序级别资源的ApplicationResources类

    <Application.Resources>
        
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="pack://application:,,,/Fluent;Component/Themes/Generic.xaml" />
                <ResourceDictionary>
                    <vm:ViewModelLocator x:Key="Locator" d:IsDataSource="True" xmlns:vm="clr-namespace:PickMasterUtility.ViewModel" />
                </ResourceDictionary>
            </ResourceDictionary.MergedDictionaries>
            <local:ApplicationResources x:Key="R"/>
        </ResourceDictionary>
       
    </Application.Resources>

### 绑定应用程序级别资源的ApplicationResources到控件上
    <Fluent:Button x:Name="MenuItem_ControlTemplateDisplay" Header="{Binding Labels.ControlTemplate, Source={StaticResource R}}" ToolTip="Display Control Template Window" Click="MenuItem_ControlTemplateDisplay_Click"/>

### 动态改变语言
    if (PickMasterUtility.Properties.Resources.Culture== CultureInfo.InstalledUICulture)
    {
        var cultureInfo = new CultureInfo("zh-CN");
        ApplicationResources.Current.ChangeCulture(cultureInfo);
    }
    else
    {
        ApplicationResources.Current.ChangeCulture(CultureInfo.InstalledUICulture);
    }

### 设计时支持
在应用程序资源的Application.Resources中可以直接设置语言，可以在设计时自动切换语言。

	<local:ApplicationResources x:Key="R"  Language="zh-CN"/>

### 拆分主程序和语言包
可以把语言包和主程序分成两个项目，以dll的形式嵌入到主程序中。这里有一个bug，如果使用拆分项目，那么需要手动把资源类的internal改为public，虽然类是public，但是Visual Studio不会把构造函数改为public。

![日志文件夹](/assets/wpf/ResourcesDll.png)  

### ResXManager插件
可以使用Visual Studio Extension "ResXManager"管理多语言。安装好该插件后，可以从菜单Tools -> ResX Manager打开。

![日志文件夹](/assets/wpf/ResXManager.png)  


# 方案二：使用资源字典方案
使用该方案，有一个致命缺点，就是在 XAML 中，引用 DynamicResource 的属性必须为依赖属性，否则会出错。智能感应支持XAML，但是不支持在代码中感应。

## 在Resources文件夹中创建StringResources.xaml, StringResources.xx-xx.xaml文件。

	//默认资源字典文件：Resources/StringResources.xaml
	<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
	                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
	                    xmlns:system="clr-namespace:System;assembly=mscorlib">
	
	    <system:String x:Key="S.Culture">Culture</system:String>
	    <system:String x:Key="S.Tools">Tools</system:String>
	    
	</ResourceDictionary>

	//中文资源字典文件：Resources/StringResources.zh-CN.xaml
	<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
	                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
	                    xmlns:system="clr-namespace:System;assembly=mscorlib">
	
	    <system:String x:Key="S.Culture">区域性</system:String>
	    <system:String x:Key="S.Tools">工具</system:String>
	    
	</ResourceDictionary>

## 添加资源文件到应用程序资源中使设计时支持，理论上不需要这一步，但是会方便设计
    <Application.Resources>
        
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="pack://application:,,,/Fluent;Component/Themes/Generic.xaml" />
                <ResourceDictionary>
                    <vm:ViewModelLocator x:Key="Locator" d:IsDataSource="True" xmlns:vm="clr-namespace:PickMasterUtility.ViewModel" />
                </ResourceDictionary>
                <ResourceDictionary Source="/PickMasterUtility;component/Resources/StringResources.xaml"/>
                <!--<ResourceDictionary Source="/PickMasterUtility;component/Resources/StringResources.zh-CN.xaml"/>-->
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
       
    </Application.Resources>

## 启动时加载资源，设置语言文本

    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

			string culture = "zh-CN";
            ResourceDictionary dictionary = new ResourceDictionary { Source = new Uri($@"Resources\StringResources.{culture}.xaml", UriKind.RelativeOrAbsolute) };
            Application.Current.Resources.MergedDictionaries.Add(dictionary);
        }
    }

## 动态切换语言

	string culture = "zh-CN";
    ResourceDictionary dictionary = new ResourceDictionary { Source = new Uri($@"Resources\StringResources.{culture}.xaml", UriKind.RelativeOrAbsolute) };
    Application.Current.Resources.MergedDictionaries.Add(dictionary);


# CultureInfo, DateTimeFormatInfo, NumberFormatInfo 
System.Globalization命名空间最重要的类是CultureInfo，表示文化，定义了日历、数字和日期的格式，以及和文化一起使用的排序字符串。CultureInfo, DateTimeFormatInfo, NumberFormatInfo均实现了IFormatProvider接口。

    int val = 1234567890;
    Console.WriteLine(val.ToString("N"));
    Console.WriteLine(val.ToString("N", new CultureInfo("fr-FR")));
    Thread.CurrentThread.CurrentCulture = new CultureInfo("de-DE");
    Console.WriteLine(val.ToString("N"));

# 当前操作系统CultureInfo
CultureInfo.InstalledUICulture

# 语言字符串

	fr-FR : French
	zh-CN : Chinese
	en-US : English
	de-DE : German
	it-IT : Italian
	es-ES : Spanish
	ja-JP : Japanese
	ko-KR : Korean

# resgen工具
可以使用resgen把一个使用等于号定义的简单字符串表转化为resX格式的字符串。同样也可以使用该程序把resX文件转化为简单字符串表。

	//strings.txt，简单字符串表
	Title=book
	Author=Michael
	Company=ABB

	//转化为resX格式的字符串
	resgen strings.txt strings.resX

	//转化为简单字符串
	resgen Resources.zh-CN.resx strings.zh-CN.txt

# NeutralLanaguage设置
可以把应用程序的NeutralLanaguage设置为主要语言。可以提高ResourceManager性能。

![日志文件夹](/assets/wpf/NeutralLanaguage.png)  
