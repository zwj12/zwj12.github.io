---
layout: page
title: "Me"
permalink: /about/contact/
---

Hi, it's me!

# 升级RubyGems
	// 一般不需要升级RubyGems，因为RubyGems包含在Ruby中，可以直接安装最新的Ruby软件
	gem update --system 

# 安装jekyll
	gem install jekyll bundler

# 如果jekyll版本不对，可以使用下列指令更新
	bundle update jekyll
	// or just
	bundle update

# 查看版本
	ruby -v
	gem -v
	jekyll -v

# 创建新的目录文件
	jekyll new .
	// uncomment the line below. To upgrade, run `bundle update github-pages`.
	gem "github-pages", group: :jekyll_plugins


# 运行服务器，打开浏览器浏览页面
	bundle exec jekyll serve
	
# 升级github-pages
	//打开Gemfile文件，修改`gem "github-pages", "~> 209", group: :jekyll_plugins`这一行的版本号。
	//如最新的版本号为226，那么就修改为：`gem "github-pages", "~> 226", group: :jekyll_plugins`
	//查看最新版本的网址为：https://pages.github.com/versions/
	bundle update github-pages

# 缺少组件时，在jekyll项目目录下运行bundle install自动安装缺失的组件
	bundle install

	jekyll new myblog	

	https://zwj12.github.io/

如需在MarkdownPad2中正常显示图片，只要同时打开根目录下一个md文件即可。

建议使用SSH连接。