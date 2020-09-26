import tkinter as tk
win = tk.Tk()
win.title("登入")
win.geometry("200x80")

tk.Button(win, text = '使用者名稱', width = 6).place(x = 1, y = 1)
tk.Entry(win, width = 20).place()