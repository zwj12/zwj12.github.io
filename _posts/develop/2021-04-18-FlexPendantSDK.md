---
layout: post
title: "FlexPendant SDK"
date: 2021-04-18 17:41:00 +0800
author: Michael
categories: Develop
---

# 创建新项目

![日志文件夹](/assets/develop/FlexPendantSDK/NewProductionScreenApp.png)  

# 创建新页面
	using ABB.Robotics.Tps.Windows.Forms;
	using ABB.Robotics.Tps.Taf;
	using ABB.Robotics.Tps.Resources;
	using ABB.Robotics.Controllers.IOSystemDomain;
	using ABB.Robotics.ProductionScreen.Base;
	using TpsViewYuTongCINameSpace.Robot;
	using TpsViewYuTongCINameSpace.YTCI;
	
	namespace TpsViewYuTongCINameSpace
	{
	    public class TpsFormScanData : TpsForm, ITpsViewActivation
	    {
	        private TpsResourceManager _tpsRm = null;
	        private RWSystem rwSystem = null;
	        private ScanData scanData = null;
			...
	
	        public TpsFormScanData(TpsResourceManager rM, RWSystem rwSystem, ScanData scanData)
	        {
	            try
	            {
	                InitializeComponent();
	                this._tpsRm = rM;
	                this.rwSystem = rwSystem;
	                this.scanData = scanData;
	
	                this.InitializeTexts();
	            }
	            catch (System.Exception ex)
	            {
	                // If initialization of application fails a message box is shown
	                GTPUMessageBox.Show(this.Parent
	                    , null
	                    , string.Format("An unexpected error occurred while starting up TpsFormScanData Application. \n\n{0}", ex.Message)
	                    , "TpsFormScanData Application Start-up Error"
	                    , MessageBoxIcon.Hand, MessageBoxButtons.OK);
	            }
	        }
			...

![日志文件夹](/assets/develop/FlexPendantSDK/NewFormView.png) 

# Post Build Event
	call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\\VC\vcvarsall.bat" x86
	copy "$(TargetDir)$(TargetName).dll" "\\VBOXSVR\RobotStudio\Virtual Controllers\Controller_JQR365\HOME\ProdScr\tps"

![日志文件夹](/assets/develop/FlexPendantSDK/PostBuildEvent.png) 



	call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\\VC\vcvarsall.bat" x86
	  "C:\Program Files (x86)\ABB Industrial IT\Robotics IT\SDK\FlexPendant SDK 6.11\abbct.exe " "$(TargetDir)$(TargetName).dll"