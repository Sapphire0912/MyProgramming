# 訓練模型
# (這個單元數學理論偏重)
# 通過 閉式方程 直接計算出最適合訓練集的模型參數(使訓練集上的成本函數最小化)
# 使用迭代優化方法(梯度下降), 逐漸調整模型參數直到訓練集上的成本函數調到最低
# 關於梯度下降有: 批量梯度下降, 小批量梯度下降, 隨機梯度下降(在神經網路會頻繁使用到這些)

# 線性回歸
# 公式: y = {sigma(i from 1 to n)[ theta_i * X_i ]} + theta_0
# y 代表預測值, n 是特徵的數量, X_i 為第 i 個特徵值, theta_i 為第 i 個模型參數(包含偏置項 i = 0 和 特徵權重 i > 0 )
# 在訓練回歸模型時, 需要找到最小化 RMSE 的 theta 值
# (實務上, MSE 最小化比 RMSE 最小化容易, 因為函數最小值其平方根也最小)

# 標準方程 (線性代數的內容)
# 為了得到使成本函數最小的 theta 值的一種閉式解法
# theta = (X.T * X)^-1 * X.T * y <- 這裡的 * 代表 dot
# theta 是使成本函數最小的值, y是 y 從 1 到 m 的目標值向量
# 以下生成一些線性數據來測試公式
import numpy as np

# X = 2 * np.random.rand(100, 1) # x.shape = (100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)
# 接著使用 標準方程來計算 theta, 且使用 numpy 的線性代數模塊(np.linalg)
# X_b = np.c_[np.ones((100, 1)), X]
# theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y) # inv 求逆矩陣
# print("theta_best: \n", theta_best) # [[4.20380823], [2.67835011]] <- 每次執行結果都會不一樣
# 上面的結果是根據函數 y = 4 + 3x + noise
# 也就是我們預期得到的結果是 theta_0 = 4, theta_1 = 3, 實際上是 theta_0 = 4.203, theta_1 = 2.678
# 有雜訊存在就不可能還原成原本的函數

# 現在可以用 theta_best 做出預測
# X_new = np.array([[0], [2]])
# X_new_b = np.c_[np.ones((2, 1)), X_new]
# y_predict = X_new_b.dot(theta_best)
# print("y_predict: \n", y_predict)

# 繪製模型的預測結果
import matplotlib as mpl
import matplotlib.pyplot as plt

# plt.plot(X_new, y_predict, "r-")
# plt.plot(X, y, "b.")
# plt.axis([0, 2, 0, 15])
# plt.show()

# 上面的代碼等同於以下的 Scikit-Learn LinearRegression Code
from sklearn.linear_model import LinearRegression as LR
# lin_reg = LR()
# lin_reg.fit(X, y)
# print("Intercept: %f, Coef: %f" % (lin_reg.intercept_, lin_reg.coef_))
# print("sklearn_LR model predict: \n", lin_reg.predict(X_new))
# 會發現執行結果會一樣, 不論截距, 特徵權重(coef_ <- coefficient), 預測結果都相同

# 計算複雜度
# 標準方程求逆矩陣的計算複雜度通常為 O(n^2.4) ~ O(n^3) <- 若特徵數量(n)較大, 計算時極為緩慢
# 以下再看看幾個不同的線性回歸模型的訓練方法, 這些方法更適合特徵數或者訓練實例數量大到記憶體無法滿足要求的時候


# 梯度下降 (Gradient Descent)
# 梯度下降是一種非常通用的優化算法, 能夠大範圍找到問題的最佳解, 它的中心思想是迭代調整參數使成本函數最小化
# 梯度下降中一個重要的參數是每一步的步長
# 補充: 深度瞭解可以看課本或者搜尋 Lipschitz Continuous, 凸函數(次梯度法)
# 使用梯度下降時, 需要保證所有特徵值的大小比例都差不多(可以使用 sklearn StandardScaler), 否則收斂時間會很長
# 以下解釋三種梯度下降法(參考連結: https://www.itread01.com/content/1531293969.html)

