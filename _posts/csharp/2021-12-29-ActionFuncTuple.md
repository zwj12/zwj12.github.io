---
layout: post
title: "Action & Func & Tuple"
date: 2021-12-29 10:52:00 +0800
author: Michael
categories: CSharp
---

# Action & Func & Predicate
1. Action用于没有返回值的方法（参数可以根据自己情况进行传递）
2. Func恰恰相反用于有返回值的方法（同样参数根据自己情况情况）
3. 记住无返回就用action，有返回就用Func
4. Predicate是返回bool型的泛型委托，Predicate<int>表示传入参数为int，返回bool的委托，
Predicate有且只有一个参数，返回值固定为bool

# 元组 
开发人员在元组和匿名类型之间进行选择时，需要考虑几个因素。 一般来说，如果不使用表达式树，并且你熟悉元组语法，请选择 ValueTuple，因为它们提供可灵活命名属性的值类型。 如果使用表达式树并且想要命名属性，请选择匿名类型。 否则，请使用 Tuple。

## Tuple<T1,T2> Class

    public void NewItemSourceCreated(Tuple<int, string, int> tuple)
    {

    }

## ValueTuple 和 Tuple
ValueTuple 是一个轻量级的值类型，并支持强命名，而 Tuple 是一个引用类型，总的来说，ValueTuple 要比 Tuple 拥有更高的性能，Tuple 中的属性是只读的，也就是说一旦创建好之后就不能进行变更了，而 ValueTuple 的属性就可以在创建之后进行修改。

    var author = (Id: 1, FirstName: "Joydip", LastName: "Kanjilal");

    static (int, string, string) GetAuthor()
    {
        return (Id: 1, FirstName: "Joydip", LastName: "Kanjilal");
    }