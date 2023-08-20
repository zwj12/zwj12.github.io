---
layout: post
title: "Design Patterns"
date: 2023-08-19 10:36:00 +0800
author: Michael
categories: CSharp
---

# 创建型模式
## Singleton 单例模式

    public class LogService
    {
        #region Singleton

        /// <summary>
        /// Thread Safety Singleton
        /// </summary>  
        private static readonly Lazy<LogService> lazy = new Lazy<LogService>(() => new LogService());
        public static LogService Current
        {
            get
            {
                return lazy.Value;
            }
        }
        private LogService()
        {
        }

        #endregion
    }

## Factory Method 工厂方法
工厂方法模式是一种创建型设计模式，它提供了一种创建对象的接口，但允许子类决定实例化哪个类。工厂方法让类的实例化推迟到子类中进行。客户端代码不需要直接实例化产品类，而只需要依赖工厂接口，增加了程序的灵活性。

    // 抽象产品
    public interface IProduct
    {
        string Operation();
    }

    // 具体产品A
    public class ProductA : IProduct
    {
        public string Operation()
        {
            return "{Result of ProductA}";
        }
    }

    // 具体产品B
    public class ProductB : IProduct
    {
        public string Operation()
        {
            return "{Result of ProductB}";
        }
    }

    // 抽象创建者
    public abstract class Creator
    {
        public abstract IProduct FactoryMethod();
    }

    // 具体创建者A
    public class CreatorA : Creator
    {
        public override IProduct FactoryMethod()
        {
            return new ProductA();
        }
    }

    // 具体创建者B
    public class CreatorB : Creator
    {
        public override IProduct FactoryMethod()
        {
            return new ProductB();
        }
    }

## Abstract Factory 抽象工厂模式

## Builder 建造者模式
Car是我们要创建的产品，CarBuilder是抽象的建造者，定义了制造一个产品所需要的各个步骤，FerrariBuilder是具体的建造者，实现了CarBuilder定义的所有步骤，Director是指挥者，它告诉建造者应该按照什么顺序去执行哪些步骤。

    // 产品
    public class Car
    {
        public string Engine { get; set; }
        public string Wheels { get; set; }
        public string Doors { get; set; }
    }

    // 建造者抽象类
    public abstract class CarBuilder
    {
        protected Car car;

        public void CreateNewCar()
        {
            car = new Car();
        }

        public Car GetCar()
        {
            return car;
        }

        public abstract void SetEngine();
        public abstract void SetWheels();
        public abstract void SetDoors();
    }

    // 具体建造者
    public class FerrariBuilder : CarBuilder
    {
        public override void SetEngine()
        {
            car.Engine = "V8";
        }

        public override void SetWheels()
        {
            car.Wheels = "18 inch";
        }

        public override void SetDoors()
        {
            car.Doors = "2";
        }
    }

    // 指挥者
    public class Director
    {
        public Car Construct(CarBuilder carBuilder)
        {
            carBuilder.CreateNewCar();
            carBuilder.SetEngine();
            carBuilder.SetWheels();
            carBuilder.SetDoors();
            return carBuilder.GetCar();
        }
    }

## Prototype 原型模式

    // 抽象原型
    public interface IPrototype
    {
        IPrototype Clone();
    }

    // 具体原型
    public class ConcretePrototype : IPrototype
    {
        public string Name { get; set; }
        public int Value { get; set; }

        public IPrototype Clone()
        {
            // 实现深拷贝
            return (ConcretePrototype)this.MemberwiseClone(); // Clones the concrete object.
        }
    }