# 批量梯度下降(Batch Gradient Descent, BGD)
# BGD 計算梯度下降時每一步都是基於完整的訓練集X(因此, 訓練集大很耗時)
# 對成本函數偏微分(∇ nabla梯度)
# 公式: ∇MSE(theta) = 2 / m * X.T * (X * theta - y) <- * 代表 dot
# 梯度下降步長公式: theta_next_step = theta - eta * ∇MSE(theta)
# 以下用程式碼來實現
# eta = 0.1 # <- 學習率 learning rate
# n_iterations = 1000 # 迭代次數
# m = 100 # 數據量

# theta = np.random.randn(2, 1) # 隨機初始化

# for iteration in range(n_iterations):
#     gradients = 2 / m * X_b.T.dot(X_b.dot(theta) - y)
#     theta = theta - eta * gradients

# print("Using BGD: \n", theta) # 和前面的 theta_best 比較 會發現結果相同
# 可以測試 在不同學習率的情況下 theta值和效率為多少

# 隨機梯度下降(Stochastic Gradient Descent, SGD)
# SGD 計算每一步是在訓練集中隨機選擇一個實例, 並且僅基於該單個實例來計算梯度(用來計算海量數據集, 但解通常不是最佳的)
# 有一種辦法叫做 模擬退火, 是逐步降低學習率, 開始的步長較大然後越來越小, 計算盡量靠近全局最小值
# 以下用程式碼實現
# n_epochs = 50
# t0, t1 = 5, 50 # 學習進度超參數 learning schedule hyperparameters

# def learning_schedule(t):
#     return t0 / (t + t1)

# theta = np.random.randn(2, 1) # 隨機初始化
# m = 100 # 迭代次數

# for epoch in range(n_epochs):
#     for i in range(m):
#         random_index = np.random.randint(m)
#         xi = X_b[random_index:random_index + 1]
#         yi = y[random_index:random_index + 1]
#         gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
#         eta = learning_schedule(epoch * m + i)
#         theta = theta - eta * gradients
# print("Using SGD: \n", theta) # 和前面的 theta_best 比較會發現結果上差一點點

# 在 sklearn 用 SGDRegressor
from sklearn.linear_model import SGDRegressor as sgdr
# sgd_reg = sgdr(n_iter_no_change = 50, penalty = None, eta0 = 0.1)
# sgd_reg.fit(X, y.ravel())
# print("sklearn_SGDRegreesor(intercept, coef): %f, %f" % (sgd_reg.intercept_, sgd_reg.coef_))

# 小批量梯度下降(Mini-Batch Gradient Descent, MBGD)
# MBGD 採取資料集的一部份使用隨機梯度下降算法, 但是容易卡在局部最小值上
# 主要優勢, 從矩陣運算的硬體優化中顯著的性能提升, 特別是需要用到圖形處理器時

# 目前為止的線性回歸算法(在當前目錄下的xlsx檔案)
# 訓練後的模型幾乎無差別: 所有算法最後出來的模型都非常相似, 並且都以完全相同方式做出預測


# 多項式回歸(Polynomial Regression)
# 直接看以下的例子(二次多項式為例)
m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)
# 顯然上面的資料無法用直線來擬合數據
# 使用 Scikit-Learn PolynomialFeatures 來對訓練數據進行轉換
# 將每個特徵的平方作為新特徵加入訓練集
from sklearn.preprocessing import PolynomialFeatures
# poly_features = PolynomialFeatures(degree = 2, include_bias = False)
# X_poly = poly_features.fit_transform(X)
# print("X[0]: ", X[0], "X_poly[0]: ", X_poly[0]) # X[0]:  [-2.37125826] X_poly[0]:  [-2.37125826  5.62286573]
# 此時 X_poly 包含原本的特徵X和該特徵的平方
# lin_reg = LR()
# lin_reg.fit(X_poly, y)
# print("Intercept: ", lin_reg.intercept_, "Coef:", lin_reg.coef_)
# Intercept:  [2.06272886] Coef: [[0.92440081 0.46032866]] <- 此為模型預估
# 實際上我們的原始函數是 0.5X^2 + X + 2 , 模型預估為 0.46X^2 + 0.92X + 2.06

