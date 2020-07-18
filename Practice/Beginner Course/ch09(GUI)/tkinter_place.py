import tkinter as tk
win = tk.Tk()
win.geometry("400x150")
# place() method
# parameter:
#     relx: 調整橫軸位置(0~1)
#     rely: 調整縱軸位置(0~1)
#     anchor: 設定元件位置的基準點, 有9種(center為正中心, 其他位置為方位第一個字的簡寫)

button1 = tk.Button(win, text = "Button 1", width = 20)
button1.place(relx = 0.5, rely = 0.5, anchor = "center")

button2 = tk.Button(win, text = "Button 2", width = 20)
button2.place(relx = 0.1, rely = 0.1, anchor = "nw")

button3 = tk.Button(win, text = "Button 3", width = 20)
button3.place(relx = 0.1, rely = 0.8, anchor = "se")
win.mainloop()