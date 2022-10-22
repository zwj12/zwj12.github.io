---
layout: post
title: "CSplitterWnd"
date: 2022-09-30 16:12:00 +0800
author: Michael
categories: CPP
---

# 单文档窗口分割
1. 在父框架中嵌入 CSplitterWnd 成员变量。
2. 替代父框架的 OnCreateClient 成员函数。
3. 从已替代的 CFrameWnd::OnCreateClient 中调用 CreateStatic 成员函数。

	//MainFrm.h
	protected:
		CSplitterWnd m_wndSplitter;

	//MainFrm.cpp
	BOOL CMainFrame::OnCreateClient(LPCREATESTRUCT lpcs, CCreateContext* pContext)
	{
		// TODO: Add your specialized code here and/or call the base class
	
		m_wndSplitter.CreateStatic(this, 1, 2);
		m_wndSplitter.CreateView(0, 0, RUNTIME_CLASS(CMFCRoboticsView), CSize(190, 600), pContext);
		m_wndSplitter.CreateView(0, 1, RUNTIME_CLASS(CMFCRoboticsView), CSize(520, 600), pContext);
	
		return TRUE;
		//return CFrameWnd::OnCreateClient(lpcs, pContext);
	}

# CSplitterWnd -> CWnd -> CCmdTarget -> CObject

# CreateStatic
创建几行几列的静态拆分器窗口，

	virtual BOOL CreateStatic(
	    CWnd* pParentWnd, //父框架窗口
	    int nRows, //行数
	    int nCols, // 列数
	    DWORD dwStyle = WS_CHILD | WS_VISIBLE, //窗口样式
	    UINT nID = AFX_IDW_PANE_FIRST); //嵌入到另一个拆分器的窗口

# CreateView
为静态拆分器窗口创建窗格

	virtual BOOL CreateView(
	    int row,
	    int col,
	    CRuntimeClass* pViewClass, //CView视图类
	    SIZE sizeInit, //初始大小，如果初始大小小于剩余的空间，则使用剩余的空间，如果初始大小大于最大的窗口大小，则使用窗口大小
	    CCreateContext* pContext);

# IdFromRowCol
获取位于指定行和列的窗格的子窗口 ID。

	int IdFromRowCol(
	    int row,
	    int col) const;