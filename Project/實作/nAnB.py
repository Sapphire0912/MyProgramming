import tkinter as tk
import tkinter.font 

# 包含處理例外錯誤的問題
# 包含再一局, 結束按鈕
# 可以的話 新增開始按鈕 點擊按鈕後 進到遊戲開始的畫面

# 視窗架構
win = tk.Tk()
win.geometry("320x320")
win.title("MynAnB")

# 玩家輸入數字
ft = ("標楷體", 12, "bold")
input_num = tk.Label(win, text = '輸入要猜的數字: ', font = ft)
input_num.grid(row = 0, column = 0, sticky = 'e')
_input = tk.StringVar()
entry_input = tk.Entry(win, textvariable = _input, font = ft, width = 10) 
entry_input.grid(row = 0, column = 1, sticky = 'w')

# 電腦輸出結果
output_AB = tk.Label(win, text = '結果: ', font = ft)
output_AB.grid(row = 1, column = 0, sticky = 'e')
_output = tk.StringVar()
entry_AB = tk.Entry(win, textvariable = _output, font = ft, width = 10, state = 'readonly')
entry_AB.grid(row = 1, column = 1, sticky = 'w')

# 猜過的紀錄

# 猜, 清除 按鈕

win.mainloop()