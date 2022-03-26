---
layout: post
title: "Conveyor Tracking"
date: 2021-11-03 08:56:00 +0800
author: Michael
categories: PickMaster
---

# 传送带工作区域划分
传送带上共有四个区域：

1. 未进入Synchronization switch。（如下图中产品7所在位置）
2. 进入Synchronization switch，但是未进入机器人监控范围区域，如下图产品5和6,该区域的产品会被加入传送带跟踪队列，但如果机器人请求数据，是不会发送给机器人的，因为在机器人的运动区域外。
3. 进入机器人监控区域，如下图产品4和3，此时一旦机器人请求数据，就会立刻收到该区域的产品信息。
4. 离开机器人监控区域，如下图的2和1，该区域的产品如果已经被机器人跟踪抓取（在第三步获取到数据），产品会被抓取和放置。但是如果产品没有被机器人跟踪，那么这个产品会被放弃。
 
![日志文件夹](/assets/pickmaster/startwindow.png) 

# Activation and Deactivation only done from Rapid
RW6.13的Motion -> Mechanical Unit中有一个新的设置：Activation and Deactivation only done from Rapid，该设置可以确保程序在移动指针时，外轴不会被自动激活或者停用