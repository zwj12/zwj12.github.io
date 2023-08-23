---
layout: post
title: "Cryptography"
date: 2023-08-21 10:36:00 +0800
author: Michael
categories: CSharp
---

# verify password
If you are just going to verify/validate the entered user name and password, use the Rfc2898DerivedBytes class (also known as Password Based Key Derivation Function 2 or PBKDF2). This is more secure than using encryption like Triple DES or AES because there is no practical way to go from the result of RFC2898DerivedBytes back to the password. You can only go from a password to the result. See Is it ok to use SHA1 hash of password as a salt when deriving encryption key and IV from password string? for an example and discussion for .Net or String encrypt / decrypt with password c# Metro Style for WinRT/Metro.

# Store password
If you are storing the password for reuse, such as supplying it to a third party, use the Windows Data Protection API (DPAPI). This uses operating system generated and protected keys and the Triple DES encryption algorithm to encrypt and decrypt information. This means your application does not have to worry about generating and protecting the encryption keys, a major concern when using cryptography.In C#, use the System.Security.Cryptography.ProtectedData class. For example, to encrypt a piece of data, use ProtectedData.Protect():

    // Generate additional entropy (will be used as the Initialization vector)
    byte[] entropy = new byte[20];
    using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
    {
        rng.GetBytes(entropy);
    }

    string plaintext = "\"Hello World!\"";
    byte[] plaintextBytes = Encoding.UTF8.GetBytes(plaintext);

    byte[] ciphertext = ProtectedData.Protect(plaintextBytes, entropy, DataProtectionScope.CurrentUser);

    byte[] plaintextBytes2 = ProtectedData.Unprotect(ciphertext, entropy, DataProtectionScope.CurrentUser);

    string plaintext2 = Encoding.UTF8.GetString(plaintextBytes2).Trim(); 

# Credential Manager
## C++ codes

    #include <iostream>
    #include <windows.h>
    #include <wincred.h>
    #include <wchar.h>
    #pragma hdrstop

    #pragma comment(lib, "advapi32.lib")  // Or pass it to the cl command line.

    int main()
    {

        { //--- SAVE
            char password[] = "brillant";
            DWORD cbCreds = 1 + strlen(password);

            CREDENTIALW cred = { 0 };
            cred.Type = CRED_TYPE_GENERIC;
            cred.TargetName = L"FOO/account";
            cred.CredentialBlobSize = cbCreds;
            cred.CredentialBlob = (LPBYTE)password;
            cred.Persist = CRED_PERSIST_LOCAL_MACHINE;
            cred.UserName = L"paula";

            BOOL ok = ::CredWriteW(&cred, 0);
            wprintf(L"CredWrite() - errno %d\n", ok ? 0 : ::GetLastError());
            if (!ok) exit(1);
        }
        { //--- RETRIEVE
            PCREDENTIALW pcred;
            BOOL ok = ::CredReadW(L"FOO/account", CRED_TYPE_GENERIC, 0, &pcred);
            wprintf(L"CredRead() - errno %d\n", ok ? 0 : ::GetLastError());
            if (!ok) exit(1);
            wprintf(L"Read username = '%s', password='%S' (%d bytes)\n",
                pcred->UserName, (char*)pcred->CredentialBlob, pcred->CredentialBlobSize);
            // Memory allocated by CredRead() must be freed!
            ::CredFree(pcred);
        }

        std::cout << "Hello World!\n";
    }

