#coding=utf8
# from sklearn.datasets import load_digits
# X_digits, y_digits = load_digits(return_X_y = True)

# from sklearn.model_selection import train_test_split as tts
# X_train, X_test, y_train, y_test = tts(X_digits, y_digits)

# 底下執行結果每次執行都會不同
# from sklearn.linear_model import LogisticRegression as LogR
# model = LogR()
# model.fit(X_train, y_train)
# test_score = model.score(X_test, y_test)
# print(test_score) # 會有 Increase the number of iterations(max_iter) or scale the data 的問題

# from sklearn.cluster import KMeans
# from sklearn.pipeline import Pipeline
# pipe = Pipeline([
#     ("kmeans", KMeans(n_clusters = 50)),
#     ("LogR", LogR())
# ])
# pipe.fit(X_train, y_train)
# pipe_score = pipe.score(X_test, y_test)
# print(pipe_score) 

# 使用網格搜尋找出最佳的 n_clusters
# from sklearn.model_selection import GridSearchCV
# params = dict(kmeans__n_clusters = range(2, 100))
# grid = GridSearchCV(pipe, param_grid = params, cv = 3, verbose = 2)
# grid.fit(X_train, y_train)
# print(grid.best_params_)  # {'kmeans__n_clusters': 50}

# 接著做 DBSCAN (記得把上面的程式碼註解 不然會一直報 ConvergenceWarning)
# from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, y = make_moons(n_samples = 1000, noise = 0.5)
# print(y)

# dbscan = DBSCAN(eps = 0.05, min_samples = 5)
# dbscan.fit(X)

# import matplotlib as mpt
# import matplotlib.pyplot as plt

# plt.scatter(X[:, 0], X[:, 1], c = y, cmap = 'Blues', alpha = 0.4)
# plt.show()


# 高斯混合
from sklearn.mixture import GaussianMixture as gmm
gm = gmm(n_components = 3, n_init = 10)
gm.fit(X)
# print(gm.weights_) # [0.27565134 0.46979456 0.2545541 ]
# print(gm.means_) # [[-0.48666994  0.24902082]
                 #  [ 1.2365377  -0.13938913]
                 #  [ 0.24214324  0.98431594]]
# print(gm.covariances_) 
# [[[ 0.35313405 -0.06505064]
#   [-0.06505064  0.27590391]]

#  [[ 0.46521907  0.08082033]
#   [ 0.08082033  0.34744874]]

#  [[ 0.40641319 -0.07908257]
#   [-0.07908257  0.20770555]]]

# print(gm.converged_) # True
# print(gm.n_iter_) # 5

# print(gm.predict(X)) # 硬分群
# print(gm.predict_proba(X)) # 軟分群

# 高斯混合模型是生成模型, 也就是可以從裡面抽樣新實例
# import numpy as np
# X_new, y_new = gm.sample(6)
# densities = gm.score_samples(X) # 估算模型在任何位置的密度, 此方法可以估計它收到的實例位置的機率密度函數(PDF)
# density_threshold = np.percentile(densities, 4)
# anomalies = X[densities < density_threshold]

# gm.bic(X)
# gm.aic(X)


# 貝氏高斯混合模型
from sklearn.mixture import BayesianGaussianMixture as BGM
import numpy as np
bgm = BGM(n_components = 10, n_init = 10)
bgm.fit(X)
print(np.round(bgm.weights_, 2))