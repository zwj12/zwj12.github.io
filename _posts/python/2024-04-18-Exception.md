---
layout: post
title: "Exception"
date: 2024-04-18 12:54:00 +0800
author: Michael
categories: Python
---

# sys.excepthook
sys.excepthook 是Python中的一个全局函数，它在脚本遇到未捕获的异常时被调用。
默认情况下，当一个异常没有被任何 try-except 块捕获时，Python会调用 sys.excepthook，打印出异常信息以及堆栈跟踪。

1. 允许在程序的任何地方捕获未被处理的异常；使用起来相对简单。
2. 不能阻止程序因未处理的异常而终止；只能用于处理未被 try-except 块捕获的异常。


        import sys

        def test_func4():
            temp = 1 / 0
            return temp

        def test_func5():
            test_func4()

        def custom_excepthook(ttype, tvalue, ttraceback):
            print("Process exception by sys.excepthook")
            # print(f'ttype:{ttype}, tvalue:{tvalue}')
            # index = 1
            # while ttraceback:
            #     print(f"call stack: at index:{index}")
            #     traceback_code = ttraceback.tb_frame.f_code
            #     print(f"    file_name: {traceback_code.co_filename}")
            #     print(f"    func/module_name: {traceback_code.co_name}")
            #     ttraceback = ttraceback.tb_next
            #     index += 1


        if __name__ == '__main__':
            sys.excepthook = custom_excepthook
            test_func5()
            try:
                test_func5()
            except Exception:
                print("Catch exception by try")

# example
    try:
        a = float("3.15a")
        print(a)
    except Exception as ex:
        print(f"Unexpected {ex=}, {type(ex)=}")