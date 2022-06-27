---
layout: post
title: "Entity Framework"
date: 2022-05-21 20:40:00 +0800
author: Michael
categories: CSharp
---

# Entity Framework Core安装
1. dotnet add package Microsoft.EntityFrameworkCore.SqlServer
1. Install-Package Microsoft.EntityFrameworkCore.Sqlite
1. .NET Core CLI工具： dotnet add package Microsoft.EntityFrameworkCore.Design，该程序在使用CLI工具需要安装，推荐使用Visual Studio包管理工具，不要使用这个。
1. Visual Studio包管理工具： Install-Package Microsoft.EntityFrameworkCore.Tools， 该工具会随ASP.NET Core自动安装，但不会随Microsoft.EntityFrameworkCore.SqlServer安装，所以如果创建控制台，WPF等程序时，还需要安装该包。


# 实体框架
实体框架由适用于 Visual Studio 的 EF Tools 以及 EF 运行时组成。  

1. 适用于 Visual Studio 的 Entity Framework Tools 包括 EF Designer 和 EF 模型向导，对于 Database First 工作流和 Model First 工作流是必需的。 EF Tools 包含在所有最新版本的 Visual Studio 中。
1. 实体框架的最新版本作为 EntityFramework NuGet 包提供。`Install-Package EntityFramework`

# Visual Studio包管理工具Code First，Cord First又称为数据迁移
1. Enable-Migrations，Enable-Migrations is obsolete. Use Add-Migration to start using Migrations.
2. 修改代码，添加属性
3. Add-Migration InitialCreate
4. Update-Database

# 新建数据库
如果在Visual Studio的Server Explorer中新建数据库，那么默认存储位置在用户文件夹下%USERPROFILE%中，一旦创建，数据库会自动加载到(localdb)\MSSQLLocalDB数据库服务器上。  
![日志文件夹](/assets/csharp/CreateNewSQLServerDatabaseByVisualStudio.png)   
![日志文件夹](/assets/csharp/localdbMSSQLLocalDB.png) 

# DbContext 派生类
如果使用的是 EF Designer，则会自动生成上下文。 如果使用的是 Code First，通常需要自行编写上下文。

# 生存期
1. 在使用 Web 应用程序时，针对每个请求使用一个上下文实例。
1. 在使用 Windows Presentation Foundation (WPF) 或 Windows 窗体时，针对每个窗体使用一个上下文实例。 这使您能够使用上下文所提供的更改跟踪功能。
1. 如果上下文实例是由依赖关系注入容器创建的，则通常由该容器负责释放上下文。
1. 如果上下文是在应用程序代码中创建的，请记住不再需要上下文时将其释放。

# EF设计器Model First
使用实体框架设计器创建新模型，然后从该模型生成数据库架构。模型存储在EDMS文件中。 每次通过模型生成数据库，都会导致数据丢失，因为生成数据库的方式是先删除，再重新创建一个新的数据表。  
![日志文件夹](/assets/csharp/EmptyEFDesignerModel.png)   
![日志文件夹](/assets/csharp/AddEntity.png)   
![日志文件夹](/assets/csharp/AddAssociation.png)   
![日志文件夹](/assets/csharp/ReferentialConstraint.png)   
![日志文件夹](/assets/csharp/GenerateDatabaseFromEFModel.png)   

