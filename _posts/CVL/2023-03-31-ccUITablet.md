---
layout: post
title: "ccUITablet"
date: 2023-03-31 09:49:00 +0800
author: Michael
categories: CVL
---

# 在ccDisplayConsole中显示文字等信息

    ccUITablet tablet;
    ccPoint where(20, 20);
    tablet.drawPointIcon(where, ccColor::red);
    tablet.draw(cmT("Point (2,2)"), where, ccColor::blue, ccColor::yellow, ccUIFormat());
    console.drawSketch(tablet.sketch(), ccDisplay::eDisplayCoords);

# drawPointIcon
Draws a static point icon centered at the specified location. 

# draw
输出文字等信息

# ccGraphicProps
图像属性

    ccGraphicProps props;
    props.penColor(ccColor::greenColor());
    tablet.drawPointIcon(ccPoint(200, 100), props);

# ccUIRectangle
画矩形框

    ccUIRectangle *uiRect2 = new ccUIRectangle;
    uiRect2->rect(ccRect(cc2Vect(0,0), cc2Vect(20,20)));
    uiRect2->color(ccColor::white);
    uiRect2->condVisible(true);
    //uiRect->drawLayer(ccUITablet::eOverlayLayer);
    display->addShape(uiRect2, ccDisplayConsole::eClientCoords);

# ccLineSeg 画直线
第一个参数是方向，第二个参数是位置，表示经过一点的直线，该直线无限长。

    ccLine(const cc2Vect& dir, const cc2Vect& pos);

    ccUITablet tablet;
    ccGraphicProps redProp(ccColor::redColor());
    ccGraphicProps blueProp(ccColor::blueColor());
    tablet.draw(ccRect(cc2Vect(10,10), cc2Vect(240, 100)),
    redProp);
    tablet.draw(ccLineSeg(cc2Vect(100,100), cc2Vect(101,100)),
    blueProp);
    display->drawSketch(tablet.sketch(),
    ccDisplay::eImageCoords);

# ccCircle 画圆
    ccGraphicProps redProp(ccColor::redColor());
    tablet.draw(ccCircle(cc2Vect(100,100), 30.0), redProp);

# ccGraphicProps 样式
    ccGraphicProps p;
    p = uiRect2->props();
    p.penColor(ccColor::greenColor());
    p.penStyle(ccGraphicProps::ePenStyleDash);
    uiRect2->props(p);

# multiSelectable
当图形在同显示模式下是，可以设置multiSelectable允许多选

    ccUIRectangle* uiRect = new ccUIRectangle;
    uiRect->rect(ccRect(cc2Vect(20, 20), cc2Vect(30, 30)));
    uiRect->color(ccColor::blue);
    uiRect->condVisible(true);
    uiRect->multiSelectable(true);
    console.addShape(uiRect, ccDisplayConsole::eClientCoords);

    ccUIRectangle* uiRect1 = new ccUIRectangle;
    uiRect1->rect(ccRect(cc2Vect(0, 0), cc2Vect(20, 20)));
    uiRect1->color(ccColor::green);
    uiRect1->condVisible(true);
    uiRect1->multiSelectable(true);
    console.addShape(uiRect1, ccDisplayConsole::eClientCoords);

# 删除图形
    console.eraseSketch(ccDisplay::eImageCoords);