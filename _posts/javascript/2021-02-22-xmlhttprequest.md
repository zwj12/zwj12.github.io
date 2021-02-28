---
layout: post
title: "XMLHttpRequest"
date: 2021-02-22 10:57:00 +0800
author: Michael
categories: javascript
---

# XMLHttpRequest事件处理器

## 通过属性onreadystatechange支持，必须支持

## 通过接口XMLHttpRequestEventTarget支持，大部分支持
	
	XMLHttpRequestEventTarget.onabort
	XMLHttpRequestEventTarget.onerror
	XMLHttpRequestEventTarget.onload
	XMLHttpRequestEventTarget.onloadstart
	XMLHttpRequestEventTarget.onprogress
	XMLHttpRequestEventTarget.ontimeout
	XMLHttpRequestEventTarget.onloadend

## 通过标准的监听器接口EventTarget支持，现代浏览器支持

	EventTarget.addEventListener()
	EventTarget.removeEventListener()
	EventTarget.dispatchEvent()