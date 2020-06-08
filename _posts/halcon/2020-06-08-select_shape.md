---
layout: post
title: "select_shape"
date: 2020-06-08 12:47:00 +0800
author: Michael
categories: Halcon
---

# Description:
选择Region
	
	read_image(Image,'monkey')
	threshold(Image,Region,128,255)
	connection(Region,ConnectedRegions)
	select_shape(ConnectedRegions,Eyes,['area','max_diameter'],'and',[500,30.0],[1000,50.0])
