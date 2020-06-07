---
layout: post
title: "complement 补集"
date: 2020-06-05 13:31:00 +0800
author: Michael
categories: Halcon
---

#Description:

集合运算，补集

	read_image (Image, 'particle')
	threshold (Image, Large, 110, 255)
	* Dilate regions with a circular structuring element
	dilation_circle (Large, LargeDilation, 7.5)
	complement (LargeDilation, NotLarge)


对应的其他的集合函数还有：

- difference 
- union1
- intersection