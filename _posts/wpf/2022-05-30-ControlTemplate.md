---
layout: post
title: "ControlTemplate"
date: 2022-05-30 16:38:00 +0800
author: Michael
categories: WPF
---

# 模板
模板是用来定义(或重定义)对象的外观的好东西. WPF已经提供了Style来自定义外观, 那为什么还需要Template呢? 是因为Style只能让你一个一个地设置对象的属性, 但template用来改变对象的组织结构. Style就好象是更改一台电脑的配置, 你可以换个内存, 换个显卡, 但它还是一台电脑, 而Template则是把电脑整个换成一部汽车, 或者是其它一种你想要的东西.

# 绑定
ControlTemplate通常只包含TemplateBinding表达式，绑定回控件本身的属性，而DataTemplate包含标准绑定表达式。

# ContentControl和ItemsControl
Control分两种, ContentControl和ItemsControl (以下简称CC和IC), 其概念上的区别在两者包含的子物件个数不一样 (CC一个, IC多个), 其代码上面的区别在于CC有一个叫Content的属性接受单个对象, IC有一个叫Items的属性接受对象集合. Control.Template和CC.ContentControl的作用无用多说, 可能带来疑问的是IC中的template. IC可以看作是很多个”小”CC的集合. 而这些”小”CC的Template和ContentTemplate属性就是可以通过IC的ItemContainerStyle, ItemTemplate和ItemTemplateSelector属性指定的.

- Control.Template: ControlTemplate
- ContentControl.ContentTemplate: DataTemplate
- ItemsControl.ItemTemplate: DataTemplate
- GridViewColumn.CellTemplate: DataTemplate
- GridViewColumn.HeaderTemplate: DataTemplate

# Control.Template 
The ControlTemplate specifies the appearance of a Control; if a Control does not have a ControlTemplate, the Control will not appear in your application. The control author defines the default control template, and the application author can override the ControlTemplate to redefine the visual tree of the control. A ControlTemplate is intended to be a self-contained unit of implementation detail that is invisible to outside users and objects, including Style objects. The only way to manipulate the content of the control template is from within the same control template.

	public System.Windows.Controls.ControlTemplate Template { get; set; }

	<Style TargetType="Button">
	  <!--Set to true to not get any properties from the themes.-->
	  <Setter Property="OverridesDefaultStyle" Value="True"/>
	  <Setter Property="Template">
	    <Setter.Value>
	      <ControlTemplate TargetType="Button">
	        <Grid>
	          <Ellipse Fill="{TemplateBinding Background}"/>
	          <ContentPresenter HorizontalAlignment="Center"
	                            VerticalAlignment="Center"/>
	        </Grid>
	      </ControlTemplate>
	    </Setter.Value>
	  </Setter>
	</Style>

# Content绑定
由于使用了CT, Button的内容被完全自定义了; 那如何在新的CT中使用Button原有的Content呢? 我们当然可以手动在CT中添加一个控件, 并将其Content绑定到TemplatedParent上。可以使用ControlTemplate，也可以使用WPF提供的内建的方法ContentPresenter。

	//使用ContentPresenter
    <Button Content="xxcvsdfds" >
        <Button.Template>
            <ControlTemplate >
                <Grid>
                    <Ellipse Width="20" Height="20" Fill="Red"></Ellipse>
                    <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" 
                                      Content="{Binding Content, RelativeSource={RelativeSource TemplatedParent}}"
                                      ContentTemplate="{Binding ContentTemplate, RelativeSource={RelativeSource TemplatedParent}}"/>
                </Grid>
            </ControlTemplate>
        </Button.Template>
    </Button>

	//使用ControlTemplate
    <Button Content="xxcvsdfds" >
        <Button.Template>
            <ControlTemplate >
                <Grid>
                    <Ellipse Width="20" Height="20" Fill="Red"></Ellipse>
                    <ContentControl HorizontalAlignment="Center" VerticalAlignment="Center"
                                    Content="{Binding Content, RelativeSource={RelativeSource TemplatedParent}}"
                                    ContentTemplate="{Binding ContentTemplate, RelativeSource={RelativeSource TemplatedParent}}"/>
                </Grid>
            </ControlTemplate>
        </Button.Template>
    </Button>

# Border
定义按钮的标准可视化外观。

# ContentPresenter
存储提供的所有内容

# TemplateBinding模板绑定
1. TemplateBinding的数据绑定是单向的，从数据源到目标(即从应用Template的控件到Template)，Binding的数据绑定方式是能够经过Mode设置的，可单向、双向等。数据类型1. 
1. TemplateBinding不能对数据对象进行自动转换，数据源和目标的数据类型若不一样，须要本身写转换器。Bing会对数据源和目标的数据类型进行自动转换。数据1. 
1. TemplateBinding是Binding的特殊状况。TemplateBinding等价于

		{Binding RelativeSource={RelativeSource TemplatedParent}，Path=属性名}

		Content="{TemplateBinding  Content}"
		//相当于
		Content="{Binding Content, RelativeSource={RelativeSource TemplatedParent}}"     


# 绑定自己
	{Binding ActualHeight, RelativeSource={RelativeSource Self}}

# 触发器修改背景颜色
使用控件模板触发器，当修改button的IsEnabled值时，触发修改背景颜色。

    <Button Name="BtnConncetion" IsEnabled="True" Content="Connect" Cursor="Hand" Foreground="White" Click="BtnConncetion_Click" Width="74"  Height="36" HorizontalAlignment="Right" Margin="0,-60,37,0"  >
        <Button.Template>
            <ControlTemplate TargetType="{x:Type Button}">
                <Border BorderBrush="{TemplateBinding Control.BorderBrush}" Background="{TemplateBinding Button.Background}" BorderThickness="0" CornerRadius="5,5,5,5" Name="PART_Background">
                    <ContentPresenter Content="{TemplateBinding ContentControl.Content}" HorizontalAlignment="Center" VerticalAlignment="Center" />
                </Border>
                <ControlTemplate.Triggers >
                    <Trigger Property="Button.IsEnabled" Value="True">
                        <Setter Property="Button.Background" Value="#33CCFF"/>
                    </Trigger >
                    <Trigger Property="Button.IsEnabled" Value="False">
                        <Setter Property="Button.Background" Value="#CCCCCC"/>
                    </Trigger >
                </ControlTemplate.Triggers >
            </ControlTemplate>
        </Button.Template>
    </Button>