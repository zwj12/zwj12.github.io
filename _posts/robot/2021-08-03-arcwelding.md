---
layout: post
title: "ArcWelding"
date: 2021-08-03 13:03:00 +0800
author: Michael
categories: robot
---

# Process Markup
ArcWelding 2中的Process Markup和RobotStudio中的Markup不是同一个的东西，ArcWelding 2中的Process Markup是为了标记焊缝位置而创建的，除了包含焊缝起点、焊缝终点外，还有焊缝长度，焊接方向等信息。但是Process Markup不包含任何焊接路径，它只是一个物理模型，为了后面依赖它创建焊接程序而定义的。ArcWelding 2中有一个Ribbon菜单Label Manager，可以控制隐藏或显示Process Markup。如果后面创建焊接程序时，选择了焊接程序所对应的Process Markup时，当设置该焊接程序为Active时，RobotStudio会自动显示对应的Process Markup，如果不能显示，请确保该焊接程序设置了对应的Process Markup，或者启用Label Manager中的Show Markup功能。
