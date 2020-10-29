import numpy as np
import time as t
# 聚合操作

# 在陣列中求和(np.sum(array))
# L = np.random.random(100)
# print("sum(L) = ", sum(L))
# print("np.sum(L) = ", np.sum(L))
# 和python的sum函數達到相同的效果, 但是...
# Big_Data = np.random.random(1000000)
# start = t.time()
# pysum = sum(Big_Data)
# print("Py_sum Time : ", t.time() - start, " sec.")
# start = t.time()
# numpysum = np.sum(Big_Data)
# print("Numpy_sum Time : ", t.time() - start, "sec.")
# 在資料量非常龐大的時候, 效率很明顯就有很大的落差了, Numpy的效率至少快了40倍

# 求最大值,最小值
# print("Python min, max : ", min(Big_Data), " ", max(Big_Data))
# print("Numpy min, max: ", np.min(Big_Data), " ", np.max(Big_Data))
# 或者寫成 Big_Data.min(), Big_Data.max(), Big_Data.sum() ... etc.

# 多維度的聚合運算
# M = np.random.random((3, 4))
# default: M.sum() 會傳回所有值的運算結果
# 在裡面加上 axis 的參數 就可以傳回指定軸的值了
# print("每一行 : ", M.sum(axis = 0))
# print("每一列 : ", M.sum(axis = 1))

# 其他的聚合函式
array = np.random.randint(1, 50, (3, 5))
print("Array: \n", array)
print("求和: ", np.sum(array))
print("求積: ", np.prod(array))
print("求平均: ", np.mean(array))
print("求標準差: ", np.std(array))
print("求變異數: ", np.var(array))
print("最小值: ", np.min(array))
print("最大值: ", np.max(array))
print("最小值的索引: ", np.argmin(array))
print("最大值的索引: ", np.argmax(array))
print("求中位數: ", np.median(array))
print("排名統計: ", np.percentile(array, 25)) # 四分位差(25, 50, 75)
print("any, all: ", np.any(1), ", ", np.all(1))