#coding=utf8
# 導入 mnist 資料集
from sklearn.datasets import fetch_openml
mnist = fetch_openml("mnist_784")
X, y = mnist.data, mnist.target

testsize = int(y.shape[0] * 0.2)
X_train, X_test, y_train, y_test = X[:-testsize], X[-testsize:], y[:-testsize], y[-testsize:]

# import matplotlib as mpt
# import matplotlib.pyplot as plt
# test_digit = X[44500]
# test_digit = test_digit.reshape(28, 28)
# plt.imshow(test_digit, cmap = mpt.cm.binary, interpolation = 'nearest')
# plt.show()
