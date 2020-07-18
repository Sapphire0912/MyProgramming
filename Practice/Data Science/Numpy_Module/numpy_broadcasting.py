import numpy as np
# 陣列的計算: Broadcasting
# 在Python 的 list 只能和同樣為list資料類型的數據做運算
# 在Numpy 的 array 即使是空間維度不同的array也可以進行擴展做計算(但是長度要相同), 稱為Broadcasting
# a = np.array([0, 1, 2])
# b = np.array([5, 5, 5])
# print("a + b = ", a + b)
# print("a + 5 = ", a + 5) # 代表陣列的每個元素都加5

# M = np.ones((4, 3)) 
# print("M + a = \n", M + a)
# 一開始的a已經設定為3行, 也就是說要做運算的陣列也必須是3行結構; 
# 可以寫成(4, ) 讓程式去進行擴展猶如下面的例子

# 使用arange產生 直行(y)和橫列(x) 運算後所產生的陣列數會是 x * y
# a = np.arange(3)
# b = np.arange(4)[:, np.newaxis]
# print("a = ", a)
# print("b = ", b)
# print("a - b = ", a - b)

# Broadcasting 規則:
# 1. 若兩個陣列的維度不同, 則把較低維度的那個陣列使用最左邊的元素開始擴展
# 2. 若兩個陣列的維度不能互相符合, 則把為1的那個陣列擴展到符合另一個陣列(廣義上同第一點)
# 3. 若任意維度的大小不符合, 也沒有任何維度大小等於1, 則產生錯誤

# Broadcasting 實務:
# 陣列的置中, 二微陣列函數的繪製, 在往後的地方會討論