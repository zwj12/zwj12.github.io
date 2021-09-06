---
layout: post
title: "BootstrapBlazor "
date: 2021-08-31 13:08:00 +0800
author: Michael
categories: CSharp
---

#  安装BootstrapBlazor 
使用NuGet引用BootstrapBlazor 类库

# 加载BootstrapBlazor
	//Startup.cs
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddRazorPages();
        services.AddServerSideBlazor();
        services.AddSingleton<WeatherForecastService>();

        services.AddBootstrapBlazor();
    }

# 添加命名空间
	//razor组件中添加，或者在根目录的_Imports.razor组件中添加
	@using BootstrapBlazor.Components