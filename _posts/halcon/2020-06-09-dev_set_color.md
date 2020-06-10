---
layout: post
title: "dev_set_color "
date: 2020-06-09 11:37:00 +0800
author: Michael
categories: Halcon
---

# Description:

设置regions，XLDs和其他几何图形的颜色

	* 关闭显示
	dev_update_window ('off')
	dev_set_color ('red')

设置图像显示区域，设置后窗口的坐标原点会跟着改变。可以设置为负数

	dev_set_part 

设置文字的位置

	set_tposition

设置箭头的位置和方向

	disp_arrow

打开新的窗口，获取窗口句柄，显示图像

	dev_open_window
	dev_display