---
layout: post
title: "Windows Update"
date: 2022-12-12 12:17:00 +0800
author: Michael
categories: Windows
---


# 禁止升级Windows 11
## 查看目前支持的Windows版本
打开网址aka.ms/WindowsTargetVersioninfo。   
![日志文件夹](/assets/windows/Windows10supportedversions.png)  

## 设置系统更新目标版本
单击开始菜单，输入gpedit，打开本地组策略编辑器。导航到“计算机配置”》“管理模板”》“Windows组件”》“Windows更新”》“适用于企业的Windows更新”。双击“选择目标功能更新版本”。将策略设置为“已启用”，在第一个框中键入Windows 10，在第二个框中键入21H1。选择确定，这会将目标版本设置为Windows 10版本21H1。

![日志文件夹](/assets/windows/SelectTheTargetFeatureUpdateVersion.png)  
![日志文件夹](/assets/windows/WindowsUpdateForBusiness.png)  