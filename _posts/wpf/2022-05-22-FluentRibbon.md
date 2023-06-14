---
layout: post
title: "Fluent.Ribbon"
date: 2022-05-22 16:37:00 +0800
author: Michael
categories: WPF
---

# NuGet包
	Fluent.Ribbon

# 添加资源
	<Application.Resources>
	    <!-- Attach default Theme -->
	    <ResourceDictionary Source="pack://application:,,,/Fluent;Component/Themes/Generic.xaml" />
	</Application.Resources>

    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="pack://application:,,,/Fluent;Component/Themes/Generic.xaml" />
                <ResourceDictionary>
                    <vm:ViewModelLocator x:Key="Locator" d:IsDataSource="True" xmlns:vm="clr-namespace:PickMasterUtility.ViewModel" />
                </ResourceDictionary>
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>

# 替换窗口
	<Fluent:RibbonWindow x:Class="MyFirstRibbonProject.MyFirstWindow"
	                     xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
	                     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
	                     xmlns:Fluent="urn:fluent-ribbon"
	                     Title="My first RibbonWindow" 
	                     Width="800" 
	                     Height="600">
	    <Grid>
	        <Grid.RowDefinitions>
	            <RowDefinition Height="Auto" />
	            <RowDefinition Height="*" />
	        </Grid.RowDefinitions>
	    </Grid>
	</Fluent:RibbonWindow>

	namespace MyFirstRibbonProject
	{
	    /// <summary>
	    /// Represents the main window of the application
	    /// </summary>
	    public partial class MyFirstWindow
		//public partial class MainWindow : Fluent.RibbonWindow
	    {
	        /// <summary>
	        /// Default constructor
	        /// </summary>
	        public MyFirstWindow()
	        {
	            this.InitializeComponent();
	        }
	    }
	}

# 布局
    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition />
            <RowDefinition Height="Auto"></RowDefinition>
        </Grid.RowDefinitions>

        <Fluent:Ribbon Grid.Row="0">
            <Fluent:Ribbon.QuickAccessItems>
                <Fluent:QuickAccessMenuItem Header="Test1"/>
                <Fluent:QuickAccessMenuItem  Header="Test2" />
            </Fluent:Ribbon.QuickAccessItems>

            <Fluent:Ribbon.Menu>
                <Fluent:Backstage>
                    <Fluent:BackstageTabControl>
                        <Fluent:BackstageTabItem Header="Test3" />
                        <Fluent:BackstageTabItem Header="Test4" />
                        <Fluent:Button Header="Test5" />
                    </Fluent:BackstageTabControl>
                </Fluent:Backstage>
            </Fluent:Ribbon.Menu>

            <Fluent:RibbonTabItem Header="Home" ReduceOrder="View"  >
                <Fluent:RibbonGroupBox Header="View">
                    <Fluent:Button x:Name="btnProductsView" Header="Products" SizeDefinition = "Large, Middle, Small" />
                </Fluent:RibbonGroupBox>
            </Fluent:RibbonTabItem>

        </Fluent:Ribbon>

        <ContentControl Name="contentPage" Grid.Row="1"/>

        <Fluent:StatusBar Grid.Row ="2">
            <Fluent:StatusBarItem Title="Left placed item"
                          Value="150"
                          HorizontalAlignment="Left">
                <TextBlock Text="150 px" />
            </Fluent:StatusBarItem>

            <Separator HorizontalAlignment="Left" />

            <Fluent:StatusBarItem Title="Second left placed item"
                          Value="Value shown in ContextMenu"
                          ToolTip="Your ToolTip"
                          Content="Content shown in StatusBar"
                          HorizontalAlignment="Left" />

            <Fluent:StatusBarItem Title="Item placed on the right side"
                          HorizontalAlignment="Right"
                          Value="Your value which is also used as content if no content is set." />
        </Fluent:StatusBar>
    </Grid>

# RibbonTabItem.ReduceOrder
当界面缩小时，按设置的值从右到左依次缩小，括号代表可以Scaleable。

# SizeDefinition
SizeDefinition = "Large, Middle, Small"  
[https://docs.microsoft.com/en-us/windows/win32/windowsribbon/windowsribbon-templates](https://docs.microsoft.com/en-us/windows/win32/windowsribbon/windowsribbon-templates)  

1. Large，占一格
1. Middle，占一行
1. Small，占一行，只显示图标