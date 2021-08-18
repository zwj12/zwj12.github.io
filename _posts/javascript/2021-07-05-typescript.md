---
layout: post
title: "TypeScript"
date: 2021-07-05 14:40:00 +0800
author: Michael
categories: javascript
---

# 安装
	npm install -g typescript
	npm update -g typescript

# 装饰器执行时机
修饰器对类的行为的改变，是代码编译时发生的（不是TypeScript编译，而是js在执行机中编译阶段），而不是在运行时。这意味着，修饰器能在编译阶段运行代码。也就是说，修饰器本质就是编译时执行的函数。在Node.js环境中模块一加载时就会执行

# 类装饰器
应用于类构造函数，其参数是类的构造函数。

	function Path(path: string) {
	    return function (target: Function) {
	        !target.prototype.$Meta && (target.prototype.$Meta = {})
	        target.prototype.$Meta.baseUrl = path;
	    };
	}
	
	@Path('/hello')
	class HelloService {
	    constructor() {}
	}
	
	console.log(HelloService.prototype.$Meta);// 输出：{ baseUrl: '/hello' }
	let hello = new HelloService();
	console.log(hello.$Meta) // 输出：{ baseUrl: '/hello' }

# 构造函数的参数直接定义属性
	class Info {
		constructor(
			public name: string,
			private age: number ) {}
	}