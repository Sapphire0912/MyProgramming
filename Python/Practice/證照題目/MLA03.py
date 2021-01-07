from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
print(iris)


from sklearn.model_selection import train_test_split as tts
X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.4, random_state = 1)

from sklearn.neighbors import KNeighborsClassifier as knn
model = knn(n_neighbors = 3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = round(accuracy_score(y_test, y_pred), 4)
# print(accuracy) # 0.9833

# ['setosa', 'versicolor', 'virginica'] <- [0, 1, 2]
q10 = [[5, 2.9, 1, 0.2]]
a10 = model.predict(q10)
# print(a10) <- 'setosa' B

q11 = [[5.7, 2.8, 4.5, 1.2]]
a11 = model.predict(q11)
# print(a11) <- 'versicolor' C

q12 = [[7.7, 3.8, 6.7, 2.1]]
a12 = model.predict(q12)
# print(a12) <- 'virginica' B