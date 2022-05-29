---
layout: post
title: "Microsoft.Toolkit.Mvvm"
date: 2022-05-25 09:25:00 +0800
author: Michael
categories: CSharp
---

# NuGet包
	Microsoft.Toolkit.Mvvm
	Microsoft.Extensions.DependencyInjection

# IOC
Microsoft.Toolkit.Mvvm的NuGet包中，包含了一个IOC类：Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc，该类实现了IServiceProvider接口

# IOC 依赖注入
在App类中使用Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc直接注册，也可以同时把注册的IServiceProvider类暴露出去。推荐直接使用IOC注册。没必要暴露App和Services。

## 暴露App和Services，记得引用Microsoft.Extensions.DependencyInjection
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

## 直接使用Microsoft.Toolkit.Mvvm.DependencyInjection.Ioc注册
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

## 使用类似MVVMLight的ViewModelLocator依赖注入
MVVMLight使用了一个应用程序资源实例化了一个.Net类ViewModelLocator，然后通过该应用程序资源实例化类绑定到页面的DataContext中，这个方法的好处是可以在XAML中输入绑定字段时，会自动弹出绑定源的字段。

	<Application x:Class="ERPApp.App" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:local="clr-namespace:ERPApp" StartupUri="MainWindow.xaml" xmlns:d="http://schemas.microsoft.com/expression/blend/2008" d1p1:Ignorable="d" xmlns:d1p1="http://schemas.openxmlformats.org/markup-compatibility/2006">
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