---
layout: post
title: "fill_up_shape"
date: 2020-06-08 4:07:00 +0800
author: Michael
categories: Halcon
---

Fill up holes in regions having given shape features.

把Region内部的洞填满

	read_image(Image, 'monkey')
	threshold(Image,Seg,120.0,255.0)
	fill_up_shape(Seg,Filled,'area',0.0,200.0)