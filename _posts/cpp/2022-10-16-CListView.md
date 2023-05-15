---
layout: post
title: "CListView"
date: 2022-10-16 14:12:00 +0800
author: Michael
categories: CPP
---

# 设置报表样式

    BOOL CMFCApplication1View::PreCreateWindow(CREATESTRUCT& cs)
    {
        cs.style |= LVS_REPORT | LVS_SHOWSELALWAYS | LVS_OWNERDRAWFIXED;
        return CListView::PreCreateWindow(cs);
    }

# 添加列

    void CMFCApplication1View::OnInitialUpdate()
    {
        CListView::OnInitialUpdate();

        LV_COLUMN lvc;
        lvc.mask = LVCF_TEXT | LVCF_SUBITEM | LVCF_WIDTH;

        lvc.iSubItem = 0;
        lvc.pszText = _T("Email");
        lvc.cx = 75;
        GetListCtrl().InsertColumn(0, &lvc);

        lvc.iSubItem = 1;
        lvc.pszText = _T("Name (First, Last)");
        lvc.cx = 125;
        GetListCtrl().InsertColumn(1, &lvc);

        lvc.iSubItem = 2;
        lvc.pszText = _T("Phone");
        lvc.cx = 75;
        GetListCtrl().InsertColumn(2, &lvc);

        lvc.iSubItem = 3;
        lvc.pszText = _T("Location");
        lvc.cx = 75;
        GetListCtrl().InsertColumn(3, &lvc);

        lvc.iSubItem = 4;
        lvc.pszText = _T("Title");
        lvc.cx = 150;
        GetListCtrl().InsertColumn(4, &lvc);

        lvc.iSubItem = 5;
        lvc.pszText = _T("Dept");
        lvc.cx = 150;
        GetListCtrl().InsertColumn(5, &lvc);
    }