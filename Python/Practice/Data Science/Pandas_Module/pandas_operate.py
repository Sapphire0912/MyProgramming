import pandas as pd
import numpy as np
# Pandas 是設計來和 Numpy 一起工作的，所以任何 Numpy 的 ufuncs 都可以在 pandas 操作

# ufuncs 索引的保存
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns = ['A', 'B', 'C', 'D'])
# print("ser: \n", ser)
# print("df: \n", df)
# print(np.exp(ser))
# print(np.sin(df * np.pi / 4))
# 經過計算後也不影響原本的值

# ufuncs 索引對齊
# Pandas 在運算時, 若遇到不完整的資料會用NaN來補齊

# 在Series中對齊索引
area = pd.Series({'Alaska':1723337, 'Texas':695662, 'California':423967}, name = 'area')
population = pd.Series({'California':38332521, 'Texas':26448193, 'New York':19651127}, name = 'population')
# print(population / area)
# 此輸出結果, 是兩個陣列的聯集資料(Python集合運算), 若遇到有缺失資料默認以NaN代替

A = pd.Series([2, 4, 6], index = [0, 1, 2])
B = pd.Series([1, 3, 5], index = [1, 2 ,3])
# print(A + B)
# 如果不想要缺失值(NaN) 則可以用A.add(B)的函式
# print(A.add(B, fill_value = 0)) # 代表缺失值(NaN)以0代替

# 在DataFrame中索引對齊
A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns = list('AB'))
B = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns = list('BAC'))

# print(A)
# print(B)
# print(A + B) # 輸出為3*3的矩陣, 但是只有2*2的範圍有值

fill = A.stack().mean() # 先堆疊所有的列再計算平均值 ((1+11+5+1)/4)
# print(A.add(B, fill_value = fill))

# line 38 補充: (URL: https://www.itread01.com/content/1545044287.html)
# 1.stack：將資料的列“旋轉”為行
# 2.unstack：將資料的行“旋轉”為列
# 3.stack和unstack預設操作為最內層
# 4.stack和unstack預設旋轉軸的級別將會成果結果中的最低級別（最內層）
# 5.stack和unstack為一組逆運算操作

# python 運算子 對應Pandas的方法
# (+, add())、(-, sub(), subtract())、(*, mul(), multiply())、(/, truediv(), div(), divide())
# (//, floordiv())、(%, mod())、(**, pow())

# 在DataFrame和Series之間操作
x = rng.randint(10, size = (3, 4))
# print("x: \n", x)
# print(x - x[0])
# 這種操作和在 Numpy 的 Broadcasting 一樣

df = pd.DataFrame(x, columns = list('QRST'))
print(df - df.iloc[0])
print(df.subtract(df['R'], axis = 0)) # 減去每一列(一定要加上axis, 不然每一個值都會是缺失值)
halfrow = df.iloc[0, ::2]
print(df.sub(halfrow)) # halfrow裡面由於沒有RT行, 所以無法取值則給予NaN
