import tkinter as tk
win = tk.Tk()
# 視窗區塊(frame)
# syntax: name = tk.frame(item[,parameter...etc])
# parameter:
#     width, height: 視窗區塊的寬, 高
#     bg: 視窗區塊的背景顏色

frame1 = tk.Frame(win)
frame1.pack()
label1 = tk.Label(frame1, text = "Title1: ")
entry = tk.Entry(frame1)
label1.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)

frame2 = tk.Frame(win)
frame2.pack()
button1 = tk.Button(frame2, text = "確定")
button2 = tk.Button(frame2, text = "取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
win.mainloop()