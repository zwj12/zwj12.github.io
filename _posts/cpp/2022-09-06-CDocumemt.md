---
layout: post
title: "CDocument"
date: 2022-09-06 14:55:00 +0800
author: Michael
categories: CPP
---

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

# 强制更新视图
	void CMyDoc::OnFileNew()
	{
		this->str = _T("Hello World");
		this->UpdateAllViews(NULL);
	}

	void CMyView::OnDraw(CDC* pDC)
	{
		// TODO: Add your specialized code here and/or call the base class
		CMyDoc * cmyDoc=(CMyDoc*) this->m_pDocument;
		pDC->TextOut(100, 100, cmyDoc->str);
	}