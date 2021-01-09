import tkinter as tk
win = tk.Tk()
win.title("登入")
win.geometry("320x120")

tk.Label(win, text='帳號', width=6).place(x=1, y=1)
tk.Entry(win, width=20).place(x=45, y=1)
tk.Label(win, text="密碼", width=6).place(x=1, y=20)
tk.Entry(win, width=20, show="*").place(x=45, y=20)
tk.Button(win, text="登入", width=8).place(x=40, y=40)
tk.Button(win, text='取消', width=8).place(x=110, y=40)
win.mainloop()