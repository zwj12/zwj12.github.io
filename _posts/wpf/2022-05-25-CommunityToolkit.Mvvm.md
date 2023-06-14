---
layout: post
title: "CommunityToolkit.Mvvm"
date: 2022-05-25 09:25:00 +0800
author: Michael
categories: CSharp
---

# NuGet包
	CommunityToolkit.Mvvm
	Microsoft.Extensions.DependencyInjection

# IOC
CommunityToolkit.Mvvm的NuGet包中，包含了一个IOC类：Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc，该类实现了IServiceProvider接口

# IOC 依赖注入
在App类中使用Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc直接注册，也可以同时把注册的IServiceProvider类暴露出去。推荐直接使用IOC注册。没必要暴露App和Services。

## 方案一：暴露App和Services，记得引用Microsoft.Extensions.DependencyInjection，不推荐使用。
    public partial class App : Application
    {
        public new static App Current => (App)Application.Current;

        public IServiceProvider Services { get; }

        public App()
        {
            Services = ConfigureServices();

            Ioc.Default.ConfigureServices(Services);

            this.InitializeComponent();
        }

        private static IServiceProvider ConfigureServices()
        {
            var services = new ServiceCollection();

            services.AddSingleton<ProductsViewModel>();
            services.AddSingleton<ProductViewModel>();
            services.AddSingleton<ERPModelContainer>();

            return services.BuildServiceProvider();
        }
    }

## 方案二：直接使用Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc注册，可以使用，但推荐使用第三种。
    public partial class App : Application
    {

        public App()
        {
            Ioc.Default.ConfigureServices(
                new ServiceCollection()
                .AddSingleton<ProductsViewModel>()
                .AddSingleton<ProductViewModel>()
                .AddSingleton<ERPModelContainer>()
                .BuildServiceProvider());

            this.InitializeComponent();
        }

    }

## 方案三：使用类似MVVMLight的ViewModelLocator依赖注入，推荐使用
MVVMLight使用了一个应用程序资源实例化了一个.Net类ViewModelLocator，然后通过该应用程序资源实例化类绑定到页面的DataContext中，这个方法的好处是可以在XAML中输入绑定字段时，会自动弹出绑定源的字段。

	<Application x:Class="ERPApp.App" 
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
        xmlns:local="clr-namespace:ERPApp" 
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"        
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        mc:Ignorable="d"
        StartupUri="MainWindow.xaml" >
	    <Application.Resources>
	        <ResourceDictionary>
	            <ResourceDictionary.MergedDictionaries>
	                <ResourceDictionary Source="pack://application:,,,/Fluent;Component/Themes/Generic.xaml" />
	                <ResourceDictionary>
	                    <vm:ViewModelLocator 
	                        x:Key="Locator"
	                        d:IsDataSource="True"
	                        xmlns:vm="clr-namespace:ERPApp.ViewModel" />
	                </ResourceDictionary>
	            </ResourceDictionary.MergedDictionaries>
	        </ResourceDictionary>
	    </Application.Resources>
	</Application>

	namespace ERPApp.ViewModel
	{
	    public class ViewModelLocator
	    {
	        /// <summary>
	        /// Initializes a new instance of the ViewModelLocator class.
	        /// </summary>
	        public ViewModelLocator()
	        {
	            Ioc.Default.ConfigureServices(
	                new ServiceCollection()
	                .AddSingleton<ProductsViewModel>()
	                .AddSingleton<ProductViewModel>()
	                .AddSingleton<ERPModelContainer>()
	                .BuildServiceProvider());
	
	        }	
	
	        public ProductsViewModel Products
	        {
	            get
	            {
	                return Ioc.Default.GetRequiredService<ProductsViewModel>();
	            }
	        }
			
			//Remember use Ioc.Default.GetRequiredService
	        public ProductViewModel Product
	        {
	            get
	            {
	                return Ioc.Default.GetRequiredService<ProductViewModel>();
	            }
	        }
	
	        public ERPModelContainer ERPModelContainer
	        {
	            get
	            {
	                return Ioc.Default.GetRequiredService<ERPModelContainer>();
	            }
	        }
	
	    }
	}

