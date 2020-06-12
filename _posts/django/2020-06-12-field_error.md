---
layout: post
title: "FieldError"
date: 2020-06-12 20:51:00 +0800
author: Michael
categories: Django
---

# 错误信息

	'balance' cannot be specified for CashOnHand model form as it is a non-editable field. Check fields/fieldsets/exclude attributes of class CashOnHandAdmin.

# 原因
Model中有字段是不可编辑的，但是对应的Admin类中确定义了该字段，fields中需要删除，但是list_display中可以保留该字段用于显示

	# Model - CashOnHand
    balance = models.FloatField(editable=False)

	# CashOnHandAdmin
    # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark']
    fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
	list_display = ('operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark')
