---
layout: post
title: "Docking Pane"
date: 2023-10-13 10:12:00 +0800
author: Michael
categories: ToolkitPro
---

# Docking Pane
    //CMainFrame.h
    public:
        CXTPDockingPaneManager m_paneManager;

    //resource
    IDR_PANE_OPTIONS       61446    Options
    IDR_PANE_PROPERTIES    61447    Properties

    //CMainFrame.cpp, CMainFrame::OnCreate: 
	// Initialize the docking pane manager and set the
	// initial them for the docking panes.  Do this only after all
	// control bars objects have been created and docked.
	m_paneManager.InstallDockingPanes(this);
	m_paneManager.SetTheme(xtpPaneThemeOffice);

	// Create docking panes.
	CXTPDockingPane* pwndPane1 = m_paneManager.CreatePane(IDR_PANE_OPTIONS, CRect(0, 0,200, 120), xtpPaneDockLeft);
	CXTPDockingPane* pwndPane2 = m_paneManager.CreatePane(IDR_PANE_PROPERTIES, CRect(0, 0,200, 120), xtpPaneDockBottom, pwndPane1);
    
# Attach controls to pane
    //CMainFrame.h
	public:
		CStatic m_wndOptions;
		CEdit m_wndProperties;

	afx_msg LRESULT OnDockingPaneNotify(WPARAM wParam, LPARAM lParam);

	//CMainFrame.cpp
	ON_MESSAGE(XTPWM_DOCKINGPANE_NOTIFY, OnDockingPaneNotify)

	LRESULT CMainFrame::OnDockingPaneNotify(WPARAM wParam, LPARAM lParam)
	{
		if (wParam == XTP_DPN_SHOWWINDOW)
		{
			CXTPDockingPane* pPane = (CXTPDockingPane*)lParam;

			if (!pPane->IsValid())
			{
				switch (pPane->GetID())
				{
				case IDR_PANE_PROPERTIES:
					{
						if (m_wndProperties.GetSafeHwnd() == 0)
						{
							m_wndProperties.Create(WS_CHILD|
								ES_AUTOVSCROLL|ES_MULTILINE,
								CRect(0, 0, 0, 0), this, 0);
						}
						pPane->Attach(&m_wndProperties);
						break;
					}
				case IDR_PANE_OPTIONS:
					{
						if (m_wndOptions.GetSafeHwnd() == 0)
						{
							m_wndOptions.Create(_T("\n\nOptions"),
								WS_CHILD|WS_CLIPCHILDREN|
								WS_CLIPSIBLINGS|SS_CENTER,
								CRect(0, 0, 0, 0), this, 0);
						}
						pPane->Attach(&m_wndOptions);
						break;
					}
				}
			}
			return TRUE;
		}
		return FALSE;
	}

# Icon
Create Bitmap with icons for created panes, Bitmap的大小为16*16*count，其中16*16为icon的大小，count为icon的数量，比如如果只有两个icon，那么大小为16*32。宽度必须为16的倍数，且倍数为icon的数量，如果不一致，程序加载时会报错，暂不清楚报错原因。

	int nIDIcons[] = {IDR_PANE_OPTIONS, IDR_PANE_PROPERTIES};
	m_paneManager.SetIcons(IDB_BITMAP_ICONS, nIDIcons, _countof(nIDIcons), RGB(0, 255, 0));


# Save and Load State Handlers

    //MainFrm.h 
 	afx_msg void OnClose();

    //MainFrm.cpp 
	ON_WM_CLOSE()

	int CMainFrame::OnCreate(LPCREATESTRUCT lpCreateStruct)
	{
		...

		// Load the previous state for docking panes.
		CXTPDockingPaneLayout layoutNormal(&m_paneManager);
		if (layoutNormal.Load(_T("NormalLayout")))
		{
			m_paneManager.SetLayout(&layoutNormal);
		}
		return 0;
	}

	void CMainFrame::OnClose()
	{
		// Save the current state for docking panes.
		CXTPDockingPaneLayout layoutNormal(&m_paneManager);
		m_paneManager.GetLayout(&layoutNormal);
		layoutNormal.Save(_T("NormalLayout"));
		CMDIFrameWnd::OnClose();
	}