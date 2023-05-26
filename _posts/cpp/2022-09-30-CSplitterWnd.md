---
layout: post
title: "CSplitterWnd"
date: 2022-09-30 16:12:00 +0800
author: Michael
categories: CPP
---

# 创建
使用SDI模板创建，无需修改CView的基类。

# 单文档窗口分割
1. 在父框架CMainFrame中添加 CSplitterWnd 成员变量。
2. 重写父框架的 OnCreateClient 成员函数。
3. 在 CFrameWnd::OnCreateClient 中调用 CreateStatic 成员函数，分割窗口为多行多列。
4. 定义消息ID和消息处理函数，关联消息处理函数OnSelectViewChange

	//MainFrm.h

	#define NM_CAMERA (WM_USER+100)
	#define NM_ROBOTCONTROLLER (WM_USER+101)
	#define NM_OTHER (WM_USER+102)

	protected:
		CSplitterWnd m_wndSplitter;
		afx_msg LRESULT OnSelectViewChange(WPARAM wParam, LPARAM lParam);

	//MainFrm.cpp

	#include "CSelectView.h"
	#include "CCameraView.h"

	ON_MESSAGE(NM_CAMERA, OnSelectViewChange)
	ON_MESSAGE(NM_ROBOTCONTROLLER, OnSelectViewChange)
	ON_MESSAGE(NM_OTHER, OnSelectViewChange)

	BOOL CMainFrame::OnCreateClient(LPCREATESTRUCT lpcs, CCreateContext* pContext)
	{
		// TODO: Add your specialized code here and/or call the base class
	
		m_wndSplitter.CreateStatic(this, 1, 2);
		m_wndSplitter.CreateView(0, 0, RUNTIME_CLASS(CMFCRoboticsView), CSize(190, 600), pContext);
		m_wndSplitter.CreateView(0, 1, RUNTIME_CLASS(CMFCRoboticsView), CSize(520, 600), pContext);
	
		return TRUE;
		//return CFrameWnd::OnCreateClient(lpcs, pContext);
	}

	//手动创建一个新视图后，需要把该视图添加到文档类中
	LRESULT CMainFrame::OnSelectViewChange(WPARAM wParam, LPARAM lParam)
	{
		CCreateContext context;
		CDocument* pDoc = this->GetActiveView()->GetDocument();

		if (wParam == NM_CAMERA) {
			context.m_pNewViewClass = RUNTIME_CLASS(CCameraView);
			context.m_pCurrentFrame = this;
			context.m_pCurrentDoc = pDoc;
			context.m_pLastView = (CFormView*)m_wndSplitter.GetPane(0, 1);
			m_wndSplitter.DeleteView(0, 1);
			m_wndSplitter.CreateView(0, 1, RUNTIME_CLASS(CCameraView), CSize(520, 600), &context);
			CCameraView* pNewView = (CCameraView*)m_wndSplitter.GetPane(0, 1);
			m_wndSplitter.RecalcLayout();
			pNewView->OnInitialUpdate();
			m_wndSplitter.SetActivePane(0, 1);
		}

		return LRESULT();
	}

# CCreateContext
这是一个很重要的结构，在CMainFrame::OnCreateClient和CSplitterWnd::CreateView中需要设置正确的文档和视图类，特别是文档，这是把视图和文档关联的关键参数。

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
		
# 左侧菜单栏
基于CTreeView创建一个新类，该类需要引用头文件"afxcview.h"。
1. 重写基类函数OnInitialUpdate，添加菜单项
2. 重写菜单选择事件OnTvnSelchanged，向主框架窗口发送消息，消息参数包含需要切换的视图类型信息。

	#include "afxcview.h"

	private:
		CTreeCtrl* m_treeCtrl;
		CImageList m_imageList;

	void CSelectView::OnInitialUpdate()
	{
		CTreeView::OnInitialUpdate();

		// TODO: Add your specialized code here and/or call the base class

		HICON icon = AfxGetApp()->LoadIconW(IDR_MAINFRAME);
		m_imageList.Create(30, 30, ILC_COLOR32, 1, 1);
		m_imageList.Add(icon);

		m_treeCtrl = &GetTreeCtrl();
		m_treeCtrl->SetImageList(&m_imageList, TVSIL_NORMAL);

		m_treeCtrl->InsertItem(_T("Robotics"), 0, 0, NULL);
		m_treeCtrl->InsertItem(_T("Other"), 0, 0, NULL);
	}

	void CSelectView::OnTvnSelchanged(NMHDR* pNMHDR, LRESULT* pResult)
	{
		LPNMTREEVIEW pNMTreeView = reinterpret_cast<LPNMTREEVIEW>(pNMHDR);
		// TODO: Add your control notification handler code here
		*pResult = 0;

		HTREEITEM item = m_treeCtrl->GetSelectedItem();
		CString str = m_treeCtrl->GetItemText(item);

		if (str == _T("Cameras")) {
			::PostMessage(AfxGetMainWnd()->GetSafeHwnd(), NM_CAMERA, (WPARAM)NM_CAMERA, (LPARAM)0);
		}
		if (str == _T("Robotics")) {
			::PostMessage(AfxGetMainWnd()->GetSafeHwnd(), NM_ROBOTCONTROLLER, (WPARAM)NM_ROBOTCONTROLLER, (LPARAM)0);
		}
		else if (str == _T("Other")) {
			::PostMessage(AfxGetMainWnd()->GetSafeHwnd(), NM_OTHER, (WPARAM)NM_OTHER, (LPARAM)0);
		}
	}

![日志文件夹](/assets/cpp/CTreeViewWizard.png)  

# 右侧窗口栏

![日志文件夹](/assets/cpp/CFormViewWizard.png)  
