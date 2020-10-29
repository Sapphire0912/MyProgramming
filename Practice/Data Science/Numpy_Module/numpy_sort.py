import numpy as np
# numpy裡面的排序,　default: np.sort為Quick Sort(Time: N logN)
x = np.array([2, 4, 3, 1, 5])
# print("np.sort(x): ", np.sort(x)) # 傳回排序後的陣列, 但不會改變原本的內容
# x.sort() # 會改變原本的陣列內容
# print("x: ", x)

# 另一種排序為np.argsort() 傳會被排序過後元素的索引值
i = np.argsort(x)
# print("index: ", i)

# 沿著行或列排序 增加axis參數即可
rand = np.random.RandomState(1)
array = rand.randint(0, 10, (4, 6))
print("Array: \n", array)
# print("row sorted: \n", np.sort(array, axis = 0)) # 行排序
# print("column sorted: \n", np.sort(array, axis = 1)) # 列排序

# 分區(Partitioning): 將陣列中最小的K個值放入左側 np.partition(array, K) # 
x = np.array([7, 2, 3, 1, 6, 5, 4])
# print(np.partition(x, 2)) # 排列順序隨意 (BTW: 只排列K個數值, 則被分開的數值順序隨意)
print(np.partition(array, 2, axis = 1)) # 每一列中的兩個最小值會被放在左側