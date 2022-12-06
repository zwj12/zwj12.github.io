---
layout: post
title: "Alignment Margin Padding"
date: 2022-12-03 09:09:00 +0800
author: Michael
categories: CSharp
---

# HorizontalAlignment 和 VerticalAlignment
HorizontalAlignment 和 VerticalAlignment 属性描述**子元素**应当如何在**父元素**的已分配布局空间中定位。

# Height 和 Width 属性优先于 Stretch 
元素上显式设置的 Height 和 Width 属性优先于 Stretch 属性值。 尝试设置 Height、Width 和被忽略的 Stretch 请求中的 Stretch 结果的 HorizontalAlignment 值。Stretch拉伸子元素以填充父元素的已分配布局空间，显式 Width 值和 Height 值优先。

