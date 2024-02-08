---
layout: post
title: "PyObjectConvert"
date: 2024-02-05 12:54:00 +0800
author: Michael
categories: Python
---

# Long
    int PyLong_Check(PyObject *p)
    PyObject *PyLong_FromLong(long v)
    long PyLong_AsLong(PyObject *obj)

# Tuple
    int PyTuple_Check(PyObject *p)
    Py_ssize_t PyTuple_Size(PyObject *p)
    PyObject *PyTuple_New(Py_ssize_t len)
    int PyTuple_SetItem(PyObject *p, Py_ssize_t pos, PyObject *o)
    PyObject *PyTuple_GetItem(PyObject *p, Py_ssize_t pos)

    PyObject* pArgs = PyTuple_New(2);
    PyObject* pValue = PyLong_FromLong(2);
    PyTuple_SetItem(pArgs, 0, pValue);
    pValue = PyLong_FromLong(3);
    PyTuple_SetItem(pArgs, 1, pValue);

# Py_DECREF
当函数的返回值是New reference时，需要对PyObject * 变量使用Py_DECREF()，返回值是 Borrowed reference时，无需使用Py_DECREF()。

# Reference Counts 引用计数
Reference Counts counts how many different places there are that have a strong reference to an object. When the last strong reference to an object is released (i.e. its reference count becomes zero), the object is deallocated. Reference counts are always manipulated explicitly. The normal way is to use the macro Py_INCREF() to take a new reference to an object (i.e. increment its reference count by one), and Py_DECREF() to release that reference (i.e. decrement the reference count by one). 

# 引用形式
Python有三种引用形式，分别为 “New”, “Stolen” 和“Borrowed” 引用。When a function passes ownership of a reference on to its caller, the caller is said to receive a new reference. When no ownership is transferred, the caller is said to borrow the reference. Conversely, when a calling function passes in a reference to an object, there are two possibilities: the function steals a reference to the object, or it does not. Stealing a reference means that when you pass a reference to a function, that function assumes that it now owns that reference, and you are not responsible for it any longer.  当一个函数将引用所有权转给其调用方时，则称调用方收到一个 新的 引用。 当未转移所有权时，则称调用方是 借入 这个引用。 对于 borrowed reference 来说不需要任何额外操作。相反地，当调用方函数传入一个对象的引用时，存在两种可能：该函数 窃取 了一个对象的引用，或是没有窃取。 窃取引用 意味着当你向一个函数传入引用时，该函数会假定它拥有该引用，而你将不再对它负有责任。

## New引用
通过Python C Api创建出的PyObject，调用者对该PyObject具有完全的所有权。针对于New引用的PyObject，有如下两种选择。否则，就会出现内存泄漏。
- 使用完成后，调用Py_DECREF将其释放掉。
- 将引用通过函数返回值等形式传递给上层调用函数，但是接收者必须负责最终的Py_DECREF调用。

        PyObject *PyLong_FromLong(long v)
        Return value: New reference. Part of the Stable ABI.

        static PyObject *subtract_long(long a, long b) {
            PyObject *pA, *pB, *r;
        
            pA = PyLong_FromLong(a);        /* pA: New reference. */
            pB = PyLong_FromLong(b);        /* pB: New reference. */
            r = PyNumber_Subtract(pA, pB);  /*  r: New reference. */
            Py_DECREF(pA);                  /* My responsibility to decref. */
            Py_DECREF(pB);                  /* My responsibility to decref. */
            return r;                       /* Callers responsibility to decref. */
        }

## Stolen引用
当创建的PyObject传递给其他的容器，例如PyTuple_SetItem、PyList_SetItem。需要注意PyDict_SetItem内部会引用计数加一。

    int PyList_SetItem(PyObject *list, Py_ssize_t index, PyObject *item)
    Part of the Stable ABI.
    Set the item at index index in list to item. Return 0 on success. If index is out of bounds, return -1 and set an IndexError exception.

    Note This function “steals” a reference to item and discards a reference to an item already in the list at the affected position.


    static PyObject *make_tuple(void) {
        PyObject *r;
        PyObject *v;
    
        r = PyTuple_New(3);         /* New reference. */
        v = PyLong_FromLong(1L);    /* New reference. */
        /* PyTuple_SetItem "steals" the new reference v. */
        PyTuple_SetItem(r, 0, v);
        /* This is fine. */
        v = PyLong_FromLong(2L);
        PyTuple_SetItem(r, 1, v);
        /* More common pattern. */
        PyTuple_SetItem(r, 2, PyUnicode_FromString("three"));
        return r; /* Callers responsibility to decref. */
    }

## Borrowed引用
Borrowed 引用的所有者不应该调用 Py_DECREF()，使用Borrowed 引用在函数退出时不会出现内存泄露。但是不要让一个对象处理未保护的状态Borrowed 引用，如果对象处理未保护状态，它随时可能会被销毁。例如：从一个 list 获取对象，继续操作它，但并不递增它的引用。PyList_GetItem 会返回一个 borrowed reference ，所以 item 处于未保护状态。一些其他的操作可能会从 list 中将这个对象删除（递减它的引用计数，或者释放它），导致 item 成为一个悬垂指针。通过查看Python手册可以确定函数返回对象是否是Borrowed reference。

In Python’s C API, a borrowed reference is a reference to an object, where the code using the object does not own the reference. It becomes a dangling pointer if the object is destroyed. For example, a garbage collection can remove the last strong reference to the object and so destroy it. Calling Py_INCREF() on the borrowed reference is recommended to convert it to a strong reference in-place, except when the object cannot be destroyed before the last usage of the borrowed reference. The Py_NewRef() function can be used to create a new strong reference.

    PyObject *PyTuple_GetItem(PyObject *p, Py_ssize_t pos)
    Return value: Borrowed reference. Part of the Stable ABI.

    bug(PyObject *list) {
        PyObject *item = PyList_GetItem(list, 0);
        PyList_SetItem(list, 1, PyInt_FromLong(0L));
        PyObject_Print(item, stdout, 0); /* BUG! */
    }
    
    no_bug(PyObject *list) {
        PyObject *item = PyList_GetItem(list, 0);
        Py_INCREF(item); /* Protect item. */
        PyList_SetItem(list, 1, PyInt_FromLong(0L));
        PyObject_Print(item, stdout, 0);
        Py_DECREF(item);
    }