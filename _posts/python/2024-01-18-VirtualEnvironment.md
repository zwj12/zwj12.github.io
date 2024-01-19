---
layout: post
title: "Virtual Environment"
date: 2024-01-18 12:54:00 +0800
author: Michael
categories: Python
---

# Python虚拟环境
Python 之所以强大，除了语言本身的特性外，更重要的是拥有无所不及的第三方库。强大的软件库，让开发者将精力集中在业务上，而避免重复造轮子的浪费。但众多的软件库，形成了复杂的依赖关系，加上 Python2 和 Python3 旷日持久之争，对采用 Python 开发的项目造成了不少困扰，所以 Python 建议，通过虚拟环境工具为项目创建纯净的依赖环境。

Python 应用经常需要使用一些包第三方包或者模块，有时需要依赖特定的包或者库的版本，所以不能有一个能适应所有 Python 应用的软件环境，很多时候不同的 Python 应用所依赖的版本是冲突的，满足了其中一个，另一个则无法运行，解决这一问题的方法是 虚拟环境。虚拟环境是一个包含了特定 Python 解析器以及一些软件包的自包含目录，不同的应用程序可以使用不同的虚拟环境，从而解决了依赖冲突问题，而且虚拟环境中只需要安装应用相关的包或者模块，可以给部署提供便利。

# 原理
虚拟环境并不是什么新技术，主要是利用了操作系统中环境变量以及进程间环境隔离的特性。操作系统的环境变量可以为程序提供信息和做信息交换介质，进程可以共享操作系统中的环境变量，也可以为进程指定环境变量，其中 PATH 是很重要的环境变量，用于为操作系统和程序提供可执行文件的访问路径。Python 虚拟环境就是利用这个特性构建的，在激活虚拟环境之时，激活脚本会将当前命令行程序的 PATH 修改为虚拟环境的，这样执行命令就会在被修改的 PATH 中查找，从而避免了原本 PATH 可以找到的命令，从而实现了 Python 环境的隔离。

# sys.base_prefix & sys.prefix
base Python installation，Python安装目录，当不使用虚拟环境时，sys.base_prefix和sys.prefix相同；当使用虚拟环境时，sys.prefix会重新指向虚拟环境。

    sys.base_prefix = 'C:\\Program Files\\Python312'
    sys.prefix = 'C:\\Program Files\\Python312'

# sys.base_exec_prefix & sys.exec_prefix
当不使用虚拟环境时，sys.base_exec_prefix和sys.exec_prefix相同；当使用虚拟环境时，sys.exec_prefix会重新指向虚拟环境。

    sys.base_exec_prefix = 'C:\\Program Files\\Python312'
    sys.exec_prefix = 'C:\\Program Files\\Python312'