---
layout: post
title: "Region Of Interest"
date: 2020-06-09 15:22:00 +0800
author: Michael
categories: Halcon
---

- reduce_domain: 把region添加到图像中
- change_domain: faster than reduce_domain，直接设置，而不是在之前的region中再添加
- get_domain: 获取域
- disp_image: 显示图像
- rectangle1_domain: gen_rectangle1 + reduce_domainin
- gen_circle: 创建圆
- gen_rectangle2: 创建矩形
- gen_region_polygon_filled: 创建多边形
- edges_sub_pix: 提取边缘，边缘提取算法有很多种，比如canny
- dilation_rectangle1: 矩形膨胀
- fill_up: 填充孔洞，使用系统默认值进行填充
- shape_trans: 转换region为标准形状
- erosion_circle: 腐蚀，使用圆腐蚀
- closing_circle: 闭运算（膨胀—腐蚀），闭运算是填充掉物体内小沟壑
- opening_circle: 开运算（腐蚀—膨胀），开运算是去掉物体多余的尾巴
- draw_circle, draw_rectangle1, draw_rectangle2, draw_region
- draw_circle_mod, draw_rectangle1_mod, draw_rectangle2_mod, draw_xld, draw_xld_mod
- gen_circle, gen_ellipse, gen_rectangle2, gen_region_polygon_filled
- gen_checker_region, gen_grid_region
- change_domain, full_domain, add_channels
- gen_measure_arc, gen_measure_rectangle2
- write_region, read_region
- threshold
- gen_image1, region_to_bin, get_image_pointer1
