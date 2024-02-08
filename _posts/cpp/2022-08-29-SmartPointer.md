---
layout: post
title: "smart pointer"
date: 2022-08-29 10:12:00 +0800
author: Michael
categories: CPP
---

# 智能指针
智能指针就是帮我们C++程序员管理动态分配的内存的，它会帮助我们自动释放new出来的内存，从而避免内存泄漏！C++智能指针是包含重载运算符的类，其行为像常规指针，但智能指针能够及时、妥善地销毁动态分配的数据，并实现了明确的对象生命周期。

# auto_ptr
auto_ptr 是c++ 98定义的智能指针模板，其定义了管理指针的对象，可以将new 获得（直接或间接）的地址赋给这种对象。当对象过期时，其析构函数将使用delete 来释放内存！

auto_ptr是用于C++11之前的智能指针。由于 auto_ptr 基于排他所有权模式：两个指针不能指向同一个资源，复制或赋值都会改变资源的所有权。auto_ptr 主要有三大问题：

1. 复制和赋值会改变资源的所有权，不符合人的直觉。
1. 在 STL 容器中使用auto_ptr存在重大风险，因为容器内的元素必需支持可复制（copy constructable）和可赋值（assignable）。
1. 不支持对象数组的操作

# unique_ptr 
C++11用更严谨的unique_ptr 取代了auto_ptr。它持有对对象的独有权，即两个 unique_ptr 不能指向一个对象，不能进行复制操作只能进行移动操作。unique_ptr 之所以叫这个名字，是因为它只能指向一个对象，即当它指向其他对象时，之前所指向的对象会被摧毁。其次，当 unique_ptr 超出作用域时，指向的对象也会被自动摧毁，帮助程序员实现了自动释放的功能。unique_ptr 也可能还未指向对象，这时的状态被称为 empty。

    unique_ptr<int> pInt(new int(5));
    cout << *pInt;

    std::unique_ptr<int>p1(new int(5));
    std::unique_ptr<int>p2=p1;// 编译会出错
    std::unique_ptr<int>p3=std::move(p1);// 转移所有权, 现在那块内存归p3所有, p1成为无效的针.
    p3.reset();//释放内存.
    p1.reset();//无效

# shared_ptr
可以记录引用特定内存对象的智能指针数量，当复制或拷贝时，引用计数加1，当智能指针析构时，引用计数减1，如果计数为零，代表已经没有指针指向这块内存，那么我们就释放它！这就是 shared_ptr 采用的策略！

    //1
    auto sp1 = make_shared<int>(100);
    //2
    shared_ptr<int> sp1 = make_shared<int>(100);
    //3
    shared_ptr<int> sp1(new int(100));
    //err
    shared_ptr<int> p = new int(1);

# weak_ptr

# shared_ptr、unique_ptr以及weak_ptr
- shared_ptr允许多个指针指向同一个对象 
- unique_ptr则“独占”所指向的对象
- weak_ptr则是一种弱引用，指向shared_ptr所管理的对象

# static_pointer_cast
静态指针类型转换，指针是shared_ptr类型的，对于普通指针是无效的。

    auto userData = static_pointer_cast<UserData>(msg->msg);