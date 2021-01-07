# 超參數以及模型驗證
# 使用 holdout sets 和 cross-validation 進行更強固的模型評估之前, 先行說明

# 錯誤的模型驗證方式:
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target

# 選用模型的超參數, 這裡使用KNN分類器, 並設定 n_neighbors = 1
from sklearn.neighbors import KNeighborsClassifier as KNN
model = KNN(n_neighbors = 1)
# model.fit(x, y)
# y_model = model.predict(x)

# 計算正確率
from sklearn import metrics
# accuracy = metrics.accuracy_score(y, y_model)
# print("Accuracy: ", accuracy)

# 上面的做法 可得到 100% 的正確率
# 事實上, 這個預測不是我們所想要的結果. 這種做法存在著基本的缺陷: 它的訓練和驗證模型使用同一組資料
# 加上, KNN 是以實例為基礎的評估器, 可以簡單的儲存訓練資料, 然後透過和新資料所儲存的資料做比較來預測標籤
# 除非人為情況, 否則每次的正確率都會 100%

# 正確的模型驗證方式: holdout sets 
from sklearn.model_selection import train_test_split as tts
# 對每個集合切割50%的資料
x_train, x_test, y_train, y_test = tts(x, y, train_size = 0.5, random_state = 0)

# 模型擬合
model.fit(x_train, y_train)
# y2_model = model.predict(x_test)
# accuracy = metrics.accuracy_score(y_test, y2_model)
# print("Accuracy: ", accuracy)  # 0.9066666666666666

# 透過 cross-validation 進行模型驗證
# 使用 holdout sets 做模型驗證有一個缺點, 在模型訓練的時候會少一部分的資料
# 尤其在訓練集很少的情況下更有可能會發生問題

# 使用 cross-validation 執行一系列的擬合, 其中資料中的每個部分都必須當作訓練集以及驗證用的資料集
# y2_model = model.fit(x_train, y_train).predict(x_test)
# y1_model = model.fit(x_test, y_test).predict(x_train)
# 交叉驗證(cross validation)
# accuracy2 = metrics.accuracy_score(y_test, y2_model)
# accuracy1 = metrics.accuracy_score(y_train, y1_model)
# print("Accuracy2: %2.3f %% \nAccuracy1: %2.3f %%" % (accuracy2 * 100, accuracy1 * 100))
# 90.667 %, 96.000 %

# 多次的交叉驗證, 可以更加得到模型正確率的量測

# 若把資料分成5組評估
from sklearn.model_selection import cross_val_score as cvs
n = cvs(model, x, y, cv = 5)
# print(n) # [0.96666667 0.96666667 0.93333333 0.93333333 1.        ]
# model 為擬合模型, x 為資料集, y為目標標籤, cv參數調整 要進行n次的交叉驗證
# reference: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score


# Scikit-Learn 實作許多 cross-validation 方案在某些特定的情形下非常有用, 
# 這些是使用 迭代器 應用在cross-validation 模組上的實作
# Example: 如果希望使用極端的情況, 分割的數目=資料點的數目(訓練資料只留下一個資料做驗證使用)
# 上述例子的cross-validation 的方式 稱為 leave-one-out cross-validation
from sklearn.model_selection import LeaveOneOut
scores = cvs(model, x, y, cv = LeaveOneOut())
# print(scores)  # scores.shape (150,1)
# 對 150 個樣本資料進行預測, 預測正確為(1.0), 錯誤為(0.0)
# 取平均就可以得到預測正確率
# print(scores.mean())  # 0.96

# 選用最佳的模型
# 模型以及超參數的選擇
# 思考一個問題: 如果評估之後的效能是不好的, 那應該朝哪一個方向改進
# 可能的答案: 
#   使用 更複雜的/更有彈性的 模型
#   使用 較不複雜的/較沒有彈性的 模型
#   收集更多的訓練樣本
#   收集更多的資料加到每一個樣本的特徵中

