from sklearn.datasets import load_wine
wine = load_wine()
X, y = wine.data, wine.target

from sklearn.model_selection import train_test_split as tts
X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.25, train_size = 0.75, random_state = 5)

from sklearn.tree import DecisionTreeClassifier as DTC
model = DTC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score 
accuracy = round(accuracy_score(y_pred, y_test), 2)
# print(accuracy) # 0.91

q2 = [[1.51, 1.73, 1.98, 20.15, 85, 2.2, 1.92, .32, 1.48, 2.94, 1, 3.57, 172]]
a2 = model.predict(q2)
# print(a2) [1] <- C

q3 = [[14.23, 1.71, 2.43, 15.6, 127, 2.8, 3.06, .28, 2.29, 5.64, 1.04,  3.92, 1065]]
a3 = model.predict(q3)
# print(a3) [0] <- C

q4 = [[13.71, 5.65, 2.45, 20.5, 95, 1.68, .61, .52, 1.06, 7.7, .64, 1.74, 720]]
a4 = model.predict(q4)
# print(a4) [2] <- B