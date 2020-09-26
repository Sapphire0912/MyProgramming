import tkinter as tk
win = tk.Tk()  # 建立 Windows 視窗物件
win.title('我的第一個 GUI 程式') # 設定視窗標題
win.geometry("800x600") # 設定視窗大小

label = tk.Label(win, text = "Hello, Python")
label.pack() # 把 Label1 元件增加到視窗中顯示

button1 = tk.Button(win, text = "BUTTON1")
button1.pack(side = tk.LEFT) # 放在父元件的左邊

button2 = tk.Button(win, text = "BUTTON2")
button2.pack(side = tk.RIGHT) # 放在父元件的右邊

win.mainloop() # 進入訊息循環, 也就是顯示視窗
