---
layout: post
title: "shape_trans"
date: 2020-06-05 11:40:00 +0800
author: Michael
categories: Halcon
---

# Description:

通过情况下，通过Connection函数获取的区域都是不规则的，测试可以使用凸包形状转换函数，该函数类似于把分割后的区域用一个橡皮筋包围起来，然后获取该橡皮筋的Region

	read_image (Image, 'crystal')
	mean_image (Image, ImageMean, 21, 21)
	dyn_threshold (Image, ImageMean, RegionDynThresh, 8, 'dark')
	connection (RegionDynThresh, ConnectedRegions)
	shape_trans (ConnectedRegions, ConvexRegions, 'convex')
	select_shape (ConvexRegions, LargeRegions, 'area', 'and', 600, 2000)
	select_gray (LargeRegions, Image, Crystals, 'entropy', 'and', 1, 5.6)
