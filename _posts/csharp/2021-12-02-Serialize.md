---
layout: post
title: "Serialize"
date: 2021-12-02 11:10:00 +0800
author: Michael
categories: CSharp
---

# SerializableAttribute 
当一个类标记为SerializableAttribute 特性时，那么这个类就可以直接调用Serialize和Deserialize 函数进行类数据的序列化和反序列化。例如使用BinaryFormatter进行序列化时，一定要指定类的SerializableAttribute特性，否则运行时会报异常。但是，不是所有的类在序列化或反序列化时都需要SerializableAttribute特性，比如XmlSerializer序列化或反序列化就不需要该特性。

    [Serializable]
    public class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    public static void Main(string[] args)
    {
        Person person = new Person { Name = "John Doe", Age = 30 };

        // Serialize the object to a file
        using (FileStream fs = new FileStream("person1.dat", FileMode.Create))
        {
            BinaryFormatter formatter = new BinaryFormatter();
            formatter.Serialize(fs, person);
        }

        // Deserialize the object from the file
        using (FileStream fs = new FileStream("person1.dat", FileMode.Open))
        {
            BinaryFormatter formatter = new BinaryFormatter();
            Person deserializedPerson = (Person)formatter.Deserialize(fs);
            Console.WriteLine($"Name: {deserializedPerson.Name}, Age: {deserializedPerson.Age}");
        }

        // Serialize the object to a file
        using (FileStream fs = new FileStream("person.xml", FileMode.Create))
        {
            XmlSerializer serializer = new XmlSerializer(typeof(Person));
            serializer.Serialize(fs, person);
        }

        // Deserialize the object from the file
        using (FileStream fs = new FileStream("person.xml", FileMode.Open))
        {
            XmlSerializer serializer = new XmlSerializer(typeof(Person));
            Person deserializedPerson = (Person)serializer.Deserialize(fs);
            Console.WriteLine($"Name: {deserializedPerson.Name}, Age: {deserializedPerson.Age}");
        }
        
        Console.ReadKey();

    }



![日志文件夹](/assets/csharp/SerializationException.png)   
    