# 學習曲線
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split as tts

# def plot_learning_curves(model, X, y):
#     X_train, X_val, y_train, y_val = tts(X, y, test_size = 0.2)
#     train_errors, val_errors = [], []
#     for m in range(1, len(X_train)):
#         model.fit(X_train[:m], y_train[:m])
#         y_train_predict = model.predict(X_train[:m])
#         y_val_predict = model.predict(X_val)
#         train_errors.append(mse(y_train_predict, y_train[:m]))
#         val_errors.append(mse(y_val_predict, y_val))
#     plt.plot(np.sqrt(train_errors), "r-+", linewidth = 2, label = 'train')
#     plt.plot(np.sqrt(val_errors), "b-", linewidth = 3, label = 'val')
#     plt.legend(loc = "lower right")
#     plt.xlabel("Train_Set")
#     plt.ylabel("RMSE")
#     plt.show()

# lin_reg = LR()
# plot_learning_curves(lin_reg, X, y)
# 從圖上可以觀察出此模型擬合不足, 因為兩條曲線都非常接近且RMSE非常高
# 面對訓練數據的擬合不足, 需要使用更複雜的模型或者找到更好的特徵

# 使用同樣的數據集, 一個 10 階多項式模型的學習曲線
from sklearn.pipeline import make_pipeline, Pipeline
# polynomial_model = make_pipeline(
#     PolynomialFeatures(degree = 10, include_bias = False), LR()
# )
# polynomial_model = Pipeline((
#     ("poly_features", PolynomialFeatures(degree = 10, include_bias = False)),
#     ("sgd_reg", LR()),
# ))

# plot_learning_curves(polynomial_model, X, y)
# 再次複習: 原本內容在資料科學的驗證及學習曲線就有提到
# 高偏差: 造成的原因是 錯誤的假設, 導致對訓練數據擬合不足
# 高變異(方差): 造成的原因是 模型對訓練數據微小變化過度敏感, 容易造成過度擬合
# 不可避免的誤差: 造成的原因是, 雜訊導致的, 唯一的做法就是清理數據(數據預處理)
# 補充: 降低方差就會提升偏差, 反之亦然, 要去取得平衡點才是主要的


# 正則線性模型(正規化)
# 正規化通常透過約束模型的權重來實現
# 接下來有三個例子: 嶺回歸(Ridge Regression), 套所回歸(Lasso Regression), 彈性網路(Elastic Net)

# Ridge Regression(嶺回歸, 又稱 吉洪若夫正規化): 線性回歸的正規化版
# 在成本函數中添加一個等於 alpha(sigma i from 1 to n)[theta_i^2] 正規項
# 使得學習中的算法不僅要擬合數據, 同時要讓模型權重保持最小
# 正則項只能在訓練時添加到成本函數中, 訓練完後必須要使用未經過正則化的性能指標來評估模型
# 嶺回歸的成本函數: J(theta) = MSE(theta) + alpha(1/2 sigma(i from 1 to n)[theta_i^2])
# 注意: 大多數的正規化模型都必須對數據進行縮放(例如: StandardScaler), 因為對輸入特徵的大小非常敏感

# 也可以使用 閉式方程或梯度下降執行嶺回歸
# 閉式解的嶺回歸: theta = (X.T.dot(X) + alphaA)^-1.dot(X.T).dot(y)
# 使用 Scikit-Learn 執行閉式嶺回歸
from sklearn.linear_model import Ridge
# ridge_reg = Ridge(alpha = 1, solver = "cholesky")
# ridge_reg.fit(X, y)
# print(ridge_reg.predict([[1.5]])) # 預測: [[4.88595712]]
# print(ridge_reg.coef_) # [[1.14684929]]

