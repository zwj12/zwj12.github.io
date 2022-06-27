---
layout: post
title: "AutoMapper"
date: 2022-06-03 16:37:00 +0800
author: Michael
categories: CSharp
---

# 
    public class Model
    {
        public int SomeValue { get; set; }
        public string AnotherValue { get; set; }
    }
 
    public class ViewModel
    {
        public int SomeValue { get; set; }
        public string AnotherValue { get; set; }
    }

	public static class AutoMapperConfiguration
    {
        public static void Init()
        {
            MapperConfiguration = new MapperConfiguration(cfg =>
            {
 
                #region
                //将领域实体映射到视图实体
                cfg.CreateMap<Model, ViewModel>();
                #endregion
            });
 
            Mapper = MapperConfiguration.CreateMapper();
        }
 
        public static IMapper Mapper { get; private set; }
 
        public static MapperConfiguration MapperConfiguration { get; private set; }
    }

    public class AutoMapperStartupTask
    {
        public void Execute()
        {
            AutoMapperConfiguration.Init();
        }
    }

    public static class MappingExtensions
    {
        public static TDestination MapTo<TSource, TDestination>(this TSource source)
        {
            return AutoMapperConfiguration.Mapper.Map<TSource, TDestination>(source);
        }
 
        public static TDestination MapTo<TSource, TDestination>(this TSource source, TDestination destination)
        {
            return AutoMapperConfiguration.Mapper.Map(source, destination);
        }
 
        #region     
        public static ViewModel ToViewModel(this Model entity)
        {
            return entity.MapTo<Model, ViewModel>();
        }
 
        public static Model ToModel(this ViewModel model)
        {
            return model.MapTo<ViewModel, Model>();
        }
        #endregion
    }

    class Program
    {
        static void Main(string[] args)
        {
 
            Model model = new Model
            {
                SomeValue = 100,
                AnotherValue = "10001"
            };
            //注册映射配置
            AutoMapperStartupTask auto = new AutoMapperStartupTask();
            auto.Execute();
 
            //接收映射结果
            ViewModel view = MappingExtensions.ToViewModel(model);
 
            Console.WriteLine("ViewModel.SomeValue:" + view.SomeValue);
            Console.WriteLine("ViewModel.AnotherValue:" + view.AnotherValue);
            Console.ReadKey();
        }
    }