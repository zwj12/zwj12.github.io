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

# C函数 
- 对模块级函数， self 参数指向模块对象；对于方法则指向对象实例。
- args 参数是指向一个 Python 的 tuple 对象的指针，其中包含参数。 每个 tuple 项对应一个调用参数。 

        static PyObject* spam_system(PyObject* self, PyObject* args)

# PyArg_ParseTuple()
检查参数类型并将其转换为 C 值。 它使用模板字符串确定需要的参数类型以及存储被转换的值的 C 变量类型。在所有参数都有正确类型且组成部分按顺序放在传递进来的地址里时，返回真(非零)。其在传入无效参数时返回假(零)。

# PyErr_SetString()
参数是异常对象和 C 字符串。 异常对象一般是像 PyExc_ZeroDivisionError 这样的预定义对象。 C 字符串指明异常原因，并被转换为一个 Python 字符串对象存储为异常的“关联值”。

# PyMethodDef
static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

# PyModuleDef
这个结构体必须在模块的初始化函数中传递给解释器。 初始化函数必须命名为 PyInit_name()，其中 name 是模块的名称，并且应该是模块文件中定义的唯一非 static 条目。

    static struct PyModuleDef spammodule = {
        PyModuleDef_HEAD_INIT,
        "spam",   /* name of module */
        NULL, /* module documentation, may be NULL */
        -1,       /* size of per-interpreter state of the module,
                    or -1 if the module keeps state in global variables. */
        SpamMethods
    };

# PyMODINIT_FUNC
模块初始化函数，当 Python 程序首次导入 spam 模块时，PyInit_spam() 将被调用。它将调用 PyModule_Create()，该函数会返回一个模块对象，并基于在模块定义中找到的表（一个 PyMethodDef 结构体的数组）将内置函数对象插入到新创建的模块中。 PyModule_Create() 返回一个指向它所创建的模块对象的指针。 它可能会会程度严重的特定错误而中止，或者在模块无法成功初始化时返回 NULL。 初始化函数必须将模块对象返回给其调用者，以便将其插入到 sys.modules 中。

    PyMODINIT_FUNC PyInit_spam(void)
    {
        return PyModule_Create(&spammodule);
    }