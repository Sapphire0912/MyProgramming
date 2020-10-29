# 分類
# 此處使用MNIST數據集(在0.20版本之後 使用 fetch_openml 取代 fetch_mldata)

from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784')
# print(mnist)
# 裡面有三個鍵值['DESCR', 'data', 'target']

# 查看數據
X, y = mnist["data"], mnist["target"]
# print(X.shape) # (70000, 784) <- 28 * 28 像素組成的 784 個特徵
# print(y.shape) # (70000,)

# 先隨機看其中一個數據 使用 Matplotlib imshow()
import matplotlib as mpt
import matplotlib.pyplot as plt

some_digit = X[36001]
some_digit_image = some_digit.reshape(28, 28)
# plt.imshow(some_digit_image, cmap = mpt.cm.binary, interpolation = 'nearest')
# plt.axis('off')
# plt.show()

# print(y[36001]) # 2 <- 該數據對應的標籤

# 創建測試集和訓練集(本數據已經分成了訓練集和測試集了 前60000 和 後10000)
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

import numpy as np
shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
y_train = y_train.astype(np.int8) # <- 處理 ValueError

# 訓練一個二元分類器(假如先識別數字為 2 或 非2 )
# y_train_2 = (y_train == 2)
# y_test_2 = (y_test == 2)

# 一個好的初始選擇是 隨機梯度下降(SGD)分類器 使用 Scikit-Learn SGDClassifier
# SGD的優勢是: 有效處理非常大型的數據集, 因為SGD是處理訓練實例, 使得SGD非常適合增量學習
from sklearn.linear_model import SGDClassifier

# sgd_clf = SGDClassifier(random_state = 42)
# sgd_clf.fit(X_train, y_train_2)
# print(sgd_clf.predict([some_digit]))

# 性能考核
# 使用交叉驗證測量精度
# 自定義交叉驗證
# from sklearn.model_selection import StratifiedKFold
# from sklearn.base import clone

# skfolds = StratifiedKFold(n_splits = 3, random_state = 42, shuffle = True) # n_splits 相當於 cvs 的 cv參數

# for train_index, test_index in skfolds.split(X_train, y_train_2):
#     clone_clf = clone(sgd_clf)
#     X_train_folds = X_train[train_index]
#     y_train_folds = (y_train_2[train_index])
#     X_test_fold = X_train[test_index]
#     y_test_fold = (y_train_2[test_index])

#     clone_clf.fit(X_train_folds, y_train_folds)
#     y_pred = clone_clf.predict(X_test_fold)
#     n_correct = sum(y_pred == y_test_fold)
#     print(n_correct / len(y_pred)) # 0.9736, 0.96925, 0.97325

from sklearn.model_selection import cross_val_score as cvs
# score = cvs(sgd_clf, X_train, y_train_2, cv = 3, scoring = "accuracy")
# print(score)  # [0.97215 0.97385 0.97355] <- 正確率大於 95% 
# 經過自定義或者Scikit-Learn的 cross_val_score 甚至更笨的分類器預測的正確率都高達90%, 
# 同時也說明了正確率不能成為分類器的首要性能指標

# 混淆矩陣
# 評估分類器性能的更好方法是混淆矩陣(意旨: A類別的東西被誤以為B類別)
from sklearn.model_selection import cross_val_predict as cvp
# y_train_pred = cvp(sgd_clf, X_train, y_train_2, cv = 3)
# cvp 不同於 cvs, 前者是傳回每個折疊的預測, 後者是傳回評估分數

# 使用 confusion_matrix 來取得混淆矩陣
from sklearn.metrics import confusion_matrix
# confused = confusion_matrix(y_train_2, y_train_pred)
# print(confused) # 下面為輸出結果
# [[50891  3151]
#  [  591  5367]]
# 左上: 有 50891 張圖片被正確分類為 非2 的數字
# 右上: 有 3151  張圖片被錯誤分類為   2 的數字
# 左下: 有 591   張圖片被錯誤分類為 非2 的數字
# 右下: 有 5367  張圖片被正確分類為   2 的數字
# 若一個完美的分類器, 只會有正確的分類也就是(左上 到 右下) 

# 精度和召回率(每次執行程式會得到不一樣的結果 <- 透過混淆矩陣可得知)
# from sklearn.metrics import precision_score, recall_score
# print(precision_score(y_train_2, y_train_pred)) # <- 5021 / (5021 + 1467)
# print(recall_score(y_train_2, y_train_pred)) # <- 5021 / (5021 + 937)
# 0.7738902589395807 <- 精度
# 0.8427324605572339 <- 召回率

# f1 分數: 公式 TP / [TP + (FN + FP) / 2]
# 用來比較不同分類器的(精度和召回率的諧波平均值)
# 使用 Scikit-Learn f1_score
from sklearn.metrics import f1_score
# print(f1_score(y_train_2, y_train_pred)) # 0.8548711081352528

