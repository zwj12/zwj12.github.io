---
layout: post
title: "git rebase"
date: 2023-03-17 11:18:00 +0800
author: Michael
categories: Develop
---

# git rebase master
A分支和B分支都是基于master的分支，然后分别修改代码后，如果B先提交了一个PR，合并到master分支后，此时A如果使用git merge合并后，会导致图谱分叉，可以使用git rebase把master上B提交的修改先合并到A后，A在提交，就不会分叉。rebase会把A所有的修改都滞后。

![日志文件夹](/assets/develop/git/gitmergenorebase.png)  
![日志文件夹](/assets/develop/git/gitmergewithrebase.png)  
![日志文件夹](/assets/develop/git/gitrebase.png) 