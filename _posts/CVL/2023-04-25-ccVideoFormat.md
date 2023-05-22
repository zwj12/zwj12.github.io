---
layout: post
title: "ccVideoFormat"
date: 2023-04-25 09:49:00 +0800
author: Michael
categories: CVL
---

# ccVideoFormat
    #include <ch_cvl/vidfmt.h>
    class ccVideoFormat;
    class ccGreyVideoFormat : public ccVideoFormat;
    class ccStdGreyVideoFormat : public ccGreyVideoFormat;
    class ccStdVideoFormat: public ccStdGreyVideoFormat;

# ccVideoFormat::filterList()
获取相机的图像格式

	ccGigEVisionCamera& fg = ccGigEVisionCamera::get(0);
	std::vector<const ccVideoFormat*> x= ccVideoFormat::filterList(ccVideoFormat::fullList(), fg);
	for (size_t i = 0; i < x.size(); i++)
	{
		CString y=x[i]->name();
	}

## 获取当前相机支持的图像格式
	this->videoFormatList=ccStdVideoFormat::filterList(ccStdVideoFormat::fullList(), fg);
	for (size_t i = 0; i < this->videoFormatList.size(); ++i)
		OutputDebugString(this->videoFormatList[i]->name());

# ccVideoFormat::fullList()
获取CVL库支持的图像格式

	std::vector<const ccVideoFormat*> x = ccVideoFormat::fullList();
	for (size_t i = 0; i < x.size(); i++)
	{
		CString y = x[i]->name();
	}

# pixel formats for GigE Vision Cameras
GigE相机支持的格式如下，在使用是，需要使用全称：Generic GigEVision (Mono)

- Mono8
- Mono10
- Mono10Packed
- Mono12
- Mono12Packed
- Mono14
- Mono16
- RGB8Packed
- YUV422Packed
- BayerGR8
- BayerRG8
- BayerGB8
- BayerBG8

	ccGigEVisionCamera& fg = ccGigEVisionCamera::get(0);
	const ccStdVideoFormat& fmt = ccStdVideoFormat::getFormat(cmT("Generic GigEVision (Mono)"));

	ccAcqFifoPtrh fifo = fmt.newAcqFifoEx(fg);
	fifo->properties().exposure(0.005);  
	fifo->prepare(0.0);                  
	fifo->start();

	ccAcqImagePtrh img = fifo->completeAcq();

	console =new ccDisplayConsole (ccIPair(300, 300), cmT("Camera Image"));
	console->image(img);

	fifo = 0;
	fg.disconnect(false);


	this->videoFormatList=ccStdVideoFormat::filterList(ccStdVideoFormat::fullList(), fg);
	for (size_t i = 0; i < this->videoFormatList.size(); ++i)
		OutputDebugString(this->videoFormatList[i]->name());

# ccStdVideoFormat::newAcqFifoEx()
通过图像格式绑定相机，就可以获取图像了。Once you have obtained a video format, use its newAcqFifoEx() member function and the reference to the frame grabber to create an acquisition FIFO:

    const ccStdVideoFormat& fmt = ccStdVideoFormat::getFormat(cmT("Sony XC-ST50 640x480"))
    ccAcqFifoPtrh fifo = fmt.newAcqFifoEx(fg);