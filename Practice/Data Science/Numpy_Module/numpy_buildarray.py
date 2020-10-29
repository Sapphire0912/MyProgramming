import numpy as np

# 建立一個內容全為0, 長度為10的整數陣列
# intlist = np.zeros(10, dtype = int) # 若不加上dtype=int, 則資料類型會變成float64
# print(intlist)

# 建立一個內容全為1的3x5的浮點數陣列
# floatlist = np.ones((3,5), dtype = float)
# print(floatlist)

# 建立一個內容全為3.14的2x4陣列
# fulluse = np.full((2, 4), 3.14)
# print(fulluse)

# 建立一個內容0~20間隔為2的陣列 (類似內建的range()函數)
# even = np.arange(0, 20, 2)
# print(even)

# 建立一個內容只有5個值的陣列, 且值域為[0,1]
# space = np.linspace(0, 1, 5)
# print(space)

# 建立一個平均分布的3x3陣列, 且值為0~1之間的亂數值
# rand = np.random.random((3,3))
# print(rand)

# 建立一個3x3陣列, 內容為常態分析的亂數值, avg=2, SD=5(SD為標準差)
# normal = np.random.normal(2, 5, (3, 3))
# print(normal)

# 建立一個3x3, 內容介於0~10之間的整數亂數
# intrand = np.random.randint(0, 10, (3, 3))
# print(intrand)

# 建立一個4x4的單位矩陣(若要 3x3 則 把 4 改成 3 )
# matrix = np.eye(4)
# print(matrix)

# 建立一個3個整數的未初始化陣列, 這些值是原本就存在於記憶體中的值(程式執行到現在所被創建且未被刪除的值)
# noninit = np.empty(3)
# print(noninit)