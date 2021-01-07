import tkinter as tk
win = tk.Tk()
win.geometry("200x100")

def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if(btntext.get() == "按我！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")

labeltext = tk.StringVar()
label1 = tk.Label(win, fg="blue",font=("標楷體",12), textvariable = labeltext)
count = 0
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

btntext = tk.StringVar()
button1 = tk.Button(win, textvariable = btntext, command = clickme)
btntext.set("按我！")
button1.pack()
win.mainloop()