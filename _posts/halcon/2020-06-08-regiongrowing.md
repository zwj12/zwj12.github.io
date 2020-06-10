---
layout: post
title: "regiongrowing"
date: 2020-06-08 3:27:00 +0800
author: Michael
categories: Halcon
---

# 函数原型：

	regiongrowing(Image: Regions: Row, Column, Tolerance, MinSize: )

# 函数作用：

用区域生长实现图像分割

	read_image(Image,'fabrik')
	mean_image(Image,Mean,5,5)
	regiongrowing(Mean,Result,5,5,6.0,100)

# 函数原理：

如果相邻像素的灰度值差小于等于Tolerance，则被融为一个区域。因为矩形一般大于1个像素，所以常常在调用regiongrowing前会用大小至少为Row*Column的低通滤波器平滑一下。如果图像包含小噪声并且矩形很小，平滑后这些因素大都会被去除。而区域包含至少MinSize个点才被挑选出来。区域生长是一个非常快的算子，因此适合用于对时间要求严苛的应用中。

# 参数列表：

Image：输入图像

Regions：输出被分割后的区域

Row：被检测像素的行距离，Row >= 1 && odd(Row) (为奇数的意思)

Column：被检测像素的列距离，Column >= 1 && odd(Column)

Tolerance：被检测像素的灰度差小于等于该值时，被计入同一区域，Tolerance >= 0 && Tolerance < 127

MinSize：输出区域的最小大小，MinSize >= 1

类似元组算子还有：

1. regiongrowing_mean