---
layout: post
title: "Zenon Add-Ins"
date: 2021-10-09 15:09:00 +0800
author: Michael
categories: PickMaster
---

# Could not find AddInFramework.Build.targets
如果创建的AddIn程序不能编译，可能需要重新注册zenon。  
![日志文件夹](/assets/zenon/AddInFrameworkBuildTargetsError.png)   
![日志文件夹](/assets/zenon/RegisterSCADAsoftware.png)   

# 修改Addin名称
导入Addin到zenon工程后，如果想在编译程序时就把name设置好，可以修改文件AddInProjectService1\AddInProjectService1\Properties\AddInInfo.cs中的设置，通过修改dll名称或者其他地方的配置均不会修改zenon中name的属性。Visual Studio编译后，会按项目的Assembly Name创建scadaAddIn文件，但是导入zenon后，在zenon编译后，会再按AddInInfo.cs文件中设置的assembly: Addin名称创建scadaAddIn文件，如果两边设置不一样，会导致创建的scadaAddIn文件名称不一致，但不影响使用。  

	using Mono.Addins;
	
	// Declares that this assembly is an add-in
	[assembly: Addin("AddInProjectService36", "1.0")]
	
	// Declares that this add-in depends on the scada v1.0 add-in root
	[assembly: AddinDependency("::scada", "1.0")]
	
	[assembly: AddinName("AddInProjectServiceByMichael")]
	[assembly: AddinDescription("DescriptionByMichael")]

![日志文件夹](/assets/zenon/AddInName.png)   
![日志文件夹](/assets/zenon/scadaAddInAssemblyName.png)   
![日志文件夹](/assets/zenon/scadaAddInVisualStudio.png)   
![日志文件夹](/assets/zenon/AddInStore.png)   

# AddInStore
该文件夹存储着AddIn的打包程序，当`RT\FILES\zenon\system\AddInCache\DotNet\addin-db-002`文件夹缺失时，会自动解压该文件夹下的scadaAddIn文件，并把dll文件复制到`RT\FILES\zenon\system\AddInCache\DotNet\addins`对应的dll文件夹中。

# AddInCache文件夹
当没有添加AddIn时，运行Runtime的同时，同样也会生成文件夹`RT\FILES\zenon\system\AddInCache\DotNet\addin-db-002`，但是没有目录`RT\FILES\zenon\system\AddInCache\DotNet\addins`，只有在添加了AddIn时，才会生成对应的RT\FILES\zenon\system\AddInCache\DotNet\addins\AddInProjectService2.1.0目录，并且把dll添加进入。如果需要恢复修改，该文件可以直接删除，再下一次启动时，会自动从AddInStore文件中恢复程序。

# additional文件夹
如果通过添加文件的方式，添加文件和dll，只会保存在文件夹`\RT\FILES\zenon\custom\additional`

# 存储位置
Add-Ins are copied to the following folder when **creating** the Runtime files for a project: ...\RT\FILES\zenon\system\AddInStore\...  
The Add-Ins are installed in the following folder when **starting** the Runtime: ...\RT\FILES\zenon\system\AddInCache\...  

# Debug Runtime Add-Ins
	...\RT\FILES\zenon\system\AddInCache\...
1. Programming Interfaces -> Add-Ins中删除原先的dll，使用Visual Studio项目中编译的bin -> Debug目录下的dll替换掉原先的dll。
2. 启动Zenon工程的Runtime。
3. 在Visual Studio中附加Zenrt32.exe进程。
4. 设置断点，如果第二次调试，可以直接使用Reattach快速附件调试进程。