## Adapter 适配器模式
适配器模式主要应用于“希望复用一些现存的类，但是接口又与复用环境要求不一致”的情况，在遗留代码复用，类库迁移等方面非常有用。如将XML格式文件转换为JSON格式。适配器模式本身要求我们尽可能地使用“面向接口的编程方式”，这样才能在后期很方便地适配。

    /// <summary>
    /// 后续添加的接口 -- 需要适配的目标接口
    /// </summary>
    interface ICannon
    {
        void FireGun();
    }

    /// <summary>
    /// 对象适配器 -- 实现目标接口，适配发射类
    /// </summary>
    class Cannon : ICannon
    {
        private Shoot _Shoot;

        //public Cannon()
        //{
        //    this._Shoot = new Shoot();
        //}

        public Cannon(Shoot shoot)
        {
            this._Shoot = shoot;
        }

        public void FireGun()
        {
            this._Shoot.FireBullet();
            //使用一些Shoot的属性，来确定要发射什么样的炮弹
            Console.WriteLine(" --- 对象适配 发射炮弹 --- ");
        }
    }

    /// <summary>
    /// 类适配器 -- 实现目标接口，适配发射类
    /// 只能借用继承来实现，不能多继承而且是紧耦合 （很少使用）
    /// </summary>
    class CannonClass : Shoot, ICannon
    {
        public void FireGun()
        {
            base.FireBullet();
            //使用一些Shoot的属性，来确定要发射什么样的炮弹
            Console.WriteLine(" --- 类适配器 发射炮弹 --- ");
        }
    }

# 结构型模式
## Bridge 桥接模式
桥接模式是一种结构型设计模式，用于将抽象部分与其实现部分分离，使它们都可以独立地变化。
   // 实现类接口
   public interface IImplementor
   {
       void OperationImp();
   }

   // 具体实现类A
   public class ConcreteImplementorA : IImplementor
   {
       public void OperationImp()
       {
           Console.WriteLine("Concrete Implementor A");
       }
   }

   // 具体实现类B
   public class ConcreteImplementorB : IImplementor
   {
       public void OperationImp()
       {
           Console.WriteLine("Concrete Implementor B");
       }
   }

   // 抽象类
   public abstract class Abstraction
   {
       protected IImplementor implementor;

       public Abstraction(IImplementor implementor)
       {
           this.implementor = implementor;
       }

       public virtual void Operation()
       {
           implementor.OperationImp();
       }
   }

   // 扩充的抽象类
   public class RefinedAbstraction : Abstraction
   {
       public RefinedAbstraction(IImplementor implementor) : base(implementor) { }


       public override void Operation()
       {
           Console.WriteLine("Refined Abstraction is calling implementor's method:");
           base.Operation();
       }
   }

## Composite 组合模式
组合模式（Composite pattern）是一种结构型设计模式，它可以使你将对象组合成树形结构，并且能像使用独立对象一样使用它们。这种模式的主要目的是使单个对象和组合对象具有一致性。
    // 抽象组件类
    public abstract class Component
    {
        protected string name;

        public Component(string name)
        {
            this.name = name;
        }

        public abstract void Add(Component c);
        public abstract void Remove(Component c);
        public abstract void Display(int depth);
    }

    // 叶节点类
    public class Leaf : Component
    {
        public Leaf(string name) : base(name) { }


        public override void Add(Component c)
        {
            Console.WriteLine("Cannot add to a leaf");
        }

        public override void Remove(Component c)
        {
            Console.WriteLine("Cannot remove from a leaf");
        }

        public override void Display(int depth)
        {
            Console.WriteLine(new String('-', depth) + name);
        }
    }

    // 构件容器类
    public class Composite : Component
    {
        private List<Component> _children = new List<Component>();

        public Composite(string name) : base(name) { }

        public override void Add(Component component)
        {
            _children.Add(component);
        }

        public override void Remove(Component component)
        {
            _children.Remove(component);
        }

        public override void Display(int depth)
        {
            Console.WriteLine(new String('-', depth) + name);

            // 显示每个节点的子节点
            foreach (Component component in _children)
            {
                component.Display(depth + 2);
            }
        }
    }

