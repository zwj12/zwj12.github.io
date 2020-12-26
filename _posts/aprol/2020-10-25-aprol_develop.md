---
layout: post
title: "APROL Development"
date: 2020-10-25 09:53:00 +0800
author: Michael
categories: Linux
---

WebService程序存储的cookie路径如下：  
![日志文件夹](/assets/aprol/cookie.png)

如果需要DisplayCenter启动后，默认自动打开某一个页面，在下图位置配置：  
![日志文件夹](/assets/aprol/DisplayCenterStartPage.png)

如果需要进入账号后，自动打开DisplayCenter，那么使用下图配置，该配置还可以设置是否显示报警信息等区域：  
![日志文件夹](/assets/aprol/DisplayCenterAutoStart.png)

对于UCB模块，默认设置为一个实例在同一个时间内，只能运行一次，对于需要同时获取多个机器人数据的UCB模块，需要取消该设置：  
![日志文件夹](/assets/aprol/DeactivateGolbalLocking.png)

如果需要移动或关闭Faceplate，那么可以直接使用PythonButton属性设置即可：  
![日志文件夹](/assets/aprol/CloseFaceplate.png)

对于PDA和UCB模块，每次只有检测到上升沿的信号才会运行一次，也就是说，如果把trigger信号一直设置为1，并不能使PDA和UCB模块持续不断的运行下去。对于需要被动触发一个信号的上升沿和下降沿，可以使用X_TRIG(IEC61131_3)模块，该模块会在检测到信号值变化时，输出一个周期的脉冲信号，当这个周期结束后，它会自动置为0。这其实也就意味着，PDA和UCB模块的最小运行时间是两个周期。

可以把JasperReport嵌入到DisplayCenter页面上，**注意**，免费版不支持viewAsDashboardFrame=true功能：  
http://10.0.2.2:8082/jasperserver/flow.html?_flowId=viewReportFlow&reportUnit=%2Freports%2Frobot_elog&j_username=jasperadmin&j_password=jasperadmin&decorate=no&viewAsDashboardFrame=true&IPAddress=10.0.2.2&SystemName=Controller_Aprol  
http://127.0.0.1:8082/jasperserver/flow.html?_flowId=viewReportFlow&reportUnit=%2Freports%2Frobot_oee&j_username=jasperadmin&j_password=jasperadmin&decorate=no&viewAsDashboardFrame=true&IPAddress=10.0.2.2&SystemName=Controller_Aprol2&OEEFrom=2020-11-28&OEETo=2020-11-29

对于Process Graphic页面，也是可以建立动态变量的，首先需要对控件设置一个变量，该变量其实是一个内部变量，所以需要把该变量关联到Connector变量上，才能在CFC模块中调用：  
![日志文件夹](/assets/aprol/PulsControl.png)  
![日志文件夹](/assets/aprol/PGIOMapping.png)

Windows系统下，MariaDB默认会把数据库和表名的大写字母改为小写字母，通过设置lower_case_table_names为2可以使其重新支持大写字母命名：

	[mysqld]
	datadir=C:/Program Files/MariaDB 10.5/data
	port=3306
	innodb_buffer_pool_size=2023M
	character-set-server=utf8
	[client]
	port=3306
	plugin-dir=C:/Program Files/MariaDB 10.5/lib/plugin
	[mariadb]
	lower_case_table_names=2

西门子PLC开启OPC UA服务时，需要添加一个服务器的证书，但是目前好像不能使用自签名证书，不清楚为什么：  
![日志文件夹](/assets/aprol/SiemensPLCOPCUACertificate.png)  

对于JasperReport，如果报表里有参数，那么每次打开时，页面都会弹出一个对话框，提示用户输入参数数据，即使URL中已经设置了参数值，也会弹出该对话框，可以通过取消“Always prompt”复选框，取消弹出对话框功能:  
![日志文件夹](/assets/aprol/JSInputControlsPrompt.png)  

OPCUA中的变量可以单独设置操作员权限，但是默认该选项隐藏起来了，需要在设置上侧的滑动条移至右侧才能看到：  
![日志文件夹](/assets/aprol/OPCUAOperatorRight.png)

如果文本框显示有阴影，除了背景阴影导致外，还可能是设置原因导致的，把文本框DynamicBorder属性选中，去掉WordBreak属性就可以了。  
![日志文件夹](/assets/aprol/DynamicBorder.png)