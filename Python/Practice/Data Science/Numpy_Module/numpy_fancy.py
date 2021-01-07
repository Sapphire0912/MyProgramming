import numpy as np
# fancy 索引
# 設定隨機亂數的定值, 使接下來的程式碼使用variable.random會產生一樣的亂數
rand = np.random.RandomState(1) 
x = rand.randint(100, size = 10)
# print("x = ", x)

# 取得元素的方式: x[1],x[3]...etc.; 另一種是(如下)
# index = [3, 7, 4]
# print("x[index] = ", x[index])
# 使用fancy索引所產生結果的陣列形狀, 反映到了索引陣列的形狀
# index = np.array([[3, 7], [4, 5]])
# print("x[index] = \n", x[index])

# fancy index 也可以運用在多維陣列
x = np.arange(12).reshape((3, 4))
# print("x = \n", x)
# row = np.array([0, 1, 2])
# col = np.array([2, 1, 3])
# print("x[row, col] = \n", x[row, col]) #相當於x[0,2],x[1,1],x[2,3]
# print("x[row[:, np.newaxis], col] = \n", x[row[:, np.newaxis], col])
# 上面的代碼相當於 [0][2,1,3],[1][2,1,3],[2][2,1,3]
# np.newaxis 使得row原本為[0,1,2] 變成 [[0],[1],[2]]
# Important: 使用fancy index傳回的值都是 索引broadcasting後的形狀, 而不是被索引陣列的形狀

# fancy index 修改陣列值
s = np.arange(10)
i = np.array([2, 1, 8, 4])
s[i] = 100
print("s = ", s) # 使s[2],s[1],s[8],s[4]的值都被改成100
# 但是不建議用這種方式做運算, 容易造成不是想要得到的結果
# 若要重複計算可以使用at()方法 at(array, index, numbers)
o = np.zeros(10)
i = np.array([2, 3, 4, 3, 4, 2, 3])
np.add.at(o, i, 1) # 其中o[2],o[3],o[4]分別累加了numbers
print("o = ", o) 