# 偏差(bias)和變異(variance)的權衡(p381)
# Underfit(低度擬合): 沒有足夠的模型彈性去合適的說明此資料中的所有特徵, 代表這個模型會有高度偏差(bias)
# Overfit(過度擬合): 越精準的描述訓練資料, 但是這個精確度只針對已知的訓練資料, 若遇到與以往不同的資料
#                   進行預測時將會得到近乎錯誤的結果, 稱為高變異(variance)

# 決定係數(驗證分數) 為 R^2: 它用來測量一個模型在執行相對一個簡單的目標值平均的好壞程度
# reference: https://en.wikipedia.org/wiki/Coefficient_of_determination
# R^2 = 1: 表示完美符合, R^2 = 0: 表示此模型不會比簡單的拿取資料的平均值好, 負值表示更糟

# 對於 高偏差模型: 驗證資料集的效能 和 訓練資料集的效能 相同
# 對於 高變異模型: 驗證資料集的效能 和 訓練資料集的效能 更差 

# Scikit-Learn 中的驗證曲線(validation curve)
# 使用交叉驗證計算模型類別的驗證曲線, 多項式回歸(polynomial regression)
# degree-n: y = ax^n + bx^(n-1) + cx^(n-2) + ... dx^(n-n)
# 一般化這個方程式到任意數量的多項式特徵, Scikit-Learn 中用LR可以做到
# 使用一個管線(pipeline)把這些運算串在一起

from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression as LR
from sklearn.pipeline import make_pipeline

def PolynomialRegression(degree = 2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LR(**kwargs))

# 建立用來擬合模型的資料
import numpy as np

def make_data(N, err = 1.0, rseed = 1):
    # randomly sample the data
    rng = np.random.RandomState(rseed)
    X = rng.rand(N, 1) ** 2
    y = 10 - 1. / (X.ravel() + 0.1)
    if err > 0:
        y += err * rng.randn(N)
    return X, y
    # X.ravel(): 如果非必要, 將不會產生源數據的副本
    # Reference: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html
X, y = make_data(40)

# 視覺化
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

X_test = np.linspace(-0.1, 1.1, 500)[:, None] # (500,) 轉成 (500,1)

# plt.scatter(X.ravel(), y, color = 'black')
# axis = plt.axis()
# for degree in [1, 3, 5]:
#     y_test = PolynomialRegression(degree).fit(X, y).predict(X_test)
#     plt.plot(X_test.ravel(), y_test, label = 'degree = {0}'.format(degree))
# plt.xlim(-0.1, 1.0)
# plt.ylim(-2, 12)
# plt.legend(loc = 'best')

# plt.show()

# 進一步視覺化它的驗證曲線, 在此可以使用 validation_curve 由 Scikit-Learn 提供
# 給一個模型, 資料, 參數名稱, 以及要探討的範圍, 此函式會自動計算所提供的範圍內的訓練分數以及驗證分數
from sklearn.model_selection import validation_curve
degree = np.arange(0, 21)
train_score, val_score = validation_curve(PolynomialRegression(), X, y, 
                                         'polynomialfeatures__degree', degree, cv = 7)
# plt.plot(degree, np.median(train_score, 1), color = 'blue', label = 'training score')
# plt.plot(degree, np.median(val_score, 1), color = 'red', label = 'validation score')
# plt.legend(loc = 'best')
# plt.ylim(0, 1)
# plt.xlabel('degree')
# plt.ylabel('score')

# plt.show()
# validation_curve()
# Reference: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve

# 經過上面的驗證曲線的評估後, 使用多項式回歸模型的最佳解在三階多項式的時候(degree-3)
# plt.scatter(X.ravel(), y)
# lim = plt.axis()
# y_test = PolynomialRegression(3).fit(X, y).predict(X_test)
# plt.plot(X_test.ravel(), y_test, color = 'red')
# plt.axis(lim)

# plt.show()

