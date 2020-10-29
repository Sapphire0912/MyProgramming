import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# 自訂刻度(格式器, 定位器)
# 主要和次要的刻度
# ax = plt.axes(xscale = 'log', yscale = 'log')
# x, y軸的刻度 以log來表示

# 透過設定每一個軸的formatter, locator 物件 來自訂刻度的特性
# print(ax.xaxis.get_major_locator())
# print(ax.yaxis.get_minor_locator())
# locator 用來指定位置(讓對數圖有意義)
# print(ax.xaxis.get_major_formatter())
# print(ax.xaxis.get_minor_formatter())
# formatter NullFormatter 格式化標籤(可以將標籤隱藏)

# 隱藏刻度或標籤
# ax.plot(np.random.rand(50))
# ax.yaxis.set_major_locator(plt.NullLocator())
# ax.xaxis.set_major_formatter(plt.NullFormatter())
# 移除x, y軸的標籤 但是保留了刻度和格線

# 顯示影像格線時就可以這麼用
# 在監督式學習時經常會使用的例子
# fig, ax = plt.subplots(5, 5, figsize = (5, 5))
# fig.subplots_adjust(hspace = 0, wspace = 0)

# 從 scikit-learn 取得臉的資料
# from sklearn.datasets import fetch_olivetti_faces
# faces = fetch_olivetti_faces().images

# for i in range(5):
#     for j in range(5):
#         ax[i, j].xaxis.set_major_locator(plt.NullLocator())
#         ax[i, j].yaxis.set_major_locator(plt.NullLocator())
#         ax[i, j].imshow(faces[10 * i + j], cmap = "bone")
# 因為每一個影像都有自己的axes, 因此刻度並無法給視覺圖形有意義的資訊

# 減少或增加刻度的數目(這裡可以看課本例子, 應該是後來的matplotlib版本有優化這裡)
# fig, ax = plt.subplots(4, 4, sharex = True, sharey = True)
# sharex, sharey參數: bool, (default:False). True則將統一所有子圖的x, y軸刻度
# 顯示的結果會導致x軸的標籤太接近了, 圖多時不好辨認
# 因此使用 plt.MaxNLocator()來修正問題

# 對每一個軸, 設定x, y刻度
# for axi in ax.flat:
#     axi.xaxis.set_major_locator(plt.MaxNLocator(2))
#     axi.yaxis.set_major_locator(plt.MaxNLocator(2))
# 若想要控制刻度間隔位置, 可以使用plt.MultipleLocator()

# 花式刻度格式
# 畫一個sin, cos的圖形
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw = 3, label = 'Sine')
ax.plot(x, np.cos(x), lw = 3, label = 'Cosine')

# 設定格線, 圖例, 範圍
ax.legend(frameon = False) # 調整圖例
ax.grid(True) # 是否顯示網格線
ax.axis('equal')
ax.set_xlim(0, 3 * np.pi)
# 使用整數刻度的預設圖表

# 三角函數把x軸用pi為單位顯示會比較自然
# 使用 plt.MultipleLocator()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2)) 
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
# 主要在 pi/2 位置顯示刻度, 次要在 pi/4 位置顯示刻度
# Q. 有無 line 71 結果都相同

# 上面的刻度沒辦法立刻想到是 pi/2, 為了修正這點, 可以更改刻度格式
# 使用plt.FuncFormatter()
def format_func(value, tick_number):
    # 找出多個 pi/2 的數目
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

# 格式器和定位器的類別
# NullLocator 沒有刻度
# FixedLocator 刻度位置固定的
# IndexLocator 索引圖表的定位器(Ex. x = range(len(y)))
# LinearLocator 從min to max平均分配刻度間隔
# LogLocator 從 min to 做對數刻度
# MultipltLocator 同時指定多個刻度和範圍
# MaxNLocator 找出一個到最大數刻度的最佳位置
# AutoLocator (預設值) 使用簡單預設值的 MaxNLocator
# AutoMinorLocator 次要刻度的定位器

# NullFormatter 在刻度上不要設定標籤
# IndexFormatter 用一個標籤串列來設定字串
# FixedFormatter 手動字串設定標籤
# FuncFormatter 使用者自訂函式設定標籤
# FormatStrFormatter 為每一個值使用一個格式字串
# ScalarFormatter (預設)使用純量做格式器
# LogFormatter 座標格式以對數表示

plt.show()