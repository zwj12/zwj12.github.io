---
layout: post
title: "AddInUtility"
date: 2022-10-13 19:44:00 +0800
author: Michael
categories: zenon
---

# 手动生成scadaAddIn程序包
	"C:\Program Files (x86)\ABB\zenon 8.00 SP0\AddInFramework\AddInUtility.exe" -a BuildPackage -p AddInProjectService1.dll

# dll打包策略
貌似.net库的dll和zenon的dll是不会被打包的，为什么？如果想让自己的dll不打包，应如何操作。

# AnalyzerConfiguration
dll打包策略的配置文件在Scada.Internal.AddIn.Analysis的Resources中，在打包时，会匹配该文件的PublicKeyToken,如果一致就不会被打包。

	<?xml version="1.0" encoding="utf-8" ?>
	<AnalyzerConfiguration>
	  <!--<PlugInAssemblyReferences>
	    <AssemblyReference FullName="Scada.AddIn.Contracts, Version=8.00.0.0, Culture=neutral, PublicKeyToken=dbcf9a9c17b53ba" />
	  </PlugInAssemblyReferences>-->
	
	  <KeyTokenReferences>
	    <!-- .NET Framework -->
	    <KeyTokenReference PublicKeyToken="b77a5c561934e089" Type="NetFramework" />
	    <KeyTokenReference PublicKeyToken="31bf3856ad364e35" Type="NetFramework" />
	    <KeyTokenReference PublicKeyToken="b03f5f7f11d50a3a" Type="NetFramework" />
	    <!-- Mono.Addins -->
	    <KeyTokenReference PublicKeyToken="0738eb9f132ed756" Type="System" />
	    <!-- Scada -->
	    <KeyTokenReference PublicKeyToken="dbcf9a9c17b53bac" Type="System" />
	  </KeyTokenReferences>
	</AnalyzerConfiguration>

![日志文件夹](/assets/zenon/AnalyzerConfiguration.png)  

# 递归获取引用的dll代码

	using Mono.Cecil;
	using Scada.Common;
	using Scada.Internal.AddIn.Analysis.Configuration;
	using Scada.Internal.AddIn.Analysis.DependencySearching;
	using System;
	using System.Collections.Generic;
	using System.ComponentModel.Composition;
	using System.Linq;
	using System.Runtime.CompilerServices;
	using System.Threading.Tasks;
	
	namespace Scada.Internal.AddIn.Analysis
	{
		[Export(typeof(IReferenceAnalyzer)), PartCreationPolicy(CreationPolicy.NonShared)]
		internal class ReferenceAnalyzer : IReferenceAnalyzer
		{
			private readonly AnalyzerConfiguration _analyzerConfiguration;
	
			[Import]
			private IComposedSearchStrategy _dependencySearchStrategies;
	
			public ReferenceAnalyzer(AnalyzerConfiguration analyzerConfiguration)
			{
				this._analyzerConfiguration = analyzerConfiguration;
			}
	
			public ReferenceAnalyzer()
			{
				this._analyzerConfiguration = ConfigReader.GetDefaultAnalyzerConfiguration();
			}
	
			[AsyncStateMachine(typeof(ReferenceAnalyzer.<Analyze>d__4))]
			public Task<IEnumerable<IReferenceAssembly>> Analyze(string filePath)
			{
				ReferenceAnalyzer.<Analyze>d__4 <Analyze>d__;
				<Analyze>d__.<>4__this = this;
				<Analyze>d__.filePath = filePath;
				<Analyze>d__.<>t__builder = AsyncTaskMethodBuilder<IEnumerable<IReferenceAssembly>>.Create();
				<Analyze>d__.<>1__state = -1;
				AsyncTaskMethodBuilder<IEnumerable<IReferenceAssembly>> <>t__builder = <Analyze>d__.<>t__builder;
				<>t__builder.Start<ReferenceAnalyzer.<Analyze>d__4>(ref <Analyze>d__);
				return <Analyze>d__.<>t__builder.Task;
			}
	
			private void AnalyzeReferences(AssemblyDefinition assemblyDefinition, IAssemblyResolver assemblyResolver, List<ReferenceAssembly> referenceList)
			{
				ArgumentValidation.Validate("assemblyDefinition", assemblyDefinition);
				ArgumentValidation.Validate("referenceList", referenceList);
				this._dependencySearchStrategies.Search(assemblyDefinition).ToList<AssemblyNameReference>().ForEach(delegate(AssemblyNameReference x)
				{
					this.Analyze(assemblyResolver, referenceList, x);
				});
			}
	
			private void Analyze(IAssemblyResolver assemblyResolver, List<ReferenceAssembly> referenceList, AssemblyNameReference assemblyNameReference)
			{
				if (referenceList.Any((ReferenceAssembly x) => string.Compare(x.FullName, assemblyNameReference.get_FullName(), StringComparison.OrdinalIgnoreCase) == 0))
				{
					return;
				}
				string s = assemblyNameReference.get_PublicKeyToken().ToByteArrayString();
				ReferenceType referenceType = this._analyzerConfiguration.KeyTokenReferences.Any((KeyTokenReference x) => string.Compare(x.PublicKeyToken, s, StringComparison.OrdinalIgnoreCase) == 0) ? ReferenceType.System : ReferenceType.Foreign;
				if (referenceType == ReferenceType.System)
				{
					ReferenceAssembly item = new ReferenceAssembly(assemblyNameReference.get_FullName(), referenceType);
					referenceList.Add(item);
					return;
				}
				try
				{
					AssemblyDefinition assemblyDefinition = assemblyResolver.Resolve(assemblyNameReference.get_FullName());
					ReferenceAssembly item2 = new ReferenceAssembly(assemblyNameReference.get_FullName(), assemblyDefinition.get_MainModule().get_FullyQualifiedName(), referenceType);
					referenceList.Add(item2);
					this.AnalyzeReferences(assemblyDefinition, assemblyResolver, referenceList);
				}
				catch (AssemblyResolutionException ex)
				{
					throw new ReferenceNotFoundException(ex.Message, ex);
				}
			}
		}
	}