## Decorator 装饰模式
装饰模式是一种结构型设计模式，它允许在运行时动态地将功能添加到对象中，这种模式提供了比继承更有弹性的解决方案。

    // 抽象组件
    public abstract class Component
    {
        public abstract string Operation();
    }

    // 具体组件
    public class ConcreteComponent : Component
    {
        public override string Operation()
        {
            return "ConcreteComponent";
        }
    }

    // 抽象装饰器
    public abstract class Decorator : Component
    {
        protected Component component;

        public Decorator(Component component)
        {
            this.component = component;
        }

        public override string Operation()
        {
            if (component != null)
            {
                return component.Operation();
            }
            else
            {
                return string.Empty;
            }
        }
    }

    // 具体装饰器A
    public class ConcreteDecoratorA : Decorator
    {
        public ConcreteDecoratorA(Component comp) : base(comp) { }


        public override string Operation()
        {
            return $"ConcreteDecoratorA({base.Operation()})";
        }
    }

    // 具体装饰器B
    public class ConcreteDecoratorB : Decorator
    {
        public ConcreteDecoratorB(Component comp) : base(comp) { }


        public override string Operation()
        {
            return $"ConcreteDecoratorB({base.Operation()})";
        }
    }

## Facade 外观模式
外观模式是一种结构型设计模式，提供了一个统一的接口，用来访问子系统中的一群接口。外观模式定义了一个高层接口，让子系统更容易使用。

    // 子系统A
    public class SubSystemA
    {
        public string OperationA()
        {
            return "SubSystemA, OperationA\n";
        }
    }

    // 子系统B
    public class SubSystemB
    {
        public string OperationB()
        {
            return "SubSystemB, OperationB\n";
        }
    }

    // 子系统C
    public class SubSystemC
    {
        public string OperationC()
        {
            return "SubSystemC, OperationC\n";
        }
    }

    // 外观类
    public class Facade
    {
        private SubSystemA a = new SubSystemA();
        private SubSystemB b = new SubSystemB();
        private SubSystemC c = new SubSystemC();

        public string OperationWrapper()
        {
            string result = "Facade initializes subsystems:\n";
            result += a.OperationA();
            result += b.OperationB();
            result += c.OperationC();
            return result;
        }
    }

## Flyweight 享元模式
享元模式（Flyweight Pattern）是一种结构型设计模式，该模式主要用于减少创建对象的数量，以减少内存占用和提高性能。这种类型的设计模式属于结构型模式，它提供了一种减少对象数量从而改善应用所需的对象结构的方式。

   // 享元类
   public class Flyweight
   {
       private string intrinsicState;

       // 构造函数
       public Flyweight(string intrinsicState)
       {
           this.intrinsicState = intrinsicState;
       }

       // 业务方法
       public void Operation(string extrinsicState)
       {
           Console.WriteLine($"Intrinsic State = {intrinsicState}, Extrinsic State = {extrinsicState}");
       }
   }

   // 享元工厂类
   public class FlyweightFactory
   {
       private Dictionary<string, Flyweight> flyweights = new Dictionary<string, Flyweight>();

       public Flyweight GetFlyweight(string key)
       {
           if (!flyweights.ContainsKey(key))
           {
               flyweights[key] = new Flyweight(key);
           }

           return flyweights[key];
       }

       public int GetFlyweightCount()
       {
           return flyweights.Count;
       }
   }

## Proxy 代理模式
代理模式是一种结构型设计模式，它提供了一个对象代替另一个对象来控制对它的访问。代理对象可以在客户端和目标对象之间起到中介的作用，并添加其他的功能。

    // 抽象主题接口
    public interface ISubject
    {
        void Request();
    }

    // 真实主题
    public class RealSubject : ISubject
    {
        public void Request()
        {
            Console.WriteLine("RealSubject: Handling Request.");
        }
    }

    // 代理
    public class Proxy : ISubject
    {
        private RealSubject _realSubject;

        public Proxy(RealSubject realSubject)
        {
            this._realSubject = realSubject;
        }

        public void Request()
        {
            if (this.CheckAccess())
            {
                this._realSubject.Request();
                this.LogAccess();
            }
        }

        public bool CheckAccess()
        {
            // 检查是否有权限访问
            Console.WriteLine("Proxy: Checking access prior to firing a real request.");
            return true;
        }

        public void LogAccess()
        {
            // 记录请求
            Console.WriteLine("Proxy: Logging the time of request.");
        }
    }

