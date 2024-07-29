---
layout: post
title: "MVVM"
date: 2024-07-25 14:49:00 +0800
author: Michael
categories: Avalonia
---

# INotifyPropertyChanged 


	<!-- Our Simple ViewModel-->
	<StackPanel DataContext="{Binding SimpleViewModel}" Spacing="10">
		<TextBlock>Enter your Name:</TextBlock>
		<TextBox Text="{Binding Name}" />
		<TextBox Text="{Binding Greeting, Mode=OneWay}"
				 IsReadOnly="True"
				 FontWeight="Bold" />
	</StackPanel>

    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
        {
            desktop.MainWindow = new MainWindow
            {
                DataContext = new MainWindowViewModel(),
            };
        }

        base.OnFrameworkInitializationCompleted();
    }

    public SimpleViewModel SimpleViewModel { get; } = new SimpleViewModel();

    public class SimpleViewModel : INotifyPropertyChanged
    {
        // This event is implemented by "INotifyPropertyChanged" and is all we need to inform
        // our view about changes.
        public event PropertyChangedEventHandler? PropertyChanged;

        private void RaisePropertyChanged([CallerMemberName] string? propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        private string? _Name; // This is our backing field for Name

        public string? Name
        {
            get
            {
                return _Name;
            }
            set
            {
                // We only want to update the UI if the Name actually changed, so we check if the value is actually new
                if (_Name != value)
                {
                    // 1. update our backing field
                    _Name = value;

                    // 2. We call RaisePropertyChanged() to notify the UI about changes.
                    // We can omit the property name here because [CallerMemberName] will provide it for us.
                    RaisePropertyChanged();

                    // 3. Greeting also changed. So let's notify the UI about it.
                    RaisePropertyChanged(nameof(Greeting));
                }
            }
        }

        // Greeting will change based on a Name.
        public string Greeting
        {
            get
            {
                if (string.IsNullOrEmpty(Name))
                {
                    // If no Name is provided, use a default Greeting
                    return "Hello World from Avalonia.Samples";
                }
                else
                {
                    // else greet the User.
                    return $"Hello {Name}";
                }
            }
        }
    }

# ReactiveUI

    public class ReactiveViewModel : ReactiveObject
    {
        public ReactiveViewModel()
        {
            // We can listen to any property changes with "WhenAnyValue" and do whatever we want in "Subscribe".
            this.WhenAnyValue(o => o.Name)
                .Subscribe(o => this.RaisePropertyChanged(nameof(Greeting)));
        }

        private string? _Name; // This is our backing field for Name

        public string? Name
        {
            get
            {
                return _Name;
            }
            set
            {
                // We can use "RaiseAndSetIfChanged" to check if the value changed and automatically notify the UI
                this.RaiseAndSetIfChanged(ref _Name, value);
            }
        }

        // Greeting will change based on a Name.
        public string Greeting
        {
            get
            {
                if (string.IsNullOrEmpty(Name))
                {
                    // If no Name is provided, use a default Greeting
                    return "Hello World from Avalonia.Samples";
                }
                else
                {
                    // else greet the User.
                    return $"Hello {Name}";
                }
            }
        }
    }

    <!-- Our ReactiveViewModel -->
    <TabItem Header="Reactive UI" >
        <StackPanel DataContext="{Binding ReactiveViewModel}" Spacing="10">
            <TextBlock>Enter your Name:</TextBlock>
            <TextBox Text="{Binding Name}" />
            <TextBox Text="{Binding Greeting, Mode=OneWay}"
                        IsReadOnly="True"
                        FontWeight="Bold" />
        </StackPanel>
    </TabItem>