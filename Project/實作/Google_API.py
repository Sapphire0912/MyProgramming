import tkinter as tk
import tkinter.font
import googletrans
from PIL import Image, ImageTk

# 視窗大小
win = tk.Tk()
win.geometry("640x480")
win.title("MyGoogleTrans_GUI")

# 輸入, 輸出的方框
ft = ('標楷體', 12, "bold")
input_trans = tk.Label(win, text = "輸入要翻譯的文字: ", font = ft)
input_trans.grid(row = 0, column = 0)
_input = tk.StringVar()
entry_input = tk.Entry(win, textvariable = _input, width = 50)
entry_input.grid(row = 0, column = 1)

output_trans = tk.Label(win, text = "翻譯的結果: ", font = ft)
output_trans.grid(row = 1, column = 0, sticky = 'e')
_output = tk.StringVar()
entry_output = tk.Entry(win, textvariable = _output, width = 50, state = 'readonly')
entry_output.grid(row = 1, column = 1)

# 選擇輸入語言, 選擇翻譯語言(先做 中英日三種)
# 使用核取方塊來做
rad_l = tk.StringVar()
rad_l.set(2)
radio = tk.Radiobutton(win, variable = rad_l, value = "zh-tw", text = "中文", font = ft)
radio.grid(row = 2, column = 0, sticky = 'e')
radio = tk.Radiobutton(win, variable = rad_l, value = "en", text = "英文", font = ft)
radio.grid(row = 3, column = 0, sticky = 'e')
radio = tk.Radiobutton(win, variable = rad_l, value = "ja", text = "日文", font = ft)
radio.grid(row = 4, column = 0, sticky = 'e')

# 暫時不用圖片
# path = "C:\\Users\\iris2\\OneDrive\\桌面\\MyProgramming\\Project\\實作\\arrow.jpg"
# img = Image.open(path)
# img_conv = ImageTk.PhotoImage(img)
# img_label = tk.Label(win, image = img_conv)
# img_label.img_conv = img_conv
# img_label.grid(row = 2, column = 1, ipady = 20)

text_cov = tk.Label(win, text = ">>>>>>", font = ft)
text_cov.grid(row = 3, column = 1, sticky = 'w', padx = 42)

rad_r = tk.StringVar()
rad_r.set(2)
radio = tk.Radiobutton(win, variable = rad_r, value = "zh-tw", text = "中文", font = ft)
radio.grid(row = 2, column = 1)
radio = tk.Radiobutton(win, variable = rad_r, value = "en", text = "英文", font = ft)
radio.grid(row = 3, column = 1)
radio = tk.Radiobutton(win, variable = rad_r, value = "ja", text = "日文", font = ft)
radio.grid(row = 4, column = 1)

# 歷史紀錄
his_label = tk.Label(win, text = "歷史紀錄: ", font = ft)
his_label.grid(row = 6, column = 0, sticky = "ne", pady = 20)
history_text = tk.Text(win, height = 20, width = 60, font = ("標楷體", 9))
history_text.grid(row = 6, column = 1, sticky = 'we', pady = 20)

# 翻譯, 清除 按鈕
def trans_click():
    translator = googletrans.Translator()
    target_text = _input.get()
    language = rad_r.get()
    result = translator.translate(target_text, dest = language)
    result = result.text
    _output.set(result)
    
    history_text.insert("insert", target_text)
    history_text.insert("insert", " -> " + result)
    history_text.insert("insert", "\n")

def clr_click():
    _input.set("")
    _output.set("")

button_trans = tk.Button(win, text = "翻譯", font = ft, command = trans_click)
button_clr = tk.Button(win, text = "清除", font = ft, command = clr_click)

button_trans.grid(row = 5, column = 1, sticky = 'w', padx = 20)
button_clr.grid(row = 5, column = 1, sticky = 'w', padx = 70)

win.mainloop()