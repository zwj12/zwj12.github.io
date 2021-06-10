---
layout: post
title: "gray_erosion_shape"
date: 2020-06-10 16:23:00 +0800
author: Michael
categories: Halcon
---

- gray_erosion_shape: 
- gray_erosion_rect: 给定一个矩形模板，计算图像内每个点的输出值，输出该区域内的最小值
- gray_dilation_shape 
- gray_dilation_rect

# 灰度图腐蚀和膨胀，开运算、闭运算 #

若我们把重合区域中所有点灰度值的最大值赋给当前点，就是对灰度图的腐蚀操作；若我们把重合区域中所有点灰度值的最小值赋给当前点，就是对灰度图的膨胀操作。

示例代码：

	read_image (Image, 'mreut')
	gray_erosion_rect (Image, Erosion, 11, 11)
	gray_dilation_rect (Erosion, Opening, 11, 11)

	read_image (Image, 'mreut')
	gray_dilation_rect (Image, Dilation, 11, 11)
	gray_erosion_rect (Dilation, Closing, 11, 11)