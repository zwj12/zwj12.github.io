---
layout: post
title: "ccPtrHandle"
date: 2023-03-27 09:49:00 +0800
author: Michael
categories: CVL
---

# ccPtrHandle and ccPtrHandle_const
Pointer handles are reference-counted pointers to heap-allocated objects. In general, they work the same way as pointers do in C++, but have the additional benefit that the object pointed to maintains a count of how many pointer handles are pointing to it. The pointer handle classes use this count, called the reference count, to manage the heap memory occupied by the object. When the reference count reaches zero, the object is 
automatically deleted and its memory returned to the heap.

# 智能指针别名
可以通过typedef定义一个CVL类智能指针的别名。

    typedef ccPtrHandle<ccAlpha> ccAlphaPtrh;
