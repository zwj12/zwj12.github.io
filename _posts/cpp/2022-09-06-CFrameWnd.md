---
layout: post
title: "CFrameWnd "
date: 2022-09-06 14:55:00 +0800
author: Michael
categories: CPP
---

# Create & OnCreate
OnCreate是一个消息响应函数，是响应WM_CREATE消息的一个函数，而WM_CREATE消息是由Create函数调用的。在view类中，Create 是虚函数由框架调用，是用来“生成一个窗口的子窗口”。 而OnCreate 函数是用来“表示一个窗口正在生成”。一个窗口创建（Create）之后，会向操作系统发送WM_CREATE消息，OnCreate()函数主要是用来响应此消息的。因为在MFC里面用一种消息映射的机制来响应消息，也就是可以用函数来响应相应的消息。就拿CMainFrame类来说，当窗口创建后会产生WM_CREATE消息，我们可以在OnCreate函数里实现我们要在窗口里面增加的东西，例如按扭，状态栏，工具栏等。这些子窗口一般是定义成类中的一个成员变量，因为要保证生命周期。一般以m_开头来表示成员(member)。OnCreate()不产生窗口，只是在窗口显示前设置窗口的属性如风格、位置等，Create()负责注册并产生窗口。Create()不是对应于消息WM_CREATE的，OnCreate（）才是。Create()只用于产生窗口，像动态创建控件中的Create()一样。

# 拆分窗口
在OnCreateClient函数中，可以使用CSplitterWnd::CreateStatic()可以设置窗口为几行几列。

	CSplitterWnd split;

	BOOL CMyFrameWnd::OnCreateClient(LPCREATESTRUCT lpcs, CCreateContext* pContext)
	{
		// TODO: Add your specialized code here and/or call the base class
		split.CreateStatic(this, 1, 2);
		split.CreateView(0, 0, RUNTIME_CLASS(CMyView), CSize(100, 100), pContext);
		split.CreateView(0, 1, pContext->m_pNewViewClass, CSize(100, 100), pContext);
		m_pViewActive = (CView*)split.GetPane(0, 0);
		return true;
		//return CFrameWnd::OnCreateClient(lpcs, pContext);
	}