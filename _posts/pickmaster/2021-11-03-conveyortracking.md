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
5. Queue tracking distance (QueueTrckDist),这个距离对于Pick Master Twin，应该对应着IO Sensor的检测点到Work Area的Enter点位置。
6. Start window width (StartWinWidth)，这个距离对于PickMaster Twin，应该对应着WorkArea的Exit-Enter的距离。应该不是对应着Start Stop点，因为Start和Stop点按我理解只用于传送带的启停，不用于区分WorkArea的跟踪范围大小。
 
![日志文件夹](/assets/pickmaster/startwindow.png) 

# Activation and Deactivation only done from Rapid
RW6.13的Motion -> Mechanical Unit中有一个新的设置：Activation and Deactivation only done from Rapid，该设置可以确保程序在移动指针时，外轴不会被自动激活或者停用

# WaitWObj wobjCNV1 & DropWObj wobjCNV1
## c1CntFromEnc自动触发
每次c1CntFromEnc变化，都会导致c1ObjectsInQ加1，同时机器人内部有一个队列，存储着每一次的变化值，当使用WaitWObj wobjCNV1 指令时，会获取队列中存储的最小c1CntFromEnc值，并关联到CNV1的坐标上，也就是用该最小的c1CntFromEnc值作为CNV1传送带的原点或零位，可以从示教器的Job界面看出，传送带的坐标为c1Counts-c1CntFromEnc，当运行DropWObj时，CNV1的坐标会变为0，注意只有真正DropWObj才会变为0，如果之前没有WaitWObj，那么重复的DropWObj不会改变传送带的坐标位置值。

![日志文件夹](/assets/pickmaster/WaitWObjSignals.png) 

## c1NewObjStrobe手动触发
当手动触发c1NewObjStrobe信号时，会删除队列里所有数据，然后把当前的c1Counts值赋值到c1CntToEnc,同时发出脉冲信号c1CntToEncStr。生产wobj供WaitWObj指令返回。

![日志文件夹](/assets/pickmaster/WaitWObjc1NewObjStrobe.png) 

