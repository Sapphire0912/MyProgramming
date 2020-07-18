import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')
# 自訂色彩條
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])
# plt.imshow(I)

# plt.imshow() cmap 參數: 
# plt.imshow(I, cmap = 'gray')
# 詳細顏色可以使用 plt.cm.<TAB> 查詢

# 色彩對應表的選擇(有三種)
# Sequential : 由連續的一系列色彩所組成的(Ex. binary, viridis)
# Divergent : 通常包含兩個獨立的顏色, 然後從平均值中顯示正, 負偏差(Ex. RdBu, PuOr)
# Qualitative : 沒有特別順序的色彩所組成的(Ex. rainbow, jet)
from matplotlib.colors import LinearSegmentedColormap

def grayscale_cmap(cmap):
    '''給一個色彩對應表, 然後傳回一個灰階版本'''
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # 轉換 RGBA 成為感知的灰階亮度
    # Reference: http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)

def view_colormap(cmap):
    '''畫出和上面的函式一樣的灰階版本'''
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize = (6, 2), subplot_kw = dict(xticks = [], yticks = []))
    ax[0].imshow([colors], extent = [0, 10, 0, 1])
    ax[1].imshow([grayscale], extent = [0, 10, 0, 1])
# view_colormap('jet') # jet對應表不均勻的亮度刻度
# view_colormap('viridis') # viridis 色彩對應表和均勻亮度比例
# view_colormap('cubehelix') # 彩虹的組合, 適合用cubehelix組合

# 平均顯示的正負偏差(Ex. RdBu)
# view_colormap('RdBu') # RdBu 色彩對應表和亮度
# 關於顏色的研究可以參考 Seaborn程式庫的工具和說明

# 色彩的限制和延伸
# Matplotlib 允許色彩條自製化, 色彩調本身由一個plt.axes執行實例
# 假設要顯示一個雜訊有關的影像:
# 製造一個影像中 1% 的雜訊
# speckles = (np.random.random(I.shape) < 0.01)
# I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))
# np.count_nonzero(a, axis = None)
# Counts the number of non-zero values in the array a.

# plt.figure(figsize = (10, 3.5))
# figure(figsize = (float, float)) width, height in inches(defaults: (6.4, 4.8))

# plt.subplot(1, 2, 1) # 創建子圖, 1 row, 2 cols, 1 index(1x2的panel裡的第1個位置)
# plt.imshow(I, cmap = 'Purples')
# plt.colorbar()

# plt.subplot(1, 2, 2) # 第2位置
# plt.imshow(I, cmap = 'Oranges')
# plt.colorbar(extend = 'both')
# plt.clim(-1, 1) # 將色彩刻度限制在1~-1的範圍

# 左邊的 panel 預設色彩限制反映了雜訊點, 雜訊的範圍會把要得資料清除掉
# 右邊的 panel 手動設定色彩的限制, 加上延伸指示超過和低於限制的值(line 72), 在視覺化會更加有用

# 離散的色彩條
# 色彩對應表預設是連續的, 若想要較離散的值, 可以使用plt.cm.get_cmap()
# 傳入一個合適的色彩對應表名稱以及要呈現之箱子裡的數目(n等分)
plt.imshow(I, cmap = plt.cm.get_cmap('Blues', 6)) # 切成6等分
plt.colorbar()
plt.clim(-1, 1)

plt.show()