---
layout: post
title: "WindowsService"
date: 2021-08-30 8:44:00 +0800
author: Michael
categories: CSharp
---

# 创建WindowsService
	选择Windows Service项目模板

# 设置服务名称等属性
双击Service1.cs，在属性窗口设置服务名称

# 添加安装程序
双击Service1.cs，右击空白背景区域，选择“添加安装程序”菜单，添加ProjectInstaller组件类。然后选择serviceInstaller1，查看属性，验证ServiceName属性是否为Service1。可以添加Description属性、DisplayName属性。DisplayName可以用于启动服务的 net start 命令的名称。选择serviceProcessInstaller1，把Account属性改为LocalSystem，提升服务程序的权限。

# 添加服务启动关闭程序
启动和关闭服务会在系统事件中添加事件。
![日志文件夹](/assets/develop/EventViewer.png)  

    public partial class Service1 : ServiceBase
    {
        private EventLog eventLog1;
        private int eventId = 1;
        private string filePath = @"D:\MyServiceLog.txt";

        public Service1()
        {
            InitializeComponent();
            eventLog1 = new EventLog();
            if (!EventLog.SourceExists("TestMichaelSource"))
            {
                EventLog.CreateEventSource(
                    "TestMichael", "TestMichaelNewLog");
            }
            eventLog1.Source = "TestMichaelSource";
            eventLog1.Log = "TestMichaelNewLog";
        }

        protected override void OnStart(string[] args)
        {
            eventLog1.WriteEntry("In OnStart.");

            Timer timer = new Timer();
            timer.Interval = 60000; // 60 seconds
            timer.Elapsed += new ElapsedEventHandler(this.OnTimer);
            timer.Start();

            using (FileStream stream = new FileStream(filePath, FileMode.Append))
            using (StreamWriter writer = new StreamWriter(stream))
            {
                writer.WriteLine($"{DateTime.Now},服务启动！");
            }
        }

        public void OnTimer(object sender, ElapsedEventArgs args)
        {
            // TODO: Insert monitoring activities here.
            eventLog1.WriteEntry("Monitoring the System", EventLogEntryType.Information, eventId++);
        }

        protected override void OnStop()
        {
            eventLog1.WriteEntry("In OnStop.");

            using (FileStream stream = new FileStream(filePath, FileMode.Append))
            using (StreamWriter writer = new StreamWriter(stream))
            {
                writer.WriteLine($"{DateTime.Now},服务停止！");
            }
        }
    }

# 新建Windows Forms程序，用于安装、启动、停止、卸载服务
	！添加Windows Service项目引用，把上面创建的服务程序引用到WinForm程序中
	！添加System.ServiceProcess和System.Configuration.Install引用
	using System.Collections;
	using System.Configuration.Install;
	using System.ServiceProcess;
	
	namespace WindowsFormsApp2
	{
	    public partial class Form1 : Form
	    {
	        string serviceFilePath = $"{Application.StartupPath}\\WindowsService4.exe";
	        string serviceName = "Service1";
	
	        public Form1()
	        {
	            InitializeComponent();
	        }
	
	        private void button_Install_Click(object sender, EventArgs e)
	        {
	            if (this.IsServiceExisted(serviceName)) this.UninstallService(serviceName);
	            this.InstallService(serviceFilePath);
	        }
	
	        private void button_Start_Click(object sender, EventArgs e)
	        {
	            if (this.IsServiceExisted(serviceName)) this.ServiceStart(serviceName);
	        }
	
	        private void button_Stop_Click(object sender, EventArgs e)
	        {
	            if (this.IsServiceExisted(serviceName)) this.ServiceStop(serviceName);
	        }
	
	        private void button_UnInstall_Click(object sender, EventArgs e)
	        {
	            if (this.IsServiceExisted(serviceName))
	            {
	                this.ServiceStop(serviceName);
	                this.UninstallService(serviceFilePath);
	            }
	        }
	        //判断服务是否存在
	        private bool IsServiceExisted(string serviceName)
	        {
	            ServiceController[] services = ServiceController.GetServices();
	            foreach (ServiceController sc in services)
	            {
	                if (sc.ServiceName.ToLower() == serviceName.ToLower())
	                {
	                    return true;
	                }
	            }
	            return false;
	        }
	
	        //安装服务
	        private void InstallService(string serviceFilePath)
	        {
	            using (AssemblyInstaller installer = new AssemblyInstaller())
	            {
	                installer.UseNewContext = true;
	                installer.Path = serviceFilePath;
	                IDictionary savedState = new Hashtable();
	                installer.Install(savedState);
	                installer.Commit(savedState);
	            }
	        }
	
	        //卸载服务
	        private void UninstallService(string serviceFilePath)
	        {
	            using (AssemblyInstaller installer = new AssemblyInstaller())
	            {
	                installer.UseNewContext = true;
	                installer.Path = serviceFilePath;
	                installer.Uninstall(null);
	            }
	        }
	        //启动服务
	        private void ServiceStart(string serviceName)
	        {
	            using (ServiceController control = new ServiceController(serviceName))
	            {
	                if (control.Status == ServiceControllerStatus.Stopped)
	                {
	                    control.Start();
	                }
	            }
	        }
	
	        //停止服务
	        private void ServiceStop(string serviceName)
	        {
	            using (ServiceController control = new ServiceController(serviceName))
	            {
	                if (control.Status == ServiceControllerStatus.Running)
	                {
	                    control.Stop();
	                }
	            }
	        }
	
	    }
	}

# app.manifest
	!提升应用程序权限
	<requestedExecutionLevel level="requireAdministrator" uiAccess="false" />

