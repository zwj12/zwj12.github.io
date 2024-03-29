---
layout: post
title: "Single Executable File"
date: 2022-07-28 16:03:00 +0800
author: Michael
categories: WPF
---

# 单文件可执行程序
通常情况下，如果WPF程序引用其它dll时，在运行该程序时，需要把引用的dll复制到WPF程序同一个目录下，否则会导致不可运行。但是我们可以通过如下方式把dll嵌入到WPF程序中，让dll和exe文件合并一个单独的exe可执行程序。  

## 修改项目配置，xxxx.csproj文件

	<Target Name="AfterResolveReferences">
		<ItemGroup>
		  <EmbeddedResource Include="@(ReferenceCopyLocalPaths)" Condition="'%(ReferenceCopyLocalPaths.Extension)' == '.dll'">
		    <LogicalName>%(ReferenceCopyLocalPaths.DestinationSubDirectory)%(ReferenceCopyLocalPaths.Filename)%(ReferenceCopyLocalPaths.Extension)</LogicalName>
		  </EmbeddedResource>
		</ItemGroup>
	</Target>

## 修改App类

	public partial class App : Application
    {
        private static Assembly OnResolveAssembly(object sender, ResolveEventArgs args)
        {
            Assembly executingAssembly = Assembly.GetExecutingAssembly();
            var executingAssemblyName = executingAssembly.GetName();
            var resName = executingAssemblyName.Name + ".resources";

            AssemblyName assemblyName = new AssemblyName(args.Name); string path = "";
            if (resName == assemblyName.Name)
            {
                path = executingAssemblyName.Name + ".g.resources"; ;
            }
            else
            {
                path = assemblyName.Name + ".dll";
                if (assemblyName.CultureInfo.Equals(CultureInfo.InvariantCulture) == false)
                {
                    path = string.Format(@"{0}\{1}", assemblyName.CultureInfo, path);
                }
            }

            using (Stream stream = executingAssembly.GetManifestResourceStream(path))
            {
                if (stream == null)
                    return null;

                byte[] assemblyRawBytes = new byte[stream.Length];
                stream.Read(assemblyRawBytes, 0, assemblyRawBytes.Length);
                return Assembly.Load(assemblyRawBytes);
            }
        }

        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            AppDomain.CurrentDomain.AssemblyResolve += OnResolveAssembly;
        }
    }

## 删除自动生成的dll
在Build Events -> Post-build event command line中添加如下配置，但是如果WPF控件中使用外部引用作为XAML的资源时，则通常不建议添加改指令，因为它会删除外面dll，导致引用失败。

	cd $(TargetDir)
	del *.dll

# 单实例应用程序 Single Instance Application

    public partial class App : Application
    {
        private EventWaitHandle programStarted { get; set; }

        protected override void OnStartup(StartupEventArgs e)
        {
            CheckSingleInstanceApplication();            

            base.OnStartup(e);
        }

        private void CheckSingleInstanceApplication()
        {
            programStarted = new EventWaitHandle(false, EventResetMode.AutoReset, "PMOP.WPF.Startup", out bool createNew);
            if (!createNew)
            {
                MessageBox.Show("PMOP is already started.");
                App.Current.Shutdown();
                Environment.Exit(0);
            }
        }
    }