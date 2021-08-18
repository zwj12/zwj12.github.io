---
layout: post
title: "External Axis Wizard"
date: 2021-06-28 09:25:00 +0800
author: Michael
categories: robot
---

# 锁定轴Locked Axis
在通过RobotStudio创建机械结构时，最后一个连杆上必须有一个Frame，且这个Frame的Z轴必须与最后一个轴的轴线运动方向重合，否则就会产生一个额外的锁定轴。  
![日志文件夹](/assets/robot/LockedAxis.png)

# Calibration
每个轴都有一个自身坐标系，这个坐标系就是Calibration，其中BaseFrame的坐标系和第一轴的坐标系重合，第一轴的坐标系Z向为轴线方向，X向为第一轴和第二轴的公垂线方向，如果第一轴和第二轴相交，那么方向为第一轴和第二轴的轴向组成平面的法向方向，符合右手螺旋规格