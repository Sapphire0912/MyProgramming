# -*- coding = utf8 -*-
import tkinter as tk
import random, time
number = random.randint(0, 1024) # 玩家要猜的數字
running = True
count = 0 # 猜的次數
nmaxn = 1024 # 提示猜測的最大範圍
nminn = 0 # 提示猜測範圍的最小數

def BtnClose(event):  # 關閉按鈕事件函數
    root.destroy()

def BtnGuess(event):
    global nmaxn
    global nminn
    global count
    global running
    if running:
        val_a = int(entry_a.get()) # 取得使用者猜的數字並轉換成數字
        if val_a == number:
            labelqval("恭喜答對了")
            count += 1
            running = False
            numGuess()  # 顯示猜的次數
        elif val_a < number:
            if val_a > nminn:
                nminn = val_a
                count += 1
                labelqval("猜小了, 請輸入 " + str(nminn) + " 到 " + str(nmaxn) + "之間的整數")
        else:
            if val_a < nmaxn:
                nmaxn = val_a
                count += 1
                labelqval("猜大了, 請輸入 "+ str(nminn) + " 到 " + str(nmaxn) + "之間的整數")
    else:
        labelqval("你已經答對了")

def numGuess(): # 顯示猜的次數
    if count == 1:
        labelqval("一次答對")
    elif count < 10 and ~running:
        labelqval("恭喜十次以內答對, 看來你很熟悉 log 呢")
    time.sleep(2)
    labelqval('嘗試次數: ' + str(count))

def labelqval(vText):
    label_val_q.config(label_val_q, text = vText) # 修改提示標籤文字

root = tk.Tk(className = "猜數字遊戲")
root.geometry("400x90+200+200")
label_val_q = tk.Label(root, width = 80) # 提示標籤
label_val_q.pack(side = 'top')

entry_a = tk.Entry(root, width = 40) # 單行輸入文字標籤
btnguess = tk.Button(root, text = "猜") # 猜的按鈕
entry_a.pack(side = "left")
entry_a.bind('<Return>', BtnGuess) # 綁定事件
btnguess.bind('<Button-1>', BtnGuess) # 猜的按鈕
btnguess.pack(side = 'left')

btnclose = tk.Button(root, text = "關閉") # 關閉 按鈕
btnclose.bind('<Button-1>', BtnClose)
btnclose.pack(side = "left")
labelqval("請輸入 0 ~ 1024 之間的任意整數")
entry_a.focus_set()
print(number)
root.mainloop()

# Q. GUI 寫成 nAnB 的猜數字 先由玩家猜電腦

