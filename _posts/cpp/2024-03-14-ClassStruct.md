---
layout: post
title: "Class & Struct"
date: 2024-03-14 10:12:00 +0800
author: Michael
categories: CPP
---

# 虚析构函数
虚析构函数是为了解决基类的指针指向派生类对象，并用基类的指针删除派生类对象。如果某个类不包含虚函数，那一般是表示它将不作为一个基类来使用。当一个类不准备作为基类使用时，使析构函数为虚一般是个坏主意。因为它会为类增加一个虚函数表，使得对象的体积翻倍，还有可能降低其可移植性。

# struct

    struct Student
    {
        int Code;
        char Name[20];
        char Sex;
        int Age;
    };
    struct Student Stu;