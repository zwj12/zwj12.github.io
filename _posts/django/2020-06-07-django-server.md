---
layout: post
title: "Django Server"
date: 2020-06-07 10:18:00 +0800
author: Michael
categories: Django
---

# Description:
Django服务器安装配置。

# 安装Apache  
下载地址：[Apache 2.4.43 Win64](https://www.apachelounge.com/download/)，解压到C盘根目录C:\Apache24。  
安装服务：httpd.exe -k install  
修改配置文件httpd.conf：  
Listen 8002

# 安装Microsoft Visual C++ 14.0 is required
Microsoft Visual C++ 14.0 is required. Get it with [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/downloads/)  

# 安装mod_wsgi  
	pip install mod_wsgi

运行指令mod_wsgi-express module-config  
修改Apache配置文件httpd.conf：

	#添加mod_wsgi.so模块,这三行是上面命令行中显示出来的
	LoadFile "c:/program files/python38/python38.dll"
	LoadModule wsgi_module "c:/program files/python38/lib/site-packages/mod_wsgi/server/mod_wsgi.cp38-win_amd64.pyd"
	WSGIPythonHome "c:/program files/python38"	 
	 
	#指定项目的wsgi.py配置文件路径,这个py文件是在你的Django项目中  
	WSGIScriptAlias / C:/Users/CNMIZHU7/source/repos/Django/accounting/accounting/wsgi.py  
	  
	#指定项目目录,即你的Django项目路径 
	WSGIPythonPath  C:/Users/CNMIZHU7/source/repos/Django/accounting
	  
	<Directory C:/Users/CNMIZHU7/source/repos/Django/accounting>  
	<Files wsgi.py>  
	    Require all granted  
	</Files>  
	</Directory>  
	  
	#项目静态文件地址, Django项目中静态文件的路径  
	Alias /static C:/Users/CNMIZHU7/source/repos/Django/accounting/cash/static
	<Directory C:/Users/CNMIZHU7/source/repos/Django/accounting/cash/static>  
	    AllowOverride None  
	    Options None  
	    Require all granted  
	</Directory>  
	  
	#项目media地址, 上传图片等文件夹的路径  
	Alias /media C:/Users/CNMIZHU7/source/repos/Django/accounting/cash/media
	<Directory C:/Users/CNMIZHU7/source/repos/Django/accounting/cash/media>  
	    AllowOverride None  
	    Options None  
	    Require all granted  
	</Directory> 


# 重启Apache  


注意：Python安装时需要选中所有用户权限，默认安装目录为C:\Program Files\Python38