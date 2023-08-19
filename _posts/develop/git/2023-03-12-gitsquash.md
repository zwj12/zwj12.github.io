---
layout: post
title: "git squash"
date: 2023-03-12 11:18:00 +0800
author: Michael
categories: Develop
---

# 分支
	git branch //列出所有分支
	git branch branch_name //创建分支
	git branch -d branch_name //删除分支
	git checkout branch_name //切换分支
	git checkout -b branch_name //创建并切换分支

# 如何使用Git Squash 提交, 建议使用git merge --squash指令
请注意，没有 git squash 命令。有两种方法可以实现 Git 压缩：

- git rebase -i 作为用于压缩提交的交互式工具
- git merge -squash 在合并时使用 -squash 选项

# git rebase -i 合并提交
要压缩四个提交，我们将执行以下操作。

    git rebase -i HEAD~4

# git merge --squash feature
feature分支合并到master分支

	git checkout master
	git merge --squash feature
	git commit -m "Merge feature" 

	//?
	git checkout feature
	git merge master​​​