---
layout: post
title: "Xml Serialization "
date: 2021-12-02 11:11:00 +0800
author: Michael
categories: CSharp
---

# XmlRoot
使用XmlRoot标注根节点，该属性用于标准类，而不是类字段。

# XmlElement
默认情况下，XML序列化会直接使用类属性名称作为xml元素的名称。但是如果确实需要让类属性名称和xml元素名称不一致，可以使用XmlElement特性注解。下面示例使用该功能格式化日期  

	<Date>2021-12-01 09:17:07</Date>


    [XmlIgnore]
    public DateTime Date { get; set; }

    [XmlElement("Date")]
    public string Date2
    {
        get { return Date.ToString("yyyy-MM-dd HH:mm:ss"); }
        set { Date = DateTime.Parse(value); }
    }

# XmlTextAttribute
如果需要对字符串元素设置特性，那么需要新建一个类，使用XmlTextAttribute特性注解。

	<CalibrationWarp dt:dt="bin.base64" xmlns:dt="dt">This is a test</CalibrationWarp>


    public class CalibrationWarp
    {       
        [XmlNamespaceDeclarations]
        public XmlSerializerNamespaces Xmlns { get; set; }

        [XmlAttribute( Namespace ="dt")]
        public string dt { get; set; }

        [XmlTextAttribute()]
        public string Value { get; set; }

    }

# XmlAttribute
类的字段默认会转化为xml的元素，如果需要把类的字段转换为xml的属性，可以使用XmlAttribute注解。

    [XmlAttribute]
    public string Name { get; set; }

# XmlArrayItem
设置xml中列表元素的元素名。

    public class IRC5
    {
        [XmlAttribute]
        public string Name { get; set; }

        [XmlAttribute]
        public Guid Id { get; set; }

        public Gui Gui { get; set; }

        [XmlArrayItem(ElementName = "Robot")]
        public List<RobotInIRC5> Robots { get; set; }

        public Motion Motion { get; set; }

        public IRC5()
        {
            //Robots = new List<RobotInIRC5>();
            //Motion = new Motion();
        }

    }


    <Irc5 Name="PMController_1" Id="3e6fe840-a6f2-40e2-aedf-46bfda6c5f1e">
      <Gui>
        <X>0</X>
        <Y>0</Y>
        <Width>50</Width>
        <Heigth>63</Heigth>
        <ShowName>true</ShowName>
      </Gui>
      <Robots>
        <Robot Id="759d8699-3b8e-4a25-b59f-a99607a9541e" />
      </Robots>
      <Motion>
        <SystemId>{9705339F-8CD8-46C8-ACC5-261AC0AA3A0D}</SystemId>
        <User>Default User</User>
        <Password>robotics</Password>
        <Robot>
          <Task>T_ROB1</Task>
          <Id>759d8699-3b8e-4a25-b59f-a99607a9541e</Id>
        </Robot>
      </Motion>
    </Irc5>

# 数组列表
默认情况下，如果使用List直接序列化xml元素，会直接生产一个父节点，可以把该List标记为XmlElement，会自动消除这个父节点。

    public class Modified:Version
    {
        public string OperatingSystem { get; set; }

        public string User { get; set; }

        public string Computer { get; set; }

        [XmlElement()]
        public List<string> IpAddress { get; set; }

    }
	
	  <Modified>
	    <Date>2021-12-01 09:17:07</Date>
	    <Major>0</Major>
	    <Minor>0</Minor>
	    <Build>0</Build>
	    <OperatingSystem>Microsoft Windows NT 10.0.19042.0</OperatingSystem>
	    <User>CNMIZHU7</User>
	    <Computer>CN-L-7256975</Computer>
	    <IpAddress>192.168.2.100</IpAddress>
	    <IpAddress>192.168.56.1</IpAddress>
	    <IpAddress>fe80::1e:5be:737b:411f%11</IpAddress>
	    <IpAddress>fe80::a162:9311:906b:404f%9</IpAddress>
	    <IpAddress>fe80::281c:f96d:8733:c217%13</IpAddress>
	    <IpAddress>2001:0:2851:b9f0:281c:f96d:8733:c217</IpAddress>
	  </Modified>


    [XmlRoot("LogMessages")]
    public class RIS2WSLogMessages
    {
        [XmlElement("LogMessage")]
        public List<RIS2WSLogMessage> LogMessages{ get; set; }
    }

# XmlNamespaceDeclarations
如果xml节点有命名空间定义，创建一个XmlSerializerNamespaces变量，使用XmlNamespaceDeclarations注解。

	<CalibrationWarp dt:dt="bin.base64" xmlns:dt="dt">This is a test</CalibrationWarp>


    public class CalibrationWarp
    {       
        [XmlNamespaceDeclarations]
        public XmlSerializerNamespaces Xmlns { get; set; }

        [XmlAttribute( Namespace ="dt")]
        public string dt { get; set; }

        [XmlTextAttribute()]
        public string Value { get; set; }

    }


# XmlArray And XmlArrayItem
对于数组列表，既可以设置父节点名称，也可以设置数组列表项名称

      <Z-GripLocation>
        <ApplyZ-GripLocation>0</ApplyZ-GripLocation>
      </Z-GripLocation>

    [XmlArray(ElementName = "Z-GripLocation")]
    [XmlArrayItem(ElementName = "ApplyZ-GripLocation")]
    public List<int> ZGripLocation { get; set; }

# Example

    public static class XmlHelper
    {

        public static T LoadFromXml<T>(string filePath)
        {
            object result = null;
            if (File.Exists(filePath))
            {
                using (StreamReader reader = new StreamReader(filePath))
                {
                    XmlSerializer xmlSerializer = new XmlSerializer(typeof(T));
                    result = xmlSerializer.Deserialize(reader);
                }
            }
            return (T)result;
        }

        public static void SaveToXml<T>(string filePath, T sourceObj)
        {
            if (!string.IsNullOrWhiteSpace(filePath) && sourceObj != null)
            {
                using (StreamWriter writer = new StreamWriter(filePath))
                {
                    XmlSerializer xmlSerializer = new XmlSerializer(sourceObj.GetType());
                    XmlSerializerNamespaces nameSpace = new XmlSerializerNamespaces();
                    nameSpace.Add("", ""); //replace default namespace with empty namespace
                    xmlSerializer.Serialize(writer, sourceObj, nameSpace);
                }
            }
        }

    }