# connectionStrings

	//使用数据库名，数据库已经attach到数据库服务器中
	<add name="BloggingContext" connectionString="metadata=res://*/BloggingModel.csdl|res://*/BloggingModel.ssdl|res://*/BloggingModel.msl;provider=System.Data.SqlClient;provider connection string=&quot;data source=(localdb)\MSSQLLocalDB;initial catalog=ModelFirst.Blogging.Learn;integrated security=True;MultipleActiveResultSets=True;App=EntityFramework&quot;" providerName="System.Data.EntityClient" />

	//使用数据库路径，程序在第一次运行时会自动把数据库文件attach到数据库服务器中，如果没有提供initial catalog值，则把该路径作为数据库名使用，如果提供了initial catalog，则用initial catalog定义的值作为数据库名。
	<add name="BloggingContext" connectionString="metadata=res://*/BloggingModel.csdl|res://*/BloggingModel.ssdl|res://*/BloggingModel.msl;provider=System.Data.SqlClient;provider connection string=&quot;data source=(localdb)\MSSQLLocalDB;initial catalog=ModelFirst.Blogging.Learn;attachdbfilename=C:\Users\CNMIZHU7\ModelFirst.Blogging.Learn.mdf;integrated security=True;MultipleActiveResultSets=True;App=EntityFramework&quot;" providerName="System.Data.EntityClient" />

	//使用|DataDirectory|作为数据路路径根目录，该目录为程序运行exe的目录，通常情况下会把数据库保存在app_data文件夹内
	<add name="BloggingContext" connectionString="metadata=res://*/BloggingModel.csdl|res://*/BloggingModel.ssdl|res://*/BloggingModel.msl;provider=System.Data.SqlClient;provider connection string=&quot;data source=(localdb)\MSSQLLocalDB;initial catalog=ModelFirst.Blogging.Learn;attachdbfilename=|DataDirectory|\app_data\ModelFirst.Blogging.Learn.mdf;integrated security=True;MultipleActiveResultSets=True;App=EntityFramework&quot;" providerName="System.Data.EntityClient" />

# WPF 
1. 双击 ProductModel.tt 文件以在 Visual Studio 编辑器中打开
1. 找到并用“ObservableCollection”替换两次出现的“ICollection”。 它们大约位于第 296 行和第 484 行。
1. 找到并用“ObservableCollection”替换第一次出现的“HashSet”。 此事件大约位于第 50 行。 请勿替换代码中稍后第二次出现的 HashSet。
1. 找到并用“System.Collections.ObjectModel”替换仅出现一次的“System.Collections.Generic”。 它大约位于第 424 行。
1. 保存 ProductModel.tt 文件。 这应该会导致重新生成实体的代码。 如果未自动重新生成代码，则右键单击 ProductModel.tt，然后选择“运行自定义工具”。
1. 如果现在打开 Category.cs 文件 (嵌套在 ProductModel.tt) 下，则应看到 Products 集合的类型为 ObservableCollectionProduct<>。

# 添加数据
    using (var db = new BloggingContext())
    {
        var blog = new Blog { Name = "Michael" };
        db.Blogs.Add(blog);
        db.SaveChanges();
    }

# 获取数据
    using (var db = new BloggingContext())
    {
        var query = from b in db.Blogs
                    orderby b.Name
                    select b;

        foreach (var item in query)
        {
        }
    }

# DataGrid

  	<Window.Resources>
        <CollectionViewSource x:Key="categoryViewSource"/>
        <CollectionViewSource x:Key="categoryProductsViewSource" Source="{Binding Products, Source={StaticResource categoryViewSource}}"/>
    </Window.Resources>
    
    <Grid DataContext="{StaticResource categoryViewSource}">
        <Grid.RowDefinitions>
            <RowDefinition></RowDefinition>
            <RowDefinition></RowDefinition>
            <RowDefinition Height="Auto"></RowDefinition>
        </Grid.RowDefinitions>
        
        <DataGrid x:Name="categoryDataGrid" Grid.Row="0" AutoGenerateColumns="False" ItemsSource="{Binding}">
            <DataGrid.Columns>
                <DataGridTextColumn x:Name="categoryIdColumn" Binding="{Binding Id}" Header="Category Id" Width="SizeToHeader"/>
                <DataGridTextColumn x:Name="nameColumn" Binding="{Binding Name}" Header="Name" Width="SizeToHeader"/>
            </DataGrid.Columns>
        </DataGrid>

        <DataGrid x:Name="productsDataGrid" Grid.Row="1" AutoGenerateColumns="False" ItemsSource="{Binding Source={StaticResource categoryProductsViewSource}}">
            <DataGrid.Columns>
                <DataGridTextColumn Binding="{Binding CategoryId}" Header="Category Id" Width="SizeToHeader" IsReadOnly="True"/>
                <DataGridTextColumn Binding="{Binding Id}" Header="Product Id" Width="SizeToHeader" IsReadOnly="True"/>
                <DataGridTextColumn Binding="{Binding Name}" Header="Name" Width="*"/>
            </DataGrid.Columns>
        </DataGrid>

        <Button Content="Save" Grid.Row="2" HorizontalAlignment="Center" Click="buttonSave_Click" />
    </Grid>

