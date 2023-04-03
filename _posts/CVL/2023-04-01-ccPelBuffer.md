---
layout: post
title: "ccPelBuffer"
date: 2023-04-01 09:49:00 +0800
author: Michael
categories: CVL
---

# cc2Vect
When you specify locations in images for the vision tools, you usually use the class cc2Vect which describes a two-element vector. The cc2Vect class provides several member functions that let you set and access the elements of the vector as x and y locations.

# ccPelRoot
原始图像

# ccPelBuffer
窗口图像，可以是ccPelRoot的一个子区域

# window() & offset()
Calling the window() member function only made the window, or pel buffer, smaller. It did not change either the image coordinates or the client coordinates. To change the coordinate system, call offset(), changing the offset also changes the client coordinate system by the corresponding amount.

    thePelBuf.window(4, 0, 9, 6);
    thePelBuf.offset(0,0);