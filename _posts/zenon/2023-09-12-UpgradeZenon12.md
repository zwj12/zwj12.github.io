---
layout: post
title: "Upgrade To Zenon 12"
date: 2023-09-12 09:44:00 +0800
author: Michael
categories: zenon
---

# Too many I/O variables when using demo license
In zenon12: If the numberof fieldbus's signals is greater than 256, an error will be reported: Too many I/O variables. 这个只在使用Demo License时报错，如果自己购买的license有足够的tags，则不会报错。

![日志文件夹](/assets/zenon/ToomanyIOvariables.png)      
    