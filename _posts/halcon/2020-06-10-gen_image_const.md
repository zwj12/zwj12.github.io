---
layout: post
title: "gen_image_const"
date: 2020-06-10 16:44:00 +0800
author: Michael
categories: Halcon
---

- gen_image_const: 创建一个空的图
- gen_circle: 生成一个圆region
- paint_region: 把region画到图片中

示例代码：

	dev_close_window()
	dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
	Row:=250
	Column:=250
	Radius:=100
	gen_circle(Circle,Row,Column,Radius)
	gen_image_const (Image1, 'byte', 512, 512)
	paint_region (Circle, Image1, ImageResult, 255, 'fill')
	gray_erosion_rect (ImageResult, Erosion, 3, 3)
	gray_dilation_rect (ImageResult, Opening, 3, 3)