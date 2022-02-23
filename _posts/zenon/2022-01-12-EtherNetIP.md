---
layout: post
title: "EtherNet/IP"
date: 2022-01-12 13:44:00 +0800
author: Michael
categories: zenon
---

# EtherNet/IP Overview
EtherNet/IP is an adaptation of the open standard Common Industrial Protocol (CIP), which is designed for vendor-independent device interoperability that is strictly object-oriented protocol.
CIP can use different transport layers. If EtherNet/IP, Ethernet (IEEE 802.3 and the TCP/IP protocol suite) is used. The ‘IP’ in ‘EtherNet/IP’ refers to ‘Industrial Protocol’.

## Messaging
EtherNet/IP supports unconnected and connected modes of messaging.

- Unconnected messaging refers to peer-to-peer communication, where the opening and the closing of connections is allowed via unconnected messaging. The Unconnected Message Manager (**UCMM**) handles the messaging. Messages are sent over TCP/IP.
- Connected messaging is dedicated to a particular purpose, such as frequent explicit message transactions or real-time I/O data transfers. Connection resources are reserved and configured using communications services available via the UCMM. Messages are sent over TCIP/IP and UDP.

EtherNet/IP specifies a special encapsulation protocol to carry CIP messages over TCP/IP and UDP. There are two types of connections, explicit and implicit.

- Explicitconnections refer to request-resp
onse connections, which are general-purpose connections. Explicit connections use TCP/IP and use either unconnected messaging via UCMM (Unconnected Message Manager-one-time request/response) or Class 3 connections (cyclic request /response).
- With Implicitconnections, only application data is contained within the messages. Implicit data can be polled, cyclic, or COS (Change of State) messages. Implicit connections are either point-to-point (unicast) or one-to-many (multicast) connections. Implicit connections use UDP/IP.

## Devices
There are two classes of devices in a CIP network, adapters and scanners.

- Adapters are targets of real-time I/O data connection. Adapters cannot send or receive real-time data unless requested to do so by a scanner device. Adapters can exchange data by using explicit messages with any class of devices but cannot originate a connection.
- Scanners are originators of I/O data connection requests and originators or targets of explicit connection requests.

# telegram size
PROFINET networks achieve speeds of 100 Mbit/s or even 1 Gbit/s and higher. The telegram size can be up to 1440 bytes, and there are no limits on the address space. Although the specification does not limit the address space, individual controllers will have restrictions based on their processor and memory. With multiple telegrams: up to 2^32-65 (acyclic) - telegram size.

# Explicit Messaging
## eipReadAttr
显示消息读取，输入的字节数组可以与instance长度不一致，如果字节数组短，则后面的数据会被截取掉。
## eipWriteAttr
显示消息写入，输入的字节数组必须与instance长度一致，不一致会报错。