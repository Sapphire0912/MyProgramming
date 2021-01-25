from tkinter import *


def use_volt():
    global voltage
    voltage = volt_val.get()
    volt.destroy()


def sw_all_check():
    sw_val0.set(1)
    sw_val1.set(1)
    sw_val2.set(1)
    sw_val3.set(1)
    sw_val4.set(1)
    sw_val5.set(1)
    sw_val6.set(1)
    sw_val7.set(1)


def sw_clear():
    sw_val0.set(0)
    sw_val1.set(0)
    sw_val2.set(0)
    sw_val3.set(0)
    sw_val4.set(0)
    sw_val5.set(0)
    sw_val6.set(0)
    sw_val7.set(0)


def btn_all_check():
    btn_val_center.set(1)
    btn_val_left.set(1)
    btn_val_right.set(1)
    btn_val_up.set(1)
    btn_val_down.set(1)


def btn_clear():
    btn_val_center.set(0)
    btn_val_left.set(0)
    btn_val_right.set(0)
    btn_val_up.set(0)
    btn_val_down.set(0)


def led_all_check():
    led_val0.set(1)
    led_val1.set(1)
    led_val2.set(1)
    led_val3.set(1)
    led_val4.set(1)
    led_val5.set(1)
    led_val6.set(1)
    led_val7.set(1)


def led_clear():
    led_val0.set(0)
    led_val1.set(0)
    led_val2.set(0)
    led_val3.set(0)
    led_val4.set(0)
    led_val5.set(0)
    led_val6.set(0)
    led_val7.set(0)


def pi_clear():
    pi_val3.set(0)
    pi_val5.set(0)
    pi_val11.set(0)
    pi_val13.set(0)
    pi_val15.set(0)
    pi_val19.set(0)
    pi_val21.set(0)
    pi_val23.set(0)
    pi_val29.set(0)
    pi_val31.set(0)
    pi_val33.set(0)
    pi_val35.set(0)
    pi_val37.set(0)
    pi_val8.set(0)
    pi_val10.set(0)
    pi_val12.set(0)
    pi_val16.set(0)
    pi_val18.set(0)
    pi_val22.set(0)
    pi_val24.set(0)
    pi_val26.set(0)
    pi_val32.set(0)
    pi_val36.set(0)
    pi_val38.set(0)
    pi_val40.set(0)


def transform():
    global set_sw_name
    # handle switch
    s0 = sw_val0.get()
    s1 = sw_val1.get()
    s2 = sw_val2.get()
    s3 = sw_val3.get()
    s4 = sw_val4.get()
    s5 = sw_val5.get()
    s6 = sw_val6.get()
    s7 = sw_val7.get()
    switch_type = sw_type.get()
    switch_list = [s0, s1, s2, s3, s4, s5, s6, s7]


# 全局變數
voltage = '25'
title = "xdc檔案生成"
ft = ('標楷體', '12', "bold")
set_sw_name = list()

# 設定電壓後才進入設定腳位視窗
volt = Tk()
volt.title(title)
volt.geometry('200x200')
volt_val = StringVar()
volt_val.set('25')
volt_25 = Radiobutton(volt, variable=volt_val, value='25', text='2.5V', font=ft)
volt_33 = Radiobutton(volt, variable=volt_val, value='33', text='3.3V', font=ft)
volt_25.pack()
volt_33.pack()
volt_check = Button(volt, text='確定', font=ft, command=use_volt)
volt_check.pack()
volt.mainloop()

win = Tk()
win.geometry('960x480')
win.title(title)

