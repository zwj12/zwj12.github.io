---
layout: post
title: "ccAcqFifoPtrh"
date: 2023-04-25 09:49:00 +0800
author: Michael
categories: CVL
---

# ccAcqFifo
- You configure the FIFO for the camera and format you are using.
- acquire images by calling its start() method.
- call the FIFO completeAcq() method to initiate processing the acquired image.
- start() and completeAcq() should always be issued in pairs, one pair for each acquired image.
- Only one FIFO is required to process a stream of acquisitions from the same camera. For a multiple camera application you will generally create one FIFO for each camera. 

![日志文件夹](/assets/CVL/CVLAcquisitionSubsystem.png)  

# engine queue & user queue
Each FIFO contains two internal queues, the engine queue and the user queue. 

1. The engine queue contains acquisition requests for which images **have not been acquired**. 
2. The user queue contains acquisition requests for which image acquisition is completed, but the completeAcq() method **has not been called**. 

# triggerEnable()
he FIFO provides a triggerEnable property that enables or disables 
the engine thread. When triggerEnable is set to false, the engine 
thread immediately aborts any acquisition in progress and 
terminates. 经过测试，每次连接相机后，该参数默认都会被设置为true

	public: bool triggerEnable() const;
	// effect    Set/get the trigger enable setting.
	//
	//           In general, true allows acquisitions to happen, and false
	//           prevents acquisitions from happening.  See cfManualTrigger,
	//           cfAutoTrigger, cfSemiTrigger and cfSlaveTrigger for more
	//           details.
	//
	//           Invoking triggerEnable(e) for a master or any of its slaves has
	//           the effect of invoking triggerEnable(e) for all.  That is,
	//           masters and slaves have the same triggerEnable setting.
	//
	// note      The default is true.

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
软件触发拍照，硬件触发不需要运行该函数。

# triggerModel() 相机触发拍照方式
经过测试，每次连接相机后，该参数默认为cfManualTrigger().

- Manual trigger (Software Trigger)， 软件触发，需要使用函数`ccAcqFifo::start()`
- Auto trigger (Hardware trigger)， 硬件触发，不需要运行函数`ccAcqFifo::start()`，直接通过外部信号触发拍照。
- Semi trigger, 半自动触发，先运行函数`ccAcqFifo::start()，然后等外部信号触发拍照
- Free run trigger， ccAcqFifo:triggerEnable()设置为true。

	public: const ccTriggerModel& triggerModel() const;
	// effect    Set/get the trigger model for acquisitions.
	// note      The default trigger model is cfManualTrigger().
	// note      It is recommended that custom trigger models be set using the
	//           ccTriggerModelPtrh overload.  Built-in trigger models
	//           (cfManualTrigger, etc.) can only be set using ccTriggerModel&
	//           overload.
	// see also  cfManualTrigger, cfAutoTrigger, cfSemiTrigger, cfSlaveTrigger.

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

# 32 images per FIFO
每个相机最多会缓存32张图像，如果在triger第33张图像时，没有使用completeAcq把第1张图像取出来，那么第一张图像会被抛弃掉。

For all acquisition FIFOs, including those used with the MVS-8100D, the acquisition engine does not queue up more than 32 images per FIFO, regardless of image size, pel pool size, frame grabber image buffer size, or the amount of available host PC memory. (This number is set as ccAcqFifo::kMaxOutstanding.) Once there are 32 images in the acquisition FIFO, your application must deal with the first image in the FIFO before a 
33rd image can be acquired. Your application need not process the image, but the image must be removed from the FIFO by calling completeAcq() and stored in host PC memory or discarded, for image acquisition to continue. Your application can call ccAcqFifo::completedAcqs() to determine how many completed acquisitions are currently being held by the FIFO.

For most applications, if you find the acquisition FIFO’s 32 image buffering capacity is consistently exhausted, your application must either slow down the trigger rate or increase the rate at which images are retrieved and processed. 

# ccAcqFifo::pendingAcqs(), completedAcqs(), availableAcqs()
1. availableAcqs(), 当前还可以触发拍照的数量，最小0，最大32，触发一次拍照（软件或硬件触发)，该值减1。运行一次completeAcq()，该值加1。
2. pendingAcqs(), 触发拍照，但是还没有completeAcq()的次数，可能会超过32，但是一旦发现没有图片后，该值就会变0。
3. completedAcqs(), Returns the number of acquisitions in the completed state. 如果触发40次，当completeAcq()32次后，因为最大32个图像缓存，所以最后8次的completeAcq()会以失败直接返回，所以在第33次后，completedAcqs()返回的是8，第34次后，变为7。