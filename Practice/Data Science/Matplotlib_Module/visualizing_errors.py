import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 基本的誤差圖
plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 50)
# dy = 0.8
# y = np.sin(x) + dy * np.random.randn(50)
# plt.errorbar(x, y, yerr = dy, fmt = '.r') 
# yerr: y軸的誤差值, fmt: format string(輸出圖形的樣式)

# 客製化的誤差圖(較美觀)
# plt.errorbar(x, y, yerr = dy, fmt = 'o', color = 'black', ecolor = 'lightgray', elinewidth = 3, capsize = 0)
# 詳情可以查找 help(plt.errorbar)

# 連續型的誤差
# plt.plot() 和 plt.fill_between() 以產生有用的結果
# 在此提前使用 高斯過程遞歸(GPR) (使用Scikit-Learn API)
# GPR: 使用非常有彈性的無母數函數到具有不確定值的連續量測上

# from sklearn.gaussian_process import GaussianProcess # 書上的版本為 0.16
# 定義一個model 並畫出一些資料
# model = lambda x: x * np.sin(x)
# xdata = np.array([1, 3, 5, 6, 8])
# ydata = model(xdata)

# 計算 Gaussian process fit (高斯過程擬和)
# gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1, random_start=100)
# gp.fit(xdata[:, np.newaxis], ydata)
# xfit = np.linspace(0, 10, 1000)
# yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE = True)
# dyfit = 2 * np.sqrt(MSE) # 2 * sigma ~ 95% 信賴區間

# 視覺化畫出結果
# plt.plot(xdata, ydata, 'or')
# plt.plot(xfit, yfit, '-', color = 'gray')
# plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color = 'gray', alpha = 0.2)
# plt.xlim(0, 10)

# Review: 
# model = lambda x: x * np.sin(x) 等同於
# def model(x):
#     return x * np.sin(x)
# xdata[:, np.newaxis]: 橫軸和縱軸交換, (Ex: 1x5 -> 5x1)

plt.show()

# 安裝0.16.1 的 sklearn套件
# 等要使用機器學習的資料時, 使用python3.6.8 安裝舊版本的套件
# 或者 直接用 python3.7.0, 學新版本的套件

# 看後面書上的版本決定