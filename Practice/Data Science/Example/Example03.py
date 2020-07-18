# 選取隨機點
# Fancy 索引常用的地方是從一個矩陣中選取一個子集合
# 假如, 有一個 NxD 的矩陣用來表示D維度上的N個點, 如以下二維常態分佈中取出的點

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

rand = np.random.RandomState(42)
mean = [0, 0]
cov = [[1, 2], [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)

# plt.scatter(X[:, 0], X[:, 1])
# plt.show()

# 使用 Fancy 索引來選取 20個隨機點. 
indices = np.random.choice(X.shape[0], 20, replace = False)
# replace = False <- 表示不重複
selection = X[indices]
plt.scatter(X[:, 0], X[:, 1], color = 'Red', alpha = 0.3)
plt.scatter(selection[:, 0], selection[:, 1], marker = 'o', facecolor = 'None', 
            edgecolor = 'black', s = 200)
plt.xlim(-4, 3)
plt.ylim(-10, 8)
plt.axes().xaxis.set_major_locator(plt.MaxNLocator(8))
plt.show()
