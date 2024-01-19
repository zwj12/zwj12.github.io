---
layout: post
title: "RobotStudio"
date: 2021-07-12 15:46:00 +0800
author: Michael
categories: robot
---

# Place - Two Points
![日志文件夹](/assets/robot/Place_TwoPoints.png)

# Stopwatch
统计程序运行时间
![日志文件夹](/assets/robot/Stopwatch.png)

# 删除License
RD /S /Q "%programdata%\ABB\RobotStudio\7.x" "%program files(x86)%\ABB\RobotStudio 2023\Bin\RobotStudio.Installer.exe" -InitLicenseStorage

# 允许RW降级
打开配置文件，C:\Program Files (x86)\ABB\RobotStudio 2023\Bin\RobotStudio.UI.InstallationEditor.dll.config，设置DeveloperMode参数为true

    <?xml version="1.0" encoding="utf-8" ?>
    <configuration>
    <appSettings>
        <add key="DeveloperMode" value="true"/>
        <add key="LogLevel" value="info"/>
    </appSettings>
    </configuration>