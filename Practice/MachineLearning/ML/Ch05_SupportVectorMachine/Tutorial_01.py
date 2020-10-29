# 支持向量機(SVM)
# 這一章節圖片的部分可以看課本或者網路的原文電子書
# SVM 可以執行線性或非線性分類, 回歸甚至異常值檢測任務, 是最受歡迎的模型之一
# SVM 特別適合用於中小型複雜數據集的分類

# 線性SVM分類
# SVM 在邊界以外增加更多的訓練實例並不會對決策邊界造成影響; 另外, SVM對特徵縮放非常敏感
# 在 Scikit-Learn 的 SVM 中, 可以透過參數 C 來調整決策邊界的範圍, C 越小邊界越寬, 否則反之
# 如果 SVM 過度擬合, 可以通過降低 C 參數來進行正則化
# 看以下程式碼
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
sns.set()
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# iris = load_iris()
# X = iris["data"][:, (2, 3)] # petal length, petal width (cm)
# y = (iris["target"] == 2).astype(np.float64) # Iris-Virginica

# svm_clf = Pipeline((
#     ("scaler", StandardScaler()),
#     ("linear_svc", LinearSVC(C = 1, loss = "hinge"))
# ))

# svm_clf.fit(X, y)
# print(svm_clf.predict([[5.5, 1.7]])) # [1.]

# 非線性 SVM 分類
# 在有些情況下, 數據是不是靠線性就可分離的, 因此可以增加多項式特徵來分開數據
# Scikit-Learn 使用 PolynomialFeatures 轉換器可以做到
# 以下使用 衛星數據集
from sklearn.datasets import make_moons
from sklearn.preprocessing import PolynomialFeatures
# X, y = make_moons()

# poly_svm_clf = Pipeline((
#     ("poly_features", PolynomialFeatures(degree = 3)),
#     ("scaler", StandardScaler()),
#     ("svm_clf", LinearSVC(C = 10, loss = "hinge", max_iter = 10000))
# ))

# poly_svm_clf.fit(X, y)

# 核多項式
# SVM 的 核(kernel)技巧, 產生的結果就跟添加了許多多項式特徵一樣, 但實際上並不需要真的添加.
# 因為實際沒有添加任何特徵, 所以也不存在數量爆炸的組合特徵
from sklearn.svm import SVC
# poly_kernel_svm_clf = Pipeline((
#     ("scaler", StandardScaler()),
#     ("svm_clf", SVC(kernel = "poly", degree = 3, coef0 = 1, C = 5))
# ))
# poly_kernel_svm_clf.fit(X, y)
# 上面的程式碼, 使用 3階多項式的核SVM訓練分類器; 依據實際情況, 來調整多項式階數.
# 超參數 coef0 是控制模型受高階多項式還是低階多項式影響

# 添加相似特徵
# 解決一種非線性問題的另一種技巧是 添加相似特徵, 這些特徵可以經過相似函數計算得出, 
# 相似函數可以測量每個實例與一個特定地標(landmark)之間的相似度
# 接著採用 高斯徑向基函數(Radial Basis Function, RBF)作為相似函數
# 公式: Φγ(x, l) = exp(-γ || x - l || ^ 2)

# 高斯 RBF 核函數
# 使用 SVC 嘗試 高斯 RBF 核
# rbf_kernel_svm_clf = Pipeline((
#     ("scaler", StandardScaler()),
#     ("svm_clf", SVC(kernel = "rbf", gamma = 0.5, C = 0.001))
# ))
# rbf_kernel_svm_clf.fit(X, y)
# 這裡的參數 gamma 就如同 超參數 C 一樣

# 計算複雜度
# liblinear 資料庫為 線性 SVM 實現的一個優化算法, LinearSVC 基於該庫的, 該算法不支援核技巧
# 它與訓練實例數量和特徵數量幾乎呈線性相關: 訓練時間複雜度為: O(m*n)
# 若要求非常高的精度, 算法需要的時間很長, 由超參數 ε(Scikit-Learn 的 tol 參數) 來控制(大多數情況, 默認值就夠了)
# SVC 則是基於 libsvm 資料庫, 此庫支援核技巧, 時間複雜度為: O(m^2 * n) to O(m^3 * n),
# 也就是如果訓練實例非常大, 速度就會非常慢, 所以此算法完美適用於複雜但中小型的訓練集 
# 但還是可以良好適應特徵數量增加, 特別是對應稀疏矩陣, 此算法複雜度大致與實例平均非零特徵數成比例
# 該目錄的xlsx檔案有整理的表格


# SVM 回歸
# 不同於SVM分類, SVM分類是要把多類別給切開或是調整邊界寬度, SVM回歸是 盡可能讓更多的實例位於邊界上和限制間隔違例
# 寬度由 超參數 ε 控制, 越大則邊界寬度越寬, 否則反之
# 可以使用 Scikit-Learn 的 LinearSVR 來執行線性 SVM 回歸
# 以下程式碼只是示例
from sklearn.svm import LinearSVR
# X_data = np.random.rand(50)
# y_data = np.random.randn(50) + 3 * X_data + 2 * X_data ** 2

# svm_reg = LinearSVR(epsilon = 1.5)
# svm_reg.fit(X_data[:, None], y_data.ravel())

# X_test = np.linspace(0, 1, 10)
# y_pred = svm_reg.predict(X_test[:, None])
# plt.scatter(X_data, y_data)
# plt.plot(X_test, y_pred, color = "Red")
# plt.show()

# 解決非線性回歸任務, 可以使用核化的 SVM 模型
# 以下程式碼只是示例
from sklearn.svm import SVR
# svm_poly_reg = SVR(kernel = "poly", degree = 2, C = 100, epsilon = 0.1)
# svm_poly_reg.fit(X_data[:, None], y_data.ravel())
# SVM 也可以用於異常值檢測, 詳細可以參考 Scikit-Learn 文檔


# 工作原理
# 這裡是介紹 SVM 是如何進行預測及如何訓練的
# 假設偏置項為 b, 特徵權重為 w, 同時輸入特徵項量中不添加偏置特徵, 預測類別為 y

# 決策函數和預測
# 線性 SVM 分類器的決策函數: w.T.dot(x) + b = w_1 * x_1 + ... + w_n * x_n + b 來預測新實例x的分類
# 則 y = 0 if w.T.dot(x) + b < 0 else 1

# 訓練目標
# 這部分可直接看書上的筆記和畫線, 主要都是數學原理
