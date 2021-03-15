---
layout: post
title: "MvvmLight"
date: 2021-02-03 09:25:00 +0800
author: Michael
categories: CSharp
---

替换ViewModelLocator.cs代码中的命名空间：

	//using Microsoft.Practices.ServiceLocation;
	using CommonServiceLocator;

# MVVM
MVVM是Model、View、ViewModel的简写，这种模式的引入就是使用ViewModel来降低View和Model的耦合，说是降低View和Model的耦合。也可以说是是降低界面和逻辑的耦合，理想情况下界面和逻辑是完全分离的，单方面更改界面时不需要对逻辑代码改动，同样的逻辑代码更改时也不需要更改界面。同一个ViewModel可以使用完全不用的View进行展示，同一个View也可以使用不同的ViewModel以提供不同的操作。

1. Model  
Model就是一个class，是对现实中事物的抽象，开发过程中涉及到的事物都可以抽象为Model，例如客户，客户的姓名、编号、电话、住址等属性也对应了class中的Property，客户的下订单、付款等行为对应了class中的方法。

2. View  
View很好理解，就是界面。

3. ViewModel  
上面说过Model抽象，那么ViewModel就是对View的抽象。显示的数据对应着ViewMode中的Property，执行的命令对应着ViewModel中的Command。

![日志文件夹](/assets/develop/mvvm.jpg)  

# WPF中MVVM的解耦方式
在WPF的MVVM模式中，View和ViewModel之间数据和命令的关联都是通过绑定实现的，绑定后View和ViewModel并不产生直接的依赖。具体就是View中出现数据变化时会尝试修改绑定的目标。同样View执行命令时也会去寻找绑定的Command并执行。反过来，ViewModel在Property发生改变时会发个通知说“名字叫XXX的Property改变了，你们这些View中谁绑定了XXX也要跟着变啊!”，至于有没有View收到是不是做出变化也不关心。ViewModel中的Command脱离View就更简单了，因为Command在执行操作过程中操作数据时，根本不需要操作View中的数据，只需要操作ViewModel中的Property就可以了，Property的变化通过绑定就可以反映到View上。这样在测试Command时也不需要View的参与。这样一来ViewMode可以在完全没有View的情况下测试，View也可以在完全没有ViewModel的情况下测试。


#MVVMLight开发过程
1. 定义Model: UserInfoModel:ObservableObject（Model/UserInfoModel）
2. 定义ViewModel: MainViewModel:ViewModelBase (ViewModel/MainViewModel)
3. 在ViewModelLocator中注册ViewModel， 添加MainViewModel字段
4. 定义View: 添加View数据绑定，DataContext="{Binding Source={StaticResource Locator},Path=Main}"
5. 定义命令，在ViewModel中添加命令AddUserCommand = new RelayCommand(ExecuteAddUser);
6. 命令绑定：<Button Command="{Binding AddUserCommand}">