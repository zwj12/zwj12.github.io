---
layout: post
title: "MFC Message"
date: 2022-07-06 19:23:00 +0800
author: Michael
categories: CPP
---

# 消息映射机制
类内必须添加声明宏 DECLARE_MESSAGE_MAP(), 类外必须添加实现宏BEGIN_MESSAGE_MAP(theClass, baseClass) END_MESSAGE_MAP()

	//宏展开
	//DECLARE_MESSAGE_MAP()
	protected: 
		static const AFX_MSGMAP* PASCAL GetThisMessageMap(); 
		virtual const AFX_MSGMAP* GetMessageMap() const; 


	//BEGIN_MESSAGE_MAP(CMyFrameWnd, CFrameWnd)
		//ON_MESSAGE(WM_CREATE,OnCreate)
	//END_MESSAGE_MAP()
	
	//PTM_WARNING_DISABLE 
	const AFX_MSGMAP* CMyFrameWnd::GetMessageMap() const
	{
		return GetThisMessageMap();
	}
	
	const AFX_MSGMAP* PASCAL CMyFrameWnd::GetThisMessageMap()
	{
		static const AFX_MSGMAP_ENTRY _messageEntries[] =
		{
			{ WM_CREATE, 0, 0, 0, AfxSig_lwl,(AFX_PMSG)(AFX_PMSGW)(static_cast<LRESULT(AFX_MSG_CALL CWnd::*)(WPARAM, LPARAM)>(&OnCreate)) },
	
			{0, 0, 0, 0, AfxSig_end, (AFX_PMSG)0}
		};
		static const AFX_MSGMAP messageMap ={ &CFrameWnd::GetThisMessageMap, &_messageEntries[0] };
		return &messageMap;
	}
	//PTM_WARNING_RESTORE

	//以WM_CREATE消息为例。从CWnd::OnWndMsg函数开始，WM_COMMAND消息开始分叉
	AfxWndProc(...)
	{
		CWnd* pWnd = CWnd::FromHandlePermanent(hWnd);//获取和hWnd绑定在一起的框架类对象地址(pFrame=pWnd)
		AfxCallWndProc(pWnd, ...)
		{	
			pWnd->WindowProc(...)
			{
				OnWndMsg(...)
				{
					const AFX_MSGMAP* pMessageMap; pMessageMap = GetMessageMap(); //获取本类宏站开的静态变量的地址（链表头节点）
					const AFX_MSGMAP_ENTRY* lpEntry;
					for (; pMessageMap->pfnGetBaseMap != NULL;pMessageMap = (*pMessageMap->pfnGetBaseMap)()) //遍历链表
					{
						lpEntry = AfxFindMessageEntry(pMessageMap->lpEntries,message, 0, 0))；//找到数组元素的地址或NULL
						if(lpEntry!=NULL)
						{
							goto LDispatch;
						}
					}
					LDispatch:
					lpEntry->pfn; //CMyFrameWnd::OnCreate
					调用CMyFrameWnd::OnCreate函数，完成消息处理函数
				}
			}
		}
	}

# 消息的分类
1. 标准Windows窗口消息，除WM_COMMAND之外，所有以WM_开头的消息。ON_WM_XXX，由系统产生。从CWnd派生的类，都可以接收到这类消息。 
2. 命令消息，WM_COMMAND，由菜单和工具栏或快捷键产生，以WM_COMMAND形式发出。从CCmdTarget派生的类，都可以接收到这类消息。
3. 控件通知消息，有多种格式

# 消息类型：
1. 系统消息，[0x0000, 0x03ff]，（0 到 WM_USER–1），系统消息有可以分成三类: 窗口消息(WM_), 命令消息(WM_COMMAND), 控件通知消息(WM_NOTIFY)
2. 窗口类内部自定义消息， 0x0400-0x7FFF（WM_USER 到 WM_APP-1）
3. 应用程序内部自定义消息，0x8000-0xBFFF（WM_APP 到 0xBFFF）
4. 应用程序之间自定义消息，0xC000-0xFFFF（0xC000 到 0xFFFF）

- ON_COMMAND 是响应菜单栏，状态栏，工具栏发送给框架窗口的命令消息的宏。命令类型是：CN_COMMAND
- ON_UPDATE_COMMAND_UI 是响应程序空闲时促发的界面更新消息的宏。
- ON_CONTROL 是父窗口响应控件发送的通知消息的宏。
- ON_CONTROL_REFLECT 是子控件响应父窗口反射回来的通知消息的的宏。
- ON_NOTIFY 是父窗口响应复杂控件发送的通知消息的宏
- ON_NOTIFY_REFLECT 是复杂子控件响应父窗口反射回来的通知消息的的宏。
- ON_MESSAGE 是窗口响应自定义的消息的宏
- ON_THREAD_MESSAGE是线程响应自定义的消息的宏
- ON_REGISTERED_MESSAGE 是响应通过RegisterWindowMessage注册得到的消息宏。

![日志文件夹](/assets/cpp/MFCMessageType.png)  

# 消息宏
1. 通用宏：ON_MESSAGE，可以定义所有消息，但是尽量使用标准宏和命令宏
2. 专职宏：定义具体的消息，推荐使用

# 自定义消息
	//定义消息
	#define WM_MYMESSAGE WM_USER+1001

	//定义消息处理函数
	LRESULT OnMyMessage(WPARAM wParam, LPARAM lParam);

	//定义消息宏
	ON_MESSAGE(WM_MYMESSAGE,OnMyMessage)

	//实现消息处理函数
	LRESULT CMyFrameWnd::OnMyMessage(WPARAM wParam, LPARAM lParam)
	{
		CString str;
		str.Format(_T("x=%d,y=%d"), wParam, lParam);
		AfxMessageBox(str);
		return LRESULT();
	}

	//发送自定义消息
	::PostMessage(this->m_hWnd, WM_MYMESSAGE, 1, 2);