# 精度與召回率的平衡
# 這兩者之間是呈現反比關係, 除非兩個都非常高 f1分數才會高, 此分類器才會非常準確
# Scikit-Learn 不允許直接設定閾值(臨界值), 但是可以得到用於預測的決策分數(調用decision_function)
# y_scores = sgd_clf.decision_function([some_digit])
# print(y_scores) # [6389.1310717]
# 上面的結果會傳回每個實例的分數, 之後就可以根據這些分數使用任意閾值(臨界值)進行預測了
# 看以下例子
# threshold = 0
# y_some_digit_pred = (y_scores > threshold)
# print(y_some_digit_pred) # [ True]
# 若提升臨界值(閾值) <- 只要臨界值大於決策分數, 此圖就會被錯過(此處是誤判)
# threshold = 200000
# y_some_digit_pred = (y_scores > threshold)
# print(y_some_digit_pred) # [False]

# 如何決定使用閾值
# 首先, 使用 cross_val_predict 獲取訓練集中所有實例的決策分數
# y_scores = cvp(sgd_clf, X_train, y_train_2, cv = 3, method = "decision_function")
# 使用 precision_recall_curve 計算所有可能閾值的精度和召回率
# from sklearn.metrics import precision_recall_curve
# precisions, recalls, thresholds = precision_recall_curve(y_train_2, y_scores)

# 下面的函式是 繪製 精度和召回率 決策閾值 之間的關係
# def plot_precision_recell(precisions, recalls, thresholds):
#     plt.plot(thresholds, precisions[:-1], "b--", label = "Precision")
#     plt.plot(thresholds, recalls[:-1], "g-", label = "Recall")
#     plt.xlabel("Threshold")
#     plt.legend(loc = "upper left")
#     plt.ylim(0, 1)
#     plt.show()

# 下面的函式是 繪製 精度 召回率 之間的關係]
# def plot_precision_vs_recall(precisions, recalls):
#     plt.plot(precisions, recalls, "-")
#     plt.xlabel("Precision")
#     plt.ylabel("Recall")
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.show()

# plot_precision_recell(precisions, recalls, thresholds)
# plot_precision_vs_recall(precisions, recalls)

# ROC 曲線(接收者操作特徵曲線 receiver operating characteristic curve)
# 主要是繪製 召回率以及假正類率(FPR, 被誤分為正確的錯誤實例)
# 使用 sklern.metrics 裡面的 roc_curve
# from sklearn.metrics import roc_curve
# fpr, tpr, thresholds = roc_curve(y_train_2, y_scores)

# def plot_roc_curve(fpr, tpr, label = None):
#     plt.plot(fpr, tpr, linewidth = 2, label = label)
#     plt.plot([0, 1], [0, 1], "k--")
#     plt.axis([0, 1, 0, 1])
#     plt.xlabel('False Positive Rate')
#     plt.ylabel('True Positive Rate')
    # plt.show()

# plot_roc_curve(fpr, tpr)

# 測量曲線下的面積(AUC)
# 完美的分類器 AUC = 1, 純隨機分類器的 AUC = 0.5
# 使用 Scikit-Learn 的 roc_auc_score
# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(y_train_2, y_scores)) # 0.9708370681667048
# 在何時使用 ROC 曲線 或者 PR(Precision Recall) 曲線
# 當正類非常少見或者更關注的是假正類(FPR)而不是假負類(FNR)的時候


# 訓練一個 RandomForestClassifier 分類器 並和 SGDClassifier 分類器的 ROC, ROC_AUC 比較
# from sklearn.ensemble import RandomForestClassifier as rfc
# forest_clf = rfc(random_state = 42)
# y_probas_forest = cvp(forest_clf, X_train, y_train_2, cv = 3, method = "predict_proba")
# print(y_probas_forest)

# 繪製 RFC 的 ROC 曲線
# y_scores_forest = y_probas_forest[:, 1]
# fpr_forest, tpr_forest, thresholds_forest = roc_curve(y_train_2, y_scores_forest)
# plt.plot(fpr, tpr, "b:", label = "SGD")
# plot_roc_curve(fpr_forest, tpr_forest, "Random Forest")
# plt.legend(loc = "lower right")
# plt.show()

# print(roc_auc_score(y_train_2, y_scores_forest)) # 0.9974222863648914


# 多類別分類器(這也是一般Scikit-Learn 系統上訓練了10個二元分類器, 來辨別 0~9 10個數字)
# sgd_clf = SGDClassifier(random_state = 42)
# sgd_clf.fit(X_train, y_train)
# print(sgd_clf.predict([some_digit])) # [2]
# 可以調用 decision_function 查看
# some_digit_score = sgd_clf.decision_function([some_digit])
# print(some_digit_score)
# [[-32382.43706269 -28795.31892146   3472.51981866   -956.05254888
#   -16090.6080616   -9543.78986588 -24432.50883194 -33809.69510247
#    -3875.07060874 -16031.29649287]]
# print(np.argmax(some_digit_score)) # 2
# print(sgd_clf.classes_) # [0 1 2 3 4 5 6 7 8 9]

