---
layout: post
title: "IValueConveyor"
date: 2023-10-26 09:09:00 +0800
author: Michael
categories: WPF
---

# IValueConverter

    [ValueConversion(typeof(Visibility), typeof(string))]
    public class VisibilityStringConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            Visibility visibility = (Visibility)value;
            return visibility.ToString();
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            string visibility = value.ToString().ToLower();
            Visibility result = Visibility.Collapsed;
            if (visibility == "true" || visibility == "visible")
            {
                result = Visibility.Visible;
            }
            return result;
        }
    }

    [ValueConversion(typeof(string), typeof(Visibility))]
    public class StringVisibilityConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            string visibility = value.ToString();
            Visibility result = Visibility.Collapsed;
            if (visibility == "true" || visibility == "visible")
            {
                result = Visibility.Visible;
            }
            return result;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            Visibility visibility = (Visibility)value;
            return visibility.ToString();
        }
    }

# StaticResource
    xmlns:Converters="clr-namespace:PMTW.PMOP.WPF.SolutionExplorer.Converters"

    <Converters:VisibilityStringConverter x:Key="VisibilityStringConverter"/>
    <Converters:StringVisibilityConverter x:Key="StringVisibilityConverter"/>

    <CheckBox Content="&#x2713;" Foreground="White" IsEnabled="False" 
                Template="{StaticResource CheckBoxTemplate}"
                IsChecked="{Binding Path=Element[IsLoaded].Value}" Visibility="{Binding Path=Element[IsLoaded].Value, Converter={StaticResource StringVisibilityConverter}}"/>
