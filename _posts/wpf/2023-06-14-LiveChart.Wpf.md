---
layout: post
title: "LiveChart.Wpf"
date: 2023-06-14 09:09:00 +0800
author: Michael
categories: CSharp
---

# NuGet包
	LiveCharts.Wpf

# XAML

    <Window x:Class="WpfApp6.MainWindow"
            xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
            xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
            xmlns:local="clr-namespace:WpfApp6"
            xmlns:lvc="clr-namespace:LiveCharts.Wpf;assembly=LiveCharts.Wpf"
            mc:Ignorable="d"
            Title="MainWindow" Height="450" Width="800">
        <Grid>
            <lvc:CartesianChart Name="chart_Test" LegendLocation="Top" Background="#FFEFD5">
                <lvc:CartesianChart.Series >
                    <lvc:LineSeries DataLabels="False" Stroke="#32CD32" StrokeThickness="1"   StrokeDashArray="5"
                                    LineSmoothness="1" Foreground="Red"
                                    Fill="#FFA07A" PointGeometrySize="10"   
                                    Values="1,2,5,1,5,4">
                        <lvc:LineSeries.PointGeometry>
                            <GeometryGroup>
                                <RectangleGeometry Rect="50,50,25,25" />
                            </GeometryGroup>
                        </lvc:LineSeries.PointGeometry>
                    </lvc:LineSeries>
                    <lvc:LineSeries Values="2,4,6,8,10,12"/>
                </lvc:CartesianChart.Series>

                <lvc:CartesianChart.AxisY>
                    <lvc:Axis Title="Value"  ShowLabels="True">
                        <lvc:Axis.Separator>
                            <lvc:Separator StrokeThickness="1" Stroke="Red"  />
                        </lvc:Axis.Separator>
                    </lvc:Axis>
                </lvc:CartesianChart.AxisY>

                <lvc:CartesianChart.AxisX>
                    <lvc:Axis Title="Type"  LabelsRotation="45" Labels="A,B,C,D,E,F" ShowLabels="True" >
                        <lvc:Axis.Separator>
                            <lvc:Separator StrokeThickness="1" Stroke="Red"  />
                        </lvc:Axis.Separator>
                    </lvc:Axis>
                </lvc:CartesianChart.AxisX>

                <lvc:CartesianChart.VisualElements>
                    <lvc:VisualElement X="0.5" Y="8">
                        <lvc:VisualElement.UIElement>
                            <TextBlock Foreground="Green">
                                Hello!, this is a note merged in the chart.
                            </TextBlock>
                        </lvc:VisualElement.UIElement>
                    </lvc:VisualElement>
                </lvc:CartesianChart.VisualElements>
            </lvc:CartesianChart>
        </Grid>
    </Window>
