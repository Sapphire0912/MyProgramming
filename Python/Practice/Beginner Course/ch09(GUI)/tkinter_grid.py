import tkinter as tk
win = tk.Tk()
win.geometry("800x400")
# grid() method:
# parameter:
#     row: 設定列的位置
#     column: 設定行的位置
#     padx, pady: 水平, 垂直間距
#     rowspan: 設定元件列位置的合併數量
#     columnspan: 同上, 行位置
#     sticky: 設定元件的排列方式, (e, w, n, s) -> (右, 左, 上, 下)

button1 = tk.Button(win, text = "Button 1", width = 20)
button1.grid(row = 0, column = 0, padx = 5, pady = 5)

button2 = tk.Button(win, text = "Button 2", width = 20)
button2.grid(row = 0, column = 1, padx = 5, pady = 5)

button3 = tk.Button(win, text = "Button 3", width = 20)
button3.grid(row = 0, column = 2, padx = 5, pady = 5)

button4 = tk.Button(win, text = "Button 4", width = 20)
button4.grid(row = 1, column = 0, padx = 5, pady = 5)

button5 = tk.Button(win, text = "Button 5", width = 20)
button5.grid(row = 1, column = 1, padx = 5, pady = 5)

button6 = tk.Button(win, text = "Button 6", width = 20)
button6.grid(row = 1, column = 2, padx = 5, pady = 5)
win.mainloop()