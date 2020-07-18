import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

plt.style.use('seaborn-whitegrid')
fig = plt.figure()

# 繪製散佈圖
x = np.linspace(0, 10, 30)
y = np.sin(x)
# plt.plot(x, y, 'o', color = 'black')
# 詳情 help(plt.plot) 裡面 **Markets** 有全部可以繪製任何類型的圖, 分別對應的字串

rng = np.random.RandomState(0)
# list_marker = ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']
# for marker in list_marker:
#     plt.plot(rng.rand(5), rng.rand(5), marker, label = "marker = '{0}'".format(marker))
# plt.legend(numpoints = 1)
# plt.xlim(0, 1.8)
# Review: 
# rng.rand(n): 產生n個[0,1)之間的數
# fig.savefig('./Matplotlib_Module/markers.png')

# plt.plot(x, y, '-ok') # line(-), circle marker(o), black(k)

# plt.plot 額外的參數
# plt.plot(x, y, '-p', color = 'gray', markersize = 15, linewidth = 4, 
#          markerfacecolor = 'white', markeredgecolor = 'red', markeredgewidth = 2)
# -p 直線+五角形

# 使用plt.scatter()繪製散佈圖
# plt.scatter(x, y, marker = 'o')
# plt.scatter() 和 plt.plot() 不同於建立散佈圖時, 它每一個點的屬性都可以被個別控制

# 使用alpha參數 來調整透明度
# a = rng.randn(100)
# b = rng.randn(100)
# colors = rng.randn(100)
# sizes = 1000 * rng.randn(100)
# plt.scatter(a, b, c = colors, s = sizes, alpha = 0.3, cmap = 'viridis')
# plt.colorbar()  # 顯示顏色刻度
# Review: rng.randn() 標準常態分布亂數

# 這裡使用來自於 Scikit-Learn 的 Iris 資料
iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha = 0.2, s = 100 * features[3], c = iris.target, cmap = 'viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# plot 和 scatter 的比較: 關於效能要注意的地方
# 小資料的情況影響不大, 但資料量非常龐大時, plot 比 scatter 還要有效率
# 因為 scatter 可以去繪製每一個點的大小和顏色, 相對的繪製時要多額外的工作去個別建立每個點
# 則 plot 的點都是複製出來的, 對於整個資料集來說外觀屬性只需要做一次就好
# 所以 plt.plot 要比 plt.scatter 優先被採用
plt.show()