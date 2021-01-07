# 集成學習和隨機森林
# 這章節會提到最流行的幾種集成方法: bagging, boosting, stacking等以及 random forests

# 投票分類器
# 在基於所有預測器互相獨立的情況下, 集成法的成效最高
# 然而, 使用多種不同的預測器, 會提高集成法的準確率

# 以下使用 Scikit-Learn 創建並訓練一個投票分類器, 由三種不同的分類器組成
from sklearn.datasets import make_moons
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split 

# X, y = make_moons()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) 

# log_clf = LogisticRegression()
# rnd_clf = RandomForestClassifier()
# svm_clf = SVC()
# voting_clf = VotingClassifier(
#     estimators = [('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf)],
#     voting = 'hard'
# )

# voting_clf.fit(X_train, y_train)

# 看看每個分類器在測試集上的準確率
from sklearn.metrics import accuracy_score
# for clf in (log_clf, rnd_clf, svm_clf, voting_clf):
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
#     print(clf.__class__.__name__, ": %.3f" % accuracy_score(y_test, y_pred))
# LogisticRegression : 0.900
# RandomForestClassifier : 0.920
# SVC : 1.000
# VotingClassifier : 0.960
# 書上是 VotingClassifier 準確率會略高於其他單個分類器
# 實際上, 多次測驗結果可能有過度擬合的問題以及資料集太少(特徵數不足, 需要預處理), 因此好幾次 SVC 準確率都 100% 

# bagging 和 pasting
# 與前面相反的是, 在同一種的預測器算法但是不一樣的訓練集進行訓練
# 若採樣時把樣本放回, 稱為 bagging, 否則為 pasting
# bagging 和 pasting 允許訓練實例在多個預測器中被多次採樣, 但只有 bagging 允許訓練實例被同一個預測器多次採樣
# 在 Scikit-Learn 使用 bagging, pasting
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
# bag_clf = BaggingClassifier(
#     DecisionTreeClassifier(max_depth = 2), n_estimators = 500,
#     bootstrap = True, n_jobs = -1, oob_score = True
# ) # <- make_moon() 總共只有 100 筆資料
# tree_clf = DecisionTreeClassifier(max_depth = 2)

# tree_clf.fit(X_train, y_train)
# bag_clf.fit(X_train, y_train)

# y_tree = tree_clf.predict(X_test)
# y_bag = bag_clf.predict(X_test)

# 包外(oob)評估(BaggingClassifier oob_score = True 才可調用)
# print(bag_clf.oob_score_) # 0.8375
# print(accuracy_score(y_test, y_bag)) # 0.95
# print(accuracy_score(y_test, y_tree)) # 0.9
# 這裡多次實測, 因為隨機採取樣本所以正確率浮動大, 目前純看數值有時會發生預測分數比包外評估及單棵決策樹還低
# 另外, 不限制樹的深度容易造成過度擬合, 最後的結果又因訓練測試集的比例有關(浮動極大)
# 之後找不同的稍大一點的資料集來做測試或自製資料

# 包外決策函數可以看到每個實例類別概率
# print(bag_clf.oob_decision_function_)

# Random Patches 和隨機子空間
# BaggingClassifier 支援對特徵進行抽樣, 透過兩個超參數控制: max_features, bootstrap_features
# 對於高維輸入特別有效(例如: 圖像)


# 隨機森林
# 隨機森林是決策樹的集成, 除了可以像上面的方式來訓練或者使用 RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier # <- 也有 RandomForestRegressor
# rnd_clf = RandomForestClassifier(n_estimators = 500, max_leaf_nodes = 16, n_jobs = -1)
# rnd_clf.fit(X_train, y_train)
# y_pred_rf = rnd_clf.predict(X_test)
# RandomForestClassifier 除了有 DecisionTreeClassifier 的超參數也有 BaggingClassifier 的超參數
# 前者控制樹的生長, 後者控制集成本身

# 極端隨機樹
# 與隨機森林不同在於, 隨機森林是 找取每棵樹的隨機訓練集裡找出最好的特徵, 但極端隨機數是從隨機訓練集裡隨機找一個特徵
# 使得訓練起來比隨機森林快很多, 畢竟找最佳值是最耗時的工作
# 在 Scikit-Learn 的 ExtraTreesClassifier 可以創建一個極端隨機樹分類
# 另外, 很難直接判斷隨機森林和極端隨機樹哪個較優, 一樣使用交叉驗證或網格搜尋找出最佳值組合

