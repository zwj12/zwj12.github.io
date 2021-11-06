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
如果程序访问的是HTTPS安全网站，那么服务器会发送证书信息给客户端，客户端需要设置回调函数并验证证书是否可信。回调函数可以在两个地方验证，一个是在全局的ServicePointManager对象属性ServerCertificateValidationCallback中设置，一个是在HttpWebRequest对象属性ServerCertificateValidationCallback中设置，证书只会验证一次，所以即使两个地方都设置了回调函数，此时也只会在HttpWebRequest.ServerCertificateValidationCallback指定的回调函数中验证。

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


