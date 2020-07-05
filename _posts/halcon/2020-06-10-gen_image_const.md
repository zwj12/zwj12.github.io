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
- gen_contour_polygon_xld: 通过多边形生成亚像素轮廓

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
	gen_contour_polygon_xld

- gen_ellipse_contour_xld 
- tuple_gen_const
- gen_tuple_const
- paint_gray: 把一幅图画到另一幅图中，类似于重叠图片，把原始图片盖住