# 特徵重要性
# 重要的特徵較可能出現在接近根節點的位置, 不重要的特徵通常出現在靠近葉節點或根本不出現
# 通過 features_importances 可以訪問到這個計算結果
# 查看以下的例子
from sklearn.datasets import load_iris
iris = load_iris()
# rnd_clf = RandomForestClassifier(n_estimators = 500, n_jobs = -1)
# rnd_clf.fit(iris["data"], iris["target"])
# for name, score in zip(iris["feature_names"], rnd_clf.feature_importances_):
#     print(name, score)
# sepal length (cm) 0.08928293287427996
# sepal width (cm) 0.02471385881545783
# petal length (cm) 0.4439832422323211
# petal width (cm) 0.44201996607794114
# 同樣的如果在MNIST 數據集上訓練一個隨機森林分類器, 然後繪製每個像素的重要性也可以得到一樣的結果
# 若想快速了解甚麼是真正重要的特徵, 隨機森林是一個非常快速的方式(特別是在執行特徵選擇的時候)


# 提升法
# 將多個弱學習器結合成一個強學習器的集成方式
# 總體來說, 提升法是循環訓練預測器, 每一次都對前一個預測做出改正
# 可用的提升法很多, 目前較流行的是 AdaBoost (自適應提升法)和 梯度提升

# AdaBoost
# 創建一個基礎分類器(例如: 決策樹), 用它對訓練集做預測, 然後對擬合不足的錯誤分類訓練實例增加權重, 不斷循環
# 這種技術有一個問題是, 無法併行(哪怕只是一小部分), 每次預測都要等上一級的回傳結果, 因此拓展沒這麼好
# Scikit-Learn 上的 AdaBoost
from sklearn.ensemble import AdaBoostClassifier
# ada_clf = AdaBoostClassifier(
#     DecisionTreeClassifier(max_depth = 2), n_estimators = 200, 
#     algorithm = "SAMME.R", learning_rate = 0.5
# )
# ada_clf.fit(X_train, y_train)
# 如果預測器可以估算類別概率, Scikit-Learn 會使用一種 SAMME 的變體(SAMME.R <- R 代表 Real),
# 它依賴的是類別概率而不是類別預測, 通常表現更好
# 如果 AdaBoost 集成 過度擬合訓練集, 可以嘗試減少估算器的數量或提高基礎估算器的正則化程度

# 梯度提升(Gradient Boosting)
# 與前者不同於, 並不是每次迭代調整權重, 而是讓新的預測器針對前一個預測器的殘差進行擬合
# 以下使用 決策樹回歸作為基礎預測器(使用自定義資料)
from sklearn.tree import DecisionTreeRegressor
import numpy as np
X = np.random.rand(100) + 1
y = np.random.randn(100) + 2 * X + X ** 2 + 1

tree_reg1 = DecisionTreeRegressor(max_depth = 1)
tree_reg1.fit(X[:, None], y.ravel())

y2 = y - tree_reg1.predict(X[:, None]) # <- 殘差(將原本的標籤 減去 預測標籤 所得到的差)
tree_reg2 = DecisionTreeRegressor(max_depth = 1)
tree_reg2.fit(X[:, None], y2.ravel())

y3 = y - tree_reg2.predict(X[:, None])
tree_reg3 = DecisionTreeRegressor(max_depth = 1)
tree_reg3.fit(X[:, None], y3.ravel())

X_new = np.linspace(0, 1, 100)
# 接者把所有樹的預測相加, 並對新實例進行預測
y_pred = sum(tree.predict(X_new[:, None]) for tree in (tree_reg1, tree_reg2, tree_reg3))

# 使用 Scikit-Learn 的 GradientBoostingRegressor 
from sklearn.ensemble import GradientBoostingRegressor
# gbrt = GradientBoostingRegressor(max_depth = 2, n_estimators = 3, learning_rate = 1.0)
# gbrt.fit(X[:, None], y.ravel())

# 另外再多一組例子
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse

X = X[:, None]
y = y.ravel()

X_train, X_val, y_train, y_val = tts(X, y)

gbrt = GradientBoostingRegressor(max_depth = 2, n_estimators = 120)
gbrt.fit(X_train, y_train)

errors = [mse(y_val, y_pred) for y_pred in gbrt.staged_predict(X_val)]
bst_n_estimators = np.argmin(errors)

gbrt_best = GradientBoostingRegressor(max_depth = 2, n_estimators = bst_n_estimators)
gbrt_best.fit(X_train, y_train)

y_pred = gbrt_best.predict(X_val)
# 事實上, 要使用早期停止法不一定要訓練大量的樹然後再回頭找最優, 可以直接提早停止訓練(warm_start = True)
# 以下的程式碼會在驗證誤差連續5次迭代未改善時, 會直接停止訓練
# gbrt_test = GradientBoostingRegressor(max_depth = 2, warm_start = True)

# min_val_error = float("inf")
# error_going_up = 0
# for n_estimators in range(1, 120):
#     gbrt_test.n_estimators = n_estimators
#     gbrt_test.fit(X_train, y_train)
#     y_pred = gbrt_test.predict(X_val)
#     val_error = mse(y_val, y_pred)

#     if val_error < min_val_error:
#         min_val_error = val_error
#         error_going_up = 0
#     else:
#         error_going_up += 1
#         if error_going_up == 5:
#             break