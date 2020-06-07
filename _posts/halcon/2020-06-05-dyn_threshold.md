---
layout: post
title: "dyn_threshold"
date: 2020-06-05 11:23:00 +0800
author: Michael
categories: Halcon
---

#Description:

先平均值滤波图像，然后以该图像为基准，选择动态灰度值差异大的区域，最后分割Regin，可以通过面积获取需要的区域。

需要注意的是，平均值滤波的尺寸一般为黑色线像素的三倍

	read_image (Image, 'crystal')
	mean_image (Image, ImageMean, 21, 21)
	dyn_threshold (Image, ImageMean, RegionDynThresh, 8, 'dark')
	connection (RegionDynThresh, ConnectedRegions)

