---
layout: post
title: "ccGigEVisionCamera"
date: 2023-04-09 09:49:00 +0800
author: Michael
categories: CVL
---

# Acquiring with GigE Vision Cameras
To the CVL acquisition system and to the vision tools, a GigE Vision camera appears to be a frame grabber.

# ccGigEVisionCamera::count()
获取GigE相机数量

# ccBoard::count()
获取所有Board的数量，包含dongle

	int ccBoardCount= ccBoard::count();
	for (size_t i = 0; i < ccBoardCount; i++)
	{
		CString str = ccBoard::get(i).name(); //Cognex Security Key v6 (USB)
	}

    

# ccGigEVisionCamera::get()
获取GigE相机对象

# heartbeat
The default heartbeat timeout period is 3 seconds.

    #ifdef _DEBUG // defined for MS Visual Studio debug builds
        // Set timeout to 1 minute (unit is mSec)
        fg.writeIntegerValue(cmT("GevHeartbeatTimeout"), 60 * 1000);
    #endif