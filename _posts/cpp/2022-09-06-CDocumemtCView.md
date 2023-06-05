---
layout: post
title: "CDocument CView"
date: 2022-09-06 14:55:00 +0800
author: Michael
categories: CPP
---

# CCreateContext 
当创建视图时，MFC使用CCreateContext结构体把视图，文档进行关联。The framework uses the CCreateContext structure when it creates the frame windows and views that are associated with a document. A CCreateContext structure contains pointers to the document, the frame window, the view, and the document template. A view should not be created for a nonexistent document. All of the pointers in CCreateContext are optional and can be NULL if unspecified or unknown.

## Member
- m_pNewViewClass：CRuntimeClass*
- m_pCurrentDoc：CDocument*
- m_pNewDocTemplate: CDocTemplate*
- m_pLastView: CView*
- m_pCurrentFrame: CFrameWnd*

## Related Function
CDocTemplate::CreateNewFrame() -> CFrameWnd::LoadFrame() -> CFrameWnd::Create() -> CMainFrame::OnCreate() -> CMainFrame::OnCreateClient() -> CFrameWnd::CreateView() -> pContext->m_pNewViewClass->CreateObject() -> CWnd::Create()

- CFrameWnd::Create()
- CFrameWnd::LoadFrame()
- CFrameWnd::OnCreateClient()
- CSplitterWnd::Create()
- CSplitterWnd::CreateView()
- CWnd::Create()

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

# CDocument::AddView
Call this function to attach a view to the document. This function adds the specified view to the list of views associated with the document; the function also sets the view's document pointer to this document. The framework calls this function when attaching a newly created view object to a document; this occurs in response to a File New, File Open, or New Window command or when a splitter window is split. Call this function only if you are manually creating and attaching a view. 