---
layout: post
title: "wait_seconds"
date: 2020-06-10 11:59:00 +0800
author: Michael
categories: Halcon
---

- wait_seconds: 延时
- system_call: 调取系统命令
- count_seconds: 计时
- get_system_time: 获取系统时间

示例代码

	count_seconds(Start)
	* program segment to be measured
	count_seconds(End)
	Seconds := End - Start
