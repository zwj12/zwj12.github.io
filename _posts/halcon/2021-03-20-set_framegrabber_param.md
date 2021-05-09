---
layout: post
title: "set_framegrabber_param"
date: 2021-03-20 11:07:00 +0800
author: Michael
categories: Halcon
---

# grab_timeout
timeout (milliseconds, default 5000) for aborting a pending grab. If -1 is specified, the timeout is set to INFINITE.

	set_framegrabber_param(AcqHandle, 'grab_timeout', 10000)

# grab_image_start
MaxDelay: This parameter is obsolete and has no effect.

	grab_image_start (AcqHandle, -1)

# grab_data_async
The grab of the next image is finished by calling grab_data_async or grab_image_async. If more than MaxDelay ms have passed since the asynchronous grab was started, the asynchronously grabbed image is considered as too old and a new image is grabbed, if necessary. If a negative value is assigned to MaxDelay, this control mechanism is deactivated.

	grab_data_async(Image, Region, Contours, AcqHandle, -1, Data) 