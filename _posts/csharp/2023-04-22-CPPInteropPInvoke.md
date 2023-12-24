---
layout: post
title: "C++ Interop PInvoke"
date: 2023-04-22 10:36:00 +0800
author: Michael
categories: CSharp
---

# 查看非托管dll所有导出的函数

    dumpbin /exports c:\windows\system32\kernel32.dll | more

![日志文件夹](/assets/csharp/dumpbin.png)   
    
# DllImport
指示由非托管动态链接库 (DLL) 公开为静态入口点的特性化方法。

    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    public static extern int MessageBox(IntPtr hWnd, String text, String caption, uint type);

## EntryPoint
可以给函数的C#声明一个不同于非托管库中的名称。在非托管库中，方法的名称在EntryPoint字段中定义。

## CharSet
定义字符编码为ANSI还是Unicode。

## SetLastError
设置为true，可以使用Marshal.GetLastWin32Error()读取错误号。

    Win32Exception ex=new Win32Exception(Marshal.GetLastWin32Error());

# 编程建议原则
1. 通过DllImport导入的函数，建议设置为private
2. 创建一个同名的public函数，调用非托管函数，并读取错误号等操作

# 数据类型互操作封送处理行为
大多数数据类型在托管和非托管内存中都具有公共的表示形式，而且不需要互操作封送处理程序进行特殊处理。 这些类型称为 blittable 类型，因为它们在托管和非托管代码之间传递时不需要进行转换。从平台调用返回的结构必须是 blittable 类型。 平台调用不支持返回类型为 non-blittable 结构。对象引用不是 blittable 类型。 这包括本身是 blittable 的对象的引用数组。

以下 System 命名空间中的类型即是 blittable 类型：

- System.Byte
- System.SByte
- System.Int16
- System.UInt16
- System.Int32
- System.UInt32
- System.Int64
- System.UInt64
- System.IntPtr
- System.UIntPtr
- System.Single
- System.Double

Non-blittable 类型	描述

- System.Array	转换为 C 样式数组或 SAFEARRAY。
- System.Boolean	转换为 1、2 或 4 字节的值，true 表示 1 或 -1。
- System.Char	转换为 Unicode 或 ANSI 字符。
- System.Class	转换为类接口。
- System.Object	转换为变量或接口。
- System.Mdarray	转换为 C 样式数组或 SAFEARRAY。
- System.String	转换为空引用中的终止字符串或转换为 BSTR。
- System.Valuetype	转换为具有固定内存布局的结构。
- System.Szarray	转换为 C 样式数组或 SAFEARRAY。

# Platform invoke data types 数据类型转换

[数据类型转换](https://learn.microsoft.com/en-us/dotnet/framework/interop/marshalling-data-with-platform-invoke)

![日志文件夹](/assets/csharp/Platforminvokedatatypes.png)   

# Example
读取和修改*.ini配置文件

    [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);

    [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);

    StringBuilder strPATH_VBF30 = new StringBuilder(255);
    GetPrivateProfileString("PATH", "VBF30", "Michael", strPATH_VBF30, 255, @"C:\ProgramData\ABB\System\zenon6.ini");
    WritePrivateProfileString("PATH", "VBF30", "Michael", @"C:\ProgramData\ABB\System\zenon6.ini");

# FindWindowEx
在窗口列表中寻找与指定条件相符的第一个子窗口 。
- hwndParent：要查找的子窗口所在的父窗口的句柄，如果hwndParent为 0 ，则函数以桌面窗口为父窗口，查找桌面窗口的所有子窗口。
- hwndChildAfter ：子窗口句柄。查找从在Z序中的下一个子窗口开始。如果HwndChildAfter为NULL，查找从hwndParent的第一个子窗口开始。如果hwndParent 和 hwndChildAfter同时为NULL，则函数查找所有的顶层窗口及消息窗口。
- lpszClass：指向一个指定了类名的空结束字符串。
- lpszWindow：指向一个指定了窗口名（窗口标题）的空结束字符串。如果该参数为 NULL，则为所有窗口全匹配。

        [DllImport("user32.dll")]
        public static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, string lpszClass, string lpszWindow);

        Process notepadProccess = Process.Start("notepad");
        notepadProccess.WaitForInputIdle();
        IntPtr notepadTextbox = FindWindowEx(notepadProccess.MainWindowHandle, IntPtr.Zero, "Edit", null);
        SendMessage(notepadTextbox, WM_SETTEXT, 0, stringBuilder.ToString());

# FindWindow
FindWindow函数返回与指定字符串相匹配的窗口类名或窗口名的最顶层窗口的窗口句柄。这个函数不会查找子窗口。

    [DllImport("user32.dll", SetLastError = true)]
    public static extern IntPtr FindWindow(string lpClassName, string lpWindowName);

    IntPtr notepadTextbox = FindWindow(null, "Image Dialog.txt - Notepad");

# SendMessage
        [DllImport("user32.dll")]
        public static extern int SendMessage(IntPtr hWnd, int uMsg, int wParam, string lParam);