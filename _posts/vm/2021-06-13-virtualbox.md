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

	//For Windows
	sdelete64 -z c:\
	VBoxManage.exe modifyhd "D:\105 Virtual machine\Win7VisualStudio2008\Win7VisualStudio2008.vdi" --compact

# 修改UUID
	C:\Program Files\Oracle\VirtualBox>VBoxManage internalcommands sethduuid "D:\105 Virtual machine\Win7EPLAN\Win7EPLAN.vdi"
	UUID changed to: 43932de1-3135-4145-a056-9207d3fadb5f

# 启用嵌套VT-x/AMD-V复选框灰色
	C:\Program Files\Oracle\VirtualBox>vboxmanage.exe list vms
	"Win7Test" {892b7e0a-6523-4beb-9026-bc24d8bbdc4e}
	"Win10Test" {e0e3ab0f-6c16-4f73-a640-9ee3879e124f}
	
	C:\Program Files\Oracle\VirtualBox>vboxmanage.exe modifyvm "Win10Test" --nested-hw-virt on