import numpy as np
import matplotlib as mpt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# SGD 圖
def f(x, y):
    return 0.05 * np.square(x) + np.square(y)

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.contour3D(X, Y, Z, 100, cmap = 'viridis')
plt.show()