## Chain of Responsibility 责任链模式
就是把业务中与主体业务只要稍微带点不稳定因素的代码，都抛出给别的方法去执行。

    /// <summary>
    /// 责任链设计模式抽象类
    /// </summary>
    public abstract class ChainOfResponsibilityContext
    {
        public int Num { get; set; }

        /// <summary>
        /// 大小判断抽象方法
        /// </summary>
        /// <param name="num"></param>
        public abstract void Adujit(int num);

        /// <summary>
        /// 存储下一个逻辑判断
        /// </summary>
        private ChainOfResponsibilityContext _NextAdujit = null;

        //设置下一个逻辑判断是谁
        public void SetNext(ChainOfResponsibilityContext data)
        {
            this._NextAdujit = data;
        }

        /// <summary>
        ///继续下一个逻辑判断
        /// </summary>
        /// <param name="num"></param>
        protected void AdujitNext(int num)
        {
            if (this._NextAdujit != null)
            {
                this._NextAdujit.Adujit(num);
            }
            else
            {
                Console.WriteLine("我是大于40的数");
            }
        }
    }

    /// <summary>
    /// 判断10区间的类
    /// </summary>
    public class Ten : ChainOfResponsibilityContext
    {
        public override void Adujit(int num)
        {
            if (num <= this.Num)
            {
                Console.WriteLine("我是小于10的数");
            }
            else
            {
                base.AdujitNext(num);
            }
        }
    }
    /// <summary>
    /// 判断20区间的类
    /// </summary>
    public class Twenty : ChainOfResponsibilityContext
    {
        public override void Adujit(int num)
        {
            if (num <= this.Num)
            {
                Console.WriteLine("我是小于20的数");
            }
            else
            {
                base.AdujitNext(num);
            }
        }
    }
    /// <summary>
    /// 判断30区间的类
    /// </summary>
    public class Thirty : ChainOfResponsibilityContext
    {
        public override void Adujit(int num)
        {
            if (num <= this.Num)
            {
                Console.WriteLine("我是小于30的数");
            }
            else
            {
                base.AdujitNext(num);
            }
        }
    }
    /// <summary>
    /// 判断40区间的类
    /// </summary>
    public class Forty : ChainOfResponsibilityContext
    {
        public override void Adujit(int num)
        {
            if (num <= this.Num)
            {
                Console.WriteLine("我是小于40的数");
            }
            else
            {
                base.AdujitNext(num);
            }
        }
    }

    /// <summary>
    /// 具体实现判断逻辑类
    /// </summary>
    public class AllContext
    {
        public static ChainOfResponsibilityContext Buid(int num)
        {

            ChainOfResponsibilityContext context = new Ten()
            {
                Num = 10
            };
            ChainOfResponsibilityContext context1 = new Twenty()
            {
                Num = 20
            };
            ChainOfResponsibilityContext context2 = new Thirty()
            {
                Num = 30
            };
            ChainOfResponsibilityContext context3 = new Forty()
            {
                Num = 40
            };
            //设置10判断之后为20
            context.SetNext(context1);
            //设置20判断之后为30
            context1.SetNext(context2);
            //设置30判断之后为40
            context2.SetNext(context3);

            return context;
        }
    }

# 行为型模式
## Command 命令模式
命令模式（Command Pattern）是一种数据驱动的设计模式，它属于行为型模式。在命令模式中，请求在对象中封装成为一个操作或行为，这些请求被送到调用对象，调用对象寻找可以处理该命令的合适的对象，并把命令直接送达到对应的对象，该对象会执行这些命令。

    // 命令接口
    public interface ICommand
    {
        void Execute();
    }

    // 具体命令类
    public class ConcreteCommand : ICommand
    {
        private Receiver receiver;

        public ConcreteCommand(Receiver receiver)
        {
            this.receiver = receiver;
        }

        public void Execute()
        {
            receiver.Action();
        }
    }

    // 接收者类
    public class Receiver
    {
        public void Action()
        {
            Console.WriteLine("Receiver performs an action");
        }
    }

    // 调用者或发送者类
    public class Invoker
    {
        private ICommand command;

        public void SetCommand(ICommand command)
        {
            this.command = command;
        }

        public void ExecuteCommand()
        {
            command.Execute();
        }
    }