# create switch
frame_sw = Frame(win, relief="groove", bd=5, padx=10)
sw_val0 = IntVar()
sw0 = Checkbutton(frame_sw, text='sw0', variable=sw_val0, onvalue=1, offvalue=0, font=ft)
sw_val1 = IntVar()
sw1 = Checkbutton(frame_sw, text='sw1', variable=sw_val1, onvalue=1, offvalue=0, font=ft)
sw_val2 = IntVar()
sw2 = Checkbutton(frame_sw, text='sw2', variable=sw_val2, onvalue=1, offvalue=0, font=ft)
sw_val3 = IntVar()
sw3 = Checkbutton(frame_sw, text='sw3', variable=sw_val3, onvalue=1, offvalue=0, font=ft)
sw_val4 = IntVar()
sw4 = Checkbutton(frame_sw, text='sw4', variable=sw_val4, onvalue=1, offvalue=0, font=ft)
sw_val5 = IntVar()
sw5 = Checkbutton(frame_sw, text='sw5', variable=sw_val5, onvalue=1, offvalue=0, font=ft)
sw_val6 = IntVar()
sw6 = Checkbutton(frame_sw, text='sw6', variable=sw_val6, onvalue=1, offvalue=0, font=ft)
sw_val7 = IntVar()
sw7 = Checkbutton(frame_sw, text='sw7', variable=sw_val7, onvalue=1, offvalue=0, font=ft)
# all/clear
sw_all = Button(frame_sw, text='全選', font=ft, command=sw_all_check)
sw_clr = Button(frame_sw, text='清除', font=ft, command=sw_clear)
# data type
sw_type = IntVar()
sw_type.set(1)
sw_logic = Radiobutton(frame_sw, variable=sw_type, text='std_logic', value=0, font=ft)
sw_vector = Radiobutton(frame_sw, variable=sw_type, text='std_logic_vector', value=1, font=ft)
# write switch name
# 用空白區分 然後使用 Entry 元件做按下轉換按鈕時讀取資料


sw0.grid(column=0, row=0)
sw1.grid(column=0, row=1)
sw2.grid(column=0, row=2)
sw3.grid(column=0, row=3)
sw4.grid(column=0, row=4)
sw5.grid(column=0, row=5)
sw6.grid(column=0, row=6)
sw7.grid(column=0, row=7)
sw_logic.grid(column=0, row=8)
sw_vector.grid(column=0, row=9)
sw_all.grid(column=0, row=10)
sw_clr.grid(column=0, row=11)
frame_sw.grid(column=0, row=0, sticky='n')

# create button
frame_btn = Frame(win, relief="groove", bd=5, padx=10)
btn_val_center = IntVar()
btn_c = Checkbutton(frame_btn, text='btn_c', variable=btn_val_center, onvalue=1, offvalue=0, font=ft)
btn_val_left = IntVar()
btn_l = Checkbutton(frame_btn, text='btn_l', variable=btn_val_left, onvalue=1, offvalue=0, font=ft)
btn_val_right = IntVar()
btn_r = Checkbutton(frame_btn, text='btn_r', variable=btn_val_right, onvalue=1, offvalue=0, font=ft)
btn_val_up = IntVar()
btn_up = Checkbutton(frame_btn, text='btn_up', variable=btn_val_up, onvalue=1, offvalue=0, font=ft)
btn_val_down = IntVar()
btn_down = Checkbutton(frame_btn, text='btn_down', variable=btn_val_down, onvalue=1, offvalue=0, font=ft)
# all/clear
btn_all = Button(frame_btn, text='全選', font=ft, command=btn_all_check)
btn_clr = Button(frame_btn, text='清除', font=ft, command=btn_clear)

btn_c.grid(column=1, row=0, sticky='w')
btn_l.grid(column=1, row=1, sticky='w')
btn_r.grid(column=1, row=2, sticky='w')
btn_up.grid(column=1, row=3, sticky='w')
btn_down.grid(column=1, row=4, sticky='w')
btn_all.grid(column=1, row=5)
btn_clr.grid(column=1, row=6)
frame_btn.grid(column=1, row=0, sticky='n')

