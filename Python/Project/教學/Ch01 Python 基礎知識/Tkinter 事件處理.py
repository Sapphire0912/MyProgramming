# 事件類型的通用格式如下
# <[modifier-]...type[-detail]>
# 事件類型必須放置於中括號<>內, type 描述類型(例如 鍵盤按鍵, 滑鼠點擊), modifier 用於組合鍵定義(例如 Ctrl Alt) 
# detail 用來明確定義是哪個鍵或按鈕事件(例如 1 滑鼠左鍵, 2 滑鼠中鍵, 3 滑鼠右鍵)
# 例子: <Button-1> 按下滑鼠左鍵, <KeyPress-A> 按下鍵盤上的A鍵, <Control-Shift-KeyPress-A> 同時按下 Ctrl+shift+A 

# 鍵盤事件
# KeyPress, 按下某按鍵時觸發(可指定某鍵)
# KeyRelease, 釋放某按鍵時觸發(可指定某鍵)

# 滑鼠事件
# ButtonPress 或 Button, 按下滑鼠某鍵(可指定某鍵)
# ButtonRelease 釋放滑鼠某鍵(可指定某鍵)
# Motion 點中元件的同時拖曳元件移動時觸發
# Enter 當滑鼠指標移進某元件時觸發
# Leave 當滑鼠指標移出某元件時觸發
# MouseWheel 滑鼠滾輪捲動時觸發

# 表單事件
# Visibility 當元件變成可視狀態觸發
# Unmap 元件由可視變隱藏狀態觸發
# Map 元件由隱藏變可視狀態觸發
# Expose 當元件從原本被其他元件遮蓋狀態中暴露出來時觸發
# FocusIn 元件獲得焦點觸發
# FocusOut 元件失去焦點觸發
# Configure 當改變元件大小時觸發(例如 拖曳表單邊緣)
# Property 當表單屬性被刪除或改變時觸發
# Destroy 當元件被銷毀時觸發
# Activate 與元件選項中的 state 項有關, 表示元件由不可用轉為可用, 例如按鈕由disabled -> enabled
# Deactivate 同上, 但反之

# modifier 組合鍵定義中常用的修飾符號
# Alt 把 Alt 鍵按下
# Any 按下任意鍵(例如 <Any-KeyPress>)
# Control Ctrl 鍵按下
# Double 兩個事件在短時間內發生(例如 雙擊滑鼠左鍵<Double-Button-1>)
# Lock Caps Lock 鍵按下
# Shift shift 鍵按下
# Triple 三個事件在短時間內同時發生

# 空白鍵為 space


# 事件綁定(觸發該元件時, 選擇要執行哪個函數)
# 建立元件物件時指定(之前的例子皆使用此種方法, 使用 command 參數指定)
# 實例綁定(元件物件實例名.bind("<事件類型>", 事件處理函數))
# 標籤綁定(例如 canvas.tag_bind('r1', "<Button-1>", printRect))
from tkinter import *
root = Tk()

# def printRect(event):
#     print("rectangle 左鍵事件")
# def printRect2(event):
#     print("rectangle 右鍵事件")
# def printLine(event):
#     print("Line 事件")

# cv = Canvas(root, bg = 'white')
# rtl = cv.create_rectangle(10, 10, 110, 110, width = 8, tags = 'r1')
# cv.tag_bind('r1', '<Button-1>', printRect)
# cv.tag_bind('r1', '<Button-3>', printRect2)

# # 建立一個 Line 並設為 tags = 'r2'
# cv.create_line(180, 70, 280, 70, width = 10, tags = "r2")
# cv.tag_bind('r2', '<Button-1>', printLine)
# cv.pack()
# root.mainloop()


# 事件處理函數
# 有關 Event 物件的參數可以查看課本或官方文檔
# 以下做一個例子 觸發KeyPress 鍵盤事件的實例

# def printkey(event):
#     print("You press the key of " + event.char)

# entry = Entry(root)
# entry.bind('<KeyPress>', printkey)
# entry.pack()
# root.mainloop()

# 接著 取得滑鼠點擊標籤時座標的滑鼠事件實例
def leftClick(event):
    print("x axis coordinate: ", event.x)
    print("y axis coordinate: ", event.y)
    print("x axis coordinate in the upper left of the screen: ", event.x_root)
    print("y axis coordinate in the upper left of the screen: ", event.y_root)

lab = Label(root, text = "Hello")
lab.pack()
lab.bind("<Button-1>", leftClick)
root.mainloop()
