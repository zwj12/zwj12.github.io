---
layout: post
title: "Certificate"
date: 2022-06-02 09:48:00 +0800
author: Michael
categories: robot
---

# 搜索证书
windows系统有两个证书管理工具**certlm.msc**和**certmgr.msc**，前者是本地计算机的证书管理工具，而后者是当前用户的证书管理工具。可以通过选中根节点，然后Action -> Find Certifates打开搜索证书窗口。  
![日志文件夹](/assets/robot/FindCertificates.png)   

# OmniCore默认存储位置证书
![日志文件夹](/assets/robot/OmniCoreCertificate.png)   

# RobotStudio首次连接保存证书
新安装的RobotStudio第一次连接OmniCore控制柜时，需要保存证书。建议选择第二个。  
![日志文件夹](/assets/robot/connectandremembercertificate.png)   

# RobotStudio保存控制器证书位置
RobotStudio首次连接OmniCore后，如果保存证书，证书信息保存在文件`C:\Users\CNMIZHU7\AppData\Local\ABB\RobotStudio\ControllerWhitelist.dat`中，貌似这个目录是RobApi控制的，如果电脑上没有安装RobotStudio，会没有这个目录，不清楚RobApi或PCSDK还能不能正常工作？  

![日志文件夹](/assets/robot/ControllerWhitelist.png)  