## C# Codes

    /// <summary>         
    /// 凭据类型         
    /// </summary> 
    public enum CRED_TYPE : uint
    {
        //普通凭据
        GENERIC = 1,
        //域密码 
        DOMAIN_PASSWORD = 2,
        //域证书 
        DOMAIN_CERTIFICATE = 3,
        //域可见密码 
        DOMAIN_VISIBLE_PASSWORD = 4,
        //一般证书 
        GENERIC_CERTIFICATE = 5,
        //域扩展 
        DOMAIN_EXTENDED = 6,
        //最大 
        MAXIMUM = 7,
        // Maximum supported cred type 
        MAXIMUM_EX = (MAXIMUM + 1000),  // Allow new applications to run on old OSes 
    }

    //永久性 
    public enum CRED_PERSIST : uint
    {
        SESSION = 1,             //本地计算机 
        LOCAL_MACHINE = 2,             //企业 
        ENTERPRISE = 3,
    }

    internal class NativeCredMan
    {
        [DllImport("Advapi32.dll", EntryPoint = "CredReadW", CharSet = CharSet.Unicode, SetLastError = true)]
        //读取凭据信息 
        static extern bool CredRead(string target, CRED_TYPE type, int reservedFlag, out IntPtr CredentialPtr);

        [DllImport("Advapi32.dll", EntryPoint = "CredWriteW", CharSet = CharSet.Unicode, SetLastError = true)]
        //增加凭据 
        static extern bool CredWrite([In] ref NativeCredential userCredential, [In] UInt32 flags);

        [DllImport("Advapi32.dll", EntryPoint = "CredFree", SetLastError = true)]
        static extern bool CredFree([In] IntPtr cred);

        [DllImport("Advapi32.dll", EntryPoint = "CredDeleteW", CharSet = CharSet.Unicode)]
        //删除凭据 
        static extern bool CredDelete(string target, CRED_TYPE type, int flags);

        //[DllImport("advapi32", SetLastError = true, CharSet = CharSet.Unicode)] 
        //static extern bool CredEnumerateold(string filter, int flag, out int count, out IntPtr pCredentials); 

        [DllImport("advapi32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
        public static extern bool CredEnumerate(string filter, uint flag, out uint count, out IntPtr pCredentials);

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        public struct NativeCredential
        {
            public UInt32 Flags;
            public CRED_TYPE Type;
            public IntPtr TargetName;
            public IntPtr Comment;
            public System.Runtime.InteropServices.ComTypes.FILETIME LastWritten;
            public UInt32 CredentialBlobSize;
            public IntPtr CredentialBlob;
            public UInt32 Persist;
            public UInt32 AttributeCount;
            public IntPtr Attributes;
            public IntPtr TargetAlias;
            public IntPtr UserName;
            internal static NativeCredential GetNativeCredential(Credential cred)
            {
                var ncred = new NativeCredential
                {
                    AttributeCount = 0,
                    Attributes = IntPtr.Zero,
                    Comment = IntPtr.Zero,
                    TargetAlias = IntPtr.Zero,                                       
                    Type = cred.Type,
                    Persist = (UInt32)cred.Persist,
                    CredentialBlobSize = (UInt32)cred.CredentialBlobSize,
                    TargetName = Marshal.StringToCoTaskMemUni(cred.TargetName),
                    CredentialBlob = Marshal.StringToCoTaskMemUni(cred.CredentialBlob),
                    UserName = Marshal.StringToCoTaskMemUni(cred.UserName)
                };
                return ncred;
            }

            internal static Credential ToCredential(NativeCredential cred)
            {
                var ncred = new Credential
                {
                    AttributeCount = 0,
                    Attributes = IntPtr.Zero,
                    Comment = string.Empty,
                    TargetAlias = string.Empty,                                     
                    Type = cred.Type,
                    Persist =  (CRED_PERSIST)cred.Persist,
                    CredentialBlobSize = (UInt32)cred.CredentialBlobSize,
                    TargetName = Marshal.PtrToStringUni(cred.TargetName),
                    CredentialBlob = Marshal.PtrToStringUni(cred.CredentialBlob),
                    UserName = Marshal.PtrToStringUni(cred.UserName)
                };
                return ncred;
            }
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        public struct Credential
        {
            public UInt32 Flags;
            public CRED_TYPE Type;
            public string TargetName;
            public string Comment;
            public System.Runtime.InteropServices.ComTypes.FILETIME LastWritten;
            public UInt32 CredentialBlobSize;
            public string CredentialBlob;
            public CRED_PERSIST Persist;
            public UInt32 AttributeCount;
            public IntPtr Attributes;
            public string TargetAlias;
            public string UserName;
        }
        /// <summary> 
        /// 向添加计算机的凭据管理其中添加凭据             
        /// </summary> 
        /// <param name="key">internet地址或者网络地址</param>             
        /// <param name="userName">用户名</param>             
        /// <param name="secret">密码</param>             
        /// <param name="type">密码类型</param>             
        /// <param name="credPersist"></param>             
        /// <returns></returns> 
        public static int WriteCred(string key, string userName, string secret, CRED_TYPE type, CRED_PERSIST credPersist)
        {
            var byteArray = Encoding.Unicode.GetBytes(secret);
            if (byteArray.Length > 512)
                throw new ArgumentOutOfRangeException("The secret message has exceeded 512 bytes.");
            var cred = new Credential
            {
                TargetName = key,
                CredentialBlob = secret,
                CredentialBlobSize = (UInt32)Encoding.Unicode.GetBytes(secret).Length,
                AttributeCount = 0,
                Attributes = IntPtr.Zero,
                UserName = userName,
                Comment = null,
                TargetAlias = null,
                Type = type,
                Persist = credPersist
            };
            var ncred = NativeCredential.GetNativeCredential(cred);
            var written = CredWrite(ref ncred, 0);
            var lastError = Marshal.GetLastWin32Error();
            if (written)
            {
                return 0;
            }

            var message = "";
            if (lastError == 1312)
            {
                message = (string.Format("Failed to save " + key + " with error code {0}.", lastError)
                + "  This error typically occurrs on home editions of Windows XP and Vista.  Verify the version of Windows is Pro/Business or higher.");
            }
            else
            {
                message = string.Format("Failed to save " + key + " with error code {0}.", lastError);
            }
            MessageBox.Show(message);
            return 1;
        }

        /// <summary>            
        /// 读取凭据            
        /// </summary> 
        /// <param name="targetName"></param>            
        /// <param name="credType"></param>            
        /// <param name="reservedFlag"></param> 
        /// <param name="intPtr"></param>            
        /// <returns></returns> 
        public static bool WReadCred(string targetName, CRED_TYPE credType, int reservedFlag, out IntPtr intPtr)
        {
            return CredRead(targetName, credType, reservedFlag, out intPtr);
        }

        /// <summary>             
        /// 删除凭据             
        /// </summary> 
        /// <param name="target"></param>             
        /// <param name="type"></param>             
        /// <param name="flags"></param>             
        /// <returns></returns> 
        public static bool DeleteCred(string target, CRED_TYPE type, int flags)
        {
            return CredDelete(target, type, flags);
        }
    }

    private void btnRead_Click(object sender, RoutedEventArgs e)
    {
        string targetName = txtIP.Text.Trim();
        IntPtr intPtr = new IntPtr();
        bool flag = false;
        try
        {
            flag = NativeCredMan.WReadCred(targetName, CRED_TYPE.GENERIC, 1, out intPtr);
            NativeCredMan.NativeCredential x= Marshal.PtrToStructure<NativeCredMan.NativeCredential>(intPtr);
            NativeCredMan.Credential y= NativeCredMan.NativeCredential.ToCredential(x);
        }
        catch
        {
            flag = false;
        }

        if (flag)
            txtMsg.Text = "该凭据已存在";
        else
            txtMsg.Text = "该凭据目前不存在";
    }

    private void btnWrite_Click(object sender, RoutedEventArgs e)
    {
        //ip地址或者网络路径 例如：TERMSRV/192.168.2.222             
        string key = txtIP.Text.Trim();
        string userName = txtUserName.Text.Trim();
        string password = txtPassword.Text.Trim();
        //用于标记凭据添加是否成功 i=0:添加成功；i=1:添加失败             
        int i = 0;
        try
        {
            i = NativeCredMan.WriteCred(key,
            userName,
            password,
            CRED_TYPE.GENERIC,
            CRED_PERSIST.LOCAL_MACHINE);
        }
        catch
        {
            i = 1;
        }
        if (i == 0)
            txtMsg.Text = "添加成功";
        else
            txtMsg.Text = "添加失败";
    }

    private void btnDelete_Click(object sender, RoutedEventArgs e)
    {
        string targetName = txtIP.Text.Trim();
        bool flag = false;
        try
        {
            flag = NativeCredMan.DeleteCred(targetName, CRED_TYPE.GENERIC, 0);
        }
        catch
        {
            flag = false;
        }

        if (flag)
            txtMsg.Text = "该凭据已删除";
        else
            txtMsg.Text = "删除失败";
    }