# 用公式驗證
# X_A = np.c_[np.ones((m, 1)), X]
# A = np.eye(2)
# theta = np.linalg.inv(X_A.T.dot(X_A) + 1 * np.linalg.cholesky(A)).dot(X_A.T).dot(y)
# print(theta) # theta_1 [1.14800746]


# 使用隨機梯度下降(SGD)
# sgd_reg = sgdr(penalty = "l2") # l2 代表是嶺回歸
# sgd_reg.fit(X, y.ravel())
# print(sgd_reg.predict([[1.5]])) # 預測: [4.86722428]

# Lasso Regression(套索回歸, 最小絕對收縮和選擇算子回歸)
# 與嶺回歸相同, 但是增加的是權重向量 l1 范數
# Lasso 成本函數: J(theta) = MSE(theta) + alpha(sigma (i from 1 to n)[abs(theta_i)])
# Lasso 回歸的一個重要特點, 傾向於完全消除掉最不重要的特徵權重
# 以下使用 Scikit-Learn Lasso
from sklearn.linear_model import Lasso
# lasso_reg = Lasso(alpha = 0.1)
# lasso_reg.fit(X, y)
# print(lasso_reg.predict([[1.5]]))  # [4.9073445]

# 彈性網路(Elastic Net)
# 彈性網路介於嶺回歸和Lasso回歸中間, 公式也是兩者的混合, 混合比例由 r 來控制
# 彈性網路成本函數: (r = 1, Lasso回歸; r = 0, 嶺回歸)
# 公式: J(theta) = MSE(theta) + r * alpha(sigma(i from 1 to n)[abs(theta_i)]) + 
#                  alpha(sigma (i from 1 to n)[theta_i^2]) * (1-r)/2
# 以下使用 Scikit-Learn 的 彈性網路
from sklearn.linear_model import ElasticNet
# elastic_net = ElasticNet(alpha = 0.1, l1_ratio = 0.5)
# elastic_net.fit(X, y)
# print(elastic_net.predict([[1.5]])) # [4.54414787]

# 整理關於三種正規化: 在大多數情況下, 避免使用純線性回歸; 嶺回歸是不錯的默認選擇, 
# 但是如果實際用到的特徵只有少數幾個, 傾向於使用 Lasso 回歸或彈性網路, 
# 彈性網路又優於 Lasso 回歸, 因為當特徵數量超過訓練實例數量或和幾個特徵強相關時, Lasso 回歸表現可能不穩定 

# 早期停止法
# 在驗證誤差達到最小值時停止訓練
# 以下用程式碼來實現(封裝在函數裡 <- 只有大概的架構 可以拿來當參考用)
# def earlier_stop(X, y, size):
#     from sklearn.base import clone
#     sgd_reg = sgdr(n_iter_no_change = 1, warm_start = True, penalty = None, 
#                    learning_rate = "constant", eta0 = 0.0005)

#     minimum_val_error = float("inf")
#     best_epoch = None
#     best_model = None
#     for epoch in range(1000):
#         sgd_reg.fit(X_train_poly_scaled, y_train)
#         y_val_predict = sgd_reg.predict(X_val_poly_scaled)
#         val_error = mse(y_val_predict, y_val)
#         if val_error < minimum_val_error:
#             minimum_val_error = val_error
#             best_epoch = epoch
#             best_model = clone(sgd_reg)


# 邏輯回歸(Logistic Regression, 羅吉斯回歸)
# 被廣泛用於估算一個實例屬於某個特定類別的機率, 屬於一個二元分類器

# 概率估算
# 和線性回歸相同, 計算輸入特徵的權重, 但不同於輸出, 邏輯回歸的輸出是一個數理邏輯
# 公式: p = h(X) = σ(θ.T.dot(X)) <- 邏輯回歸模型概率估算(向量化形式)
# 邏輯模型: 是一個 Sigmoid 函數, 輸出為 0 ~ 1 之間的數字
# 公式: σ(t) = 1 / (1 + exp(-t)); t = 0, σ(0) = 0.5
# y = [1 if p >= 0.5 else 0]

