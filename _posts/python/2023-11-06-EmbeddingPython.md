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
可向 PyRun_SimpleFile() 传入一个 stdio 文件指针和一个文件名。文件名只是用来标识错误信息

    char filename[] = "michaeltest.py";
    FILE* fp;
    Py_Initialize();
    fp = fopen(filename, "r");
    PyRun_SimpleFile(fp, filename);
    Py_Finalize();

    Py_Initialize();
    PyRun_SimpleString("print('Hello World from Embedded Python!!!')");
    FILE *fp = fopen("C:\\Users\\CNMIZHU7\\Source\\repos\\UtilityTools\\PMTWUserScript\\UserScriptSample.py", "r");
    PyRun_SimpleFile(fp, "UserScriptSample");
    Py_Finalize();

# 运行 Python 脚本中定义的函数
## C++ codes

    Py_Initialize();
    PyRun_SimpleString("print('Hello World from Embedded Python!!!')");
    FILE *fp = fopen("C:\\Users\\CNMIZHU7\\Source\\repos\\UtilityTools\\PMTWUserScript\\UserScriptSample.py", "r");
    PyRun_SimpleFile(fp, "UserScriptSample");

    PyObject* pName, * pModule, * pFunc;
    PyObject* pArgs, * pValue;
    pName = PyUnicode_DecodeFSDefault("UserScriptSample");
    pModule = PyImport_Import(pName);
    //pModule = PyImport_ImportModule("UserScriptSample");
    Py_DECREF(pName);
    if (pModule != NULL) {
        pFunc = PyObject_GetAttrString(pModule, "multiply");
        if (pFunc && PyCallable_Check(pFunc)) {
            pArgs = PyTuple_New(2);
            pValue = PyLong_FromLong(2);           
            PyTuple_SetItem(pArgs, 0, pValue);
            pValue = PyLong_FromLong(3);
            PyTuple_SetItem(pArgs, 1, pValue);
            pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);
            if (pValue != NULL) {
                printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                Py_DECREF(pValue);
            }
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }

    Py_Finalize();

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

## Example 2
    int main(int argc, wchar_t** argv)
    { 
        PyStatus status;

        //PyPreConfig preconfig;
        //PyPreConfig_InitPythonConfig(&preconfig);
        //status = Py_PreInitialize(&preconfig);
        
        PyConfig config;
        //PyConfig_InitIsolatedConfig(&config);
        PyConfig_InitPythonConfig(&config);    
        status = PyConfig_SetString(&config, &config.pythonpath_env, L"C:\\Users\\CNMIZHU7\\Source\\repos\\UtilityTools\\PMTWUserScript;");
        status = Py_InitializeFromConfig(&config);

        //PyConfig_Read(&config);
        //printPythonPathConfiguration(&config, true);

        PyRun_SimpleString("print('Hello World from Embedded Python!!!')");
        //FILE *fp = fopen("C:\\Users\\CNMIZHU7\\Source\\repos\\UtilityTools\\PMTWUserScript\\UserScriptSample.py", "r");
        //PyRun_SimpleFile(fp, "UserScriptSample");

        PyObject* pName, * pModule, * pFunc;
        PyObject* pArgs, * pValue;
        pName = PyUnicode_DecodeFSDefault("UserScriptSample");
        pModule = PyImport_Import(pName);
        //pModule = PyImport_ImportModule("UserScriptSample");
        Py_DECREF(pName);
        if (pModule != NULL) {
            pFunc = PyObject_GetAttrString(pModule, "multiply");
            if (pFunc && PyCallable_Check(pFunc)) {
                pArgs = PyTuple_New(2);
                pValue = PyLong_FromLong(2);           
                PyTuple_SetItem(pArgs, 0, pValue);
                pValue = PyLong_FromLong(3);
                PyTuple_SetItem(pArgs, 1, pValue);
                pValue = PyObject_CallObject(pFunc, pArgs);
                Py_DECREF(pArgs);
                if (pValue != NULL) {
                    printf("Result of call: %ld\n", PyLong_AsLong(pValue));
                    Py_DECREF(pValue);
                }
            }
            Py_XDECREF(pFunc);
            Py_DECREF(pModule);
        }

        Py_Finalize();

        printf("\nPress any key to exit...\n");
        std::cin.get();
    }

## command

    ConsoleApplication1 michaeltest multiply 2 3

# Py_RunMain
启动Python

    int main(int argc, char** argv)
    {
        PyStatus status;

        PyConfig config;
        PyConfig_InitPythonConfig(&config);
        config.isolated = 1;

        /* Decode command line arguments.
        Implicitly preinitialize Python (in isolated mode). */
        status = PyConfig_SetBytesArgv(&config, argc, argv);
        if (PyStatus_Exception(status)) {
            goto exception;
        }

        status = Py_InitializeFromConfig(&config);
        if (PyStatus_Exception(status)) {
            goto exception;
        }
        PyConfig_Clear(&config);

        return Py_RunMain();

    exception:
        PyConfig_Clear(&config);
        if (PyStatus_IsExit(status)) {
            return status.exitcode;
        }
        /* Display the error message and exit the process with
        non-zero exit code */
        Py_ExitStatusException(status);
    }

# Py_SetPythonHome & PYTHONHOME & PyConfig.home
Py_SetPythonHome设置环境变量PYTHONHOME，改函数的功能和直接在操作系统中添加环境变量PYTHONHOME具有同样的功能，主要是指定Python的安装文件夹位置，默认为C:\Program Files\Python312，如果Python的安装位置不在默认位置，可以通过该函数修改。通过设置PyConfig.home也具有同样的作用

