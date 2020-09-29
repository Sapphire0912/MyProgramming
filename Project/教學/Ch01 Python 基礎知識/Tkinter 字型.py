from tkinter import *
win = Tk()

# 透過元組表示字型
# 格式: (font family, size, modifiers)
# 例子: ("Times New Roman", "16", "bold italic") bold 粗體 italic 斜體 underline 底線
# for ft in ("Arial", ('Courier New', 19, 'italic'), ('Comic Sans MS',), 'Fixdsys', ('MS Sans Serif',), 'Symbol', 'System', ('Times New Roman',)):
#     Label(win, text = "Hello sticky", font = ft).grid()
# win.mainloop()

# 透過 Font 物件表示字型
# 格式: ft = tkinter.font.Font(family, size, weight, slant, underline, overstrike)
# 參數由左到右, 字型 大小 寬度(設為 bold or normal) 設定italic or normal  是否底線 0 or 1  是否有刪除線 0 or 1 
import tkinter.font
# ft = tkinter.font.Font(family = 'Fixdsys', size = 20, weight = 'bold')
# Label(win, text = 'hello sticky', font = ft).grid() 
# win.mainloop()

# print(tkinter.font.families()) # 傳回可用的字型模組