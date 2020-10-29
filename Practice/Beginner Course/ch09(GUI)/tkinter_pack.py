import tkinter as tk
win = tk.Tk()
win.geometry("400x400")
# pack() method:
# parameter:
#   padx, pady: 水平, 垂直間距
#   side: 設定位置, left,right,top,bottom

button1 = tk.Button(win, text = "Button 1")
button1.pack(side = 'left')

button2 = tk.Button(win,padx = 15 , text = "Button 2")
button2.pack(side = "top")

button3 = tk.Button(win, text = "Button 3")
button3.pack(side = "right")

button4 = tk.Button(win, text = "Button 4")
button4.pack(side = "bottom")
win.mainloop()