---
layout: post
title: "HttpWebRequest "
date: 2021-09-01 12:59:00 +0800
author: Michael
categories: CSharp
---

# 安装Json库 
使用NuGet引用Newtonsoft.Json类库

# 代码
    class Program
    {
        static void Main(string[] args)
        {
            Stream streamResponse = null;
            StreamReader srResponse = null;
            Encoding encoding = Encoding.UTF8;

            HttpWebResponse response = null;
            HttpWebRequest request = null;

            request = WebRequest.Create(@"http://127.0.0.1:3333/webapi/user") as HttpWebRequest;
            CookieContainer cookieContainer = new CookieContainer();
            request.CookieContainer = cookieContainer;
            request.AllowAutoRedirect = true;
            request.Method = "GET";
            request.ContentType = "application/x-www-form-urlencoded";
            //request.ContentType = "application/xml";
            //request.Accept = "text/xml";
            response = request.GetResponse() as HttpWebResponse;
            streamResponse = response.GetResponseStream();
            srResponse = new StreamReader(streamResponse, encoding);
            string content = srResponse.ReadToEnd();
            List<User> users = JsonConvert.DeserializeObject<List<User>>(content);
            Console.WriteLine(users[0].UserName);

            Console.ReadKey();
        }

    }

    public class User
    {
        public int Id { get; set; }

        public string UserName { get; set; }

        public DateTime CreateTime { get { return DateTime.Now; } }
    }

# 设置返回编码格式为XML
	request.Accept = "text/xml";
