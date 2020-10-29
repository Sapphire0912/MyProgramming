# 人工神經網路(Artificial Neural Networks, ANN)簡介
# 感知器(Perception)
# Scikit-Learn 提供的 單一LTU 的感知器
# import numpy as np
# from sklearn.datasets import load_iris
# from sklearn.linear_model import Perceptron
# iris = load_iris()
# X = iris.data[:, (2, 3)]
# y = (iris.target == 0).astype(np.int)
# per_clf = Perceptron(random_state = 42)
# per_clf.fit(X, y)

# y_pred = per_clf.predict([[2, 0.5]])
# 感知器 在 Scikit-Learn 裡面, 等同於 SGDClassifier(loss = "Perceptron", learning_rate = "cnostant", eta0 = 1, penalty = None)
# 另外, 感知器與邏輯回歸相反, 前者不輸出某個類的概率, 只能根據一個固定的閾值來做預測(這也是用邏輯回歸更好的原因)

# 多層感知器(Multi-Layer Perceptron, MLP) 和 反向傳播(Backpropagation, BP)
# MLP 常常被用來做分類, 每個輸出對應一個不同的二進制分類, 當每個分類是互斥的情況下, 輸出層通常被修改成一個共享的 softmax函數
# 此種方式訊號是單向流動的, 此架構是前饋神經網路(FNN)的一種
# (補充: ReLU 激活函數通常在 ANN 中工作的更好)
# 這部份建議看課本更詳細/或者找網路參考資料以及其他書


# 用 Tensorflow 的高級 API 來訓練 MLP