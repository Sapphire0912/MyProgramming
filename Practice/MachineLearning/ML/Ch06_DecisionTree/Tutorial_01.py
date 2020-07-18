# 決策樹
# 與SVM一樣, 決策樹也是多功能的機器學習演算法, 可以實現分類和回歸以及多輸出任務, 能夠擬合複雜數據集
# 決策樹也是隨機森林組成的基本部分

# 決策樹的訓練和可視化
# 先建構一棵決策樹
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier as DTC

iris = load_iris()
X = iris.data[:, 2:] # petal length and width
y = iris.target

tree_clf = DTC(max_depth = 2)
tree_clf.fit(X, y)

# 要將決策樹可視化, 使用 export_graphviz() 輸出一個圖形定義文件
# from sklearn.tree import export_graphviz 
# path = "C:\\Users\\kotori\\Desktop\\MyProgramming\\Practice\\ML\\Ch06_DecisionTree\\iris_tree.dot"
# export_graphviz(
#     tree_clf,
#     out_file = path,
#     feature_names = iris.feature_names[2:], 
#     class_names = iris.target_names,
#     rounded = True,
#     filled = True
# )

# 做出預測
# 決策樹的特質之一, 它需要的數據準備工作非常少, 特別完全不需要進行特徵縮放或集中
# Scikit-Learn 使用的是 CART 算法, 該算法僅生成二元樹

# 估算類別概率
# 決策樹一樣可以估算某個實例屬於特定類別 k 的機率
# print(tree_clf.predict_proba([[5, 1.5]])) # [[0.         0.90740741 0.09259259]]
# print(tree_clf.predict([[5, 1.5]])) # [1]
# 透過 iris_tree.dot 檔 可以得知預測類別為哪種鳶尾花

# CART 訓練法
# Scikit-Learn 使用的是分類與回歸樹來訓練決策樹; 假設 k 為單個特徵, t_k 為閾值
# CART分類的成本函數: J(k, t_k) = m_left * G_left / m + m_right * G_right / m
# 其中 G_left/right 代表 衡量左右子集的不純度, m_left/right 是左右子集的實例數量
# 接者, 使用相同的邏輯繼續分支子集, 直到達到最大深度(超參數 max_depth 控制)
# 當然也有其他的控制條件, 可以查找文檔
# CART 是一種貪婪算法, 會盡可能找出在每個階段的最佳解
# 理論上, 是在每個階段找出最佳解, 但是尋找最優樹是已知的 NP完全問題, 需要的時間複雜度為 O(exp(m))
# 也就是即使是很小的訓練集, 時間成本也相當高, 因此我們盡量接受一個不錯的解

# 計算複雜度
# 進行預測需要走訪整棵決策樹, 通常來說, 決策樹大致平衡, 因此走訪決策樹大約是 O(log_2(m))個節點,
# 而每個節點只需要檢查一個特徵值, 所以總體預測的複雜度 等於 走訪節點的複雜度
# 即使處理大型數據, 預測也很快

# 正則化超參數
# 決策樹極少對訓練數據做出假設, 不加以限制, 樹的結構將跟著訓練集變化, 且很可能過度擬合
# DecisionTreeClassifier 有一些其他的參數是可以限制樹的生長
# 例如: min_samples_split, min_samples_leaf, min_weight_fraction_leaf, max_leaf_nodes, max_features等等

# 回歸
# 決策樹回歸 Scikit-Learn DecisionTreeRegressor
# 書上寫的很精簡, 這裡用我自己自創的例子來做測試
from sklearn.tree import DecisionTreeRegressor as DTR
import numpy as np
import matplotlib.pyplot as plt

# rng = np.random.RandomState(42)
# X_data = rng.rand(200)
# y_data = rng.randn(200) + 2 * X_data + 1.3 * X_data ** 2

# X_new = np.linspace(0, 1, 100)

# tree_none = DTR()
# tree_leaf = DTR(min_samples_leaf = 10)

# tree_none.fit(X_data[:, None], y_data.ravel())
# tree_leaf.fit(X_data[:, None], y_data.ravel())

# y_pred_none = tree_none.predict(X_new[:, None])
# y_pred_leaf = tree_leaf.predict(X_new[:, None])

# fig, ax = plt.subplots(1, 2, figsize = (20, 10))
# ax[0].scatter(X_data, y_data)
# ax[1].scatter(X_data, y_data)
# ax[0].plot(X_new, y_pred_none, color = 'red', alpha = 0.6)
# ax[1].plot(X_new, y_pred_leaf, color = 'red', alpha = 0.6)

# ax[0].set_xlabel('X_data')
# ax[0].set_ylabel('y_pred')
# ax[1].set_xlabel('X_data')
# ax[1].set_ylabel('y_pred')
# ax[0].set_title("unlimited")
# ax[1].set_title("min_samples_leaf = 10")

# plt.show()

# 不穩定性
# 決策樹對於數據的旋轉敏感, 對於旋轉的數據集容易產生不必要的捲曲, 限制這種問題的方法之一是使用 PCA
# 換句話說, 決策樹主要問題是對 訓練數據中的小變化非常敏感, 從上面自創例子的視覺化執行結果可以知道
# 另外, 隨機森林通過對許多樹的預測進行平均, 限制這種不穩定性