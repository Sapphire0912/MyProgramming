import tkinter as tk
win = tk.Tk()
win.geometry("800x400")
# 設定文字區塊元件(Text)
# syntax: name = tk.Text(item[,parameter...etc])
# parameter:
#     width: 設定寬度
#     height: 設定高度
#     bg: 設定背景顏色
#     fg: 設定文字顏色
#     font: 設定字體樣式和大小
#     padx: 水平間距
#     pady: 垂直間距
#     state: 設定文字內容是否可被編輯(預設tk.NORMAL 為可被編輯, 反之tk.DISABLED)
#     insert(): 加入文字內容
# ! 文字區塊無法在建立元件時設定文字內容, 所以要使用insert方法

# insert method:
# syntax: name.insert(Type, String)
#   Type: tk.INSERT 將String加入文字方塊
#         tk.END  將String加入文字方塊, 並結束文字方塊內容

# 若已經建立元件, 卻想要變更元件的參數設定 要使用config方法
# config method: 
# syntax: name.config(parameter...etc)

text = tk.Text(win)
text.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面, \n")
text.insert(tk.INSERT, "(略)... \n")
text.insert(tk.INSERT, "含於python 系統中, 不須安裝即可使用\n")
text.pack()
text.config(state = tk.DISABLED)
win.mainloop()