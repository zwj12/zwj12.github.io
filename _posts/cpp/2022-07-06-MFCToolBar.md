---
layout: post
title: "MFC ToolBar"
date: 2022-07-06 19:23:00 +0800
author: Michael
categories: CPP
---

# 创建menu
1. 创建工具栏资源
2. 定义CFrameWnd的成员变量

		CToolBar toolbar;
3. 在CMyFrameWnd::OnCreate中加载工具栏

		toolbar.CreateEx(this, TBSTYLE_FLAT, WS_CHILD | WS_VISIBLE | CBRS_ALIGN_TOP);
		toolbar.LoadToolBar(IDR_TOOLBAR1);
	

# 工具栏消息
	ON_COMMAND(ID_FILE_NEW,OnFileNew)

	void CMyFrameWnd::OnFileNew()
	{
		AfxMessageBox(_T("Hello Menu"));
	}

# 工具栏停靠
在CMyFrameWnd::OnCreate中设置

	toolbar.CreateEx(this, TBSTYLE_FLAT, WS_CHILD | WS_VISIBLE | CBRS_ALIGN_TOP);
	toolbar.LoadToolBar(IDR_TOOLBAR1);
	toolbar.EnableDocking(CBRS_ALIGN_ANY);
	this->EnableDocking(CBRS_ALIGN_ANY);
	this->DockControlBar(&toolbar, AFX_IDW_DOCKBAR_BOTTOM);