---
layout: post
title: "threading"
date: 2024-03-28 12:54:00 +0800
author: Michael
categories: Python
---

# 多线程
## Example 1
    import threading
    import time

    def print_numbers(start, end):
        i = start
        while i < end:
            time.sleep(1)
            print(i)
            i = i + 1

    thread = threading.Thread(target=print_numbers, args=(1, 6))
    thread.start()
    thread.join()

## Example 2
    import threading
    import time

    class UtilityClass:
        def incr(i):
            return i+1
            
    def print_numbers(start, end, utilityClass):
        i = start
        while i < end:
            time.sleep(1)
            print(i)
            i = utilityClass.incr(i)

    thread = threading.Thread(target=print_numbers, args=(1, 6, UtilityClass))
    thread.start()
    thread.join()

# threading.Thread
## __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
1. self: Thread对象
2. group: 暂时未使用
3. target：线程将要执行的目标函数
4. name: 线程名称
5. args: 目标函数的参数，以元组形式传递
6. kwargs: 目标函数的关键字参数，以字典形式传递
7. daemon: 当Thread对象上设置参数daemon=True时，这个时候当主线程结束后，由它创建的子线程也已经自动结束了。