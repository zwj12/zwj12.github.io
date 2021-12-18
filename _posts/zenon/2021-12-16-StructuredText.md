---
layout: post
title: "Structured Text (ST)"
date: 2021-12-16 16:24:00 +0800
author: Michael
categories: zenon
---

# 设置主程序执行顺序
右击程序模块，打开Cycle窗口，可以设置主程序在一个程序执行周期内的执行顺序。  
![日志文件夹](/assets/zenon/programscycle.png) 

# 上升沿，定时器程序
	IF Command.CommandIdle=TRUE THEN
	    IF Command.CommandError=FALSE THEN
	        ON Command.RequestCommand DO
	            Command.CommandIdle:=FALSE;
	            bInputTest01:=TRUE;
	        END_DO;
	    ELSE
	        ON Command.ResetCommandError DO
	            Command.CommandError:=FALSE;
	            Command.CommandErrorCode:=0;
	        END_DO;
	    END_IF;
	END_IF;
	
	TON_Command(bInputTest01,T#5s);
	TimerCurrent:=TON_Command.ET;
	ON TON_Command.Q DO
	    IF RecipeRequest.ID<=150 AND RecipeCurrent.ID<>RecipeRequest.ID THEN
	        RecipeCurrent.ID:=RecipeRequest.ID;
	    ELSE
	        Command.CommandError:=TRUE;
	        Command.CommandErrorCode:=10001;
	    END_IF;
	    Command.CommandIdle:=TRUE;
	    bInputTest01:=FALSE;
	END_DO;

# Auto Completion
CTRL+SPACE 

# WAIT & WAIT_TIME
- If the expression is TRUE, the program continues normally.
- If the expression is FALSE, then the execution of the program is suspended up to the next PLC cycle. The boolean expression will be checked again during next cycles until it becomes TRUE. The execution of other programs is not affected.当等待的条件为false时，程序会挂起，直到在后续的某一次执行周期中条件为true时，才继续执行该程序。