## Interpreter 解释器模式
    // 抽象表达式
    public interface IExpression
    {
        bool Interpret(string context);
    }

    // 终结符表达式
    public class TerminalExpression : IExpression
    {
        private string data;

        public TerminalExpression(string data)
        {
            this.data = data;
        }

        public bool Interpret(string context)
        {
            if (context.Contains(data))
            {
                return true;
            }

            return false;
        }
    }

    // 非终结符表达式
    public class OrExpression : IExpression
    {
        private IExpression expr1;
        private IExpression expr2;

        public OrExpression(IExpression expr1, IExpression expr2)
        {
            this.expr1 = expr1;
            this.expr2 = expr2;
        }

        public bool Interpret(string context)
        {
            return expr1.Interpret(context) || expr2.Interpret(context);
        }
    }

## Iterator 迭代器模式
迭代器模式（Iterator Pattern）是一种行为型设计模式，它提供了一种方法来访问一个对象的元素，而不需要暴露该对象的内部表示。

    // 抽象聚合类
    public interface IAggregate
    {
        IIterator CreateIterator();
        void Add(string item);
        int Count { get; }
        string this[int index] { get; set; }
    }

    // 具体聚合类
    public class ConcreteAggregate : IAggregate
    {
        private List<string> items = new List<string>();

        public IIterator CreateIterator()
        {
            return new ConcreteIterator(this);
        }

        public int Count
        {
            get { return items.Count; }
        }

        public string this[int index]
        {
            get { return items[index]; }
            set { items.Insert(index, value); }
        }

        public void Add(string item)
        {
            items.Add(item);
        }
    }

    // 抽象迭代器
    public interface IIterator
    {
        string First();
        string Next();
        bool IsDone { get; }
        string CurrentItem { get; }
    }

    // 具体迭代器
    public class ConcreteIterator : IIterator
    {
        private ConcreteAggregate aggregate;
        private int current = 0;

        public ConcreteIterator(ConcreteAggregate aggregate)
        {
            this.aggregate = aggregate;
        }

        public string First()
        {
            return aggregate[0];
        }

        public string Next()
        {
            string ret = string.Empty;
            if (current < aggregate.Count - 1)
            {
                ret = aggregate[++current];
            }

            return ret;
        }

        public string CurrentItem
        {
            get { return aggregate[current]; }
        }

        public bool IsDone
        {
            get { return current >= aggregate.Count; }
        }
    }

    static void TestIterator()
    {
        IAggregate aggregate = new ConcreteAggregate();
        aggregate.Add("Item A");
        aggregate.Add("Item B");
        aggregate.Add("Item C");
        aggregate.Add("Item D");

        IIterator iterator = aggregate.CreateIterator();

        Console.WriteLine("Iterating over collection:");

        string item = iterator.First();
        while (item != null)
        {
            Console.WriteLine(item);
            item = iterator.Next();
        }

        Console.ReadLine();
    }

## Mediator 中介者模式
中介者模式是一种行为设计模式，它让你能减少一组对象之间复杂的通信。它提供了一个中介者对象，此对象负责在组中的对象之间进行通信，而不是这些对象直接进行通信。

    // Mediator 接口声明了与组件交互的方法。
    public interface IMediator
    {
        void Notify(object sender, string ev);
    }

    // 具体 Mediators 实现协作行为，它负责协调多个组件。
    public class ConcreteMediator : IMediator
    {
        private Component1 _component1;
        private Component2 _component2;

        public ConcreteMediator(Component1 component1, Component2 component2)
        {
            _component1 = component1;
            _component1.SetMediator(this);
            _component2 = component2;
            _component2.SetMediator(this);
        }

        public void Notify(object sender, string ev)
        {
            if (ev == "A")
            {
                Console.WriteLine("Mediator reacts on A and triggers following operations:");
                this._component2.DoC();
            }
            if (ev == "D")
            {
                Console.WriteLine("Mediator reacts on D and triggers following operations:");
                this._component1.DoB();
                this._component2.DoC();
            }
        }
    }

    public abstract class BaseComponent
    {
        protected IMediator _mediator;

        public BaseComponent(IMediator mediator = null)
        {
            _mediator = mediator;
        }

        public void SetMediator(IMediator mediator)
        {
            this._mediator = mediator;
        }
    }

    // 具体 Components 实现各种功能。它们不依赖于其他组件。
    // 它们也不依赖于任何具体 Mediator 类。
    public class Component1 : BaseComponent
    {
        public void DoA()
        {
            Console.WriteLine("Component 1 does A.");
            this._mediator.Notify(this, "A");
        }

        public void DoB()
        {
            Console.WriteLine("Component 1 does B.");
            this._mediator.Notify(this, "B");
        }
    }

    public class Component2 : BaseComponent
    {
        public void DoC()
        {
            Console.WriteLine("Component 2 does C.");
            this._mediator.Notify(this, "C");
        }

        public void DoD()
        {
            Console.WriteLine("Component 2 does D.");
            this._mediator.Notify(this, "D");
        }
    }

