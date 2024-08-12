---
layout: post
title: "Wireshark"
date: 2021-11-02 12:25:00 +0800
author: Michael
categories: Develop
---

# Wireshark抓包对应OSI七层协议模型
1. Frame: 物理层的数据帧概况
2. Ethernet II: 数据链路层以太网帧头部信息
3. Internet Protocol Version 4: 互联网层IP包头部信息
4. Transmission Control Protocol: 传输层的数据段头部信息，此处是TCP
5. Hypertext Transfer Protocol: 应用层的信息，此处是HTTP协议

![日志文件夹](/assets/develop/WiresharkOSIModel.png)  

# Wireshare数据包过滤
- 查找目的地址为192.168.101.8的数据包: ip.dst==192.168.101.8
- 查找源地址: ip.src==1.1.1.1
- 过滤80端口: tcp.port==80
- 过滤协议: http
- 过滤get包: http.request.method=="GET"

![日志文件夹](/assets/develop/WiresharkFilter.png)  

# 查看原始TCP流
右击任意一个TCP包选择Follow TCP Stream就可以查看原始的TCP流。  
![日志文件夹](/assets/develop/WiresharkFollowTCPStreamMenu.png)  
![日志文件夹](/assets/develop/WiresharkFollowTCPStream.png)  

# TCP Socket
一个TCP数据包分为TCP首部和数据部分，TCP中没有表示包长度和数据长度的字段。可由IP层获知TCP的包长，由TCP的包长可知数据的长度。TCP在协议头中使用大量的标志位来控制连接状态，其中最主要的是SYN（创建一个连接），FIN（终结一个连接），ACK（确认接收到的数据）三个标志位。

![日志文件夹](/assets/develop/TCPPackageHeader.png)  

## 源端口号（Source Port）
表示发送端端口号，字段长16位。
## 目标端口号（Destination Port）
表示接收端端口号，字段长度16位。
## 序列号（Sequence Number）
字段长32位。序列号（有时也叫序号）是指发送数据的位置。每发送一次数据，就累加一次该数据字节数的大小。序列号不会从0或1开始，而是在建立连接时由计算机生成的随机数作为其初始值，通过SYN包传给接收端主机。然后再将每转发过去的字节数累加到初始值上表示数据的位置。此外，在建立连接和断开连接时发送的SYN包和FIN包虽然并不携带数据，但是也会作为一个字节增加对应的序列号。当开始一个 TCP 会话时，此时 SYN 位为 1，会生成一个随机的 Sequence number，后续使用 Sequence number 则从 Sequence number + 1 开始。
其他时候，则表示为 data 部分第一位的位置，值为此位数据的 Sequence number ，即基于初始 Sequence number + 1 + offset。其实很好理解，我们先抛开第一次生成的 Sequence number，后续的 TCP 头中的 Sequence number 都指的是 data 部分第一位的序号。比如：我这次发送的 Sequence number 为 100，数据长度为 100，那么我下一次发送的 Sequence number 就应该是 200，再假定数据长度为 50，如果要进行第三次发送，那么 Sequence number 的值应为 250。TCP头 并不计入Length 

![日志文件夹](/assets/develop/TCPSequenceNumber.png)  

## 确认应答号（Acknowledgement Number）
确认应答号字段长度32位。是指下一次应该收到的数据的序列号。实际上，它是指已收到确认应答号减一为止的数据。发送端收到这个确认应答以后可以认为在这个序号以前的数据都已经被正常接收。回复收到的最大 Sequence number + 1，表示期望收到的 Sequence number 的值。比如收到 Sequence number 为 100，数据长度为 100，那么我们就回复Acknowledgement number = 200。

![日志文件夹](/assets/develop/TCPDataPackage.png)  

## 数据偏移(Data offset)
4位，显示头部中32位字的数量，也称为头部长度

## 保留数据(Reserved data)
6位，保留字段，始终设置为零

## 控制位标志(Control bit Flags)
TCP使用9位控制标志来管理特定情况下的数据流
- URG: 与后面的紧急指针字段相关，当设置了此位时，数据应被视为优先于其他数据。
- ACK: 与ACK相关，确认字段用于指示已成功接收到的数据量，如果设置了此字段，说明发送方期望接收方继续发送下一个TCP段
- PSH: 推送功能，表示发送方希望接收方立即传输数据，而不必等到整个TCP段的数据都准备好再传输
- RST: 重置连接，仅在存在无法恢复的错误时使用
- SYN: 同步序列号，此标志用于设置初始序列号
- FIN: 完成位用于结束TCP连接，因为TCP是全双工连接，所以双方都必须使用FIN位来结束连接

![日志文件夹](/assets/develop/TCPRST.png)  

## 窗口(Window)
16位，指定接收方愿意接收多少字节

## 校验和(Checksum)
16位，用于对头部和数据进行错误检查

## 紧急指针(Urgent Pointer)
如果设置了URG控制标志，该值表示与序列号的偏移，指示最后一个紧急数据字节

## 选项(Options)
可选，长度可为0~320位之间的任意大小

# 三次握手（three-way handshake）与四次挥手（four-way handshake）
## TCP三次握手的三个数据包(SYN, SYN/ACK, ACK)
1. 第一个数据包的状态为SYN
2. 第二个数据包的状态为SYN/ACK, 设置2个标志位，ACK用来确认收到客户端的SYN包，SYN用来表明服务端也希望建立TCP连接
3. 第三个数据包的状态为ACK，连续3个数据包代表完成了最初的TCP 3次握手

![日志文件夹](/assets/develop/TCPThreeWayHandshake.png)  

## TCP四次挥手的数据包
1. 第一个数据包，服务端发送FIN给客户端，FIN=1， ACK=1
2. 第二个数据包，客户端向服务器发送一个ACK号，确认服务器的FIN请求
3. 第三个数据包，TCP是一种全双工连接，因此，客户端也向服务器发送一条消息以关闭连接
4. 第四个数据包，服务器向客户端发送一个ACK号，确认客户端的FIN请求

![日志文件夹](/assets/develop/TCPFourWayHandshake.png)  
![日志文件夹](/assets/develop/TCPState.png)  

# TCP序列号和确认号
## 三次握手
- 第1步：客户端向服务器发送一个同步数据包请求建立连接，该数据包中，初始序列号（ISN）是客户端随机产生的一个值，确认号是0；
- 第2步：服务器收到这个同步请求数据包后，会对客户端进行一个同步确认。这个数据包中，序列号（ISN）是服务器随机产生的一个值，确认号是客户端的初始序列号+1；
- 第3步：客户端收到这个同步确认数据包后，再对服务器进行一个确认。该数据包中，序列号是第2步中，也就是同步请求确认数据包中的确认号值，确认号是服务器的初始序列号+1。
## 数据传输
- 初始序列号随机产生，后续序列号为上一个数据包(对方发送的数据包)的确认号。
- 确认号为上一个对方发送过来的数据包中的序列号+长度Len
- 如果连续发送多个数据包：确认号同样是2中的ACK号，不变；序列号为本地发送的上一个数据包(自己发送的数据包)的序列号+长度Len

