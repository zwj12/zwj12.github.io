---
layout: post
title: "VirtualBox"
date: 2021-06-13 08:20:00 +0800
author: Michael
categories: VM
---

# 压缩
	sudo dd if=/dev/zero of=zero.fill
	sudo rm -f zero.fill
	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyhd Ubuntu.vdi --compact