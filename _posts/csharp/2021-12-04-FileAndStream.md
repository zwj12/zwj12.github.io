---
layout: post
title: "Check Write Permission"
date: 2021-12-04 17:36:00 +0800
author: Michael
categories: CSharp
---

# 确认程序是否对文件夹有写权限

	public bool CheckWritePermissionOnDir(string path, bool checkUserAccountControl = false)
    {
        bool writeAllow = false;
        bool writeDeny = false;
        bool administratorPermission = true;

        DirectorySecurity directorySecurity = Directory.GetAccessControl(path);
        if (directorySecurity==null)
        {
            return false;
        }
        
        AuthorizationRuleCollection authorizationRuleCollection = directorySecurity.GetAccessRules(true, true, typeof(NTAccount));
        //AuthorizationRuleCollection authorizationRuleCollection = directorySecurity.GetAccessRules(true, true, typeof(SecurityIdentifier));
        if (authorizationRuleCollection == null)
        {
            return false;
        }

        foreach (FileSystemAccessRule rule in authorizationRuleCollection)
        {
            if ((FileSystemRights.Write& rule.FileSystemRights) != FileSystemRights.Write)
            {
                continue;
            }
            if(rule.AccessControlType==AccessControlType.Allow)
            {
                writeAllow = true;
                if (rule.IdentityReference.Value=="BUILTIN\\Users" || rule.IdentityReference.Value == "NT AUTHORITY\\Authenticated Users")
                {
                    administratorPermission = false;
                }
            }
            else if (rule.AccessControlType == AccessControlType.Deny)
            {
                writeDeny = true;
            }
        }
        if (checkUserAccountControl)
        {
            return writeAllow && !writeDeny && !administratorPermission;
        }
        else
        {
            return writeAllow && !writeDeny;
        }

    }

# FileStream
写入文件

    using (FileStream DestinationStream = new FileStream(pathElogTextRegistryLocal, FileMode.Create))
    {
        await stream.CopyToAsync(DestinationStream);
    }

# FileStream与StreamReader区别
FileStream类提供了在文件中读写字节的方法，但经常使用StreamReader或 StreamWriter执行这些功能。这是因为FileStream类操作的是字节和字节数组，而StreamReader类操作的是字符数据。因此FileStream类既可以对文本文件进行读写也可以对多媒体文件进行读写，多用于对大文件进行读写，且它对文件可进行分步读写，减小内存压力。而StreamReader和StreamWriter类多用于对小文件读写。

- FileStream操作字节，更适合大文件。
- StreamReader操作字符，更适合小文件。