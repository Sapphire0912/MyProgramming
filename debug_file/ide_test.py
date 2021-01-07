print("IDE is ok.")

# module test
import numpy
# a = numpy.arange(1, 10, 2)
# print(a)

from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
# print(X.shape, y.shape)
