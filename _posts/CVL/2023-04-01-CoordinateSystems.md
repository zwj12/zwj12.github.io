---
layout: post
title: "Coordinate Systems"
date: 2023-04-01 09:49:00 +0800
author: Michael
categories: CVL
---

# pel = picture element
An image is a two-dimensional array of values. Each element in the root image array is called a pixel or a pel (short for picture element). The value stored in each pixel of the image indicates the light intensity or brightness of each pixel. Typically, pixel values are integers, though other values may be used as well.

# Display Image Client Coords
通过cc2Xform可以把图像坐标系和用户坐标系进行变换，使其不重合。

    ccPNG png;
    //png.init(cfSamplePrependVisionRootPath(cmT("sample\\cvl\\pngfile.png")));
    png.init(cmT("C:\\Users\\CNMIZHU7\\Pictures\\test.png"));

    ccDisplayConsole console(ccIPair(600, 600), cmT("PNG Image"));

    ccPelBuffer<ccPackedRGB32Pel> imageRGB32Pel;
    png.pelBuffer(imageRGB32Pel);


    cc2Xform xform(cc2Vect(0, 0), ccRadian(0), ccRadian(0), 10, 10);
    imageRGB32Pel.imageFromClientXform(xform);

    console.image(imageRGB32Pel);
   
    ccUITablet tablet1;
    ccPoint where(8, 8);
    tablet1.drawPointIcon(where, ccColor::red);
    tablet1.draw(cmT("Display Point (8,8)"), where, ccColor::blue, ccColor::yellow, ccUIFormat());
    console.drawSketch(tablet1.sketch(), ccDisplay::eDisplayCoords);

    ccUITablet tablet2;
    tablet2.drawPointIcon(where, ccColor::red);
    tablet2.draw(cmT("Client Point (8,8)"), where, ccColor::blue, ccColor::yellow, ccUIFormat());
    console.drawSketch(tablet2.sketch(), ccDisplay::eClientCoords);

    ccUITablet tablet3;
    tablet3.drawPointIcon(where, ccColor::red);
    tablet3.draw(cmT("Image Point (8,8)"), where, ccColor::blue, ccColor::yellow, ccUIFormat());
    console.drawSketch(tablet3.sketch(), ccDisplay::eImageCoords);

![日志文件夹](/assets/CVL/DisplayImageClientCoords.png)  

# Client Coordinate System
Native units (inches or centimeters instead of pixels) are defined by the client coordinate system. The client coordinate system uses a ransformation object to map between client coordinates and image coordinates. 