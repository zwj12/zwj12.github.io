---
layout: post
title: "ControlTemplate"
date: 2022-05-30 16:38:00 +0800
author: Michael
categories: WPF
---

# Border
定义按钮的标准可视化外观。

# ContentPresenter
存储提供的所有内容

# TemplateBinding模板绑定
1. TemplateBinding的数据绑定是单向的，从数据源到目标(即从应用Template的控件到Template)，Binding的数据绑定方式是能够经过Mode设置的，可单向、双向等。数据类型1. 
1. TemplateBinding不能对数据对象进行自动转换，数据源和目标的数据类型若不一样，须要本身写转换器。Bing会对数据源和目标的数据类型进行自动转换。数据1. 
1. TemplateBinding是Binding的特殊状况。TemplateBinding等价于

		{Binding RelativeSource={RelativeSource TemplatedParent}，Path=属性名}


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