示例代码如下，记得设置DefaultStartMode为Auto模式，如果需要在VisualStudio窗口输出，使用System.Diagnostics.Debug类。

	using Scada.AddIn.Contracts;
	using System;
	using System.Diagnostics;
	using System.Timers;
	
	namespace ZenonAddInProjectServiceTest
	{
	    /// <summary>
	    /// Description of Project Service Extension.
	    /// </summary>
	    [AddInExtension("ZenonAddInProjectServiceTest", "Test by Michael","Michael", DefaultStartMode = DefaultStartupModes.Auto)]
	    public class ProjectServiceExtension : IProjectServiceExtension
	    {
	        #region Fields
	        private Timer timerUpdateZenonRuntime ;
	        private IProject zenonProject;
	        #endregion
	
	        #region IProjectServiceExtension implementation
	
	        public void Start(IProject context, IBehavior behavior)
	        {
	            this.zenonProject = context;
	            timerUpdateZenonRuntime = new Timer();
	            timerUpdateZenonRuntime.Interval = 1000;
	            timerUpdateZenonRuntime.Elapsed += this.OnTimedEvent;
	            timerUpdateZenonRuntime.AutoReset = true;
	            timerUpdateZenonRuntime.Enabled = true;
	        }
	
	        public void Stop()
	        {
	            if(timerUpdateZenonRuntime!=null)
	            {
	                timerUpdateZenonRuntime.Stop();
	                timerUpdateZenonRuntime.Dispose();
	            }
	        }
	
	        #endregion
	
	        private void OnTimedEvent(Object source, ElapsedEventArgs e)
	        {
	            Debug.WriteLine("The Elapsed event was raised at {0:HH:mm:ss.fff}",e.SignalTime);
	
	            IVariable variable01 = this.zenonProject.VariableCollection["iArray01[2]"];
	            Debug.WriteLine("Variable " + variable01.Name + " has datatype " + variable01.DataType.Name + " and "+ variable01.GetValue(0).GetType());
	            int iTest = (int)(double)this.zenonProject.VariableCollection["iArray01[2]"].GetValue(0);
	            this.zenonProject.VariableCollection["iArray01[1]"].SetValue(0, iTest);
	
	            string robotName =(string) this.zenonProject.VariableCollection["robotPanel01.SystemNameFromZenon"].GetValue(0);
	            this.zenonProject.VariableCollection["robotPanel01.SystemName"].SetValue(0, robotName);
	
	            if (robotName == "michael")
	            {
	                foreach (IVariable variable in this.zenonProject.VariableCollection)
	                {
	                    Debug.WriteLine("Variable: {0}, {1}", variable.Name, variable.Id);
	                }
	            }
	        }
	    }
	}

# Visual Studio Extensions
开发前，需要先安装插件：COPA-DATA Developer Tools
![日志文件夹](/assets/pickmaster/copadatadevelopertools.png)  

# AddInUtility.exe
C:\Program Files (x86)\ABB\zenon 8.00 SP0\AddInFramework

# Engineering Studio Wizard Extension
## AddInExtension
    [AddInExtension("TestByMichael", "Just for test", "Michael")]
运行插件时，需要打开Tools->Start Editor wizards窗口，插件的目录和名称通过AddInExtension特性设置
![日志文件夹](/assets/pickmaster/starteditorwizards.png)  

## AddInInfo
	using Mono.Addins;
	
	// Declares that this assembly is an add-in
	[assembly: Addin("MichaelTestESW", "1.0")]
	
	// Declares that this add-in depends on the scada v1.0 add-in root
	[assembly: AddinDependency("::scada", "1.0")]
	
	[assembly: AddinName("MichaelTestEngineeringStudioWizard")]
	[assembly: AddinDescription("Only for Test")]
添加插件到Zenon中，需要打开Tools->Manager Editor Add-Ins窗口。此步骤和使用Visual Studio的Deploy功能效果相同，所以开发时，可以直接使用Deploy部署插件，不需要手动添加。
![日志文件夹](/assets/pickmaster/manageeditoraddins.png)  

## Deploy
![日志文件夹](/assets/pickmaster/deploy.png)   
Deploy的目录为`C:\ProgramData\ABB\zenon800\EditorAddInCache\DotNet\addins`  
如果使用Tools->Manager Editor Add-Ins窗口安装，那么原始安装包会保存在`C:\ProgramData\ABB\zenon800\EditorAddInStore`

## Debug
设置断点，启动Visual Studio的Debug，然后打开Tools->Start Editor wizards窗口，启动插件，可以发现Visual Studio进入调试模式，程序停止在断点处。

# Project Wizard Extension
## 添加Add-in
	Workspace->Project->Programming Interfaces->Add-ins
添加后，右击项目Runtime files->create changed data/create all后，安装包会复制到文件夹`RT\FILES\zenon\system\AddInStore`，但运行后，安装包里的dll会复制到文件夹`RT\FILES\zenon\system\AddInCache\DotNet\addins`
如果没有添加Add-in，直接Visual Studio中Deploy，也会把dll复制到文件夹`RT\FILES\zenon\system\AddInCache\DotNet\addins`

