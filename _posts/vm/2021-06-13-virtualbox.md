---
layout: post
title: "VirtualBox"
date: 2021-06-13 08:20:00 +0800
author: Michael
categories: VM
---

# 压缩
	//For Linux
	sudo dd if=/dev/zero of=zero.fill
	sudo rm -f zero.fill
	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyhd Ubuntu.vdi --compact

	//For Windows, sdelete64命令需要在子系统中运行
	sdelete64 -z c:\
	VBoxManage.exe modifyhd "H:\VirtualOS\Win10Test\Win10Test.vdi" --compact

# 修改UUID
	C:\Program Files\Oracle\VirtualBox>VBoxManage internalcommands sethduuid "D:\105 Virtual machine\Win10StandardOri\Win10StandardOri.vdi"
	UUID changed to: 43932de1-3135-4145-a056-9207d3fadb5f

# 启用嵌套VT-x/AMD-V复选框灰色
	C:\Program Files\Oracle\VirtualBox>.\vboxmanage.exe list vms
	"Win7Test" {892b7e0a-6523-4beb-9026-bc24d8bbdc4e}
	"Win10Test" {e0e3ab0f-6c16-4f73-a640-9ee3879e124f}
	
	C:\Program Files\Oracle\VirtualBox>.\vboxmanage.exe modifyvm "Win10Test" --nested-hw-virt on

# 虚拟系统Win10激活
虚拟机系统如果需要激活，需要使用桥接网卡方式联网，如果使用NAT方式联网激活，会导致激活失败。  
![日志文件夹](/assets/windows/ActivateWin10InVirtualOKByBridgedAdapter.png)  

# Import Virtual Appliance
导入VirtualBox的ova文件时，需要修改名称，磁盘名称，文件夹位置等参数。  
![日志文件夹](/assets/vm/ImportVirtualAppliance.png)  

# 网络设置
## NAT模式
1. 如果主机可以上网，虚拟机可以上网
2. 虚拟机之间不能ping通
3. 虚拟机可以ping通主机（此时ping虚拟机的网关，即是ping主机）
4. 主机不能ping通虚拟机

## Bridged Adapter模式（桥接模式）
1. 如果主机可以上网，虚拟机可以上网
2. 虚拟机之间可以ping通
3. 虚拟机可以ping通主机
4. 主机可以ping通虚拟机

## Host-only Adapter模式
除了不能上网，虚拟机间，主机均可通信，相当于接了一个192.168.56.100的路由器，主机地址为192.168.56.1，虚拟机地址为192.168.56.100。如果不需要上网，推荐使用该模式。

1. 虚拟机不可以上网
2. 虚拟机之间可以ping通
3. 虚拟机可以ping通主机（注意虚拟机与主机通信是通过主机的名为VirtualBox Host-Only Network的网卡，因此ip是该网卡ip 192.168.56.1，而不是你现在正在上网所用的ip）
4. 主机可以ping通虚拟机

## Internal模式（内网模式）
只有虚拟机间可以通信。

1. 虚拟机不可以上网
2. 虚拟机之间可以ping通
3. 虚拟机不能ping通主机
4. 主机不能ping通虚拟机