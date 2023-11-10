---
layout: post
title: "Embeeding Python"
date: 2023-11-06 12:54:00 +0800
author: Michael
categories: Python
---

# Sample Codes
    #define PY_SSIZE_T_CLEAN
    #include <Python.h>
    #include <iostream>

    int main()
    {
        PyObject* pInt;
        Py_Initialize();
        PyRun_SimpleString("print('Hello World from Embedded Python!!!')");
        Py_Finalize();
        printf("\nPress any key to exit...\n");
        std::cin.get();
        std::cout << "Hello World!\n";
        
    }

# PyRun_SimpleString()
可向 PyRun_SimpleString() 传入一个包含 Python 语句的字符串。

# PyRun_SimpleFile()
可向 PyRun_SimpleFile() 传入一个 stdio 文件指针和一个文件名。

    char filename[] = "michaeltest.py";
    FILE* fp;
    Py_Initialize();
    fp = fopen(filename, "r");
    PyRun_SimpleFile(fp, filename);
    Py_Finalize();

# 运行 Python 脚本中定义的函数
## C++ codes

    //ConsoleApplication1.exe
    #define PY_SSIZE_T_CLEAN
    #include <Python.h>

    int main(int argc, char* argv[])
    {
        PyObject* pName, * pModule, * pFunc;
        PyObject* pArgs, * pValue;
        int i;

        if (argc < 3) {
            fprintf(stderr, "Usage: call pythonfile funcname [args]\n");
            return 1;
        }

        Py_Initialize();
        pName = PyUnicode_DecodeFSDefault(argv[1]);
        /* Error checking of pName left out */

        pModule = PyImport_Import(pName);
        Py_DECREF(pName);

        if (pModule != NULL) {
            pFunc = PyObject_GetAttrString(pModule, argv[2]);
            /* pFunc is a new reference */

            if (pFunc && PyCallable_Check(pFunc)) {
                pArgs = PyTuple_New(argc - 3);
                for (i = 0; i < argc - 3; ++i) {
                    pValue = PyLong_FromLong(atoi(argv[i + 3]));
                    if (!pValue) {
                        Py_DECREF(pArgs);
                        Py_DECREF(pModule);
                        fprintf(stderr, "Cannot convert argument\n");
                        return 1;
                    }
                    /* pValue reference stolen here: */
                    PyTuple_SetItem(pArgs, i, pValue);
                }
                pValue = PyObject_CallObject(pFunc, pArgs);
                Py_DECREF(pArgs);
                if (pValue != NULL) {
                    printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                    Py_DECREF(pValue);
                }
                else {
                    Py_DECREF(pFunc);
                    Py_DECREF(pModule);
                    PyErr_Print();
                    fprintf(stderr, "Call failed\n");
                    return 1;
                }
            }
            else {
                if (PyErr_Occurred())
                    PyErr_Print();
                fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
            }
            Py_XDECREF(pFunc);
            Py_DECREF(pModule);
        }
        else {
            PyErr_Print();
            fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
            return 1;
        }
        if (Py_FinalizeEx() < 0) {
            return 120;
        }
        return 0;
    }

## python codes

    //michaeltest.py
    def multiply(a,b):
        print("Will compute", a, "times", b)
        c = 0
        for i in range(0, a):
            c = c + b
        return c

## command

    ConsoleApplication1 michaeltest multiply 2 3

# 对嵌入 Python 功能进行扩展
## C++ codes

    #define PY_SSIZE_T_CLEAN
    #include <Python.h>

    static int numargs = 0;

    /* Return the number of arguments of the application command line */
    static PyObject* emb_numargs(PyObject* self, PyObject* args)
    {
        if (!PyArg_ParseTuple(args, ":numargs"))
            return NULL;
        return PyLong_FromLong(numargs);
    }

    static PyMethodDef EmbMethods[] = {
        {"numargs", emb_numargs, METH_VARARGS,
        "Return the number of arguments received by the process."},
        {NULL, NULL, 0, NULL}
    };

    static PyModuleDef EmbModule = {
        PyModuleDef_HEAD_INIT, "emb", NULL, -1, EmbMethods,
        NULL, NULL, NULL, NULL
    };

    static PyObject* PyInit_emb(void)
    {
        return PyModule_Create(&EmbModule);
    }

    int main(int argc, char* argv[])
    {
        numargs = argc;
        PyImport_AppendInittab("emb", &PyInit_emb);

        PyObject* pName, * pModule, * pFunc;
        PyObject* pArgs, * pValue;
        int i;

        if (argc < 3) {
            fprintf(stderr, "Usage: call pythonfile funcname [args]\n");
            return 1;
        }

        Py_Initialize();
        pName = PyUnicode_DecodeFSDefault(argv[1]);
        /* Error checking of pName left out */

        pModule = PyImport_Import(pName);
        Py_DECREF(pName);

        if (pModule != NULL) {
            pFunc = PyObject_GetAttrString(pModule, argv[2]);
            /* pFunc is a new reference */

            if (pFunc && PyCallable_Check(pFunc)) {
                pArgs = PyTuple_New(argc - 3);
                for (i = 0; i < argc - 3; ++i) {
                    pValue = PyLong_FromLong(atoi(argv[i + 3]));
                    if (!pValue) {
                        Py_DECREF(pArgs);
                        Py_DECREF(pModule);
                        fprintf(stderr, "Cannot convert argument\n");
                        return 1;
                    }
                    /* pValue reference stolen here: */
                    PyTuple_SetItem(pArgs, i, pValue);
                }
                pValue = PyObject_CallObject(pFunc, pArgs);
                Py_DECREF(pArgs);
                if (pValue != NULL) {
                    printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                    Py_DECREF(pValue);
                }
                else {
                    Py_DECREF(pFunc);
                    Py_DECREF(pModule);
                    PyErr_Print();
                    fprintf(stderr, "Call failed\n");
                    return 1;
                }
            }
            else {
                if (PyErr_Occurred())
                    PyErr_Print();
                fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
            }
            Py_XDECREF(pFunc);
            Py_DECREF(pModule);
        }
        else {
            PyErr_Print();
            fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
            return 1;
        }
        if (Py_FinalizeEx() < 0) {
            return 120;
        }

        system("pause");
        return 0;
    }

## python codes

    import emb

    def multiply(a,b):
        print("Number of arguments", emb.numargs())
        print("Will compute", a, "times", b)
        c = 0
        for i in range(0, a):
            c = c + b
        return c

## command

    ConsoleApplication1 michaeltest multiply 2 3