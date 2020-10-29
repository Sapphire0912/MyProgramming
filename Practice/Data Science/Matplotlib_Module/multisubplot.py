import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 多重子圖表
# 有時並排的資料會很有幫助
plt.style.use('seaborn-white')

# plt.axes() 手動建立子圖表
# plt.axes() 可以傳入一個額外4個數字的list: 
# [bottom, left, width, height] range: 0 to 1(左下角到右上角)
# ax1 = plt.axes() # 正常的大小
# ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])  # 以原圖為比例: 65%的寬和高, 圖表為20%的寬和高

# 建立垂直的堆疊axes 使用fig.add_axes()
# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels = [], ylim = (-1.2, 1.2))
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim = (-1.2, 1.2))

# x = np.linspace(0, 10)
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))

# plt.subplot() 子圖表的簡單網格
# 子圖表對齊欄和列
# plt.subplot(列, 欄(行), 位置) 
# for i in range(1, 7):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)), fontsize = 18, ha = 'center')
# plt.text(x, y, string, fontsize, horizontalalignment = 'center', 
#          verticalalignment = 'center', transform)

# fig.subplots_adjust() 調整子圖表中間的間隙 
# Parameters: hspace間隔為子圖高的百分比, wspace間隔為子圖寬的百分比 
# fig = plt.figure()
# fig.subplots_adjust(hspace = 0.4, wspace = 0.4) 
# for i in range(1, 7):
#     ax = fig.add_subplot(2, 3, i)
#     ax.text(0.5, 0.5, str((2, 3, i)), fontsize = 18, ha = 'center')

# plt.subplots(): 一次準備好整個網格
# 此函式可以用一行就建立完整的子圖表網格, 傳回值會放在一個 Numpy 的陣列中
# Parameters: sharex, sharey: 列數和行數
# fig, ax = plt.subplots(2, 3, sharex = 'col', sharey = 'row')

# axes 是在一個二維陣列中, 使用[col, row]進行索引
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i, j)), fontsize = 20, ha = 'center')

# plt.GridSpec() 更多複雜的排列
# plt.GridSpec() 是擴充多列和多欄的最佳工具
# 一個具有指定寬高間隔的網格規格
# grid = plt.GridSpec(2, 3, wspace = 0.4, hspace = 0.3)

# Python 切片語法來指定子圖表的位置和大小
# plt.subplot(grid[0, 0])
# plt.subplot(grid[0, 1:])
# plt.subplot(grid[1, :2])
# plt.subplot(grid[1, 2])

# 建立常態分析
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T  # 高斯分布

# 使用格子規格來設置axes
fig = plt.figure(figsize = (6, 6))
grid = plt.GridSpec(4, 4, hspace = 0.2, wspace = 0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels = [], sharey = main_ax) 
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels = [], sharex = main_ax)
# xticklabels: x刻度標籤
# yticklabels: y刻度標籤

# 在主要的axes 加上散佈點
main_ax.plot(x, y, 'ok', markersize = 3, alpha = 0.2)
# o 圓點, k: black

# 在附加的axes 加上直方圖
x_hist.hist(x, 40, histtype = 'stepfilled', orientation = 'vertical', color = 'black')
x_hist.invert_yaxis() # y軸反轉 之後忘記的話可以註解掉

y_hist.hist(y, 40, histtype = 'stepfilled', orientation = 'horizontal', color = 'gray')
y_hist.invert_xaxis() # x軸反轉 之後忘記的話可以註解掉

plt.show()