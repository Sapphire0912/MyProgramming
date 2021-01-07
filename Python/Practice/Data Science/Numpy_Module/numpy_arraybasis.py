import numpy as np

# 陣列基礎包含: 屬性(attributes)、索引(index)、切片(split)、重塑(reshape)

# 先生成隨機整數亂數
np.random.seed(0) # 指定一個種子, 這個種子被執行時會產生一樣的亂數內容 
# x1 = np.random.randint(10, size = 6)
# x2 = np.random.randint(10, size = (3, 4)) # 3x4 二維陣列
# x3 = np.random.randint(10, size = (3, 4, 5)) # 3x4x5 三維陣列

# Attributes: 
# print("x3 ndim: ", x3.ndim) # 維度(幾維陣列)
# print("x3 shape: ", x3.shape) # 每一個維度的大小
# print("x3 size: ", x3.size)  # 整個陣列空間的總大小
# print("x3 dtype: ", x3.dtype) # 該陣列的資料型態
# print("x3 itemsize: ", x3.itemsize, "bytes") # 陣列每一個元素的大小
# print("nbytes: ", x3.nbytes, "bytes") # 陣列所有元素的大小(nbytes = itemsize*size)

# index:
# 和python原本的list索引操作相同 list[start:stop:step]

# split:
# 多維子陣列的切片(全部都和python的list操作相同) array[列/col/y軸,欄/行/row/x軸]
# print("Array x2: \n", x2)
# print("row = 3, col = 2 : \n", x2[:2, :3])
# print("x2[:3, ::2]: \n", x2[:3, ::2]) # 所有列的偶數欄
# print("反轉: \n", x2[::-1, ::-1]) # 所有行,所有列都反轉

# 差異性:(python list, numpy array)
# L = [1, 2, 3, 4, 5, 6]
# A = np.arange(1,7)
# # 原本的
# print("Org L: ", L)
# print("Org A: ", A)
# # 切片後, 並更改數值
# L2 = L[2:5]
# A2 = A[2:5]
# L2[1] = 0
# A2[1] = 0
# print("Last L: ", L)
# print("Last A: ", A)
# Result: python list不會因為切片更改數值後而變動原本的列表,則numpy array會

# 若在numpy array下, 不想因為更改切片的數值而動到原本的陣列可以使用copy()
# print("x2: \n", x2)
# x2_copy = x2[:2, :2].copy()
# print("x2_copy: \n", x2_copy)
# x2_copy[0, 0] = 99
# print("x2: \n", x2)
# print("x2_copy: \n", x2_copy)

# reshape: (兩種使用方法, 第二種方法並不會影響到原本的陣列數值)
# First:
# grid = np.arange(1, 10).reshape((3, 3)) # 將原本1x10變成3x3的陣列
# print("grid: \n", grid)
# second:
# x = np.array([1, 6, 9, 7])
# print("Org x: \n", x)
# print("Reshape x: \n", x.reshape((4, 1)))
# print("Reshape x: \n", x.reshape((2, 2)))
# print("newaxis x: \n", x[np.newaxis, :]) # x.reshape((1, 4))
# print("newaxis x: \n", x[:, np.newaxis]) # x.reshape((4, 1))

# 陣列的串接和分割
# method: np.concatenate([array1, array2, ...])
# x = np.array([3, 5, 7])
# y = np.array([2, 4, 6])
# z = np.array([1, 0, 9])
# print("x + y: \n", np.concatenate([x, y]))
# print("x + y + z: \n", np.concatenate([x, y, z]))
# 使用在二維陣列上
# grid = np.array([[1, 4, 7],[2, 5, 8]])
# print("grid + grid: \n", np.concatenate([grid, grid]))
# print("axis = 1: \n", np.concatenate([grid, grid], axis = 1))

# method: np.vstack(垂直堆疊), np.hstack(水平堆疊), np.dstack(高度堆疊) <- 三維堆疊
# x = np.array([3, 6, 9])
# y = np.array([[0], [100]])
# grid = np.array([[2, 5, 8], [1, 4, 7]])
# print("vertical: \n", np.vstack([x, grid]))
# print("horizontal: \n", np.hstack([grid, y]))

# 分割:
# method: np.split(), np.vsplit()(垂直切割), np.hsplit()(水平切割), np.dsplit() 
grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2]) # 第二列作切割(想成 y軸只要兩行)
left, right = np.hsplit(grid, [2]) # 第二行做切割(x軸只要兩行)
print(upper)
print(lower)
print(left)
print(right)