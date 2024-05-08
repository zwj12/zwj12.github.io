---
layout: post
title: "ccVideoFormat"
date: 2023-05-13 09:49:00 +0800
author: Michael
categories: CVL
---

# ccContrastBrightnessProp::contrastBrightness()
1. Contrast (0~1) -> Gain 
2. Brightness (0~1) -> Black Level
3. Exposure -> Exposure Time
3. White balance -> Balance Ratio

    m_phTempFifo->properties().contrastBrightness(m_dContrast, m_dBrightness);
    m_phTempFifo->properties().exposure(m_dExposureMs / 1000.0);

![日志文件夹](/assets/CVL/ExposureTime.png)  
![日志文件夹](/assets/CVL/ContrastBrightness.png)  
![日志文件夹](/assets/CVL/WhiteBalance.png)  

# Black Level
The Black Level camera feature allows you to change the overall brightness of an image. Adjusting the camera's black level will result in an offset to the pixel's gray values output by the camera. Basler recommends setting the black level to 0 before using any of the color enhancement features.

# Gain
The Gain camera feature allows you to increase the brightness of the images output by the camera. Increasing the gain increases all pixel values of the image. Gain amplifies each pixel readout by a certain factor. Accordingly, signal and noise are both amplified. Increasing gain will increase the image contrast. Increasing gain will increase the image brightness. Unless your application requires extreme contrast, make sure that detail remains visible in the brightest portions of the image when increasing gain.