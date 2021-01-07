import tkinter as tk
win = tk.Tk()
win.geometry("600x400")
# Button use method: 
# name = tk.Button(item[,parameter...etc])
# parameter:
#     width: 設定按鈕寬度
#     height: 設定按鈕高度
#     text: 設定按鈕文字
#     textvariable: 設定按鈕動態文字的文字變數
#     background: 設定按鈕背景顏色
#     foreground: 設定按鈕文字顏色
#     font: 設定按鈕文字的字體和大小
#     padx: 與主視窗的水平間距
#     pady: 同上, 垂直間距
#     command: 設定使用者按下按鈕時要執行的函式

# textvariable 參數: 
#     name = tk.StringVar(): Type is string, default is None-string
#     name = tk.IntVar(): Type is integer, default is 0
#     name = tk.DoubleVar(): Type is float, default is 0.0
# 文字變數的兩種方法
#     name.get(): get the content of text 
#     name.set(string): set the content of text

def click1():
    textvar.set("我已經被按過了")

textvar = tk.StringVar() # 先設定動態文字類型 並且給予textvar變數
button1 = tk.Button(win, textvariable = textvar, command = click1)
textvar.set("按鈕")
button1.pack()
win.mainloop()