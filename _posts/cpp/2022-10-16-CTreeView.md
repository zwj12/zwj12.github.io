---
layout: post
title: "CTreeView"
date: 2022-10-16 14:12:00 +0800
author: Michael
categories: CPP
---

# CTreeView代码
	private:
		CTreeCtrl* m_treeCtrl;
		CImageList m_imageList;
	
	void CSelectView::OnInitialUpdate()
	{
		CTreeView::OnInitialUpdate();
		
		HICON icon = AfxGetApp()->LoadIconW(IDI_ICON_ROBOT);
		m_imageList.Create(30, 30, ILC_COLOR32, 1,1);
		m_imageList.Add(icon);
	
		m_treeCtrl = &GetTreeCtrl();
		m_treeCtrl->SetImageList(&m_imageList,TVSIL_NORMAL);
	
		m_treeCtrl->InsertItem(_T("Robotics"),0,0,NULL);
		m_treeCtrl->InsertItem(_T("Other"), 0, 0, NULL);
	}

	void CSelectView::OnTvnSelchanged(NMHDR* pNMHDR, LRESULT* pResult)
	{
		LPNMTREEVIEW pNMTreeView = reinterpret_cast<LPNMTREEVIEW>(pNMHDR);
		// TODO: Add your control notification handler code here
		*pResult = 0;
	
		HTREEITEM item= m_treeCtrl->GetSelectedItem();
		CString str = m_treeCtrl->GetItemText(item);

		if (str == _T("Robotics")) {
			::PostMessage(AfxGetMainWnd()->GetSafeHwnd(), NM_ROBOTCONTROLLER, (WPARAM)NM_ROBOTCONTROLLER, (LPARAM)0);
		}
		else if (str == _T("Other")) {
			::PostMessage(AfxGetMainWnd()->GetSafeHwnd(), NM_PMCLIENT, (WPARAM)NM_PMCLIENT, (LPARAM)0);
		}
	}

# OnTvnSelchanged
选中项改变事件。

	HTREEITEM item= m_treeCtrl->GetSelectedItem();
	CString str = m_treeCtrl->GetItemText(item);

# MainFrm代码

	#define NM_ROBOTCONTROLLER (WM_USER+100)
	#define NM_PMCLIENT (WM_USER+101)
	
	BEGIN_MESSAGE_MAP(CMainFrame, CFrameWnd)
		ON_WM_CREATE()
		ON_MESSAGE(NM_ROBOTCONTROLLER, OnMyChange)
		ON_MESSAGE(NM_PMCLIENT, OnMyChange)
	END_MESSAGE_MAP()

	LRESULT CMainFrame::OnMyChange(WPARAM wParam, LPARAM lParam)
	{
		CCreateContext context;
	
		if (wParam == NM_ROBOTCONTROLLER) {
			context.m_pNewViewClass = RUNTIME_CLASS(CMFCRoboticsView);
			context.m_pCurrentFrame = this;
			context.m_pLastView = (CFormView*)m_wndSplitter.GetPane(0, 1);
			m_wndSplitter.DeleteView(0, 1);
			m_wndSplitter.CreateView(0, 1, RUNTIME_CLASS(CMFCRoboticsView), CSize(520, 600), &context);
			CMFCRoboticsView* pNewView = (CMFCRoboticsView*)m_wndSplitter.GetPane(0, 1);
			m_wndSplitter.RecalcLayout();
			pNewView->OnInitialUpdate();
			m_wndSplitter.SetActivePane(0, 1);
	
		}
		else if (wParam == NM_PMCLIENT) {
			context.m_pNewViewClass = RUNTIME_CLASS(CPMClientView);
			context.m_pCurrentFrame = this;
			context.m_pLastView = (CFormView*)m_wndSplitter.GetPane(0, 1);
			m_wndSplitter.DeleteView(0, 1);
			m_wndSplitter.CreateView(0, 1, RUNTIME_CLASS(CPMClientView), CSize(520, 600), &context);
			CPMClientView* pNewView = (CPMClientView*)m_wndSplitter.GetPane(0, 1);
			m_wndSplitter.RecalcLayout();
			pNewView->OnInitialUpdate();
			m_wndSplitter.SetActivePane(0, 1);
		}
		return LRESULT();
	}

# CTreeCtrl::InsertItem
Call this function to insert a new item in a tree view control.

	HTREEITEM InsertItem(LPTVINSERTSTRUCT lpInsertStruct);

	HTREEITEM InsertItem(
		UINT nMask,
		LPCTSTR lpszItem,
		int nImage,
		int nSelectedImage,
		UINT nState,
		UINT nStateMask,
		LPARAM lParam,
		HTREEITEM hParent,
		HTREEITEM hInsertAfter);

	//只有文字
	HTREEITEM InsertItem(
		LPCTSTR lpszItem,
		HTREEITEM hParent = TVI_ROOT,
		HTREEITEM hInsertAfter = TVI_LAST);

	//包含文字和图标
	HTREEITEM InsertItem(
		LPCTSTR lpszItem,
		int nImage,
		int nSelectedImage,
		HTREEITEM hParent = TVI_ROOT,
		HTREEITEM hInsertAfter = TVI_LAST);

# CTreeCtrl::Select
Call this function to select the given tree view item, scroll the item into view, or redraw the item in the style used to indicate the target of a drag-and-drop operation.

	m_tree.SelectItem(hNewItem);
	m_tree.EnsureVisible(hNewItem);

# CTreeCtrl::DeleteItem
删除节点

# CTreeCtrl::SetItemText
设置节点字符串

# CTreeCtrl::GetSelectedItem
获取选中的节点

# CTreeCtrl::ExpandAllNode
展开所有节点

	ExpandAllNode(m_tree.GetRootItem(), m_tree);

	void CUserManual::ExpandAllNode(HTREEITEM hItem, CTreeCtrl& treeShow)
	{
		HTREEITEM hChild = treeShow.GetChildItem(hItem);
		while(hChild)
		{
			treeShow.Expand(hItem, TVE_EXPAND);
			ExpandAllNode(hChild, treeShow);
			hChild = treeShow.GetNextSiblingItem(hChild);
		}
	}