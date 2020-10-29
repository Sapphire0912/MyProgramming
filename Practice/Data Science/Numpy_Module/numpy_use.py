import numpy as np
# numpy裡面的操作是一個向量化的操作
# 在 python 建立的列表 列表裡面的數值可以為任何類型(class = list)
# 在 numpy 創建的列表 列表裡面的數值必須全部都相同(class = numpy.ndarray)

# Python 建立 list 
# L = [1, 4, 2, 5, 3]
# print(type(L)) 
# class is list

# np.array 建立 list 
# print(type(np.array([1, 4, 2, 5, 3]))) 
# class = numpy.ndarray

# 使用巢狀list產生多維陣列
l = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(l)

# Numpy 限制列表裡面的數值必須為相同型態。如果型態不同，Numpy會嘗試自動轉換為其他型態
print(np.array([3.14, 4, 2, 3]))
# executed: [3.14 4. 2. 3. ] 全部都為float的類型且為(class = numpy.float64)
for i in np.array([3.14, 4, 2, 3]):
    print(type(i), end = " ")

# 如果要明確的設定資料型態，可以使用dtype關鍵字
print(np.array([3.14, 6, 7, 0], dtype = 'float32'))
for i in np.array([3.14, 6, 7, 0], dtype = 'float32'):
    print(type(i), end = " ")