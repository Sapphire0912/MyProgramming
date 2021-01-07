import numpy as np
# 比較運算子(可以運用在多維陣列)
x = np.array([1, 2, 3, 4, 5])
# print("x < 3 : ", np.less(x, 3))
# print("x > 3 : ", np.greater(x, 3))
# print("x <= 3 : ", np.less_equal(x, 3))
# print("x >= 3 : ", np.greater_equal(x, 3))
# print("x == 3 : ", np.equal(x, 3))
# print("x != 3 : ", np.not_equal(x, 3))

# bool 陣列
# 計算數目數量
array = np.random.randint(1, 20, (4, 3))
# print("Array : \n", array)
# 計算大於10的數目有幾個
# print("{} numbers greater than ten.".format(np.count_nonzero(array > 10)))
# print("{} numbers greater than ten.".format(np.sum(array > 10))) # True當成1, False當成0

# 計算每一列的數值有多少ㄍㄧ有多少個小於7
# print("{} numbers less then six.".format(np.sum(array < 7, axis = 1)))
# 若要判斷所有陣列裡面的值可以使用np.any(condition[, axis]), np.all(condition[, axis])

# 布林運算子
# syntax: & np.bitwise_and, | np.bitwise_or, ^ np.bitwise_xor, ~ np.bitwise_not

# 布林陣列當遮罩
a = np.random.randint(1, 40, (3, 6))
print("a : \n", a)
b = a[a < 12] # 可以利用判斷式的方式來擷取陣列
print("Mask b: ", b)