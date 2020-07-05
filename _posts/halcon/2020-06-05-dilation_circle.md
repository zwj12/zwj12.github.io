---
layout: post
title: "dilation_circle"
date: 2020-06-05 13:22:00 +0800
author: Michael
categories: Halcon
---

# Description:

膨胀，Wow，bingo

	read_image (Image, 'particle')
	threshold (Image, Large, 110, 255)
	* Dilate regions with a circular structuring element
	dilation_circle (Large, LargeDilation, 7.5)

类似膨胀、腐蚀函数还有：

- opening_circle （suppress noise）
- closing_circle （ﬁll gaps）
- closing_rectangle1
- opening_rectangle1
- erosion1
- difference: 可以对比膨胀后和再腐蚀后的region，算出边界
- fill_up
