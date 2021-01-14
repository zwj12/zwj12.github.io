---
layout: post
title: "Encoder Parameter"
date: 2020-12-14 08:17:00 +0800
author: Michael
categories: Laser3DSensors
---

# 前言 #

在使用线激光对物体扫描时，为了获得物体的3D点云，有两种扫描方式：一种是线激光静止，物体随传送带或导轨移动获得整个物体的3D点云图；另一种是物体静止，线激光传感器随高精度导轨移动，获得整个物体的3D点云图。由于线激光是一帧一帧的获取图像，为了获取整个物体的3D点云图，它需要把很多帧的图像最终汇总到一个点云图中，也就是说，线激光在扫描时，其实是对物体进行了一个平均等分的切片处理。切片的精度会直接影响3D点云图的真实度。通常，我们为了提高精度，会在导轨或传送带上安装一个编码器，由于编码器的精度极高，这样，当导轨或传送带移动时，编码器会根据移动的固定距离，准确的发出采集图像的脉冲信号。在设置线激光编码器采集脉冲信号参数时，有两种方式可以获取该参数：一种是让导轨或传送带移动固定的距离，例如1m，然后查看线激光传感器所接收到的编码器AB相脉冲信号数量，例如采集到10000个脉冲信号，然后根据项目所需要达到的扫描精度，例如0.5mm，那么我们就可以估算出每5（=10000/(1/0.005))个脉冲采集一个图像的参数；还有一种方式就是通过编码器，减速机，导轨齿轮参数的数据，准确计算出每一幅图像的编码器脉冲信号数。通常推荐第二种，因为第二种更精确。本文将阐述第二种计算脉冲数的方式，我们通过机器人安装在导轨上，然后机器人手持线激光固定不动，导轨移动扫描物体为例：

# 设备参数 #

首先，如果需要通过物理参数计算出编码器与导轨移动距离的关系，我们需要通过资料查阅获取以下物理量：

