---
layout: post
title: "Exception"
date: 2023-04-18 10:12:00 +0800
author: Michael
categories: CPP
---

# noexcept
c++2.0中，一条经典的规范是：尽可能地为一个函数加上noexcept声明，意味着程序员向编译器保证该函数不会发射异常。这个原因从直观上理解应该是：既然开发者确保此函数不会发射异常，那么编译器也就没有必要为处理这个”可能“发生的异常添加一些事先预备好的目标代码，这在一定程度上减少了函数编译后生成的目标代码。需要注意的是，如果承诺了func函数是不会抛出异常的，那么必须保证func调用的其他函数也是不会抛出异常的，否则无法保证func的noexcept性质。因此，我们可以百分百确定一个函数不会发射异常的情况是比较少见的！需要了解的是，c++11为所有类的析构函数都加上了“隐式”noexcept声明。

    void func()noexcept{}
    void func()noexcept(express){}
