# coding=utf8
# 處理衛星數據集並微調一個決策樹

import numpy as np
from sklearn.datasets import make_moons
X, y = make_moons(n_samples = 10000, noise = 0.4)
# print(X.shape, y.shape) # (10000, 2) (10000, )

from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.model_selection import train_test_split as tts
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.2)
param_grid = [
    {'max_leaf_nodes': [3, 10, 18, 25, 30]}
]
dtc = DTC()
grid_search = GridSearchCV(dtc, param_grid, cv = 5)
grid_search.fit(X_train, y_train)
# print(grid_search.best_params_) # {'max_leaf_nodes': 18}
# print(grid_search.best_estimator_) # DecisionTreeClassifier(max_leaf_nodes=18)

best_estimator = grid_search.best_estimator_
best_estimator.fit(X_train, y_train)
y_pred = best_estimator.predict(X_test)
print("Accuracy: ", accuracy_score(y_pred, y_test)) # Accuracy:  0.8635