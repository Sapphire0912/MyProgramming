import tkinter as tk
win = tk.Tk()
win.geometry("800x400")
# 文字編輯元件(Entry)
# syntax: name = tk.Entry(item[,parameter...etc])
# parameter:
#   除了insert()方法以外, Entry的參數與text的參數相同

def checkpw():
    if (userin.get() != "0912"):
        hint.config(fg = "red")
        hinttext.set("密碼錯誤, 請修正密碼")
    else:
        hint.config(fg = "green")
        hinttext.set("密碼正確, 歡迎登入")

hinttext = tk.StringVar()
userin = tk.StringVar()

use = tk.Label(win, text="請輸入密碼: ")
use.pack()

enter = tk.Entry(win, textvariable = userin)
enter.pack()
login = tk.Button(win, text="登入", command = checkpw)
login.pack()

hint = tk.Label(win, textvariable = hinttext)
hint.pack()
win.mainloop()