import tkinter as tk
win = tk.Tk()
win.geometry("400x200")
# 核取方塊元件(Checkbutton可以複選)
# syntax: name = tk.Checkbutton(item[,parameter])
# parameter:
#   大部分的參數與radiobutton相同, 唯獨沒有value參數

def choose():
    global choice, ball
    str = "You like :"
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + ball[i] + " "
    msg.set(str)

choice = []
ball = ["soccer", "basketball", "baseball"]
msg = tk.StringVar()
label = tk.Label(win, text = "choose: ")
label.pack()

for i in range(0, len(ball)):
    tem = tk.IntVar()
    choice.append(tem)
    item = tk.Checkbutton(win, text = ball[i], variable = choice[i], command = choose)
    item.pack()
lblmsg = tk.Label(win, fg = "red", textvariable = msg)
lblmsg.pack()
win.mainloop()