![日志文件夹](/assets/python/PYTHONHOME.png)  

# PYTHONPATH & PyConfig.pythonpath_env
环境变量PYTHONPATH用于设置额外的Python模块搜索路径。不能通过Py_SetPath设置该变量，Py_SetPath会覆盖所有的sys.path值。但是如果在编程时，修改了PyConfig.pythonpath_env，会忽略PYTHONPATH的值，把PyConfig.pythonpath_env的值添加到路径中。

![日志文件夹](/assets/python/PYTHONPATH.png)  

# Python path configuration
    int printPythonPathConfiguration(PyConfig *config) {
        
        wcout << "Python path configuration:" << endl;
        wcout << "  " << "PYTHONHOME" << " = '" << (config->home == NULL ? _T("(not set)") : config->home) << "'" <<  endl;
        wcout << "  " << "PYTHONPATH" << " = '" << (config->pythonpath_env == NULL? _T("(not set)"): config->pythonpath_env) << "'" << endl;
        wcout << "  " << "program name" << " = '" << config->program_name << "'" << endl;
        wcout << "  " << "isolated" << " = " << config->isolated << endl;
        wcout << "  " << "environment" << " = " << config->use_environment << endl;
        wcout << "  " << "user site" << " = " << config->user_site_directory << endl;
        wcout << "  " << "safe_path" << " = " << config->safe_path << endl;
        wcout << "  " << "import site" << " = " << config->site_import << endl;
        wcout << "  " << "is in build tree" << " = " << config->_is_python_build << endl;
        wcout << "  " << "stdlib dir" << " = '" << config->stdlib_dir << "'" << endl;

        //wcout << "  " << "sys._base_executable" << " = '" << (config->pythonpath_env == NULL ? _T("(not set)") : config->base_executable) << "'" << endl;
        //wcout << "  " << "sys.base_prefix" << " = '" << (config->pythonpath_env == NULL ? _T("(not set)") : config->base_prefix) << "'" << endl;
        //wcout << "  " << "sys.base_exec_prefix" << " = '" << (config->pythonpath_env == NULL ? _T("(not set)") : config->base_exec_prefix) << "'" << endl;
        //wcout << "  " << "sys.platlibdir" << " = '" << (config->pythonpath_env == NULL ? _T("(not set)") : config->platlibdir) << "'" << endl;

        //wcout << "  " << "sys.executable" << " = '" << config->executable << "'" << endl;
        //wcout << "  " << "sys.prefix" << " = '" << config->prefix << "'" << endl;
        //wcout << "  " << "sys.exec_prefix" << " = '" << config->exec_prefix << "'" << endl;
        //wcout << "  " << "sys.path" << " = '" << config->module_search_paths.items << "'" << endl;

    #define DUMP_SYS(NAME) \
            do { \
                obj = PySys_GetObject(#NAME); \
                PySys_FormatStderr("  sys.%s = ", #NAME); \
                if (obj != NULL) { \
                    PySys_FormatStderr("%A", obj); \
                } \
                else { \
                    PySys_WriteStderr("(not set)"); \
                } \
                PySys_FormatStderr("\n"); \
            } while (0)

        PyObject* obj;
        DUMP_SYS(_base_executable);
        DUMP_SYS(base_prefix);
        DUMP_SYS(base_exec_prefix);
        DUMP_SYS(platlibdir);
        DUMP_SYS(executable);
        DUMP_SYS(prefix);
        DUMP_SYS(exec_prefix);

        PyObject* sys_path = PySys_GetObject("path");  /* borrowed reference */
        if (sys_path != NULL && PyList_Check(sys_path)) {
            PySys_WriteStderr("  sys.path = [\n");
            Py_ssize_t len = PyList_GET_SIZE(sys_path);
            for (Py_ssize_t i = 0; i < len; i++) {
                PyObject* path = PyList_GET_ITEM(sys_path, i);
                PySys_FormatStderr("    %A,\n", path);
            }
            PySys_WriteStderr("  ]\n");
        }

        return 0;
    }

# Built-in Functions
    ascii(object)

# Py_DecodeLocale
Py_DecodeLocale is used to convert a string in the current locale to a wide string。

# base_executable & executable
base_executable and executable are fields in the PyConfig structure in Python's C API. They are used to specify the paths to the Python executable and the base Python executable, respectively. In Windows, these paths would typically point to the python.exe file in your Python installation directory.

# PyConfig_Read
PyConfig_Read is a function in Python's C API that reads the configuration from environment variables and command line arguments. 该函数不会从Python中读取，只是从命令行参数和系统环境变量中去读数据。使用方式是，先PyConfig_InitPythonConfig，然后PyConfig_Read，最后使用Py_InitializeFromConfig

    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);
    Py_SetPythonHome(L"C:\\Program Files\\Python312");
    PyConfig_Read(&config);
    status = Py_InitializeFromConfig(&config);

# PyConfig.isolated
如果该值为1，会忽略环境变量的值，包括PyConfig.pythonpath_env的值

# PyConfig.module_search_paths_set, PyConfig.module_search_paths
通过设置PyConfig.module_search_paths_set为，可以完全覆盖默认的sys.path值，注意，这里不是添加路径，而是完全修改路径，通常不建议使用该值添加额外的模块搜索路径，如果需要只是添加路径，请使用PyConfig.pythonpath_env。或者If you want to modify the default set of paths, finish initialization first and then use PySys_GetObject("path")

# PyThreadState_Get();
获取当前Python线程状态，必须获取到GIL时，才能运行该函数，否则直接报错。

    PyThreadState* _current = PyThreadState_Get();