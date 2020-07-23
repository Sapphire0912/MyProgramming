# coding=utf8
# 處理衛星數據集並微調一個決策樹
from sklearn.datasets import make_moons
X, y = make_moons(n_samples = 10000, noise = 0.4)