# 绑定DataGrid，更新DataGrid数据

        private ProductContext _context = new ProductContext();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            System.Windows.Data.CollectionViewSource categoryViewSource =((System.Windows.Data.CollectionViewSource)(this.FindResource("categoryViewSource")));
            _context.Categories.Load();
            categoryViewSource.Source = _context.Categories.Local;
        }
        private void buttonSave_Click(object sender, RoutedEventArgs e)
        {
            foreach (var product in _context.Products.Local.ToList())
            {
                if (product.Category == null)
                {
                    _context.Products.Remove(product);
                }
            }

            _context.SaveChanges();

            this.categoryDataGrid.Items.Refresh();
            this.productsDataGrid.Items.Refresh();
        }

        protected override void OnClosing(System.ComponentModel.CancelEventArgs e)
        {
            base.OnClosing(e);
            this._context.Dispose();
        }


# WPF Add-Migration ConnectionStrings
如果要在WPF中使用Microsoft.EntityFrameworkCore.Tools指令，则需要使用appsettings.json存储连接字符串。需要使用`Microsoft.Extensions.Configuration.Json`包。  

## appsettings.json
	{
	  "ConnectionStrings": {
	    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=ERPCoreAppDB;Trusted_Connection=True;MultipleActiveResultSets=true"
	  }
	}

## DbContext.OnConfiguring
    public class ERPModelContainer : DbContext
    {
        public DbSet<Product> Products { get; set; }
        public DbSet<Order> Orders { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            IConfigurationRoot configuration = new ConfigurationBuilder().AddJsonFile("appsettings.json").Build();
            optionsBuilder.UseSqlServer(configuration.GetConnectionString("DefaultConnection"));
        }

    }

## Host主机依赖注入

	using System.Windows;
	using ERPCoreApp.Model;
	using Microsoft.EntityFrameworkCore;
	using Microsoft.Extensions.DependencyInjection;
	using Microsoft.Extensions.Hosting;
	
	namespace ERPCoreApp
	{
	    /// <summary>
	    /// Interaction logic for App.xaml
	    /// </summary>
	    public partial class App : Application
	    {
	        public IHost host;
	
	        public App()
	        {
	            var builder = Host.CreateDefaultBuilder();
	
	            builder.ConfigureServices((hostContext, services) =>
	            {
	                services.AddDbContext<ERPModelContainer>((options) =>
	                     options.UseSqlServer("name=ConnectionStrings:DefaultConnection"));
	            });
	
	            host = builder.Build();
	
	            //host.RunAsync();
	        }
	    }
	}
	

	namespace ERPCoreApp.Model
	{
	    public class ERPModelContainer : DbContext
	    {
	        public DbSet<Product> Products { get; set; }
	        public DbSet<Order> Orders { get; set; }
	
	        public ERPModelContainer(DbContextOptions<ERPModelContainer> options): base(options)
	        {
	        }
	
	    }
	}


    IServiceScope serviceScope=((App)(App.Current) ).host.Services.CreateScope();
    ERPModelContainer eRPModelContainer =  serviceScope.ServiceProvider.GetRequiredService<ERPModelContainer>();
    int i=  eRPModelContainer.Products.Count();
