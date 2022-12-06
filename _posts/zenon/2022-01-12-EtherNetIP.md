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

# Zenon EtherNet/IP Setting file
C:\ProgramData\ABB\SQL2012\166e715b-e6a8-400a-86b0-6c7af6c69a0a\FILES\straton\PACK_ML\__K5BusEIPS.cfg

# 类(class)，实例(instance)，属性（attribute）
CIP对象由 类(class)，实例(instance)，属性（attribute）构成。每个类可以有多个实例，每个实例可以有多个属性。（举例：一个类叫做 男人。这个 男人 类可以有实例 王二狗，李铁柱。王二狗 可以包含属性年龄，身高，体重。在读取或写入的数据的时候，协议中就要申明要操作的是哪个类的哪个实例的哪个属性。）类（class）是一组代表相同系统组件的对象。实例（instance）是该类中的某个特定对象。每个实例可以有自己特有的属性。

- CIP 网络中的每个节点都有节点地址，在EtherNet/IP 网络中，该地址即为设备的IP地址。
- CIP中每个类，实例，属性都有其对应的ID (Class ID, Instance ID, Attribute ID)。
- CIP中使用服务代码来明确操作指令。
- 类ID分为两个部分，公共对象（范围：0x0000–0x0063, 0x00F0–0x02FF），厂家自定义对象（范围：0x0064–0x00C7, 0X0300-0X04FF）。其它范围为预留部分。
- 实例ID也分为两个部分，公共实例（范围：0x0001–0x0063,0x00C8-0x02FF），厂家自定义实例（范围：0x0064-0xxC7,0x0300-0x04FF）。其它范围为预留部分。
- 属性ID,公共属性（范围：0x0000–0x0063，0x0100–0x02FF，0x0500–0x08FF），厂家自定义属性（范围：0x0064–0x00C7，0x0300–0x04FF，0x000–0x0CFF）。