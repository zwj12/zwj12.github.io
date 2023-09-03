---
layout: post
title: "FlexPendant SDK"
date: 2021-04-18 17:41:00 +0800
author: Michael
categories: robot
---

# 创建新项目
推荐使用Production Screen启动APP，项目名称格式为TpsViewxxxx。项目新建后，会自动创建一个view的页面，该页面为主页面，主要用来跳转子页面用。

![日志文件夹](/assets/robot/FlexPendantSDK/NewProductionScreenApp.png)  

# 创建新页面
命名格式为TpsFormxxxx
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
	        #region Fields
	
        	private const string CURRENT_MODULE_NAME = "TpsFormScanData";
	        private TpsResourceManager _tpsRm = null;
	        private RWSystem rwSystem = null;
	        private TemplateData templateData;
	
	        #endregion
			...
	
	        public TpsFormScanData(TpsResourceManager rM, RWSystem rwSystem, ScanData scanData)
	        {
				InitializeComponent();

	            try
	            {	                
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

	       #region ITpsViewActivation Members
	
	        public void Activate()
	        {
	            this.templateData.RefreshData(this.rwSystem);
	            this.Invoke(this.UpdateGUI);
	            //throw new NotImplementedException();
	        }
	
	        public void Deactivate()
	        {
	            throw new NotImplementedException();
	        }
	
	        #endregion
	
	
	        private void UpdateGUI(object sender, EventArgs e)
	        {
	            try
	            {
	                this.menuItem_Apply.Enabled = false;
	            }
	            catch (Exception ex)
	            {
	                GTPUMessageBox.Show(this.Parent.Parent, null
	                    , string.Format("An unexpected error occurred when reading RAPID data 'weld data'. Message {0}", ex.ToString())
	                    , "System Error"
	                    , System.Windows.Forms.MessageBoxIcon.Hand
	                    , System.Windows.Forms.MessageBoxButtons.OK);
	            }
	        }
	
	        private void menuItem_Close_Click(object sender, EventArgs e)
	        {
	            this.CloseMe();
	        }
	
	        private void menuItem_Apply_Click(object sender, EventArgs e)
	        {
	            try
	            {
	                this.menuItem_Apply.Enabled = false;
	            }
	            catch (Exception ex)
	            {
	                GTPUMessageBox.Show(this.Parent.Parent, null
	                    , string.Format("An unexpected error occurred when applying RAPID data. Message {0}", ex.ToString())
	                    , "System Error"
	                    , System.Windows.Forms.MessageBoxIcon.Hand
	                    , System.Windows.Forms.MessageBoxButtons.OK);
	            }
	        }
	
	        private void menuItem_Refresh_Click(object sender, EventArgs e)
	        {
	            this.templateData.RefreshData(this.rwSystem);
	            this.Invoke(this.UpdateGUI);
	        }
	
	        private void dataControl_PropertyChanged(object sender, PropertyChangedEventArgs e)
	        {
	            this.menuItem_Apply.Enabled = true;
	        }
	
	        void InitializeTexts()
	        {
	
	        }
			...

![日志文件夹](/assets/robot/FlexPendantSDK/NewFormView.png)   
![日志文件夹](/assets/robot/FlexPendantSDK/MenuItem.png) 

# Post Build Event
	call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\\VC\vcvarsall.bat" x86
	copy "$(TargetDir)$(TargetName).dll" "\\VBOXSVR\RobotStudio\Virtual Controllers\Controller_JQR365\HOME\ProdScr\tps"

![日志文件夹](/assets/robot/FlexPendantSDK/PostBuildEvent.png) 

	call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\\VC\vcvarsall.bat" x86
	  "C:\Program Files (x86)\ABB Industrial IT\Robotics IT\SDK\FlexPendant SDK 6.11\abbct.exe " "$(TargetDir)$(TargetName).dll"

# Production Screen设置
	<?xml version="1.0" encoding="utf-8"?>
	<ProjectSettings xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" Grid="false" Separator="true">
	  <Apps>
	    <App>
	      <Name>ZhongXun</Name>
	      <SystemApp>false</SystemApp>
	      <Index>15</Index>
	      <Assembly>TpsViewZhongXun.dll</Assembly>
	      <Type>TpsViewZhongXunNameSpace.TpsViewZhongXun</Type>
	      <Image>icon_ZhongXun.png</Image>
	      <AlertSignal />
	      <ErrorSignal />
	      <InData />
	    </App>
	   </Apps>
	  <Widgets>
	  </Widgets>
	  <WidgetPages>
	    <Page>Page 1</Page>
	    <Page>Page 2</Page>
	    <Page>Page 3</Page>
	  </WidgetPages>
	</ProjectSettings>

# 本地语言支持
1. 添加SmartDevice项目  
![日志文件夹](/assets/robot/FlexPendantSDK/SmartDevice.png)   
2. 选择Windows CE空项目  
![日志文件夹](/assets/robot/FlexPendantSDK/WindowsCE.png)   
3. 选择类库，修改为主项目命名空间，添加System引用  
![日志文件夹](/assets/robot/FlexPendantSDK/OutputType.png)   
4. 添加字符串资源文件  
![日志文件夹](/assets/robot/FlexPendantSDK/strings.png)   
5. 添加Post-build Event Command Line    

		call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\\VC\vcvarsall.bat" x86
		mkdir ..\..\language
		mkdir ..\..\language\zh
		mkdir ..\..\language\zh\tps
		cd ..\..\zh\
		del *.resources
		del *.dll
		if exist strings.zh.resx (
		"C:\Program Files (x86)\Microsoft Visual Studio 8\SDK\v2.0\Bin\resgen" strings.zh.resx TpsViewZhongXunNameSpace.strings.zh.resources
		al /t:lib /embed:TpsViewZhongXunNameSpace.strings.zh.resources /culture:en /out:TpsViewZhongXunTexts.resources.dll
		copy TpsViewZhongXunTexts.resources.dll ..\language\zh\tps\TpsViewZhongXunTexts.resources.dll)
		
		mkdir "\\VBOXSVR\RobotStudio\Virtual Controllers\Controller_ZhongXun1\HOME\ProdScr\language"
		xcopy /e /y "$(ProjectDir)\language" "\\VBOXSVR\RobotStudio\Virtual Controllers\Controller_ZhongXun1\HOME\ProdScr\language"
		copy "$(TargetDir)$(TargetName).dll" "\\VBOXSVR\RobotStudio\Virtual Controllers\Controller_ZhongXun1\HOME\ProdScr\tps"

#编程规范

1. 示教器APP包含一个主界面，多个二级页面
2. 所有数据主界面中定义，使用`#region Fields`和`#endregion`集中定义，在主界面的 ITpsViewSetup.Install接口中初始化
3. 当程序每次激活时，会自动调用`ITpsViewActivation.Activate`接口，这里分两种情况，第一种为在主界面中打开二级界面，会触发二级界面的Activate接口，第二种为当程序隐藏后，重新打开该APP，此时不管APP在哪一级界面上，都只会触发主界面的Activate接口。所以在主界面的Activate接口中，需要判断当前属于哪个界面，然后调用对应界面的Activate接口。