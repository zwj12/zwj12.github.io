---
layout: post
title: "WindowsFormHost"
date: 2022-06-28 10:03:00 +0800
author: Michael
categories: WPF
---

# WPF 中承载 Windows 窗体控件程序集的引用
- WindowsFormsIntegration
- System.Windows.Forms

# XAML命名空间
	xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

# WindowsFormsHost控件
	<Grid>
	
	    <WindowsFormsHost>
	        <wf:MaskedTextBox x:Name="mtbDate" Mask="00/00/0000"/>
	    </WindowsFormsHost>
	
	</Grid>