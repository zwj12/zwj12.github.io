---
layout: post
title: "ccDisplayConsole"
date: 2023-03-26 09:49:00 +0800
author: Michael
categories: CVL
---

# 创建
貌似ccDisplayConsole对象一创建就会打开一个窗口，该窗口非MFC主框架窗口，而是一个单独的对话框。

# image
显示图像，The image() function copies the pel buffer into the image plane. To change the contents of the display console and display a new image, simply call image() again with the new pel buffer.

    console.image(imageRGB32Pel);

# eOverlayPlane 显示多图层
    console.enableOverlay(ccWin32Display::eOverlayPlane);

# removeImage()
删除图像

    console.removeImage();

# getDisplayedImage()
获取当前显示的图像。

# mag & magExact & fit & fitExact
设置或获取显示放大倍数，正数为放大，负数为缩小。

    void mag(c_Int32 m);
    c_Int32 mag() const;
    display->mag(-2); // one-half actual size
    display->magExact(1.52); //1.52x actual size
    display->magExact(0.52); //0.52x actual size

# CloseAction
设置窗口关闭按钮的功能，禁用，关闭窗口，隐藏窗口

    enum CloseAction { eCloseDisabled, eCloseHide, eCloseDelete };
    void closeAction (CloseAction action);
    CloseAction closeAction() const { return closeAction_; }

# 工具栏，滚动条，状态栏

    console.showToolBar(true);
    console.showScrollBar(true, true);
    console.showStatusBar(true);

# 状态栏显示字符串
    void statusBarText(const ccCvlString &text, bool resize=true);

# drawSketch
Draws the sketch in the specified coordinate system，在图片上画坐标和字符串

    ccUITablet tablet;
    ccPoint where(20, 20);
    tablet.drawPointIcon(where, ccColor::red);
    tablet.draw(cmT("Point (2,2)"), where, ccColor::blue,        ccColor::yellow, ccUIFormat());
    console.drawSketch(tablet.sketch(), ccDisplay::eDisplayCoords);

![日志文件夹](/assets/CVL/DisplayImageClientCoords.png)  

# PostMessage
发送Windows消息

    cgDisplayPtr->PostMessage(WM_QUIT, 0, 0);

# mouseMode 设置鼠标图标
    console.mouseMode(ccDisplay::eZoomOut);

# GetCursorPos 获取或设置鼠标位置
    POINT pt;
    GetCursorPos(&pt);
    SetCursorPos(pt.x, pt.y);

# cfInitializeDisplayResources 初始化
When your application calls a CVL display API in your DLL, Windows looks in your DLL for the necessary resources, but does not find them there. Calling cfInitializeDisplayResources() in your application informs Windows that the CVL display resources are to be found in cogdisp.dll, and not in your DLL. 

# interpolation
图像显示插值处理

    display->interpolation(ccUITablet::eBilinear);

# displayFormat
获取桌面颜色位数

    ccDisplay::DisplayFormat d= console.displayFormat();