1. 减速机减速比例(编码器安装在减速箱导轨齿轮侧），iR (Ratio) = 8:1
2. 传动比，RTGR (Robot Transmission Gear Ratio) = 314 (rad/m)
3. 编码器每转一圈的脉冲数，EPC (Incremental rotary encoder Cycle Count) = 2048

# 计算公式 #

通过以上几个参数，我们就可以开始计算了：

1. 导轨每米齿轮转动弧度数：RPM (Radian per Meter) = RTGR/iR
2. 导轨每米脉冲数：CPM (Cycles per Meter) = EPC*(RPM/(2π)) = EPC*((RTGR/iR)/(2π)) = 2048*((314/8)/(2*3.14))= 12800
3. 编码器每脉冲导轨移动距离：DPC (Distance per full cycle) = 1000/CPM = 1000/12800 = 0.078125

以上是设备的固有理论参数，当用于实际项目时，我们还需要针对项目设备的负载和精度做一个优化，线激光的扫描频率不是越快越好，扫描过快，有可能导致传感器超频，图像丢失。通常情况下，线激光扫描的精度保证在0.5mm就可以了。所以我们可以设置如下参数：

1. 线激光触发扫描脉冲频率(考虑到AB相4倍脉冲模式)：SPL (Steps per line) = 0.5/DPC*4 = 25.6 ≈ 25
2. 线激光扫描精度：Accuracy = DPC/4* SPL = 0.078125/4*25=0.48828125

另外线激光传感器的内存也是有限的，对于较长工件，可能需要分多幅图连续采集，如果一幅图采集的帧数超出线激光传感器的容量，也会导致图像丢失。例如我们可以把一幅图设置为由500帧组成，那么：

1. 每幅图的线扫帧数：PPF (Profiles per Frame) = 500
2. 每幅图的导轨移动的距离：DPF (Distance per Frame) = Accuracy * PPF = 0.48828125*500=244.140625
3. 对于一个10m长的工件，需要扫描图像数量为：10000/244.140625 = 40.96 ≈ 42

# 工具 #

为了测试方便，我这边写了一个Python小程序，可以自动计算以上参数值：  
![日志文件夹](/assets/laser3dsensors/EncoderParameterUtility.png)

整个程序较为简单，代码如下：

	from tkinter import *
	import math
	
	class Application(Frame):
	    def __init__(self, master=None):
	        super().__init__()
	        self.master = master
	        self.master.title("Encoder Parameter Utility")
	        self.master.geometry('500x500')
	        self.create_widgets()
	
	    def create_widgets(self):
	        row = -1
	        self.pi = DoubleVar()
	        self.pi.set(round(math.pi,2))
	        self.expected_accuracy = DoubleVar()
	        self.expected_accuracy.set(0.5)
	        self.gearbox_ratio = StringVar()
	        self.gearbox_ratio.set("8")
	        self.transmission_gear_ratio = StringVar()
	        self.transmission_gear_ratio.set("314")
	        self.encoder_cycles = StringVar()
	        self.encoder_cycles.set("2048")
	        self.profiles_per_frame = IntVar()
	        self.profiles_per_frame.set(500)
	        self.scan_length = DoubleVar()
	        self.scan_length.set(10000)
	        self.encoder_type = IntVar()
	        self.encoder_type.set(4)
	        
	        self.radian_per_meter = DoubleVar()
	        self.cycles_per_meter = IntVar()
	        self.distance_per_cycle = DoubleVar()
	        self.steps_per_line = IntVar()
	        self.accuracy = DoubleVar()
	        self.distance_per_frame = DoubleVar()
	        self.number_frames = IntVar()
	        
	        row += 1
	        self.label_expected_accuracy = Label(text="Expected Accuracy (mm)")
	        self.label_expected_accuracy.grid(row=row, column=0)
	        self.text_expected_accuracy = Entry(width=30, textvariable=self.expected_accuracy) 
	        self.text_expected_accuracy.grid(row=row, column=1)
	        
	        row += 1
	        self.label_pi = Label(text="PI")
	        self.label_pi.grid(row=row, column=0)
	        self.text_pi = Entry(width=30, textvariable=self.pi) 
	        self.text_pi.grid(row=row, column=1)
	        
	        row += 1
	        self.label_gearbox_ratio = Label(text="Gearbox Ratio")
	        self.label_gearbox_ratio.grid(row=row, column=0)
	        self.text_gearbox_ratio = Entry(width=30, textvariable=self.gearbox_ratio) 
	        self.text_gearbox_ratio.grid(row=row, column=1)
	
	        row += 1
	        self.label_transmission_gear_ratio = Label(text="Transmission Gear Ratio")
	        self.label_transmission_gear_ratio.grid(row=row, column=0)
	        self.text_transmission_gear_ratio = Entry(width=30, textvariable=self.transmission_gear_ratio) 
	        self.text_transmission_gear_ratio.grid(row=row, column=1)
	
	        row += 1
	        self.radio_encoder_type_single = Radiobutton(width=30, text="Single Channel", variable=self.encoder_type, value=1) 
	        self.radio_encoder_type_single.grid(row=row, column=0)
	        self.radio_encoder_type_dual = Radiobutton(width=30, text="Dual Channel", variable=self.encoder_type, value=4) 
	        self.radio_encoder_type_dual.grid(row=row, column=1)
	        
	        row += 1
	        self.label_encoder_cycles = Label(text="Encoder Cycle Count")
	        self.label_encoder_cycles.grid(row=row, column=0)
	        self.text_encoder_cycles = Entry(width=30, textvariable=self.encoder_cycles) 
	        self.text_encoder_cycles.grid(row=row, column=1)
	
	        row += 1
	        self.label_profiles_per_frame = Label(text="Profiles Per Frame")
	        self.label_profiles_per_frame.grid(row=row, column=0)
	        self.text_profiles_per_frame = Entry(width=30, textvariable=self.profiles_per_frame) 
	        self.text_profiles_per_frame.grid(row=row, column=1)
	
	        row += 1
	        self.label_scan_length = Label(text="Scan Length (mm)")
	        self.label_scan_length.grid(row=row, column=0)
	        self.text_scan_length = Entry(width=30, textvariable=self.scan_length) 
	        self.text_scan_length.grid(row=row, column=1)
	        
	        row += 1
	        self.button_compute = Button(text="Compute", command=self.compute) 
	        self.button_compute.grid(row=row, column=0)
	
	        row += 1
	        self.label_radian_per_meter = Label(text="Radian Per Meter")
	        self.label_radian_per_meter.grid(row=row, column=0)
	        self.text_radian_per_meter = Entry(width=30, state="readonly", textvariable=self.radian_per_meter) 
	        self.text_radian_per_meter.grid(row=row, column=1)
	
	        row += 1
	        self.label_cycles_per_meter = Label(text="Cycles Per Meter")
	        self.label_cycles_per_meter.grid(row=row, column=0)
	        self.text_cycles_per_meter = Entry(width=30, state="readonly", textvariable=self.cycles_per_meter) 
	        self.text_cycles_per_meter.grid(row=row, column=1)
	
	        row += 1
	        self.label_distance_per_cycle = Label(text="Distance Per Cycle")
	        self.label_distance_per_cycle.grid(row=row, column=0)
	        self.text_distance_per_cycle = Entry(width=30, state="readonly", textvariable=self.distance_per_cycle) 
	        self.text_distance_per_cycle.grid(row=row, column=1)
	
	        row += 1
	        self.label_steps_per_line = Label(text="Steps Per Line (Dual Channel)")
	        self.label_steps_per_line.grid(row=row, column=0)
	        self.text_steps_per_line = Entry(width=30, state="readonly", textvariable=self.steps_per_line) 
	        self.text_steps_per_line.grid(row=row, column=1)
	        
	        row += 1
	        self.label_accuracy = Label(text="Accuracy")
	        self.label_accuracy.grid(row=row, column=0)
	        self.text_accuracy = Entry(width=30, state="readonly", textvariable=self.accuracy) 
	        self.text_accuracy.grid(row=row, column=1)
	        
	        row += 1
	        self.label_distance_per_frame = Label(text="Distance Per Frame")
	        self.label_distance_per_frame.grid(row=row, column=0)
	        self.text_distance_per_frame = Entry(width=30, state="readonly", textvariable=self.distance_per_frame) 
	        self.text_distance_per_frame.grid(row=row, column=1)        
	
	        row += 1
	        self.label_number_frames = Label(text="Number Frames")
	        self.label_number_frames.grid(row=row, column=0)
	        self.text_number_frames = Entry(width=30, state="readonly", textvariable=self.number_frames) 
	        self.text_number_frames.grid(row=row, column=1)        
	
	    def compute(self):
	        rtgr = float(self.transmission_gear_ratio.get().strip())
	        ir = float(self.gearbox_ratio.get().strip())
	        epc = int(self.encoder_cycles.get().strip())
	        rpm = rtgr/ir
	        cpm = epc*(rpm/(self.pi.get()*2))
	        dpc = 1000/cpm
	        spl = int(self.expected_accuracy.get()/dpc*self.encoder_type.get())
	        accuracy = dpc / self.encoder_type.get() * spl
	        dpf = accuracy * self.profiles_per_frame.get()
	        nf = round(self.scan_length.get()/dpf) + 1
	        self.radian_per_meter.set(rpm)        
	        self.cycles_per_meter.set(round(cpm))        
	        self.distance_per_cycle.set(dpc)
	        self.steps_per_line.set(spl)
	        self.accuracy.set(round(accuracy, 2))
	        self.distance_per_frame.set(round(dpf, 2))
	        self.number_frames.set(nf)
	        
	        
	root = Tk()
	app = Application(master=root)
	app.mainloop()


# 注意 #

在设置线激光触发扫描脉冲频率SPL时(Y向分辨率)，除了需要参考项目的精度要求，还需要参考X方向的分辨率，一般推荐X向和Y向的精度保持相当，这样可以使采集的图像长宽比更符合实际工件，后期使用视觉算法获取特征时也更容易。