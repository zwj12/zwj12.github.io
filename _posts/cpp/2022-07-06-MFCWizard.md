---
layout: post
title: "MFC Wizard"
date: 2022-07-06 19:23:00 +0800
author: Michael
categories: CPP
---

# MFC向导对话框类
属性页对话框包括向导对话框和一般属性页对话框两类。主要有下面两个类。  

1. CPropertyPage，继承自CDialog类，用于处理某单个的属性页，所以要为每个属性页都创建一个继承自CPropertyPage的子类。
2. CPropertySheet，继承自CWnd类，属性表类，负责加载、打开或删除属性页，并可以在属性页对话框中切换属性页。它跟对话框类似，也有模态和非模态两种。

# 属性页类CPropertyPage
属性页对话框包括向导对话框和一般属性页对话框两类。一般属性页对话框和向导对话框的创建和显示的不同包括：是否需要OnSetActive和OnWizardFinish等重载函数，是否需要调用属性表类的SetWizardMode函数设置为向导对话框模式。  

![日志文件夹](/assets/cpp/CPropertyPageWizard.png)  
![日志文件夹](/assets/cpp/CPropertyPage.png)  

## 属性
1. Caption，标题
2. Style，Child
3. Border，Thin

## 函数
1. OnSetActive
	
		//第一页
		BOOL CSummandPage::OnSetActive()   
		{   
		    // TODO: Add your specialized code here and/or call the base class  
		    CPropertySheet* psheet = (CPropertySheet*) GetParent();   
		    // 设置属性表只有“下一步”按钮   
		    psheet->SetWizardButtons(PSWIZB_NEXT);
		    return CPropertyPage::OnSetActive();   
		}
			
		//最后一页
		BOOL CAddPage::OnSetActive()   
		{   
		    // TODO: Add your specialized code here and/or call the base class
		    CPropertySheet* psheet = (CPropertySheet*) GetParent();   
		    //设置属性表只有“完成”按钮   
		    psheet->SetFinishText(_T("完成"));
		    return CPropertyPage::OnSetActive();   
		}  

2. OnWizardFinish
	
		//最后一页
		BOOL CAddPage::OnWizardFinish()
		{
			// TODO: Add your specialized code here and/or call the base class		
			MessageBox(_T("使用说明向导已阅读完！"));		
			return CMFCPropertyPage::OnWizardFinish();
		}

3. 构造函数，需要把属性页构造函数后面的pParent删掉，否则编译出错

		CSummandPage::CSummandPage(CWnd* pParent /*=nullptr*/)
			: CMFCPropertyPage(IDD_SUMMAND_PAGE)
		{
		
		}

# 属性表类CPropertySheet

	private:
		CSummandPage    m_summandPage;
		CAddendPage     m_addendPage;
		CAddPage        m_addPage;
	
	
	CAddSheet::CAddSheet(UINT nIDCaption, CWnd* pParentWnd, UINT iSelectPage)   
	    :CPropertySheet(nIDCaption, pParentWnd, iSelectPage)   
	{   
	    // 添加三个属性页到属性表   
	    AddPage(&m_summandPage);   
	    AddPage(&m_addendPage);   
	    AddPage(&m_addPage);   
	}   
	  
	CAddSheet::CAddSheet(LPCTSTR pszCaption, CWnd* pParentWnd, UINT iSelectPage)   
	    :CPropertySheet(pszCaption, pParentWnd, iSelectPage)   
	{   
	    // 添加三个属性页到属性表   
	    AddPage(&m_summandPage);   
	    AddPage(&m_addendPage);   
	    AddPage(&m_addPage);   
	}

# 显示向导对话框

    CAddSheet sheet(_T(""));   
    // 设置属性对话框为向导对话框   
    sheet.SetWizardMode(); 
    sheet.DoModal();  