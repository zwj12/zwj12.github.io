---
layout: post
title: "git squash"
date: 2023-03-12 11:18:00 +0800
author: Michael
categories: Develop
---

# 如何使用Git Squash 提交
请注意，没有 git squash 命令。有两种方法可以实现 Git 压缩：

- git rebase -i 作为用于压缩提交的交互式工具
- git merge -squash 在合并时使用 -squash 选项

# git rebase
要压缩四个提交，我们将执行以下操作。

    git rebase -i HEAD~4