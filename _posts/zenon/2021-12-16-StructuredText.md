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

# 常量 Constant expressions
1. BOOL: TRUE, FALSE
2. SINT: SINT#1
3. USINT/BYTE: USINT#1
4. INT: INT#1
5. UINT/WORD: UINT#1
6. DINT: 1, 2#1(binary), 8#1(octal), 16#1(hexadecimal)
7. UDINT/DWORD: UDINT#1
8. LINT: LINT#1
9. REAL: 1.0, 1F10, 1E10
10. LREAL: LREAL#1.0, LREAL#1F10, LREAL#1E10
11. TIME: TIME#3s, T#1h1m1s1ms
12. STRING: 'hello', 'I$'m here'

# R_TRIG上升沿触发函数
1. 第一个时钟周期：设置CLK为TRUE，当外部设备或者手动设置CLK为TRUE时，程序只会在下一个时钟周期开始时，才会真正把CLK的值设置为TRUE。例如如果时钟周期为5s，用户在1s时把CLK手动设置为TRUE，此时在调试界面，会看到CLK会短时闪烁一下为TRUE，然后紧接着就又变回原先的FALSE了，因为此周期内的CLK确实为FALSE，当该周期结束后，在下一个5s的周期开始时，CLK才会真正的变为TRUE。
2. 第二个时钟周期：CLK变为TRUE。此周期内，MyTrigger.Q并不会变为TRUE。
3. 第三个时钟周期：MyTrigger.Q变为TRUE。
4. 第四个时钟周期：MyTrigger.Q变为FALSE。
5. 第五个时钟周期：如果第三个时钟周期CLK变为FALSE，第四个时钟周期变为TRUE，那么第五个时钟周期MyTrigger.Q会继续变为TRUE

	MyTrigger (CLK);
	Q := MyTrigger.Q;

# Timer - TON

    tonReseting(gbSTS_RESETTING,T#5s);
    IF tonReseting.Q=TRUE THEN            
        for iArrayDim := 1 to 10 do
            if ((gbSTS_RESETTING)
                and (Pm_Sts_Getrobotdetailstatus[iArrayDim-1] = 23 
                    or Pm_Sts_Getrobotdetailstatus[iArrayDim-1] = 17)
                and Pml_Robot_Relevance[iArrayDim-1] = True
                and (Pm_Sts_Getcontrollerdetailstatus[iArrayDim-1] = 2
                    or Pm_Sts_Getcontrollerdetailstatus[iArrayDim-1] = 3
                    or Pm_Sts_Getcontrollerdetailstatus[iArrayDim-1] = 1))
            then
                Pm_Cmd_StopProject := True;
                Pm_Cmd_CloseProject := True; 
                Pml_Cmd_Stop := True;        
            end_if;           
        end_for;             
    END_IF;  

# String
字符串常量使用单引号： 'Hello World!'，不能使用双引号。

# IN OUT
1. IN: 函数内容修改变量，对外部不起作用，反而因为每个循环，外部都会传一次参数，导致内部修改IN变量其实不起作用（可能单个循环内部起作用，没意义）。  
2. IN_OUT： 内部修改变量，会直接同时修改外部变量。  
3. 从目前测试看, structure变量作为参数时，是通过传地址引用实现的，所以结构体变量只能作为IN或IN_OUT变量，不能作为OUT变量。Sub-programs and UDFBs may have parameters on input or ou output. Output parameters cannot be arrays of data structures but only single data. When an array is passed as an inupt parameter to a UDFB, it is considered as INOUT so the UDFB can read or write in it. The support of complex data types for input parameters may depend on selected compiling options.
4. complex data: array, structure变量作为IN时，内部时作为INOUT变量的，也就是说，即使定义为IN，内部也是可以修改结构体变量值的。

# Sub program - function
Alternatively, if a sub-program has one and only one output parameter, it can be called as a function in ST language:  

	Res := MySubProg (i1, i2);

# 程序执行过程
对于TON，CLK_BLINK之类的程序，需要让其每个cycle都一行一次，这样他们FB的out才会刷新数据，如果在某个循环启动TON，然后在后面的循环中使用if语句屏蔽TON的运行，那么TON的out变量是不会自动刷新的。这是PLC程序的原理，需要确保每个cycle都要运行一遍程序。