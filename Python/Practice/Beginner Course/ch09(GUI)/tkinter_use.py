import tkinter as tk
# 建立tkinter物件
win = tk.Tk()
# tkinter物件的方法
# geometry: 設定主視窗的尺寸:
#     item.geometry("width x height") x為小寫字母
# title("string"): 設定主視窗的標題
# mainloop(): 在主視窗建立完成之後, 使用此方法來操作GUI介面 

# Label(item[,parameter...etc]): 建立標籤物件, item為tkinter物件
# parameter:
#     width: 設定元件寬度
#     height: 設定元件高度
#     text: 設定元件文字內容
#     textvariable: 設定元件動態內容的文字變數
#     background(bg): 設定元件背景顏色
#     foreground(fg): 設定元件文字顏色
#     font: 設定文字字體和尺寸, font=("字體", 大小)
#     padx: 設定元件和視窗的水平間距
#     pady: 同上, 垂直間距
# Label方法:
# pack(): 將元件為矩形顯示

win.geometry("800x400")
win.title("Main")

label1 = tk.Label(win, text="這是標籤元件", fg="red", bg="yellow", font=("標楷體",12), padx=20, pady=10)
label1.pack()

win.mainloop()