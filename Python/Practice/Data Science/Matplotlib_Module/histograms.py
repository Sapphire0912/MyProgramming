import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 二維直方圖和裝箱法

plt.style.use('seaborn-whitegrid')
# 繪製直方圖(histograms)
# 使用 plt.hist()
data = np.random.randn(1000)
# plt.hist(data)

# plt.hist() 參數
# plt.hist(data, bins = 30, density = True, alpha = 0.5, histtype = 'stepfilled', 
#          color = 'steelblue', edgecolor = 'none')

# bins: 如果是一個整數, 設定整筆資料要由 bins 值來等值分配寬度(換句話說, 橫軸切成bins等分)
# histtype: 產生直方圖的類型 ,stepfilled產生實心填滿的直方圖
# 詳情查找 help(plt.hist)

# 直方圖疊加在一起
# x1 = np.random.normal(0, 0.8, 1000)
# x2 = np.random.normal(2, 1, 1000)
# x3 = np.random.normal(3, 2, 1000)

# kwargs = dict(histtype = 'stepfilled', alpha = 0.3, density = True, bins = 50)
# plt.hist(x1, **kwargs)
# plt.hist(x2, **kwargs)
# plt.hist(x3, **kwargs)
# **kwargs: 關鍵字傳參

# 補充: 如果單純只想計算每個資料的數量, 而不要以圖的方式顯示出來
# 使用 np.histogram() 可以做到
counts, bin_edges = np.histogram(data, bins = 7) 
# print(counts, bin_edges)
# counts 每一筆資料的高度, bin_edges 每一筆資料寬度的值

# 二維的直方圖和裝箱法
# 就像是在建立直方圖時, 把一個維度中的數值線變成資料範圍的箱子
# 可以建立一個直方圖, 把二維資料的點讓它們分到二維的箱子中
# 從定義資料開始, 多變量高斯分布(常態分布)取出x, y陣列
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

# plt.hist2d(): 二維直方圖
# plt.hist2d(x, y, bins = 30, cmap = 'Blues')
# cb = plt.colorbar()
# cb.set_label('counts in bin')  # 可以設定顏色刻度的標籤
# 詳情可以查找 help(plt.hist2d)
# 函式裡總有一些功能相仿的函式: plt.hist -> np.histogram, plt.hist2d -> np.histogram2d

counts, xedges, yedges = np.histogram2d(x, y, bins = 30)
# print(counts, xedges, yedges)

# plt.hexbin() : 六角形的裝箱
# plt.hexbin(x, y, gridsize = 30, cmap = 'Purples')
# cb = plt.colorbar()
# cb.set_label('counts in bin')

# 核密度估計(Kernel Density Estimation)
# 在後面會詳細介紹, 這裡簡單敘述
# KDE被當作是一個用來 "抹掉" 在空間中的點, 然後加上結果以取得一個平滑函數
# KDE資料可以在 scipy.stats 套件中找到
from scipy.stats import gaussian_kde

# 放入一個陣列的大小 [Ndim, Nsamples] ([N個維度, N個樣本])
data = np.vstack([x, y]) # np.vstack(), (Ex. 將原本3x8的陣列轉成8x3)
kde = gaussian_kde(data)

# 在一個方形的格子上進行估算
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid) # 在給予的向量變成向量矩陣(numpy broadcasting)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# 把結果畫成一個影像
plt.imshow(Z.reshape(Xgrid.shape), origin = 'lower', aspect = 'auto', 
           extent = [-3.5, 3.5, -6, 6], cmap = 'Blues')
plt.colorbar(label = "density")

# np.meshgrid(): 例子
# nx, ny = 3, 2  # 定義維度
# x = np.linspace(0, 1, nx) # x = [0., 0.5, 1.] 樣本資料
# y = np.linspace(0, 1, ny) # y = [0., 1.] 樣本資料
# xv, yv = np.meshgrid(x, y)
# print("xv: ")
# print(xv)
# print("yv: ")
# print(yv)
# xv:
# [[0.  0.5 1. ] x的資料 * y的維度
#  [0.  0.5 1. ]]
# yv:
# [[0. 0. 0.] y的資料 * x的維度
#  [1. 1. 1.]]

plt.show()