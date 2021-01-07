import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')
# 自訂圖表的圖例
# 使用 plt.legend() 來建立
x = np.linspace(0, 10, 1000)
# fig, ax = plt.subplots() # 繪製子圖
# ax.plot(x, np.sin(x), '-b', label = 'Sine')
# ax.plot(x, np.cos(x), '--r', label = 'Cosine')
# ax.axis('equal')
# ax.legend() # 預設圖例在右上角, 且 frameon = True
# ax.legend(loc = 'upper left', frameon = False) # frameon = False 可以讓圖例不會有資料框
# ax.legend(loc = 'lower center', frameon = False, ncol = 2) # ncol: 顯示n欄的圖例
# 若這裡 ncol = 1, sine, cosine 會並排

# 可以使用比較不一樣的圖形, 加上陰影, 改變透明度等
# ax.legend(fancybox = True, framealpha = 1, shadow = True, borderpad = 1) # fancybox: 圓角矩形
# 詳請可以找 help(plt.legend)

# 選取圖例所要使用的元素
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
# lines = plt.plot(x, y)
# # print(lines)
# plt.legend(lines[:2], ['first', 'second'])

# 實務上會使用: (這樣可以讓人比較清楚了解, 較直觀)
# plt.plot(x, y[:, 0], label='first')
# plt.plot(x, y[:, 1], label='second')
# plt.plot(x, y[:, 2:])
# plt.legend(framealpha = 1, frameon = True)
# 也可以達到一樣的效果
# legend 預設會忽略沒有加上標籤的元素

# 在圖例中的資料點大小
# 利用資料點的大小來標記資料的某些特性
import pandas as pd
# cities = pd.read_csv('.\\Matplotlib_Module\\california_cities.csv')

# 取出需要的資料
# lat, lon = cities['latd'], cities['longd']
# population, area = cities['population_total'], cities['area_total_km2']

# 使用大小和顏色但是沒有標籤, 畫上這些資料點
# plt.scatter(lon, lat, label = None, c = np.log10(population), cmap = 'viridis', s = area, 
#             linewidths = 0, alpha = 0.5)
# plt.axis('equal')
# plt.xlabel('longitude') # longitude 經度
# plt.ylabel('latitude') # latitude 緯度
# plt.colorbar(label = 'log$_{10}$(population)') # 讓 10 變成小的
# plt.clim(3, 7) # 設置當前圖像的顏色取值範圍

# 以下建立一個圖例
# 畫上一個想要大小以及標籤的空串列
# for area in [100, 300, 500]:
#     plt.scatter([], [], c = 'k', alpha = 0.3, s = area, label = str(area) + ' km$^2$') # 顯示 km平方
# plt.legend(scatterpoints = 1, frameon = False, labelspacing = 1, title = 'City Area')
# plt.title('California Cities: Area and Population')

# 多重圖例
# 在 Matplotlib 要建立多重圖例 只能使用 ax.add_artist()方法, 否則以往plt.legend的方式會把之前的覆蓋掉
# fig, ax = plt.subplots()
# lines = []
# styles = ['-', '--', '-.', ':']
# x = np.linspace(0, 10, 1000)

# for i in range(4):
#     lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color = 'black')
# ax.axis('equal')

# 指定第一個圖例的線條和標籤
# ax.legend(lines[:2], ['lineA', 'lineB'], loc = 'upper right', frameon = False)

# 建立第二個圖例
# from matplotlib.legend import Legend
# leg = Legend(ax, lines[2:], ['lineC', 'lineD'], loc = 'lower right', frameon = False)
# ax.add_artist(leg)

plt.show()