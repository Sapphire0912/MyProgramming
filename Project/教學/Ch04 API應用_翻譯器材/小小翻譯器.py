from tkinter import *
from urllib import request
from urllib import parse
import json

win = Tk()
win.title("MyTranslator")
win.geometry("250x130")

def translate_word(en_str):
    url = 'https://translate.google.com.tw/'
    re


def trans_click(event):
    pass

def clr_click(event):
    pass

# 輸入文字 以及 翻譯結果
Label(win, text = "輸入要翻譯的內容: ", width = 15).place(x = 1, y = 1)
ip = Entry(win, width = 20)
ip.place(x = 110, y = 1)
Label(win, text = "翻譯的結果: ", width = 18).place(x = 1, y = 20)
s = StringVar()
s.set("Test")
result = Entry(win, width = 20, textvariable = s)
result.place(x = 110, y = 20)

# 翻譯 和 清空 按鈕
trans = Button(win, text = "翻譯", width = 8)
trans.place(x = 40, y = 80)
clr = Button(win, text = "清空", width = 8)
clr.place(x = 110, y = 80)

# 將按鈕綁定事件
trans.bind("<Button-1>", trans_click)
clr.bind("<Button-1>", clr_click)


win.mainloop()