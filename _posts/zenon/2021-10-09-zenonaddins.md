---
layout: post
title: "Zenon Add-Ins"
date: 2021-10-09 15:09:00 +0800
author: Michael
categories: PickMaster
---

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
Zenon的变量类型和C#的变量类型并不是一一对应的，对应关系如下：
1. Zenon INT -> C# System.Double
2. Zenon BOOL -> C# System.Double

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