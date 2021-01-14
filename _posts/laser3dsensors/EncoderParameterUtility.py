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