## Debug
启动Runtime，设置Visual Studio的调试目标平台为Runtime，设置断点，启动Visual Studio的Debug模式，在Runtime中运行插件程序
![日志文件夹](/assets/pickmaster/AddinDebugTarget.png)  

# Error
启动项目后，如果Visual Studio报如下错误，应该是公司防火墙的问题，切换到iboss或者使用手机热点，可以避免该窗口弹出。
![日志文件夹](/assets/pickmaster/zenonserverfailed.png)  

# 变量类型映射
Zenon的变量类型和C#的变量类型并不是一一对应的，对应关系如下, 数字类型全部都对应着C#的double类型，：
1. Zenon INT -> C# System.Double
2. Zenon BOOL -> C# System.Double

    //double:
    object objsbyte1 = ZenonProject.VariableCollection["sbyte1"].GetValue(0);
    object objbyte1 = ZenonProject.VariableCollection["byte1"].GetValue(0);
    object objshort1 = ZenonProject.VariableCollection["short1"].GetValue(0);
    object objushort1 = ZenonProject.VariableCollection["ushort1"].GetValue(0);
    object objint1 = ZenonProject.VariableCollection["int1"].GetValue(0);
    object objuint1 = ZenonProject.VariableCollection["uint1"].GetValue(0);
    object objlong1 = ZenonProject.VariableCollection["long1"].GetValue(0);
    object objulong1 = ZenonProject.VariableCollection["ulong1"].GetValue(0);
    object objdouble1 = ZenonProject.VariableCollection["double1"].GetValue(0);
    object objfloat1 = ZenonProject.VariableCollection["float1"].GetValue(0);
    object objbool1 = ZenonProject.VariableCollection["bool1"].GetValue(0);
    //string:
    object objstring1 = ZenonProject.VariableCollection["string1"].GetValue(0);

    sbyte sbyte1 = Convert.ToSByte( ZenonProject.VariableCollection["sbyte1"].GetValue(0));
    byte byte1 = Convert.ToByte(ZenonProject.VariableCollection["byte1"].GetValue(0));
    short short1 = Convert.ToInt16(ZenonProject.VariableCollection["short1"].GetValue(0));
    ushort ushort1 = Convert.ToUInt16(ZenonProject.VariableCollection["ushort1"].GetValue(0));
    int int1 = Convert.ToInt32(ZenonProject.VariableCollection["int1"].GetValue(0));
    uint uint1 = Convert.ToUInt32(ZenonProject.VariableCollection["uint1"].GetValue(0));
    long long1 = Convert.ToInt64(ZenonProject.VariableCollection["long1"].GetValue(0));
    ulong ulong1 = Convert.ToUInt64(ZenonProject.VariableCollection["ulong1"].GetValue(0));
    double double1 = Convert.ToDouble(ZenonProject.VariableCollection["double1"].GetValue(0));
    float float1 = Convert.ToSingle(ZenonProject.VariableCollection["float1"].GetValue(0));
    bool bool1 = Convert.ToBoolean(ZenonProject.VariableCollection["bool1"].GetValue(0));
    string string1 = (string)ZenonProject.VariableCollection["string1"].GetValue(0);
                        
    ZenonProject.VariableCollection["sbyte1"].SetValue(0, ++sbyte1);
    ZenonProject.VariableCollection["byte1"].SetValue(0, ++byte1);
    ZenonProject.VariableCollection["short1"].SetValue(0, ++short1);
    ZenonProject.VariableCollection["ushort1"].SetValue(0, ++ushort1);
    ZenonProject.VariableCollection["int1"].SetValue(0, ++int1);
    ZenonProject.VariableCollection["uint1"].SetValue(0, ++uint1);
    ZenonProject.VariableCollection["long1"].SetValue(0, ++long1);
    ZenonProject.VariableCollection["ulong1"].SetValue(0, ++ulong1);
    ZenonProject.VariableCollection["double1"].SetValue(0, ++double1);
    ZenonProject.VariableCollection["float1"].SetValue(0, ++float1);
    ZenonProject.VariableCollection["bool1"].SetValue(0, !bool1);
   ZenonProject.VariableCollection["string1"].SetValue(0, double1.ToString());

