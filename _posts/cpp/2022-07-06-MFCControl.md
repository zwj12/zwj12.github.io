---
layout: post
title: "MFC Control"
date: 2022-07-06 19:23:00 +0800
author: Michael
categories: CPP
---

# Group属性
控件的Group属性是用来配合Tab Order分组使用的，MFC会按Tab顺序检索，当遇到一个Group属性为true时，此时认为该控件为下一组的第一个控件，只有控件类型相同时，才会被认为是同一组。例如如果有6个RADIO控件，Tab Order顺序分别为1，2，3，4，5，6，如果设置第4个控件的Group属性为True，那么MFC就会认为1，2，3控件为一组，4，5，6控件为另一组。

# 启用禁用控件
	m_buttonPre.EnableWindow(TRUE);
	m_buttonNext.EnableWindow(FALSE);