# create led
frame_led = Frame(win, relief="groove", bd=5, padx=10)
led_val0 = IntVar()
led0 = Checkbutton(frame_led, text='led0', variable=led_val0, onvalue=1, offvalue=0, font=ft)
led_val1 = IntVar()
led1 = Checkbutton(frame_led, text='led1', variable=led_val1, onvalue=1, offvalue=0, font=ft)
led_val2 = IntVar()
led2 = Checkbutton(frame_led, text='led2', variable=led_val2, onvalue=1, offvalue=0, font=ft)
led_val3 = IntVar()
led3 = Checkbutton(frame_led, text='led3', variable=led_val3, onvalue=1, offvalue=0, font=ft)
led_val4 = IntVar()
led4 = Checkbutton(frame_led, text='led4', variable=led_val4, onvalue=1, offvalue=0, font=ft)
led_val5 = IntVar()
led5 = Checkbutton(frame_led, text='led5', variable=led_val5, onvalue=1, offvalue=0, font=ft)
led_val6 = IntVar()
led6 = Checkbutton(frame_led, text='led6', variable=led_val6, onvalue=1, offvalue=0, font=ft)
led_val7 = IntVar()
led7 = Checkbutton(frame_led, text='led7', variable=led_val7, onvalue=1, offvalue=0, font=ft)
# all/clear
led_all = Button(frame_led, text='全選', font=ft, command=led_all_check)
led_clr = Button(frame_led, text='清除', font=ft, command=led_clear)
led_type = StringVar()
led_type.set(1)
led_logic = Radiobutton(frame_led, variable=led_type, text='std_logic', value=0, font=ft)
led_vector = Radiobutton(frame_led, variable=led_type, text='std_logic_vector', value=1, font=ft)

led0.grid(column=2, row=0)
led1.grid(column=2, row=1)
led2.grid(column=2, row=2)
led3.grid(column=2, row=3)
led4.grid(column=2, row=4)
led5.grid(column=2, row=5)
led6.grid(column=2, row=6)
led7.grid(column=2, row=7)
led_logic.grid(column=2, row=8)
led_vector.grid(column=2, row=9)
led_all.grid(column=2, row=10)
led_clr.grid(column=2, row=11)
frame_led.grid(column=2, row=0, sticky='n')

# create user Raspberry Pi
# pin 1 17 3.3V; 9 25 39 6 14 20 30 34 GND; 2 4 5.0V;
frame_pi = Frame(win, relief="groove", bd=5)
# GPIO
pi_val3 = IntVar()
pi_3 = Checkbutton(frame_pi, text='3', variable=pi_val3, onvalue=1, offvalue=0, font=ft)
pi_val5 = IntVar()
pi_5 = Checkbutton(frame_pi, text='5', variable=pi_val5, onvalue=1, offvalue=0, font=ft)
pi_val11 = IntVar()
pi_11 = Checkbutton(frame_pi, text='11', variable=pi_val11, onvalue=1, offvalue=0, font=ft)
pi_val13 = IntVar()
pi_13 = Checkbutton(frame_pi, text='13', variable=pi_val13, onvalue=1, offvalue=0, font=ft)
pi_val15 = IntVar()
pi_15 = Checkbutton(frame_pi, text='15', variable=pi_val15, onvalue=1, offvalue=0, font=ft)
pi_val19 = IntVar()
pi_19 = Checkbutton(frame_pi, text='19', variable=pi_val19, onvalue=1, offvalue=0, font=ft)
pi_val21 = IntVar()
pi_21 = Checkbutton(frame_pi, text='21', variable=pi_val21, onvalue=1, offvalue=0, font=ft)
pi_val23 = IntVar()
pi_23 = Checkbutton(frame_pi, text='23', variable=pi_val23, onvalue=1, offvalue=0, font=ft)
pi_val29 = IntVar()
pi_29 = Checkbutton(frame_pi, text='29', variable=pi_val29, onvalue=1, offvalue=0, font=ft)
pi_val31 = IntVar()
pi_31 = Checkbutton(frame_pi, text='31', variable=pi_val31, onvalue=1, offvalue=0, font=ft)
pi_val33 = IntVar()
pi_33 = Checkbutton(frame_pi, text='33', variable=pi_val33, onvalue=1, offvalue=0, font=ft)
pi_val35 = IntVar()
pi_35 = Checkbutton(frame_pi, text='35', variable=pi_val35, onvalue=1, offvalue=0, font=ft)
pi_val37 = IntVar()
pi_37 = Checkbutton(frame_pi, text='37', variable=pi_val37, onvalue=1, offvalue=0, font=ft)

