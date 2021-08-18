---
layout: post
title: "PostgreSQL"
date: 2021-06-07 09:09:00 +0800
author: Michael
categories: SmartOT
---

# 用户名密码
	# pgAdmin
	IP: http://10.0.2.15:8000
	username: admin@abb.com
	password: .edge
	# postgresql	
	database: postgres
	username: postgres
	password: .edge

![日志文件夹](/assets/smartot/dockerpgadmin.png) 

	
# 连接SmartOT中postgresql数据库 #
	psql -h 10.0.2.15 -U postgres
	psql -h 10.0.2.15 -U postgres smartot4
	\q

# 查看已经存在的数据库
	\l

# 进入数据库
	\c smartot4

# 安装数据库 
	sudo apt install postgresql

# 安装pgAdmin 4，貌似桌面版就可以了
	#
	# Setup the repository
	#
	
	# Install the public key for the repository (if not done previously):
	sudo apt install curl
	sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
	
	# Create the repository configuration file:
	sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
	
	#
	# Install pgAdmin
	#
	
	# Install for both desktop and web modes:
	sudo apt install pgadmin4
	
	# Install for desktop mode only:
	sudo apt install pgadmin4-desktop
	
	# Install for web mode only: 
	sudo apt install pgadmin4-web 
	
	# Configure the webserver, if you installed pgadmin4-web:
	sudo /usr/pgadmin4/bin/setup-web.sh

	# 注意不是https
	http://127.0.0.1/pgadmin4

# Docker安装PostgreSQL
	sudo docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=Quarter0 -d postgres
	#Host: 172.17.0.1

# Docker安装pgAdmin4
	sudo docker pull dpage/pgadmin4
	sudo docker run -d -p 5433:80 --name pgadmin4 -e PGADMIN_DEFAULT_EMAIL=michael-weijin.zhu@cn.abb.com -e PGADMIN_DEFAULT_PASSWORD=.michael dpage/pgadmin4
	http://127.0.0.1:5433

# 数据类型
	char：固定长度字符串，pgadmin中无法修改此类型的长度，默认长度为1.
	char[]：固定长度字符串，用来存储数组类型的数据，pgadmin中无法修改此类型的长度，默认长度为1.
	character：固定长度字符串，pgadmin中可以修改此类型的长度
	character[]：固定长度字符串，用来存储数组类型的数据，pgadmin中可以修改此类型的长度

# pgAdmin 4中表的箭头标记说明该表被继承，或者继承于另外一个表

# 数据库存储位置
	!通过以下代码可以查询到数据库对应的文件夹名称
	show data_directory;
	select * from pg_database;
![日志文件夹](/assets/smartot/pg_database.png)  
![日志文件夹](/assets/smartot/pg_database_file.png)  