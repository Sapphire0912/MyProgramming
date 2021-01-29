#coding=utf8
from tkinter import * 
from tkinter import messagebox

win = Tk()
win.title('我的視窗')
# win.geometry("400x200")

def label_example():
    # Label 元件 範例
    label = Label(win, text = '你好', anchor = 'nw')
    label.pack()

    # 顯示內建的點陣圖
    label2 = Label(win, bitmap = 'question') # 建立顯示疑問圖示的 Label 元件
    label2.pack()

    # 顯示自選的圖片
    path = "C:\\Users\\iris2\\OneDrive\\桌面\\MyProgramming\\Project\\教學\\emoji.png"
    bm = PhotoImage(file = path)
    label3 = Label(win, image = bm)
    label3.bm = bm 
    label3.pack()

# Button 物件, 按鈕可以包含文字或影像, 可以透過 command 屬性將呼叫函數或方法連結按鈕上

def entry_example():
    # Entry 元件, 主要用於 輸入單行和顯示文字
    # 建立 Entry 物件 (Entry 物件 = Entry(windows 視窗物件))
    
    # 使用 get() 用來取得單行文字標籤內輸入的內容
    # 設定或取得 Entry 元件內容也可以使用 StringVar() 物件來完成
    s = StringVar() # 一個 StringVar() 物件
    s.set("測試 Entry 元件")
    entry1 = Entry(win, textvariable = s) # Entry 元件顯示 s.set() 的內容
    # print(s.get())
    entry1.pack()
    # state 屬性可以設定元件狀態, 預設為 normal, 可以設為 disable, readonly
    # 常用屬性在課本裡 或者找 官方文檔

def listbox_example():
    # 列表方塊元件 Listbox 用於顯示多個專案, 並且允許使用者選擇一個或多個專案
    # 建立和顯示 Listbox 物件 (建立方法, Listbox 物件 = Listbox(windows 視窗物件))
    # 插入文字項 (Listbox 物件.insert(index, item))
    # 傳回選取專案的索引 (Listbox 物件.curselection())
    # 刪除文字項(Listbox 物件.delete(first, last))
    # 取得專案內容(Listbox 物件.get(first, last))
    # 取得專案個數 (Listbox 物件.size())
    # 取得 Listbox 內容 需要使用 listvariable 屬性為 Listbox 物件指定一個對應的變數
    # m = StringVar()
    # listb = Listbox(win, listvariable = m)
    # listb.pack()
    # 使用 m.get() 可以取得 Listbox 物件的內容
    # 若允許多選, 把 selectmode屬性 設定為 MULTIPLE, 而 SINGLE 為單選

    # 建立從一個列表方塊選擇內容增加到另一個列表方塊的 GUI 程式
    def callbutton1():
        for i in listb.curselection():  # 檢查選取項
            listb2.insert(0, listb.get(i)) # 插入右側列表方塊中

    def callbutton2():
        for i in listb2.curselection():
            listb2.delete(i)
    
    # 建立兩個列表
    li = ['C', 'Python', 'PHP', 'HTML', 'SQL', 'Java']
    listb = Listbox(win)
    listb2 = Listbox(win)
    
    for item in li:
        listb.insert(0, item) # 左側列表方塊元件插入資料
    
    listb.grid(row = 0, column = 0, rowspan = 2)
    b1 = Button(win, text = "新增 >>", command = callbutton1, width = 20)
    b2 = Button(win, text = "刪除 <<", command = callbutton2, width = 20)
    b1.grid(row = 0, column = 1, rowspan = 2)
    b2.grid(row = 1, column = 1, rowspan = 2)
    listb2.grid(row = 0, column = 2, rowspan = 2)

def choosebutton_example():
    # 選項按鈕元件, 核取方塊元件 可以實現單選複選的功能
    # 兩者的操作一樣

    # Radiobutton 操作, 建立選項按鈕元件選擇國家的程式
    r = IntVar()
    r.set(2)
    radio = Radiobutton(win, variable = r, value = '1', text = '中國')
    radio.pack()
    radio = Radiobutton(win, variable = r, value = '2', text = '美國')
    radio.pack()
    radio = Radiobutton(win, variable = r, value = '3', text = '日本')
    radio.pack()
    radio = Radiobutton(win, variable = r, value = '4', text = '加拿大')
    radio.pack()
    radio = Radiobutton(win, variable = r, value = '5', text = '台灣')
    radio.pack()
    # print(r.get())

