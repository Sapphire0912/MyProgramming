import tkinter as tk
win = tk.Tk()
win.geometry("800x400")
# 選項按鈕(Radiobutton只可以單選)
# syntax: name = tk.Radiobutton(item[,parameter...etc])
# parameter:
#     width: 寬度
#     height: 高度
#     text: 內容文字
#     variable: 動態設定元件值變數
#     bg: 背景顏色
#     fg: 文字顏色
#     font: 文字字體和大小
#     padx,pady: 與視窗的水平,垂直間距
#     value: 使用者點選後的元件值
#     command: 選擇選項後要執行的函式
#     select(): 點選元件

def choose():
    msg.set("最喜歡的運動: " + choice.get())

choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text = "選擇最喜歡的運動")
label.pack()

item1 = tk.Radiobutton(win, text="足球", value="足球", variable = choice, command = choose)
item1.pack()

item2 = tk.Radiobutton(win, text="籃球", value="籃球", variable = choice, command = choose)
item2.pack()

item3 = tk.Radiobutton(win, text="棒球", value="棒球", variable = choice, command = choose)
item3.pack()

lblmsg = tk.Label(win, fg = "red", textvariable = msg)
lblmsg.pack()
item1.select() # 預設為點選第一個物件
choose()
win.mainloop()