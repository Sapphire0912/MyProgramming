# ufuncs: universal functions 讓numpy創建出來的值以向量化的方式操作
import numpy as np

# numpy裡面的運算
x = np.arange(4)
# print("x = ", x);
# print("x + 5 = ", x + 5)
# print("x - 3 = ", x - 3)
# print("x * 4 = ", x * 4)
# print("x / 2 = ", x / 2)
# print("x // 2 = ", x // 2)
# print("x ** 3 = ", x ** 3)
# print("(x + 5) ^ 2 = ", (x + 5) ** 2)
# 對於一個向量化的資料可以直接做運算子的算術(同R語言), 在python裡面要使用迴圈迭代列表每一個值才有辦法計算出來
# 不侷限於基本的算術, 利用函數或方程式也有辦法直接計算出來

# 若不使用+ - * / 等運算符號, 在numpy有相對應的ufuncs的函數
# print("x + 7 = ", np.add(x, 7))
# print("x - 4 = ", np.subtract(x, 4))
# print("x * 6 = ", np.multiply(x, 6))
# print("- x = ", np.negative(x))
# print("x / 3 = ", np.divide(x, 3))
# print("x ** 4 = ", np.power(x, 4))
# print("x // 2 = ", np.floor_divide(x, 2))
# print("x % 2 = ", np.mod(x, 2))

# 絕對值(absolute)
y = np.array([3 - 4j, 2 + 3j, 12 - 5j, 0 + 1j])
# print("|x| = ", abs(x))
# print("|x| = ", np.abs(x))
# print("|y| = ", np.absolute(y)) # 即使是複數也可以求其值
# 上述三種呼叫方式皆可以使用絕對值函數

# 三角函數(trigonometric functions)
theta = np.linspace(0, np.pi, 3) # 0, 90, 180 度
# print("theta = ", theta)
# print("sin(theta) = ", np.sin(theta))
# print("cos(theta) = ", np.cos(theta))
# print("tan(theta) = ", np.tan(theta))

# 反三角函數也可以使用
z = [-1, 0, 1]
# print("z = ", z)
# print("arcsin(z) = ", np.arcsin(z))
# print("arccos(z) = ", np.arccos(z))
# print("arctan(z) = ", np.arctan(z))

# 指數和對數(power and log)
a = [1, 2, 4, 10]
# print("a = ", a)
# print("ln(a) = ", np.log(a)) # 自然對數
# print("log2(a) = ", np.log2(a)) # 以2為底
# print("log10(a) = ", np.log10(a)) # 以10為底
p = [2, 3, 5]
# print("p = ", p)
# print("e^p = ", np.exp(p))
# print("2^p = ", np.exp2(p))
# print("3^p = ", np.power(3, p))

# 若在給予的資料值特別小的時候, 有些函式可以提供精確的數值
b = [0, 0.1, 0.01, 0.001]
# print("exp(b) - 1 = ", np.expm1(b)) # exp() minus 1 <- expm1
# print("log(1+x) = ", np.log1p(b))  # log(1 plus x) <- log1p 

# 進階的ufuncs
# 1. 設定輸出
# x = np.arange(5)
# y = np.empty(5)
# np.multiply(x, 10, out = y)
# print(y)
# i = np.zeros(10)
# np.power(2, x, out = i[::2])
# print(i)
# 使用out方式可以節省記憶體空間

# 2. 聚合
x = np.arange(1, 6)
sum = np.add.reduce(x) # 可以 計算 x 的總和
multi = np.multiply.reduce(x) # 可以計算 x 的乘積
print("Total = ", sum) 
print("Product = ", multi)
# 如果要儲存中間運算的結果可以使用(accumulate)
print("Operator + : ", np.add.accumulate(x))
print("Operator x : ", np.multiply.accumulate(x))

# 3. 外積
x = np.arange(1, 6)
dot = np.multiply.outer(x, x)
print("Dot = ", dot)

# reference: http://www.numpy.org // http://www.scipy.org