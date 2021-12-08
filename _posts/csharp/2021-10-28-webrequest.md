---
layout: post
title: "WebRequest"
date: 2021-10-28 19:42:00 +0800
author: Michael
categories: CSharp
---

# Fiddler抓包
如果要使用Fiddler抓本机的数据包，那么必须使用本机的计算机名作为网址，不能使用localhost或者127.0.0.1

# 证书
如果程序访问的是HTTPS安全网站，那么服务器会发送证书信息给客户端，客户端需要设置回调函数并验证证书是否可信。回调函数可以在两个地方验证，一个是在全局的ServicePointManager对象属性ServerCertificateValidationCallback中设置，一个是在HttpWebRequest对象属性ServerCertificateValidationCallback中设置，证书只会验证一次，所以即使两个地方都设置了回调函数，此时也只会在HttpWebRequest.ServerCertificateValidationCallback指定的回调函数中验证。即使HttpWebRequest.ServerCertificateValidationCallback返回false，也不会继续再尝试ServicePointManager.ServerCertificateValidationCallback。
注意如果使用Fiddler抓包代理的话，程序是不会验证证书的，具体原因不明。

	//ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls | SecurityProtocolType.Tls11 | SecurityProtocolType.Tls12;
	ServicePointManager.ServerCertificateValidationCallback = delegate (Object obj, X509Certificate certificate, X509Chain chain, SslPolicyErrors errors) { return true; };

	//or
	request.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult);
	public bool CheckValidationResult(object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors errors)
	{
	    var store = new X509Store(StoreName.My, StoreLocation.CurrentUser);
	    store.Open(OpenFlags.OpenExistingOnly | OpenFlags.ReadWrite);
	    var storeCollection = store.Certificates;
	    store.Close();
	
	    var findResult = storeCollection.Find(X509FindType.FindBySerialNumber, certificate.GetSerialNumberString(), false);
	
	    if (findResult.Count > 0)
	    {
	        foreach (X509Certificate2 x509 in findResult)
	        {
	            if (x509.Subject == certificate.Subject &&
	                x509.GetPublicKeyString() == certificate.GetPublicKeyString())
	
	                return true;
	        }
	    }
	
	    return false;
	}

# HttpClient and HttpWebRequest
HttpWebRequest的默认CookieContainer是null，但是HttpClientHandler的默认UseCookies是ture。所以如果使用HttpWebRequest获取HTTP数据的话，默认是禁用cookie的，但是如果使用HttpClient，默认是启用cookie的，所以推荐使用HttpClient，因为HttpClient更符合日常使用习惯。

# HttpClient
因为HttpClient很多属性是非线程安全的，所以一旦调用了第一条request指令后，大多数属性就不能再修改了，例如设置Credentials，如果需要修改验证的用户名和密码，需要重新new一个HttpClient。