## Memento 备忘录模式
备忘录模式是一种行为设计模式，它能保存对象的状态，以便在后面可以恢复它。在大多数情况下，这种模式可以让你在不破坏对象封装的前提下，保存和恢复对象的历史状态。

    // Originator 类可以生成一个备忘录，并且可以通过备忘录恢复其状态。
    public class Originator
    {
        private string _state;

        public Originator(string state)
        {
            this._state = state;
            Console.WriteLine($"Originator: My initial state is: {_state}");
        }

        public void DoSomething()
        {
            Console.WriteLine("Originator: I'm doing something important.");
            _state = GenerateRandomString(30);
            Console.WriteLine($"Originator: and my state has changed to: {_state}");
        }

        private string GenerateRandomString(int length = 10)
        {
            string allowedSymbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string result = string.Empty;

            while (length > 0)
            {
                result += allowedSymbols[new Random().Next(0, allowedSymbols.Length)];

                length--;
            }

            return result;
        }

        public IMemento Save()
        {
            return new ConcreteMemento(_state);
        }

        public void Restore(IMemento memento)
        {
            _state = memento.GetState();
            Console.WriteLine($"Originator: My state has changed to: {_state}");
        }
    }

    // 备忘录接口提供了获取备忘录和原发器状态的方法。但在该接口中并未声明所有的方法，一些方法只在原发器中声明。
    public interface IMemento
    {
        string GetName();

        string GetState();

        DateTime GetDate();
    }

    // Concrete Memento 存储原发器状态，并通过原发器实现备份。备忘录是不可变的，因此，没有 set 方法。
    public class ConcreteMemento : IMemento
    {
        private string _state;
        private DateTime _date;

        public ConcreteMemento(string state)
        {
            _state = state;
            _date = DateTime.Now;
        }

        public string GetState()
        {
            return _state;
        }

        public string GetName()
        {
            return $"{_date} / ({_state.Substring(0, 9)})...";
        }

        public DateTime GetDate()
        {
            return _date;
        }
    }

    // Caretaker 不依赖于具体备忘录类。结果，它不会有任何访问原发器状态的权利，它只能获取备忘录的元数据。
    public class Caretaker
    {
        private List<IMemento> _mementos = new List<IMemento>();
        private Originator _originator = null;

        public Caretaker(Originator originator)
        {
            this._originator = originator;
        }

        public void Backup()
        {
            Console.WriteLine("\nCaretaker: Saving Originator's state...");
            _mementos.Add(_originator.Save());
        }

        public void Undo()
        {
            if (_mementos.Count == 0)
            {
                return;
            }

            var memento = _mementos.Last();
            _mementos.Remove(memento);

            Console.WriteLine("Caretaker: Restoring state to: " + memento.GetName());
            try
            {
                _originator.Restore(memento);
            }
            catch (Exception)
            {
                Undo();
            }
        }

        public void ShowHistory()
        {
            Console.WriteLine("Caretaker: Here's the list of mementos:");

            foreach (var memento in _mementos)
            {
                Console.WriteLine(memento.GetName());
            }
        }

    }

    // 客户端代码
    static void TestFunction()
    {
        Originator originator = new Originator("Super-duper-super-puper-super.");
        Caretaker caretaker = new Caretaker(originator);

        caretaker.Backup();
        originator.DoSomething();

        caretaker.Backup();
        originator.DoSomething();

        caretaker.Backup();
        originator.DoSomething();

        Console.WriteLine();
        caretaker.ShowHistory();

        Console.WriteLine("\nClient: Now, let's rollback!\n");
        caretaker.Undo();

        Console.WriteLine("\nClient: Once more!\n");
        caretaker.Undo();
    }

