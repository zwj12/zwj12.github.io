---
layout: post
title: "TimescaleDB"
date: 2021-06-23 16:39:00 +0800
author: Michael
categories: SmartOT
---

# 配置
	shared_preload_libraries = 'timescaledb'	# (change requires restart)
	CREATE EXTENSION IF NOT EXISTS timescaledb;