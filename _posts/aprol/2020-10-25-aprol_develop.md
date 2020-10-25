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

对于UCB模块，默认设置为一个实例在同一个时间内，只能运行一次，对于需要同时获取多个机器人数据的UCB模块，需要取消该设置：  
![日志文件夹](/assets/aprol/DeactivateGolbalLocking.png)



