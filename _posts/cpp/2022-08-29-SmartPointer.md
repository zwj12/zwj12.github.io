---
layout: post
title: "smart pointer"
date: 2022-08-29 10:12:00 +0800
author: Michael
categories: CPP
---

# 智能指针
智能指针就是帮我们C++程序员管理动态分配的内存的，它会帮助我们自动释放new出来的内存，从而避免内存泄漏！

# auto_ptr
auto_ptr 是c++ 98定义的智能指针模板，其定义了管理指针的对象，可以将new 获得（直接或间接）的地址赋给这种对象。当对象过期时，其析构函数将使用delete 来释放内存！

auto_ptr是用于C++11之前的智能指针。由于 auto_ptr 基于排他所有权模式：两个指针不能指向同一个资源，复制或赋值都会改变资源的所有权。auto_ptr 主要有三大问题：

1. 复制和赋值会改变资源的所有权，不符合人的直觉。
1. 在 STL 容器中使用auto_ptr存在重大风险，因为容器内的元素必需支持可复制（copy constructable）和可赋值（assignable）。
1. 不支持对象数组的操作

# unique_ptr 
C++11用更严谨的unique_ptr 取代了auto_ptr！

# shared_ptr
可以记录引用特定内存对象的智能指针数量，当复制或拷贝时，引用计数加1，当智能指针析构时，引用计数减1，如果计数为零，代表已经没有指针指向这块内存，那么我们就释放它！这就是 shared_ptr 采用的策略！

# weak_ptr