---
layout: post
title: "Certificate"
date: 2022-07-22 09:48:00 +0800
author: Michael
categories: robot
---

# 碰撞检测灵敏度设置
取值范围从1~300，默认为100，数字越小，机器人越敏感。  
![日志文件夹](/assets/robot/SupervisionSensitivity.png)   

# 碰撞检测报警
碰撞检测报警需要选项613-1 Collision Detection。  
![日志文件夹](/assets/robot/MotionSupervisionError.png)   

# 关节碰撞报警
当机器人没有613-1 Collision Detection时，此时机器人发生碰撞会触发JointCollision错误。所以JointCollision是比MotionSupervision报警更剧烈的碰撞。  
![日志文件夹](/assets/robot/JointCollision.png)   
