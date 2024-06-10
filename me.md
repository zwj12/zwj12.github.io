---
layout: page
title: "Me"
permalink: /about/contact/
---

Hi, it's me!


# 安装和查看版本
## 安装jekyll和bundler
Download Ruby+Devkit 3.3.2-1 (x64) and install, 安装过程如果被防火墙挡住，需要使用移动网络，当前github-pages支持版本为2.7.4。如果安装3.3.2，测试发现wdm依赖包会安装不成功，不清楚什么原因。

	ridk install and choose MSYS2 and MINGW development tool chain
	gem install jekyll bundler
	jekyll -v

## 删除jekyll
 	gem uninstall jekyll
	
## 查看版本
应定期查看软件版本，尽量保持github pages要求的最新版本，查看最新版本的网址为：https://pages.github.com/versions/。  

	ruby -v
	gem -v
	jekyll -v
	bundler -v
	github-pages -v	

## bundle update & install
开发过程中如需安装某个gem最好指定相应的版本号，然后bundle install，如需更新某个gem，可以在Gemfile里修改其版本号然后bundle install或者单独更新(bundle update [gem name])，然后测试一下，不要直接bundle update，这样会更新所有gem然后更新Gemfile.lock文件，在程序运行时可能会引发其它问题或引入新的bug。

### bundle update
把上下文环境切换到jekyll项目下，修改Gemfile文件中中的jekyll版本，运行`bundle update`更新jekyll版本。bundle update会去相应的源检查Gemfile里gem的更新，然后对比Gemfile.lock文件，如果Gemfile里没有指定版本或是指定是>=的版本，就会去相应的源下载并安装新版本的gem，然后更新Gemfile.lock文件。

	bundle update

### bundle install
bundle install会先检查Gemfile.lock文件以及里边的相关依赖，然后为本地系统安装Gemfile.lock文件中指定的版本，接着去检查Gemfile中有而Gemfile.lock中没有的，然后安装。bundle install好像不会去检查相关源中Gem版本的更新。

	bundle install

## 升级RubyGems
一般不需要升级RubyGems，因为RubyGems包含在Ruby中，可以直接安装最新的Ruby软件

	gem update --system 

# 创建新的jekyll项目目录文件
	jekyll new .
	jekyll new myblog

## 修改默认的jekyll项目，支持github pages
	// If you want to use GitHub Pages, remove the "gem "jekyll"" above and
	// uncomment the line below. To upgrade, run `bundle update github-pages`.
	// 可能需要先运行bundle update，才能运行"bundle update github-pages"。
	# gem "jekyll", "~> 3.9.3"
	gem "github-pages", group: :jekyll_plugins

## 升级github-pages
	//打开Gemfile文件，修改`gem "github-pages", "~> 209", group: :jekyll_plugins`这一行的版本号。
	//如最新的版本号为226，那么就修改为：`gem "github-pages", "~> 226", group: :jekyll_plugins`
	//查看最新版本的网址为：https://pages.github.com/versions/
	bundle update github-pages

# 运行服务器，打开浏览器浏览页面
	bundle exec jekyll serve
	
## Entry File
Create the entry file for your site. GitHub Pages will look for an index.html, index.md, index.markdown or README.md file as the entry file for your site.

# 图片显示缺失
如需在MarkdownPad2中正常显示图片，只要同时打开根目录下一个md文件即可。

# 自定义layout
默认页面布局位置存储在`C:\Ruby27-x64\lib\ruby\gems\2.7.0\gems\minima-2.5.1`，如果需要自定义该布局，需要在自己的jekyll项目目录下创建一个_layouts文件夹，然后把post.html和home.html复制到该目录下，修改post.html或home.html文件即可自定义页面布局。

# Header页面导航
jekyll项目根目录的html文件会自动被添加到header位置的导航菜单上。如果在根目录创建文件夹，然后在文件夹里添加html或md文件，同样会被添加到导航菜单上。

# Liquid语法显示所有posts

	<ul>
	{% for post in site.posts %}
		<li>
		<a href="{{ post.url }}">{{ post.title }}</a>
		</li>
	{% endfor %}
	</ul>

# 分类显示posts
	---
	layout: default
	title: Categories
	---
	<h1>Categories</h1>

	{% for category in site.categories %}
	<h3>{{ category[0] }}</h3>
	<ul>
		{% for post in category[1] %}
		<li><a href="{{ post.url }}">{{ post.title }}</a></li>
		{% endfor %}
	</ul>
	{% endfor %}