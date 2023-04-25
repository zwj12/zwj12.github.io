---
layout: post
title: "SQL Server"
date: 2023-04-25 09:49:00 +0800
author: Michael
categories: DataBase
---

# 查看远程SQL Server服务区端口
    exec sys.sp_readerrorlog 0, 1, 'listening'

 ![日志文件夹](/assets/database/SQLServerDynamicPorts.png)  
 ![日志文件夹](/assets/database/sp_readerrorloglistening.png)  
 