import tkinter as tk
import tkinter.font
import googletrans

win = tk.Tk()
win.geometry("640x320")
win.title("MyGoogleTrans_GUI")

ft = ('標楷體', 16, "bold")
input_trans = tk.Label(win, text = "輸入要翻譯的文字: ", font = ft)
input_trans.grid(row = 0, column = 0)

# 選擇輸入語言, 選擇翻譯語言


# output_trans = tk.Label(win, text = "翻譯的結果: ", font = ft)
# output_trans.grid(row = 3, column = 0)

# 翻譯, 清除 按鈕
def trans_click(event):
    pass

def clr_click(event):
    pass

button_trans = tk.Button(win, text = "翻譯", font = ft, command = trans_click)
button_clr = tk.Button(win, text = "清除", font = ft, command = clr_click)

button_trans.grid(row = 2, column = 2)
button_clr.grid(row = 2, column = 3)

win.mainloop()