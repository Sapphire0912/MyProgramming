import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

# 所有的Matplotlib圖表, 都要建立 一個 figure 和 axes 開始
# figure 是類別plt.Figure的執行實例, 包含了所有的軸, 圖形, 文字, 標籤
# axes 是類別plt.Axes 的執行實例, 有邊界和刻度以及標籤的方框
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000) # 此時的數字代表徑度, 1徑度 = 57.3度
# ax.plot(x, np.sin(x))
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))

# 如果要建立的圖形有多線條, 只要多次呼叫plot即可

# 線條顏色和樣式
# plt.plot(x, np.sin(x - 0), color = 'blue') # 使用顏色名稱指定
# plt.plot(x, np.sin(x - 1), color = 'g') # 使用顏色編碼(rgbcmyk)
# plt.plot(x, np.sin(x - 2), color = '0.75') # 0~1之間的灰階
# plt.plot(x, np.sin(x - 3), color = '#FFDD44') # 16進位編碼(RRGGBB, 從00~FF)
# plt.plot(x, np.sin(x - 4), color = (1.0, 0.2, 0.3)) # RGB tuple 值0~1
# plt.plot(x, np.sin(x - 5), color = 'chartreuse') # 所有HTML中所支援的顏色名稱
# line 26: https://zh.wikipedia.org/wiki/%E7%BD%91%E9%A1%B5%E9%A2%9C%E8%89%B2

# 設定線條樣式
# plt.plot(x, x + 0, linestyle = 'solid') # '-'
# plt.plot(x, x + 1, linestyle = 'dashed') # '--'
# plt.plot(x, x + 2, linestyle = 'dashdot') # '-.'
# plt.plot(x, x + 3, linestyle = 'dotted') # ':'

# 比較簡潔的寫法, 把linestyle 和 color合併寫在一個沒有關鍵字的參數
# plt.plot(x, x + 4, '-g') # solid green
# plt.plot(x, x + 5, '--c') # dashed cyan
# plt.plot(x, x + 6, '-.k') # dashdot black
# plt.plot(x, x + 7, ':r') # dotted red

# 調整圖表: Axes 範圍(調整座標範圍)
# 調整axis範圍最直接的方式是使用 plt.xlim() 和 plt.ylim()方法
# plt.plot(x, np.sin(x))
# plt.xlim(-1, 11)
# plt.ylim(-1.5, 1.5)
# 若要反向顯示的話, 只要把參數的順序反過來即可
# plt.xlim(10, 0)
# plt.ylim(1.2, -1.2)

# plt.axis() 可以一次設定 x, y軸的寬度
# 只要傳一個 list 參數即可 [xmin, xmax, ymin, ymax]
# plt.axis([-1, 11, -1.5, 1.5]) 

# plt.axis() 進階功能 help(plt.axis)
# plt.axis('tight') # 圖形變得比較緊密
# plt.axis('equal') # 讓 x, y的單位保持相同比例
# plt.axis('scaled') 
# 'on'     Turn on axis lines and labels. Same as ``True``.
# 'off'    Turn off axis lines and labels. Same as ``False``.
# 'equal'  Set equal scaling (i.e., make circles circular) by
#          changing axis limits. This is the same as
#          ``ax.set_aspect('equal', adjustable='datalim')``.
#          Explicit data limits may not be respected in this case.
# 'scaled' Set equal scaling (i.e., make circles circular) by
#          changing dimensions of the plot box. This is the same as
#          ``ax.set_aspect('equal', adjustable='box', anchor='C')``.
#          Additionally, further autoscaling will be disabled.
# 'tight'  Set limits just large enough to show all data, then
#          disable further autoscaling.
# 'auto'   Automatic scaling (fill plot box with data).
# 'normal' Same as 'auto'; deprecated.
# 'image'  'scaled' with axis limits equal to data limits.
# 'square' Square plot; similar to 'scaled', but initially forcing
#          ``xmax-xmin == ymax-ymin``.

# 為圖表加上標籤
# plt.title("A Sine Curve.")
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.plot(x, np.sin(x), '-g', label = 'sin(x)')
# plt.plot(x, np.cos(x), '-.r', label = 'cos(x)')
# plt.axis('equal')

# plt.legend() # 持續追蹤線條樣式和色彩, 讓他們和正確的標籤匹配
# 詳情: help(plt.legend)

# 注意: plt.xlabal() -> ax.set_xlabel(), plt.xlim() -> ax.set_xlim(), plt.title() -> ax.set_title()
# 上面這是 plt 轉換成 ax 函式一些比較不一樣的部分(x, y同理)
# 通常會直接使用 ax.set() 直接設定所有的參數
# ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim = (0, 10), ylim = (-2, 2), xlabel = 'x', ylabel = 'sin(x)', title = 'A Simple Plot')
fig.savefig('./Matplotlib_Module/lineplot.png')

plt.show()