## Observer 观察者模式

    // 抽象观察者
    public interface IObserver
    {
        void Update();
    }

    // 具体观察者
    public class ConcreteObserver : IObserver
    {
        private string name;

        public ConcreteObserver(string name)
        {
            this.name = name;
        }

        public void Update()
        {
            Console.WriteLine($"{name} received an update!");
        }
    }

    // 抽象主题
    public interface ISubject
    {
        void RegisterObserver(IObserver observer);
        void RemoveObserver(IObserver observer);
        void NotifyObservers();
    }

    // 具体主题
    public class ConcreteSubject : ISubject
    {
        private List<IObserver> observers = new List<IObserver>();

        public void RegisterObserver(IObserver observer)
        {
            observers.Add(observer);
        }

        public void RemoveObserver(IObserver observer)
        {
            if (observers.Contains(observer))
            {
                observers.Remove(observer);
            }
        }

        public void NotifyObservers()
        {
            foreach (var observer in observers)
            {
                observer.Update();
            }
        }

        public void ChangeState()
        {
            // 触发状态变化，通知所有观察者
            NotifyObservers();
        }
    }

## State 状态模式
状态模式在面向对象编程中，是一种允许对象在其内部状态改变时改变其行为的设计模式。这种类型的设计模式属于行为型模式。在状态模式中，我们创建对象表示各种状态，以及一个行为随状态改变而改变的上下文对象。

    public interface IAccountState
    {
        void Deposit(Action addToBalance);
        void Withdraw(Action subtractFromBalance);
        void ComputeInterest();
    }

    public class NormalState : IAccountState
    {
        public void Deposit(Action addToBalance)
        {
            addToBalance();
            Console.WriteLine("Deposit in NormalState");
        }

        public void Withdraw(Action subtractFromBalance)
        {
            subtractFromBalance();
            Console.WriteLine("Withdraw in NormalState");
        }

        public void ComputeInterest()
        {
            Console.WriteLine("Interest computed in NormalState");
        }
    }

    public class OverdrawnState : IAccountState
    {
        public void Deposit(Action addToBalance)
        {
            addToBalance();
            Console.WriteLine("Deposit in OverdrawnState");
        }

        public void Withdraw(Action subtractFromBalance)
        {
            Console.WriteLine("No withdraw in OverdrawnState");
        }

        public void ComputeInterest()
        {
            Console.WriteLine("Interest and fees computed in OverdrawnState");
        }
    }

    public class BankAccount
    {
        private IAccountState _state;
        private double _balance;

        public BankAccount(IAccountState state)
        {
            _state = state;
            _balance = 0;
        }

        public void Deposit(double amount)
        {
            _state.Deposit(() => _balance += amount);
            StateChangeCheck();
        }

        public void Withdraw(double amount)
        {
            _state.Withdraw(() => _balance -= amount);
            StateChangeCheck();
        }

        public void ComputeInterest()
        {
            _state.ComputeInterest();
        }

        private void StateChangeCheck()
        {
            if (_balance < 0.0)
                _state = new OverdrawnState();
            else
                _state = new NormalState();
        }
    }

