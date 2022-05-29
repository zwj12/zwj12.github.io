---
layout: post
title: "Routed Event"
date: 2022-05-20 16:37:00 +0800
author: Michael
categories: WPF
---

# 定义
路由事件由只读的静态字段表示，在静态构造函数中注册（使用EventManager.RegisterRoutedEvent方法注册），并通过标准的.Net事件定义并进行封装。

    public static readonly RoutedEvent ClickEvent = EventManager.RegisterRoutedEvent("Click", RoutingStrategy.Bubble, typeof(RoutedPropertyChangedEventHandler<string>), typeof(TuningButtonUserControl));

    public event RoutedPropertyChangedEventHandler<string> Click
    {
        add { AddHandler(ClickEvent, value); }
        remove { RemoveHandler(ClickEvent, value); }
    }

# 引发路由事件
路由事件不是通过传统的.NET事件封装器引发，而是使用RaiseEvent()方法引发事件，所有元素都从UIElement类继承了该方法。所有WPF事件都为事件签名使用熟悉的.NET约定。每个事件处理程序的第一个参数（sender参数）都提供引发改事件的对象引用。第二个参数是EventArgs对象，该对象与其他所有可能很重要的附加细节绑定在一起。  
RaiseEvent可以引发其它控件注册的事件，但是一定要注意引发控件的冒泡顺序。

	<Window x:Class="WpfAppUtility.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:WpfAppUtility"
        mc:Ignorable="d"
        Title="MainWindow" Height="800" Width="800">
       
    	<Grid x:Name="grid" >
	    </Grid>
	
	</Window>

	//如果事件注册在Window的Grid控件中，那么通过this.RaiseEvent是引发事件是不会触发动作的，因为this引用的是Window，this.RaiseEvent引发的事件只会在Window的父控件中触发动作。
    this.grid.AddHandler(TuningButtonUserControl.ClickEvent, new RoutedEventHandler(this.test_Click));
	this.RaiseEvent(new RoutedEventArgs(TuningButtonUserControl.ClickEvent));

	//如果事件注册在Window控件中，那么通过this.grid.RaiseEvent是引发事件是会触发动作的，因为RaiseEvent由grid控件引发，然后冒泡到父控件触发父控件的动作
    this.AddHandler(TuningButtonUserControl.ClickEvent, new RoutedEventHandler(this.test_Click));            
    this.grid.RaiseEvent(new RoutedEventArgs(TuningButtonUserControl.ClickEvent));

# 事件路由
1. Bubble，在包含层次中向上传递的冒泡路由事件，该事件首先由被单击的元素引发，接下来被改元素的父元素引发，然后被父元素的父元素引发，以此类推，直到WPF到达元素树的顶部为止。
2. Direct，与普通.NET事件类似的直接路由事件，它们源于一个元素，不传递给其他元素。
3. Tunnel，在包含层次中向下传递的隧道路由事件。首先在窗口级别上，然后是更具体的容器，直至到达当按下键时具有焦点的元素。

# RoutedEventArgs
冒泡路由事件时，sender参数提供了对整个链条上最后那个链接的引用。如果从图片向上冒泡到标签，sender参数就会引用标签对象。如果希望确定事件最初发生的位置，可从RoutedEventArgs类的属性获得。

# 路由事件与附加事件
1. Runtime(运行时)提供两个机制:一个机制能通知发生了紧急事件；另一个机制则规定在发生事件时应该允许什么方法，这正是事件和委托的用途。
2. WPF路由事件：路由事件的事件拥有者和事件响应者之间没有直接显示的订阅关系，事件的拥有者只负责激发事件，事件将有谁响应它并不知道，事件的响应者则安装有事件监听器，针对某类事件进行侦听，当有此类事件传递至此时事件响应者就使用事件处理器来响应事件并觉得事件是否可以继续传递。
3. 父控件可以通过附加事件订阅子控件的事件，但是需要该事件为冒泡事件才能触发动作。
4. 附加事件的本质也是路由事件，路由事件的宿主是Button、Grid等这些我们可以在界面上看得见的控件对象，而附加事件的宿主是Binding类、Mouse类、KeyBoard类这种无法在界面显示的类对象。附加事件的提出就是为了让这种我们无法看见的类也可以通过路由事件同其他类对象进行交流。
	
		//实例:一个grid中包含一个button，点击button,查看路由事件传递路径
		public Window1()
		{
		    InitializcComponent();
		    this.grid.AddHandler(Button.ClickEvent,new RouteEventHandler(this.ButtonClicked));
		}

		private void ButtonClicked(object sender,RoutedEventArgs e)
		{
		    MessageBox.Show(e.OriginalSource as FrameworkElement).Name);
		}
		/*
		    因为路由事件时从内部一层一层传递出来到最后到达最外层的grid,并且有grid元素将事件消息传递给ButtonClicked方法来处理，所以传入ButtonClicked方法的参数sender时间上是grid(LogicalTree上的消息源头)而不是点击的button，想要查看事件的源头，则需使用e.OriginalSource(VisualTree上的消息源头).
		*/