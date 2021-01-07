import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 文字和註解(先查看Example11)
# 轉換以及文字位置
# 可以透過transforms 來操作

# 這裡有3種預先定義好的轉換
# ax.transData 和資料座標相關的轉換
# ax.trnasAxes 和 axes(使用axes尺寸的單位)相關轉換
# fig.transFigure 和 figure(使用figure尺寸的單位)相關轉換 

# 不同位置上使用轉換文字的例子
# fig, ax = plt.subplots(facecolor = 'lightgray')
# ax.axis([0, 10, 0, 10])

# 預設的轉換是 ax.transData
# ax.text(1, 5, ".Data: (1, 5)", transform = ax.transData)
# ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform = ax.transAxes)
# ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform = fig.transFigure)

# axes 指的是白色畫布, figure 指的是灰色畫布
# line 20, 21轉換依據各畫布的比例來做轉換

# 若此時改變了座標範圍
# ax.set_xlim(0, 2)
# ax.set_ylim(-6, 6)
# 則只有使用 ax.transData 轉換方式的資料被改變位置

# 箭頭和註解
# 使用plt.annotate() 來建立文字和箭頭
fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local maxinum', xy = (6.28, 1), xytext = (10, 4), 
            arrowprops = dict(arrowstyle = "->", 
            connectionstyle = "angle3, angleA = 0, angleB = -90"))

ax.annotate('local minimum', xy = (5 * np.pi, -1), xytext = (2, -6),
            arrowprops = dict(facecolor = 'black', shrink = 0.05))
# 詳情請找help(ax.annotate)
# Reference: http://matplotlib.org/examples/pylab_examples/annotation_demo2.html
plt.show()
