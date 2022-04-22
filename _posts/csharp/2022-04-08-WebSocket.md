---
layout: post
title: "Web Socket"
date: 2022-04-08 09:42:00 +0800
author: Michael
categories: CSharp
---

# WebSocket.ConnectAsync
WebSocket.ReadyState的状态默认是Connecting，当调用ConnectAsync后，在没有连接成功前，一直保持Connecting，当连接成功后，修改为Open，如果连接不成功，则修改为Closed。这里要注意的是，当连接不成功，同样会引发Closed事件。如果要让程序自动重连，不能使用计时器，而应该在Closed事件中再次Reconnect，循环连接。