# IOC获取对象
## 使用App和Services获取
    public partial class ProductsView : Page
    {
        public ProductsView()
        {
            InitializeComponent();

            this.DataContext = App.Current.Services.GetService<ProductsViewModel>();
            //this.DataContext = App.Current.Services.GetService(typeof(ProductsViewModel));
        }
    }
## 使用IOC获取
    public partial class ProductsView : Page
    {
        public ProductsView()
        {
            InitializeComponent();

            this.DataContext = Ioc.Default.GetRequiredService<ProductsViewModel>();
        }
    }
## 使用应用程序资源实例化类
    <Page.DataContext>
        <Binding Path="Products" Source="{StaticResource Locator}"></Binding>
    </Page.DataContext>

## 删除MVVMLight
删除以下两个NuGet包

1. MVVMLight
1. CommonServiceLocator

![日志文件夹](/assets/wpf/MvvmLightDependencies.png)  
![日志文件夹](/assets/wpf/MvvmLightLibsDependencies.png)  

# ViewModel

	public class ProductViewModel : ObservableRecipient
    {
        private Product product;
        public Product Product
        {
            get => product;
            set => SetProperty(ref product, value);
        }

        #region RelayCommand

        public RelayCommand<System.Windows.Window> OKCommand { get; private set; }

        #endregion

        public ProductViewModel()
        {
            OKCommand = new RelayCommand<System.Windows.Window>(ExecuteOK);
        }

        public void ExecuteOK(System.Windows.Window window)
        {
            window.DialogResult = true;
            window.Close();
        }
    }

# ServiceProvider, ServiceCollection, IServiceCollection
	using Microsoft.Extensions.DependencyInjection

	void Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc.ConfigureServices(IServiceProvider serviceProvider)

	ServiceCollection : IServiceCollection

	ServiceCollectionServiceExtensions -> IServiceCollection AddSingleton<TService> (this IServiceCollection services) where TService : class

	ServiceCollectionContainerBuilderExtensions -> ServiceProvider BuildServiceProvider(this IServiceCollection services)

	T Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc.GetRequiredService<T>() where T : class

# Messenger消息
## 手动注册和发送消息
	//注册消息
	WeakReferenceMessenger.Default.Register<string>(this, OnReceive);
    private void OnReceive(object recipient, string message)
    {
        ReceiveMessage = message;
    }

	发送消息
	WeakReferenceMessenger.Default.Send("Hello");

## 使用接口自动注册和发送消息
	public class ProductViewModel : ObservableRecipient, IRecipient<String>
	{
		public string ReceiveMessage { get; set; }

        public ProductViewModel()
        {
            //WeakReferenceMessenger.Default.Register<string>(this, OnReceive);
            this.IsActive = true;
        }

        public void Receive(string message)
        {
            ReceiveMessage = message;
        }
		
	}

## 手动解除注册消息
只有手动注册时，才需要手动解除注册消息，当自动注册时，只需要通过设置IsActive为true或false，自动注册或解除消息。  

	this.Unloaded += (sender, e) => WeakReferenceMessenger.Default.UnregisterAll(this);

# 通知命令是否可以执行
	//MVVMLight
	this.UploadPMPPLineCommand.RaiseCanExecuteChanged();

	//CommunityToolkit.Mvvm
	this.UploadPMPPLineCommand.NotifyCanExecuteChanged();

# 背景线程更新UI
    Application.Current.Dispatcher.Invoke(() =>
    {
        this.WebSocketConnectCommand.NotifyCanExecuteChanged();
        this.WebSocketCloseCommand.NotifyCanExecuteChanged();
    });