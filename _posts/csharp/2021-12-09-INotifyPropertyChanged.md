---
layout: post
title: "INotifyPropertyChanged"
date: 2021-12-09 19:36:00 +0800
author: Michael
categories: CSharp
---

# INotifyPropertyChanged

	public class Person : INotifyPropertyChanged
	{
		private string name;
		// Declare the event
		public event PropertyChangedEventHandler PropertyChanged;
		
		public Person()
		{
		}
		
		public Person(string value)
		{
		  this.name = value;
		}
		
		public string PersonName
		{
		  get { return name; }
		  set
		  {
		      name = value;
		      // Call OnPropertyChanged whenever the property is updated
		      OnPropertyChanged();
		  }
		}
		
		// Create the OnPropertyChanged method to raise the event
		// The calling member's name will be used as the parameter.
		protected void OnPropertyChanged([CallerMemberName] string name = null)
		{
		  PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
		}
	}

# CallerMemberName
在.Net 4.5中引入了三个Attribute：CallerMemberName、CallerFilePath和CallerLineNumber 。在编译器的配合下，分别可以获取到调用函数（准确讲应该是成员）名称，调用文件及调用行号。函数定义时，参数必须设置为可选参数，在函数调用时，如果确实该参数，则有编译器自动添加对应的属性值，如果设置了参数，则使用调用时传过来的参数。  
 
    public void WriteError(object message,
    [CallerMemberName] string memberName = "",
    [CallerFilePath] string sourceFilePath = "",
    [CallerLineNumber] int sourceLineNumber = 0)
    {
        _log4Net.ErrorFormat("文件:{0} 行号:{1} 方法名:{2},消息:{3}", sourceFilePath, sourceLineNumber, memberName, message);
    }

#WPF控件主动刷新数据
     this.listBoxControllerID.Items.Refresh();