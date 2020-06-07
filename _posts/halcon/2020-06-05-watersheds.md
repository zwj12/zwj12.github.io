---
layout: post
title: "watersheds"
date: 2020-06-05 13:09:00 +0800
author: Michael
categories: Halcon
---

#Description:

分水岭函数，可以分离波纹

	read_image (Image, 'atoms')
	gauss_filter (Image, ImageGauss, 5)
	watersheds (ImageGauss, Basins, Watersheds)
