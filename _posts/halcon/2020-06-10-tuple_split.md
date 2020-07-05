---
layout: post
title: "tuple_split"
date: 2020-06-10 15:22:00 +0800
author: Michael
categories: Halcon
---

分割字符串，可以使用多个字符同时分割

	p_CalibFrame:='[[2571.30,-1104.17,-1039.99],[0.029151,-0.721126,-0.692176,0.0044231],[1,0,0,1],[2419.24,605.178,9E+09,9E+09,9E+09,9E+09]]'
	tuple_split (p_CalibFrame, '[],', Substrings)

- tuple_number: 把字符串转换为数字
- tuple_sort_index: 元组排序，获得排序后的索引序列