# 學習曲線
# 對於模型複雜度的一個重要觀點, 最佳的模型都會和訓練資料的大小有關
# Ex: 多了5倍的資料集
X2, y2 = make_data(200)
# plt.scatter(X2.ravel(), y2)
# plt.show()

# 畫出新資料集的驗證曲線
degree = np.arange(0, 21)
train_score2, val_score2 = validation_curve(PolynomialRegression(), X2, y2, 
                                            'polynomialfeatures__degree', degree, cv = 7)
# plt.plot(degree, np.median(train_score2, 1), color = 'blue', label = 'training score')
# plt.plot(degree, np.median(val_score2, 1), color = 'red', label = 'validation score')
# plt.plot(degree, np.median(train_score, 1), color = 'blue', alpha=0.3, linestyle = 'dashed')
# plt.plot(degree, np.median(val_score, 1), color = 'red', alpha=0.3, linestyle = 'dashed')
# plt.legend(loc = 'lower center')
# plt.ylim(0, 1)
# plt.xlabel('degree')
# plt.ylabel('score')
# plt.show()

# 學習曲線(learning curve)
# 一個給定複雜度的模型將會對於一個小的資料集過度擬合, 代表 訓練分數遠大於驗證分數
# 一個給定複雜度的模型將會對於一個大的資料集擬合不足, 代表 訓練分數降低, 驗證分數增加
# 模型絕對不會發生 驗證分數>訓練分數, 代表曲線只會接近但絕對不會交叉

# Scikit-Learn 中的學習曲線
# 在此使用 degree-2, degree-9的模型, 針對原始資料計算學習曲線
# from sklearn.model_selection import learning_curve
# fig, ax = plt.subplots(1, 2, figsize = (16, 6))
# fig.subplots_adjust(left = 0.0625, right = 0.95, wspace = 0.1)

# for i, degree in enumerate([2, 9]):
#     N, train_lc, val_lc = learning_curve(PolynomialRegression(degree), X, y, cv=7,
#                                          train_sizes = np.linspace(0.3, 1, 25))
    
#     ax[i].plot(N, np.mean(train_lc, 1), color = 'blue', label = 'training score')
#     ax[i].plot(N, np.mean(val_lc, 1), color = 'red', label = 'validation score')
#     ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1], color = 'green', linestyle = 'dashed')
#     ax[i].set_ylim(0, 1)
#     ax[i].set_xlim(N[0], N[-1])
#     ax[i].set_xlabel('training size')
#     ax[i].set_ylabel('score')
#     ax[i].set_title('degree = {0}'.format(degree), size = 14)
#     ax[i].legend(loc = 'best')
# plt.show()
# 當學習曲線已經收斂了, 即使增加更多的訓練資料並不會明顯的提升擬合程度
# 增加收斂分數(由虛線表示)唯一的方法是使用不同(通常是更複雜)的模型
# 畫出一個用來選擇特定模型和資料集的學習曲線, 有幫助改善在分析中如何更進一步的決策

# 驗證實務: 格狀搜尋(Grid Search)
# 在實務上, 通常模型都會有超過一個可以調整的地方, 這樣驗證和學習曲線就會變成多維度的面
# 因此, 會導致視覺化變得困難, 寧可去簡單的找尋一個可以最大化驗證分數的特定模型
from sklearn.model_selection import GridSearchCV
param_grid = {'polynomialfeatures__degree': np.arange(21), 
              'linearregression__fit_intercept': [True, False],
              'linearregression__normalize': [True, False]}
grid = GridSearchCV(PolynomialRegression(), param_grid, cv = 7)
grid.fit(X, y)
# print(grid.best_params_) # 最佳參數
# {'linearregression__fit_intercept': False, 
# 'linearregression__normalize': True, 
# 'polynomialfeatures__degree': 4}

model = grid.best_estimator_
plt.scatter(X.ravel(), y)
lim = plt.axis()
y_test = model.fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test)
plt.axis(lim)
plt.show()