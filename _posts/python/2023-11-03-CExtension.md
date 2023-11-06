---
layout: post
title: "C++ Extension for Python"
date: 2023-11-03 12:54:00 +0800
author: Michael
categories: Python
---

# Sample codes of using CPython extensions
1. Python约定形式的函数定义和实现 PyObject* <func-name>(PyObject* , PyObject* o)
2. 函数结构信息列表变量 <module-name>_methods[]
3. 模块结构信息变量 <module-name>_module 
4. 模块初始化函数: PyInit_<module-name>

    #include <Python.h>
    #include <Windows.h>
    #include <cmath>

    const double e = 2.7182818284590452353602874713527;

    double sinh_impl(double x) {
        return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x));
    }

    double cosh_impl(double x) {
        return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x));
    }

    //double tanh_impl(double x) {
    //    return sinh_impl(x) / cosh_impl(x);
    //}

    PyObject* tanh_impl(PyObject* self, PyObject* o) {
        double x = PyFloat_AsDouble(o);
        double tanh_x = sinh_impl(x) / cosh_impl(x);
        return PyFloat_FromDouble(tanh_x);
    }

    static PyMethodDef superfastcode_methods[] = {
        // The first property is the name exposed to Python, fast_tanh
        // The second is the C++ function with the implementation
        // METH_O means it takes a single PyObject argument
        { "fast_tanh", (PyCFunction)tanh_impl, METH_O, nullptr },

        // Terminate the array with an object containing nulls.
        { nullptr, nullptr, 0, nullptr }
    };

    static PyModuleDef superfastcode_module = {
        PyModuleDef_HEAD_INIT,
        "superfastcode",                        // Module name to use with Python import statements
        "Provides some functions, but faster",  // Module description
        0,
        superfastcode_methods                   // Structure that defines the methods of the module
    };

    PyMODINIT_FUNC PyInit_superfastcode() {
        return PyModule_Create(&superfastcode_module);
    }