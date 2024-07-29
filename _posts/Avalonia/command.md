---
layout: post
title: "Command"
date: 2024-07-25 14:49:00 +0800
author: Michael
categories: Avalonia
---

# ReactiveUI

    /// <summary>
    ///  This collection will store what the computer said
    /// </summary>
    public ObservableCollection<string> ConversationLog { get; } = new ObservableCollection<string>();

    // Just a helper to add content to ConversationLog
    private void AddToConvo(string content)
    {
        ConversationLog.Add(content);
    }

    private string? _RobotName;
    /// <summary>
    /// The name of a robot. If the name is null or empty, there is no other robot present.
    /// </summary>
    public string? RobotName
    {
        get => _RobotName;
        set => this.RaiseAndSetIfChanged(ref _RobotName, value);
    }

    IObservable<bool> canExecuteFellowRobotCommand = this.WhenAnyValue(vm => vm.RobotName, (name) => !string.IsNullOrEmpty(name));
    OpenThePodBayDoorsFellowRobotCommand =  ReactiveCommand.Create<string?>(name => OpenThePodBayDoorsFellowRobot(name), canExecuteFellowRobotCommand);


    private void OpenThePodBayDoorsFellowRobot(string? robotName)
    {
        ConversationLog.Clear();
        AddToConvo($"Hello {robotName}, the Pod Bay is open :-)");
    }

    <StackPanel Orientation="Horizontal" Spacing="5">
        <TextBox Text="{Binding RobotName}" Watermark="Robot Name" />
        <Button Command="{Binding OpenThePodBayDoorsFellowRobotCommand}"
                Content="{Binding RobotName, StringFormat='Open the Pod Bay for {0}'}"
                CommandParameter="{Binding RobotName}" />
    </StackPanel>