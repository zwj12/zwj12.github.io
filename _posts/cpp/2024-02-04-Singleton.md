---
layout: post
title: "Singleton"
date: 2024-02-04 10:12:00 +0800
author: Michael
categories: CPP
---

# Singleton
- 饿汉模式（Eager Singleton），在程序启动后立刻构造单例；
- 懒汉模式（Lazy Singleton），在第一次调用前构造单例。

# 饿汉版
基于类的静态变量，实现饿汉版的单例模式
    class Singleton {
    protected:
        Singleton() { std::cout << "Singleton: call Constructor\n"; };

        static Singleton demo;  // declare
    public:
        Singleton(const Singleton &) = delete;
        Singleton &operator=(const Singleton &) = delete;

        ~Singleton() { std::cout << "Singleton: call Destructor\n"; }

        static Singleton &get_instance() { return demo; }
    };

# 懒汉版
基于类的静态函数的局部静态变量，实现懒汉版的单例模式，推荐用这个。

class Singleton {
protected:
    Singleton() { std::cout << "Singleton: call Constructor\n"; };

public:
    Singleton(const Singleton &) = delete;
    Singleton &operator=(const Singleton &) = delete;

    virtual ~Singleton() { std::cout << "Singleton: call Destructor\n"; }

    static Singleton &get_instance() {
        static Singleton demo;
        return demo;
    }
};