pi_val8 = IntVar()
pi_8 = Checkbutton(frame_pi, text='8', variable=pi_val8, onvalue=1, offvalue=0, font=ft)
pi_val10 = IntVar()
pi_10 = Checkbutton(frame_pi, text='10', variable=pi_val10, onvalue=1, offvalue=0, font=ft)
pi_val12 = IntVar()
pi_12 = Checkbutton(frame_pi, text='12', variable=pi_val12, onvalue=1, offvalue=0, font=ft)
pi_val16 = IntVar()
pi_16 = Checkbutton(frame_pi, text='16', variable=pi_val16, onvalue=1, offvalue=0, font=ft)
pi_val18 = IntVar()
pi_18 = Checkbutton(frame_pi, text='18', variable=pi_val18, onvalue=1, offvalue=0, font=ft)
pi_val22 = IntVar()
pi_22 = Checkbutton(frame_pi, text='22', variable=pi_val22, onvalue=1, offvalue=0, font=ft)
pi_val24 = IntVar()
pi_24 = Checkbutton(frame_pi, text='24', variable=pi_val24, onvalue=1, offvalue=0, font=ft)
pi_val26 = IntVar()
pi_26 = Checkbutton(frame_pi, text='26', variable=pi_val26, onvalue=1, offvalue=0, font=ft)
pi_val32 = IntVar()
pi_32 = Checkbutton(frame_pi, text='32', variable=pi_val32, onvalue=1, offvalue=0, font=ft)
pi_val36 = IntVar()
pi_36 = Checkbutton(frame_pi, text='36', variable=pi_val36, onvalue=1, offvalue=0, font=ft)
pi_val38 = IntVar()
pi_38 = Checkbutton(frame_pi, text='38', variable=pi_val38, onvalue=1, offvalue=0, font=ft)
pi_val40 = IntVar()
pi_40 = Checkbutton(frame_pi, text='40', variable=pi_val40, onvalue=1, offvalue=0, font=ft)
pi_clr = Button(frame_pi, text='清除', font=ft, command=pi_clear)

# GPIO_4_CLOCK
# pi_val7 = IntVar()
# ID_SDA, ID_SCL
# pi_val27 = IntVar()
# pi_val28 = IntVar()
pi_3.grid(column=4, row=0, sticky='w')
pi_5.grid(column=4, row=1, sticky='w')
pi_11.grid(column=4, row=2, sticky='w')
pi_13.grid(column=4, row=3, sticky='w')
pi_15.grid(column=4, row=4, sticky='w')
pi_19.grid(column=4, row=5, sticky='w')
pi_21.grid(column=4, row=6, sticky='w')
pi_23.grid(column=4, row=7, sticky='w')
pi_29.grid(column=4, row=8, sticky='w')
pi_31.grid(column=4, row=9, sticky='w')
pi_33.grid(column=4, row=10, sticky='w')
pi_35.grid(column=4, row=11, sticky='w')
pi_37.grid(column=4, row=12, sticky='w')

pi_8.grid(column=5, row=0, sticky='w')
pi_10.grid(column=5, row=1, sticky='w')
pi_12.grid(column=5, row=2, sticky='w')
pi_16.grid(column=5, row=3, sticky='w')
pi_18.grid(column=5, row=4, sticky='w')
pi_22.grid(column=5, row=5, sticky='w')
pi_24.grid(column=5, row=6, sticky='w')
pi_26.grid(column=5, row=7, sticky='w')
pi_32.grid(column=5, row=8, sticky='w')
pi_36.grid(column=5, row=9, sticky='w')
pi_38.grid(column=5, row=10, sticky='w')
pi_40.grid(column=5, row=11, sticky='w')
pi_clr.grid(column=5, row=12, sticky='w')
frame_pi.grid(column=4, row=0, sticky='n')

# 電壓選擇 2.5, 3.3V
# sw, led 要加上資料類型

# 轉換按鈕
frame_trans = Frame(win)
trans = Button(frame_trans, text='轉換', font=('標楷體', 24, "bold"), command=transform)
trans.grid(column=6, row=0, sticky='n')

# 生成文字位置
text_label = Label(frame_trans, text='轉換後文字', font=ft)
text_label.grid(column=6, row=1, sticky='n')
text = Text(frame_trans, height=23, width=60, state='disable', font=('標楷體', 12))
text.grid(column=6, row=2, sticky='n')

frame_trans.grid(column=6, row=0, sticky='n')
win.mainloop()
