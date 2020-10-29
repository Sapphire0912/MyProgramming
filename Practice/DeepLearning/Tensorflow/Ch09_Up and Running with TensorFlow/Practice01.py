# 使用小批量梯度下降法來實現邏輯回歸, 用月亮數據集來訓練和評估
# 1. 定義 logistic_regression() 函數, 且可以被重複使用
# 2. 訓練過程中, 定期通過 Saver 把檢查點保存起來, 並將最後的模型保存起來
# 3. 訓練如果被終止, 則恢復之前的模型
# 4. 用合理的作用域來定義圖, 使在 Tensorboard 看起來漂亮
# 5. 添加彙總訊息以在 Tensorboard 可視化學習曲線
# 6. 調整學習速率和批次大小的超參數, 並查看學習曲線的形狀

from sklearn.datasets import make_moons
samples = 1000
X, y = make_moons(n_samples = samples, noise = 0.1, random_state = 42)
# print(X.shape, y.shape) # (1000, 2) (1000,)
# print(X, y) # the labels of y have two types with 0 and 1.

import matplotlib.pyplot as plt
# plt.plot(X[y == 1, 0], X[y == 1, 1], "go", label = "Positive")
# plt.plot(X[y == 0, 0], X[y == 0, 1], "r^", label = "Negative")
# plt.legend()
# plt.show()

import numpy as np
X_bias = np.c_[np.ones((samples, 1)), X]
y_vector = y.reshape(-1, 1)

# 把資料分成訓練集和測試集(用自定義的函數)
def tts(X_data, y_data, ratio = 0.2):
    size = int(X_data.shape[0] * ratio)
    X_train = X_data[:-size]
    X_test = X_data[-size:]
    y_train = y_data[:-size]
    y_test = y_data[-size:]
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = tts(X_bias, y_vector, ratio = 0.2)

# 自己選擇訓練批量大小(裡面採用隨機選擇資料的方式)
def random_batch(X_train, y_train, batch_size):
    rnd_indices = np.random.randint(0, len(X_train), batch_size)
    X_batch = X_train[rnd_indices]
    y_batch = y_train[rnd_indices]
    return X_batch, y_batch

X_batch, y_batch = random_batch(X_train, y_train, 5)