# 一對一(OvO), 一對多(OvA) 分類
# 使用 OneVsOneClassifier, OneVsRestClassifier 
# 以下基於 SGDClassifier 使用 OvO
# from sklearn.multiclass import OneVsOneClassifier as ovo
# ovo_clf = ovo(SGDClassifier(random_state = 42))
# ovo_clf.fit(X_train, y_train)
# print(ovo_clf.predict([some_digit])) # [2]
# print(len(ovo_clf.estimators_)) # 45

# 基於 RandomForestClassifier 
# forest_clf = rfc(random_state = 42)
# forest_clf.fit(X_train, y_train)
# print(forest_clf.predict([some_digit])) # [2]
# print(forest_clf.predict_proba([some_digit])) # [[0.   0.   0.99 0.   0.   0.   0.01 0.   0.   0.  ]]

# 像之前一樣使用交叉驗證來評估準確率
# accuracy = cvs(sgd_clf, X_train, y_train, cv = 3, scoring = "accuracy")
# print(accuracy) # [0.8762  0.86375 0.88485]

# 經過特徵縮放後, 可以提高準確率
# 使用 標準化縮放 Scikit-Learn StardardScaler
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
# accuracy = cvs(sgd_clf, X_train_scaled, y_train, cv = 3, scoring = "accuracy")
# print(accuracy) # 這裡無法測試(機器效能問題), 但是會知道準確率比前者的還高
# o.s. 對 60000 張圖片一次進行標準化縮放根本瘋了

# 錯誤分析(使用混淆矩陣)
# y_train_pred = cvp(sgd_clf, X_train, y_train, cv = 3) # <- 原本這裡是要使用 X_train_scaled
# conf_mx = confusion_matrix(y_train, y_train_pred)
# plt.matshow(conf_mx, cmap = plt.cm.gray)
# plt.show()

# 從混淆矩陣的結果來分析
# 若只保留錯誤的數值, 並重新繪製結果
# row_nums = conf_mx.sum(axis = 1, keepdims = True)
# norm_conf_mx = conf_mx / row_nums
# np.fill_diagonal(norm_conf_mx, 0)
# plt.matshow(norm_conf_mx, cmap = plt.cm.gray)
# plt.show()
# 從圖上可以看到哪些數字容易被混淆, 可以特別針對這部分進行預處理
# 可以使用 Scikit-Image, Pillow, OpenCV 等等讓某些模式更為突出, 例如閉環等等


# 從這裡開始以下的輸出結果還沒有確認過(設備問題, 執行時間太長)
# 多標籤分類
# 一般來說每個實例都只會被分在一個類別裡, 若希望分類器為實例分出多個標籤
# 注意: 不是所有的分類器都支援多標籤分類
from sklearn.neighbors import KNeighborsClassifier
y_train_large = (y_train >= 7) # 儲存大於等於7的標籤
y_train_odd = (y_train % 2 == 1) # 儲存奇數
y_multilabel = np.c_[y_train_large, y_train_odd]

knn_clf = KNeighborsClassifier() # default: n_neighbors = 5
knn_clf.fit(X_train, y_multilabel)
# print(knn_clf.predict([some_digit])) # [[False False]] 2 既非大於等於7也非奇數
# 計算 f1_score
y_train_knn_pred = cvp(knn_clf, X_train, y_train, cv = 3)
print(f1_score(y_train, y_train_knn_pred, average = "macro"))


# 多輸出分類
# 多標籤分類的泛化, 其標籤也可以是多種類別(兩個以上的值)
# 由以下例子說明: 構建一個系統去除圖片的雜訊
# 注意: 此分類器的輸出是多個標籤(一個pixel 一個label, 像素強度範圍 0~255)
# 首先, 先把乾淨的圖片加入雜訊並創建訓練集和測試集
rnd = np.RandomState(42)
noise_train = rnd.randint(0, 100, (len(X_train)), 784)
noise_test = rnd.randint(0, 100, (len(X_test)), 784)
X_train_mod = X_train + noise_train
X_test_mod = X_test + noise_test
y_train_mod = X_train
y_test_mod = X_test

# 隨機拿一張圖片視覺化
fig, ax = plt.subplots(1, 2, figsize = (16, 6))
ax[0].imshow(X_train_mod[36001])
ax[1].imshow(y_train_mod[36001])
ax[0].title("Noise")
ax[1].title("Original")
plt.show()

# 通過訓練分類器, 把含有雜訊的圖片還原
knn_clf.fit(X_train_mod, y_train_mod)
clean_digit = knn_clf.predict([some_digit])

# 把圖片畫出來
plt.title("Predict Picture")
plt.imshow(clean_digit)
plt.show()