# 订阅单个变量变化事件

    public void Subscribe(IProject context)
    {
        ZenonProject = context;

        ZenonProject.OnlineVariableContainerCollection.Delete(containerName);
        container = ZenonProject.OnlineVariableContainerCollection.Create(containerName);

        if (!container.AddVariable(ADDINCOMMAND))
        {
            throw new Exception("Error: variable could not be added to the container by " + containerName);
        }

        container.Changed += AddInCommand_Changed;

        if (!container.Activate())
        {
            throw new Exception("Error: Container could not be activated by " + containerName);
        }

        return;
    }

    public void UnSubscribe()
    {
        container.Changed -= AddInCommand_Changed;
        container.Deactivate();
        ZenonProject.OnlineVariableContainerCollection.Delete(containerName);
    }

    private async void AddInCommand_Changed(object sender, ChangedEventArgs e)
    {
        if (e.Variable.Name == ADDINCOMMAND)
        {
            AddInOrderCode addInCommand =(AddInOrderCode)(UInt32)(double)e.Variable.GetValue(0);
            UInt32 addinCommandErrorCode = 0;

            if (addInCommand > 0)
            {
                ZenonProject.VariableCollection[ADDINCOMMANDERRORCODE].SetValue(0, addinCommandErrorCode);
                e.Variable.SetValue(0, 0);
            }
        }
        else
        {
            MessageBox.Show("Error: Variable name is not " + ADDINCOMMAND);
            //throw new Exception("Error: Variable name is not " + ADDINCOMMAND);
        }

    }


# 订阅多个变量变化事件

       public void Subscribe(IProject context)
        {
            ZenonProject = context;

            List<string> variablesList = new List<string>();
            variablesList.Add(ADDINCOMMAND);
            variablesList.Add(RECIPETUNINGADDINORDERCODE);

            ZenonProject.OnlineVariableContainerCollection.Delete(containerName);
            container = ZenonProject.OnlineVariableContainerCollection.Create(containerName);

            if (!container.AddVariable(variablesList.ToArray()))
            {
                throw new Exception("Error: variables could not be added to the container by " + containerName);
            }

            container.BulkChanged += AddInCommand_Changed;

            if (!container.ActivateBulkMode())
            {
                throw new Exception("Error: Bulk mode could not be activated of " + containerName);
            }

            if (!container.Activate())
            {
                throw new Exception("Error: Container could not be activated by " + containerName);
            }

            return;
        }

        public void UnSubscribe()
        {
            container.BulkChanged -= AddInCommand_Changed;
            container.Deactivate();
            ZenonProject.OnlineVariableContainerCollection.Delete(containerName);
        }

        private void AddInCommand_Changed(object sender, BulkChangedEventArgs e)
        {          
            foreach (var zenonVar in e.Variables)
            {
                if (zenonVar.Name == ADDINCOMMAND)
                {
                    Task.Run(() => {

                        AddInOrderCode addInCommand = (AddInOrderCode)(UInt32)(double)zenonVar.GetValue(0);
                        UInt32 addinCommandErrorCode = 0;

                        if (addInCommand > 0)
                        {
    
                            ZenonProject.VariableCollection[ADDINCOMMANDERRORCODE].SetValue(0, addinCommandErrorCode);
                            zenonVar.SetValue(0, 0);
                        }

                    });
                 }
               
                if (zenonVar.Name == RECIPETUNINGADDINORDERCODE)
                {
                    Task.Run(() => {
                        AddInOrderCode addInCommand = (AddInOrderCode)(UInt32)(double)zenonVar.GetValue(0);
                        UInt32 addinCommandErrorCode = 0;

                        if (addInCommand > 0)
                        {
                            switch (addInCommand)
                            {
                                case AddInOrderCode.RecipeTuning:
                                    addinCommandErrorCode = RecipeTuningService.TuningObject();
                                    break;
                                default:
                                    break;
                            }
                            ZenonProject.VariableCollection[RECIPETUNINGADDINORDERERRORCODE].SetValue(0, addinCommandErrorCode);
                            zenonVar.SetValue(0, 0);
                        }
                    });                   
                }
            }
        }