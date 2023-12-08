---
layout: post
title: "InstallShield"
date: 2023-11-18 14:49:00 +0800
author: Michael
categories: Develop
---

# 合并模块 Merge Modules
合并模块实质上是简化的 .msi 文件，.msi 是 Windows Installer 安装包的文件扩展名。 标准合并模块的文件扩展名为 .msm。合并模块不能单独安装，因为它缺少安装数据库中存在的一些重要数据库表。 合并模块还包含对其自身唯一的其他表。 若要将合并模块提供的信息与应用程序一起安装，必须先将该模块合并到该应用程序的 .msi 文件中。合并模块由以下部分组成：

- 包含由合并模块提供的安装属性和设置逻辑的 Merge Module 数据库。
- 描述模块的合并模块摘要信息流参考。
- 作为流存储在合并模块中的 MergeModule.CABinet Cabinet 文件。 此 Cabinet 包含合并模块提供的组件所需的所有文件。

将合并模块合并到应用程序的 .msi 文件时，安装合并模块提供的组件所需的所有信息和资源都会合并到应用程序的 .msi 文件中。 然后，不再需要合并模块来安装这些组件，并且用户无需访问合并模块。 由于安装组件所需的所有信息都以单个文件的形式提供，因此使用合并模块可以消除许多版本冲突实例、缺少的注册表项和安装不当的文件。

可以通过InstallShield打开msm文件，查看详细信息。
![日志文件夹](/assets/develop/installshield/mergemodule.png)  

# msm
可以把msm文件放在目录C:\Program Files (x86)\InstallShield\2021\Modules\i386下，此时刷新Redistributables页面，就可以添加改msm依赖了。

![日志文件夹](/assets/develop/msmFolder.png)  
![日志文件夹](/assets/develop/msmRedistributables.png)  

# InstallShield prerequisites, merge modules, and objects 
可以通过Application Data -> Redistributables查看所有可以添加的依赖库
![日志文件夹](/assets/develop/msmRedistributables.png)  
![日志文件夹](/assets/develop/installscriptObjects.png)  

# 目录结构
MSI Project和Install Script Project在定义文件夹目录时，风格是不一样的。

![日志文件夹](/assets/develop/InstallShieldMSIFolders.png)  
![日志文件夹](/assets/develop/InstallShieldScriptFolders.png)  

# Dynamic Links
通过创建一个Component，可以关联静态文件和动态文件夹，对于静态文件，必须一个一个的全部定义清除路径，对于动态路径，可以指定一个文件夹，然后使用通配符把该文件夹目录下的所有文件全部引用进来。如果需要在根目录的子文件内动态引用目录，需要先创建一个文件夹，然后在这个文件夹内创建Component。

![日志文件夹](/assets/develop/InstallShieldDynamicLinks.png)  

# uninstall
InstallShield制作的软件包，在卸载时，只会卸载自己标定的文件，如果在文件夹中还存在其它文件，默认是不会删除的。

# Upgrade
| Update | Package Code | Product Version | Product Code | Upgrade Code | Description |
|-------------|--------------|-------------|-------------|--------------|-------------|
| Small Update | X |  |  |  |  |
| Minor Upgrade | X | X |  |  |  |
| Major Upgrade | X | X | X |  |  |

![日志文件夹](/assets/develop/InstallShieldUpgradeCode.png)  
![日志文件夹](/assets/develop/InstallShieldMajorUpgrade.png)  

## MSI Project & InstallScript MSI project
1. Major Upgrade, Uninstalls the earlier version and then installs the new version. 
2. Minor Upgrade
3. Small Upgrade
4. Patching
5. QuickPath

## InstallScript project
1. Differential Release
2. Full Release

# Files and Folders
文件是安装包的核心，文件通过Component配置，Component关联feature。当安装时，如果一个featuure被选中，那么这个feature的所有Component的所有文件都会被安装。通过Files and Folders view页面添加文件。

## Directory Identifier
每一个文件夹都有一个标识符，但是不能同名，文件夹在引用时，可以直接用这个标识符引用，但是如果被引用了，标识符就不能修改了，如果需要需要修改，需要先断开所有引用。

![日志文件夹](/assets/develop/InstallShield/DirectoryIdentifier.png)  
![日志文件夹](/assets/develop/InstallShield/DirectoryIdentifierLinked.png)  

## 预置安装目录
InstallShield默认情况下，只显示了最常用的目录，如果需要把文件安装在其它目录，需要手动设置将其显示出来。
![日志文件夹](/assets/develop/installshieldPredefinedFolder.png)  

# Path Variables
路径修改需要在Define Value列修改，修改后，Current Value会显示当前值。
![日志文件夹](/assets/develop/InstallshieldPathVariables.png)  

# Template Summary 模板摘要属性
Windows Install安装时需要指定模板摘要属性，模板摘要属性指示与此安装数据库兼容的平台和语言版本。 如果这是在 x64 平台上运行的 64 位 Windows Installer 包，请在模板摘要属性中输入 x64。如果依赖包里有一个依赖包明确指定只支持x64，那么项目中也需要指定x64，否则会导致编译失败，同样，如果Component指定位64位，项目中也需要指定x64。安装数据库的模板摘要属性信息的语法如下：

    [平台属性];[语言 ID][,语言 ID][,...]。
    x64;1033
    Intel;1033
    Intel64;1033
    ;1033
    Intel ;1033,2046
    Intel64;1033,2046
    Intel;0
    Arm;1033,2046
    Arm;0
    Arm64;1033,2046
    Arm64;0

![日志文件夹](/assets/develop/installshield/templatesummary.png)  
![日志文件夹](/assets/develop/installshield/releasetemplatesummary.png)  
![日志文件夹](/assets/develop/installshield/templatesummary5008error.png)  
![日志文件夹](/assets/develop/installshield/Compoments64Bit.png)  