# 訓練和成本函數
# 單個訓練實例的成本函數: c(θ) = [-log(p) <- (y = 1) : -log(1 - p) <- (y = 0)]
# 整個訓練集的成本函數就是所有訓練實例的平均成本, 可以記成 log 損失函數

# 邏輯回歸的成本函數(log 損失函數)
# 公式: J(θ) = (- 1/m) * Σ(i from 1 to m)[y^(i) * log(p^(i)) + (1-y^(i)) * log(1-p^(i))]
# 此函數是個凸函數, 可以透過梯度下降或任意優化算法找出全局最小值, 對此函數的任意一點(任意i值)做偏導數

# 決策邊界
# 在此使用鳶尾花資料集來說明邏輯回歸
from sklearn.datasets import load_iris
iris = load_iris()
# print(list(iris.keys()))
# ['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename']
X = iris["data"][:, 3:] # petal width <- 花瓣寬度
y = (iris["target"] == 2).astype(np.int) # 1 if Iris-Virginica else 0 <- 判斷是否屬於 Virginica鳶尾花

# 訓練回歸模型
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X, y)

# 看看對於花瓣寬度在 0~3 公分之間的鳶尾花, 模型估算出來的概率
X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_proba = log_reg.predict_proba(X_new)
# plt.plot(X_new, y_proba[:, 1], "g-", label = "Iris-Virginica")
# plt.plot(X_new, y_proba[:, 0], "b--", label = "Not Iris-Virginica")
# plt.legend(loc = "center left")
# plt.xlabel("petal width")
# plt.ylabel("probability")
# plt.show()
# 圖中可以看出兩條曲線的交叉點就是決策邊界(大約在1.6左右)

# print(log_reg.predict([[1.7], [1.5]])) # [1 0]

# Softmax 回歸
# 又稱多元邏輯回歸, 從邏輯回歸模型延伸
# 對於給定一個實例X, softmax回歸模型首先計算出每個類別 k 的分數, 接著對這些分數應用 Softmax 函數估算概率
# 公式: S(x) = (θ_k.T.dot(x)) <- 類別 k 的 Softmax 分數
# Softmax 函數: P_k = σ(s(x))_k = exp(s_k(x)) / (sigma (j from 1 to k))[exp(s_j(x))]
# K 是類別數量, s(x) 實例x每個類別的分數向量, σ(s(x))_k 給定類別分數下, 實例 x 屬於類別 k 的概率
# Softmax 回歸分類器預測: y = argmax(σ(s(x))_k) = argmax(s_k(x)) = argmax(θ_k.T.dot(x))
# argmax 傳回的是 使函數最大化所對應的變數值, 在此函數裡是估算概率最大的 k 值
# 注意: Softmax 回歸分類器, 一次只會預測一個類別(僅適用於互斥的類別上, 例如植物的不同種類, 無法識別一張照片多個人)

# 訓練目標是得到一個能對目標類別做出高概率估算的模型, 把成本函數最小化在此稱為交叉熵
# 交叉熵成本函數: J(Θ) = (-1/m) * Σ(i from 1 to m)Σ(k from 1 to K)[y_k^(i)log(p_k^(i))]
# 如果第 i 個實例的目標類別是 k, 則 y_k^(i) = 1, 否則 0
# if K = 2, 相當於邏輯回歸的成本函數(log 損失函數)

# 使用 Softmax 回歸 把鳶尾花分成三類
X = iris["data"][:, (2, 3)] # petal length, petal width
y = iris["target"]

softmax_reg = LogisticRegression(multi_class = "multinomial", solver = "lbfgs", C = 10)
softmax_reg.fit(X, y)
# print(softmax_reg.predict([[5, 2]]))  # [2]
# print(softmax_reg.predict_proba([[5, 2]]))  # [[6.38014896e-07 5.74929995e-02 9.42506362e-01]] <- 機率分布