## Strategy 策略模式
策略模式定义了一系列的算法，并将每一个算法封装起来，使得它们可以相互替换。策略模式让算法独立于使用它的客户而独立变化。
    public interface ISortStrategy
    {
        void Sort(List<int> list);
    }

    public class QuickSort : ISortStrategy
    {
        public void Sort(List<int> list)
        {
            list.Sort(); // Quick sort is in-place but here we are using built-in method
            Console.WriteLine("QuickSorted list ");
        }
    }

    public class BubbleSort : ISortStrategy
    {
        public void Sort(List<int> list)
        {
            int n = list.Count;
            for (int i = 0; i < n - 1; i++)
                for (int j = 0; j < n - i - 1; j++)
                    if (list[j] > list[j + 1])
                    {
                        // swap temp and list[i]
                        int temp = list[j];
                        list[j] = list[j + 1];
                        list[j + 1] = temp;
                    }

            Console.WriteLine("BubbleSorted list ");
        }
    }

    public class SortedList
    {
        private List<int> _list = new List<int>();
        private ISortStrategy _sortstrategy;

        public void SetSortStrategy(ISortStrategy sortstrategy)
        {
            this._sortstrategy = sortstrategy;
        }

        public void Add(int num)
        {
            _list.Add(num);
        }

        public void Sort()
        {
            _sortstrategy.Sort(_list);

            // Print sorted list
            foreach (int num in _list)
            {
                Console.Write(num + " ");
            }
            Console.WriteLine();
        }
    }

## Template Method 模板方法模式
模板方法模式定义了一个操作中算法的骨架，将这些步骤延迟到子类中。模板方法使得子类可以不改变算法的结构即可重定义该算法的某些特定步骤。

    public abstract class CookingProcedure
    {
        // The 'Template method' 
        public void PrepareDish()
        {
            PrepareIngredients();
            Cook();
            CleanUp();
        }

        public void PrepareIngredients()
        {
            Console.WriteLine("Preparing the ingredients...");
        }

        // These methods will be overridden by subclasses
        public abstract void Cook();

        public void CleanUp()
        {
            Console.WriteLine("Cleaning up...");
        }
    }

    public class CookPasta : CookingProcedure
    {
        public override void Cook()
        {
            Console.WriteLine("Cooking pasta...");
        }
    }

    public class BakeCake : CookingProcedure
    {
        public override void Cook()
        {
            Console.WriteLine("Baking cake...");
        }
    }

## Visitor 访问者模式
访问者模式（Visitor Pattern）是一种将算法与对象结构分离的软件设计模式。这种模式的基本想法就是通过所谓的"访问者"来改变元素的操作。这样一来，元素的类可以用于表示元素结构，而具体的操作则可以在访问者类中定义。


    // 访问者接口
    public interface IVisitor
    {
        void VisitConcreteElementA(ConcreteElementA concreteElementA);
        void VisitConcreteElementB(ConcreteElementB concreteElementB);
    }

    // 具体访问者A
    public class ConcreteVisitorA : IVisitor
    {
        public void VisitConcreteElementA(ConcreteElementA concreteElementA)
        {
            Console.WriteLine($"{concreteElementA.GetType().Name} is being visited by {this.GetType().Name}");
        }

        public void VisitConcreteElementB(ConcreteElementB concreteElementB)
        {
            Console.WriteLine($"{concreteElementB.GetType().Name} is being visited by {this.GetType().Name}");
        }
    }

    // 具体访问者B
    public class ConcreteVisitorB : IVisitor
    {
        public void VisitConcreteElementA(ConcreteElementA concreteElementA)
        {
            Console.WriteLine($"{concreteElementA.GetType().Name} is being visited by {this.GetType().Name}");
        }

        public void VisitConcreteElementB(ConcreteElementB concreteElementB)
        {
            Console.WriteLine($"{concreteElementB.GetType().Name} is being visited by {this.GetType().Name}");
        }
    }

    // 元素接口
    public interface IElement
    {
        void Accept(IVisitor visitor);
    }

    // 具体元素A
    public class ConcreteElementA : IElement
    {
        public void Accept(IVisitor visitor)
        {
            visitor.VisitConcreteElementA(this);
        }
    }

    // 具体元素B
    public class ConcreteElementB : IElement
    {
        public void Accept(IVisitor visitor)
        {
            visitor.VisitConcreteElementB(this);
        }
    }

    // 对象结构
    public class ObjectStructure
    {
        private List<IElement> _elements = new List<IElement>();

        public void Attach(IElement element)
        {
            _elements.Add(element);
        }

        public void Detach(IElement element)
        {
            _elements.Remove(element);
        }

        public void Accept(IVisitor visitor)
        {
            foreach (var element in _elements)
            {
                element.Accept(visitor);
            }
        }
    }