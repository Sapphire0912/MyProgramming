import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 三維繪圖法
# 使用 mplot3d 模組 建立一個三維空間的座標圖
from mpl_toolkits import mplot3d 
# fig = plt.figure()
# ax = plt.axes(projection = '3d')

# 三維的點和線
# 三維線條所需要的資料
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'blue')

# 三維散佈圖點所需要的資料
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.random(100)
# ydata = np.cos(zdata) + 0.1 * np.random.random(100)
# ax.scatter3D(xdata, ydata, zdata, c = zdata, cmap = 'winter')

# 三維的等高線圖
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y= np.meshgrid(x, y)
# Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
# ax.contour3D(X, Y, Z, 50, cmap = 'binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# 可以使用 view_init方法設定高度和方位角(簡稱視角)
# ax.view_init(60, 35)

# 線框圖和表面圖
# ax.plot_wireframe(X, Y, Z, color = 'purple')
# ax.set_title('wireframe')

# ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')
# ax.set_title('surface')

# 平面圖的資料格式一定要是二維但不一定要是直線
# r = np.linspace(0, 6, 20)
# theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
# r, theta = np.meshgrid(r, theta)

# X = r * np.sin(theta)
# Y = r * np.cos(theta)
# Z = f(X, Y)

# ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'viridis', edgecolor = 'none')

# 表面三角剖分
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)

ax.scatter(x, y, z, c = z, cmap = 'viridis', linewidth = 0.5)
ax.plot_trisurf(x, y, z, cmap = 'viridis', edgecolor = 'none')

plt.show()