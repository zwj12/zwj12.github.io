---
layout: post
title: "ccAcqFifoPtrh"
date: 2023-04-25 09:49:00 +0800
author: Michael
categories: CVL
---

# ccAcqFifo::properties()
设置相机参数

	ccGigEVisionCamera& fg = ccGigEVisionCamera::get(0);
	const ccStdVideoFormat& fmt = ccStdVideoFormat::getFormat(cmT("Generic GigEVision (Mono)"));
	ccAcqFifoPtrh fifo = fmt.newAcqFifoEx(fg);
	fifo->properties().exposure(0.005);  

# prepare()
通知相机做好准备拍照，如果返回false，那么代表相机处理错误状态，不能接受触发拍照的信号。

	ccGigEVisionCamera& fg = ccGigEVisionCamera::get(0);
	const ccStdVideoFormat& fmt = ccStdVideoFormat::getFormat(cmT("Generic GigEVision (Mono)"));
	ccAcqFifoPtrh fifo = fmt.newAcqFifoEx(fg);
	fifo->properties().exposure(0.005);  
	fifo->prepare(0.0); 

# start()
软件触发拍照

# 相机触发拍照方式
- Manual trigger (Software Trigger)， 软件触发，需要使用函数`ccAcqFifo::start()`
- Auto trigger (Hardware trigger)， 硬件触发，不需要运行函数`ccAcqFifo::start()`，直接通过外部信号触发拍照。
- Semi trigger, 半自动触发，先运行函数`ccAcqFifo::start()，然后等外部信号触发拍照
- Free run trigger， ccAcqFifo:triggerEnable()设置为true。

![日志文件夹](/assets/CVL/triggermodels.png)  

# completeAcq()
获取图像

	ccGigEVisionCamera& fg = ccGigEVisionCamera::get(0);
	const ccStdVideoFormat& fmt = ccStdVideoFormat::getFormat(cmT("Generic GigEVision (Mono)"));
	ccAcqFifoPtrh fifo = fmt.newAcqFifoEx(fg);
	fifo->properties().exposure(0.005);  
	fifo->prepare(0.0);                  
	fifo->start();
	ccAcqImagePtrh img = fifo->completeAcq();