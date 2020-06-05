---
layout: post
title: "AT 3D Laser Sensor Setting"
date: 2020-06-05 14:53:00 +0800
author: Michael
categories: Halcon
---

#Description:

AT相机设置(4096*3072) - Image Mode

	Image Format Control->Offset X:64
	Image Format Control->Width: 3968
	Camera Control->AOIs->AOI Offset Y: 1096
	Camera Control->AOIs->AOI Height: 916
	AOI：Reset
	Acquisition Control->Acquisition Mode：Single Frame
	Acquisition Control->Acquisition Status Selector：Acquisition Active
	Acquisition Control->Exposure Time:2000
	FIR Control->FIR On
	FIR Control->FIR Mode: Smoothing
	FIR Control->FIR Coefficients: AV9
	FIR Control->FIR Gain:1
	Mode and Algorithm Control->Camera Mode: Image Mode
	Light Coontrol->Light Controller Source: On
	
	Light Coontrol->Light Brightness: 100%
	Trigger Control->Sequencer Mode: Free-Run
	Trigger Control->Trigger Mode: Free-Run


AT相机设置(4096*3072) - 3D Center of Gravity(COG)

	Image Format Control->Offset X:64
	Image Format Control->Width: 3968
	Camera Control->AOIs->AOI Offset Y: 1096
	Camera Control->AOIs->AOI Height: 916
	AOI：Reset
	Acquisition Control->Acquisition Mode：Single Frame
	Acquisition Control->Acquisition Status Selector：Acquisition Active
	Acquisition Control->Exposure Time:2000
	FIR Control->FIR On
	FIR Control->FIR Mode: Smoothing
	FIR Control->FIR Coefficients: AV9
	FIR Control->FIR Gain:1
	Mode and Algorithm Control->Camera Mode: 3D Center of Gravity(COG)
	Mode and Algorithm Control->Profiles per Frame: 100
	Light Coontrol->Light Controller Source: On
	Light Coontrol->Light Brightness: 100%
	Trigger Control->Sequencer Mode: Free-Run
	Trigger Control->Trigger Mode: Free-Run