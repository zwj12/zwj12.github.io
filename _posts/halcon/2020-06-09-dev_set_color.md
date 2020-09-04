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
	dev_update_off
	dev_clear_window
	* 改变窗口位置和大小
	dev_set_window_extents 
	dev_set_color ('red')
	* PC (program counter)
	dev_update_pc
	dev_update_var

设置线的宽度

	dev_set_draw('margin') 
	dev_set_line_width


设置图像显示区域，设置后窗口的坐标原点会跟着改变。可以设置为负数，图片的坐标不会改变。

	dev_set_part 

设置文字的位置，字体，打印文件到窗口

	set_display_font
	set_tposition
	disp_message
	write_string 

设置箭头的位置和方向

	disp_arrow

显示十字架

	disp_cross

打开新的窗口，获取窗口句柄，显示图像

	dev_open_window
	dev_open_window_fit_image
	dev_display

显示圆弧

	disp_arc 

显示直线

	disp_line
	colored_display

显示变量

	dev_inspect_ctrl

输入字符串

	read_string 