import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# plt.style.use('classic')
# 客製化 Matplotlib 系統配置和樣式表
# 手動自訂圖表
# 先繪製一個十分單調的直方圖
# x = np.random.randn(1000)
# plt.hist(x)

# 透過手動調整, 會變得比較美觀
# 使用灰色背景
# ax = plt.axes(facecolor = '#E6E6E6') # gray
# ax.set_axisbelow(True)
# line 15: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html

# 畫上白色實心格線
# plt.grid(color = 'white', linestyle = '-') # while, solid

# 隱藏軸的突起
# for spine in ax.spines.values():
#     spine.set_visible(False)

# 隱藏上方和右邊的刻度(只保留底部和左邊)
# ax.xaxis.tick_bottom()
# ax.yaxis.tick_left()

# 讓刻度和標籤淡一些
# ax.tick_params(colors = 'gray', direction = 'out')
# for tick in ax.get_xticklabels():
#     tick.set_color('gray')
# for tick in ax.get_yticklabels():
#     tick.set_color('gray')

# 控制直方圖的填滿和邊線顏色
# ax.hist(x, edgecolor = '#E6E6E6', color = '#EE6666')

# 但是每次都要從頭開始畫都要重新調整非常麻煩, 所以更改內部的預設值就可以只改一次並套用到所有的圖表
# 變更預設值: rcParams
# 每次 Matplotlib 載入時它都會定義一個執行配置(runtime configuration),
# 包含每一個建立圖表元素的預設樣式, 可以使用plt.rc便利程序來隨時調整配置
Python_default = plt.rcParams.copy()
from matplotlib import cycler
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor = '#E6E6E6', edgecolor = 'none', 
        axisbelow = True, grid = True, prop_cycle = colors)
plt.rc('grid', color = 'w', linestyle = 'solid')
plt.rc('xtick', direction = 'out', color = 'gray')
plt.rc('ytick', direction = 'out', color = 'gray')
plt.rc('patch', edgecolor = '#E6E6E6')
plt.rc('lines', linewidth = 2)
# plt.hist(x) # 可以得到和上面一樣的結果

# 使用rc參數來繪製簡單的折線圖
# for i in range(4):
#     plt.plot(np.random.rand(10))

# 樣式表
# 可用的樣式表 plt.style.available
# 使用 plt.style.use('stylename')
# 所有可用的樣式表
# bmh
# classic
# dark_background
# fast
# fivethirtyeight
# ggplot
# grayscale
# seaborn-bright
# seaborn-colorblind
# seaborn-dark-palette
# seaborn-dark
# seaborn-darkgrid
# seaborn-deep
# seaborn-muted
# seaborn-notebook
# seaborn-paper
# seaborn-pastel
# seaborn-poster
# seaborn-talk
# seaborn-ticks
# seaborn-white
# seaborn-whitegrid
# seaborn
# Solarize_Light2
# tableau-colorblind10
# _classic_test

# 但要注意的, 若一開始設定樣式的話, 會直接影響所有的圖表
# 若想要單獨的設定其中一個, 使用以下的代碼

# 重置 rcParams
# plt.rcParams.update(Python_default)

def hist_and_lines():
    plt.style.use('dark_background')
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize = (11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc = 'lower left')

hist_and_lines()
plt.show()