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