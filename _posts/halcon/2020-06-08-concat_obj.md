---
layout: post
title: "concat_obj"
date: 2020-06-08 08:50:00 +0800
author: Michael
categories: Halcon
---

# Description:

连接两个元组，返回一个新元组

	gen_circle(Circle,200.0,400.0,23.0)
	gen_rectangle1(Rectangle,23.0,44.0,203.0,201.0)
	concat_obj(Circle,Rectangle,CirclAndRectangle)

类似元组算子还有：

1. count_obj
2. copy_obj
3. select_obj
4. obj_to_integer
5. integer_to_obj