# 使用GMM來產生新資料

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 使用標準的數字元素材中, 產生新的手寫數字元
from sklearn.datasets import load_digits
digits = load_digits()
# print(digits.data.shape) (1797, 64)

def plot_digits(data):
    # 保留前100個數字元的資料
    fig, ax = plt.subplots(10, 10, figsize = (8, 8), subplot_kw = dict(xticks = [], yticks = []))
    fig.subplots_adjust(hspace = 0.5, wspace = 0.5)
    for i, axi in enumerate(ax.flat):
        im = axi.imshow(data[i].reshape(8, 8), cmap = 'binary')
        im.set_clim(0, 16)
    plt.show()

# plot_digits(digits.data)

# 在高維度的空間, GMM不易收斂. 因此先把資料使用PCA進行降維(要求在投影的資料中保留99%的變異量)
from sklearn.decomposition import PCA
pca = PCA(0.99, whiten = True)
data = pca.fit_transform(digits.data)
# print(data.shape) # (1797, 41)

# 使用AIC去取得一個GMM component 數目的估計
from sklearn.mixture import GaussianMixture as GMM
# n_components = np.arange(50, 210, 10)
# models = [GMM(n, covariance_type = 'full', random_state = 0) for n in n_components]
# aics = [model.fit(data).aic(data) for model in models]
# plt.plot(n_components, aics) # 150 有最小化 AIC
# plt.show()
# best = n_components[aics.index(min(aics))]
# print(best) # 150

gmm = GMM(150, covariance_type = 'full', random_state = 0)
gmm.fit(data)
# print(gmm.converged_) # 確認是否收斂, 傳回布林值. # True

data_new = gmm.sample(100)
# print(data_new[0].shape) # (100, 41)
digits_new = pca.inverse_transform(data_new[0])
plot_digits(digits_new)