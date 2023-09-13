---
layout: post
title: "Upgrade To Zenon 11"
date: 2023-09-12 09:44:00 +0800
author: Michael
categories: zenon
---

# GestureTapAndHoldFunction
当zenon工程从zenon 8升级到zenon 11时，zenon8中GestureTapAndHoldFunction默认的值在zenon11中会认为时函数名，然后报警。如下代码时导出screen到xml时，screen中的控件配置节选。此时需要导出screen到xml，手动修改为正确的xml属性值就可以了。GestureTapAndHoldFunction对应的是控件的Service Engine -> Tap and hold -> Function。

    //zenon 8不会报错，但是zenon 11会报错
	<GestureTapAndHoldFunction>&lt;No function linked&gt;</GestureTapAndHoldFunction>

    //zenon 8和zenon 11都不会报错
    <GestureTapAndHoldFunction/>

![日志文件夹](/assets/zenon/Unabletofindlinkedfunction.png)      
![日志文件夹](/assets/zenon/TapandholdFunction.png)  

    