def menu_example():
    # 建立 Menu 物件(Menu 物件 = Menu(windows 視窗物件))
    # 將物件顯示在視窗中(Windows 視窗物件['menu'] = Menu 物件)
    def hello():
        print("你點選了主選單")
    
    m = Menu(win)
    for item in ['檔案', '編輯', '視圖']: # 增加選單項
        m.add_command(label = item, command = hello)
    win['menu'] = m

def messagebox_example():
    def btn1():
        messagebox.showinfo("Info", "Showinfo test")
    def btn2():
        messagebox.showwarning("Warning", "Showwarning test")
    def btn3():
        messagebox.showerror("Error", "Showerror test")
    def btn4():
        messagebox.askquestion("Question", "Askquestion test")
    def btn5():
        messagebox.askokcancel("OKCancel", "Askokcancel test")
    def btn6():
        messagebox.askyesno("YesNo", "Askyesno test")
    def btn7():
        messagebox.askretrycancel("Retry", "Askretrucancel test")

    win.title("Msg Box")
    btn1 = Button(win, text = 'showinfo', command = btn1)
    btn1.pack(fill = X)
    btn2 = Button(win, text = 'showwarning', command = btn2)
    btn2.pack(fill = X)
    btn3 = Button(win, text = 'showerror', command = btn3)
    btn3.pack(fill = X)
    btn4 = Button(win, text = 'askquestion', command = btn4)
    btn4.pack(fill = X)
    btn5 = Button(win, text = 'askokcancel', command = btn5)
    btn5.pack(fill = X)
    btn6 = Button(win, text = 'askyesno', command = btn6)
    btn6.pack(fill = X)
    btn7 = Button(win, text = 'askretrycancel', command = btn7)
    btn7.pack(fill = X)

x = 0
def frame_example():
    # 在分組織其他元件的過程中是非常重要的, 負責安排其他元件的位置
    # Frame 元件在螢幕上顯示為一個矩形區域, 作為顯示其他元件的容器
    # 建立 Frame 元件 Frame(windows 視窗物件, height, width, bg..etc)
    # LabelFrame 元件 是有標題的 Frame 元件, 可以使用 text 屬性設定 LabelFrame 元件的標題
    # win.title("使用 Frame 元件的實例")
    # f1 = Frame(win) # 建立 第 1 個 Frame 元件
    # f1.pack()
    # f2 = Frame(win) # 建立 第 2 個 Frame 元件
    # f2.pack()

    # f3 = LabelFrame(win, text = '第 3 個 Frame')
    # f3.pack(side = BOTTOM)

    # redbutton = Button(f1, text = "Red", fg = "red")
    # redbutton.pack(side = LEFT)
    # brownbutton = Button(f1, text = "Brown", fg = "brown")
    # brownbutton.pack(side = LEFT)
    # bluebutton = Button(f1, text = "Blue", fg = "blue")
    # bluebutton.pack(side = LEFT)

    # blackbutton = Button(f2, text = "Black", fg = "black")
    # blackbutton.pack()

    # greenbutton = Button(f3, text = "Green", fg = "green")
    # greenbutton.pack()

    # 更新 Frame, 使用 after(), 每隔幾秒更新 GUI 圖形介面
    # 例如下面的程式 實現計數器的功能, 並且文字背景顏色不斷改變
    # colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
    # f = Frame(win, height = 200, width = 200)
    # f.color = 0
    # f['bg'] = colors[f.color] # 設定架構背景顏色
    # lab1 = Label(f, text = '0')
    # lab1.pack()

    # def foo():
    #     f.color = (f.color + 1) % (len(colors))
    #     lab1['bg'] = colors[f.color]
    #     lab1['text'] = str(int(lab1['text']) + 1)
    #     f.after(1000, foo) # 隔 1s 執行 foo() 函數更新螢幕
    # f.pack()
    # f.after(1000, foo)

    # 再使用一個跑馬燈的例子
    f = Frame(win, height = 200, width = 200)
    lab1 = Label(f, text = "Tkinter 跑馬燈")
    def foo():
        global x
        x += 10
        if x > 200:
            x = 0
        lab1.place(x = x, y = 0)
        f.after(500, foo)
    f.pack()
    f.after(500, foo)

# label_example()
# entry_example()
# listbox_example()
# choosebutton_example()
# menu_example()
messagebox_example()
# frame_example()

win.mainloop()