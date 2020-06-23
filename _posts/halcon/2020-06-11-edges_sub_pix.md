---
layout: post
title: "edges_sub_pix"
date: 2020-06-11 08:32:00 +0800
author: Michael
categories: Halcon
---

抽取边缘

	read_image(Image,'fabrik')
	edges_sub_pix(Image,Edges,'lanser2',0.5,20,40)

- edges_color_sub_pix
- zero_crossing_sub_pix
- lines_gauss
- lines_color
- lines_facet
- threshold_sub_pix
- segment_contours_xld: 把XLD轮廓分解成直线、圆或椭圆
- smooth_contours_xld: 
- split_contours_xld
- gen_polygons_xld:
- gen_contour_polygon_xld
- gen_contour_polygon_rounded_xld
- gen_contours_skeleton_xld
- gen_contour_region_xld
- gen_ellipse_contour_xld 
- gen_rectangle2_contour_xld
- gen_circle_contour_xld
- select_contours_xld: 
- get_contour_xld:
- edges_color
- edges_image
- sobel_amp
- bandpass_image
- boundary
- sort_contours_xld
- calculate_lines_gauss_parameters
- get_contour_xld
- get_contour_attrib_xld
- get_contour_global_attrib_xld:
- derivate_gauss
- zoom_image_factor
- draw_xld
- draw_xld_mod
- paint_xld
- select_shape_xld
- select_obj
- select_contours_xld
- select_xld_point
- union_collinear_contours_xld
- union_straight_contours_xld
- union_adjacent_contours_xld
- union_cocircular_contours_xld
- union_cotangential_contours_xld
- shape_trans_xld
- intersection_closed_contours_xld
- difference_closed_contours_xld
- union2_closed_contours_xld
- fit_line_contour_xld
- fit_rectangle2_contour_xld 
- fit_circle_contour_xld
- fit_ellipse_contour_xld
- contour_to_world_plane_xld
- area_center_xld
- compactness_xld
- convexity_xld
- eccentricity_xld
- diameter_xld
- orientation_xld
- smallest_circle_xld
- smallest_rectangle2_xld
- moments_xld

示例代码：

	gen_image_gray_ramp (ImageGrayRamp, 0.5, 0.5, 128, 256, 256, 512, 512)
	gen_rectangle2_contour_xld(Rectangle, 256, 256, rad(-45), 512, 5)
	paint_xld(Rectangle,ImageGrayRamp,ImageResult,128)    
	* 当相邻两个点的像素差大于90，那么则认为时边缘；
	* 如果相邻两个点的像素差在10~90之间，且与它相邻的点已经被认为是边缘时，那么这个点是边缘；
	* 如果相邻两个点的像素差在10~90之间，且与它相邻的点都不是边缘，那么这个点不是边缘；
	* 如果相邻两个点的像素差在小于10，那么它肯定不是边缘
	edges_sub_pix (ImageResult, Edges, 'canny', 0.5, 10, 90)
	lines_gauss (ImageResult, Lines, 2.3, 0.0, 0.7, 'light', 'true', 'parabolic', 'true')

图片：

![边缘检测结果图 in Jekyll](/assets/edges_sub_pix/edges.png)

如果是本地，使用下述地址

	(../../assets/edges_sub_pix/edges.png)

