import numpy as np
import pandas as pd
# 資料集的合併 concat and append 方法

def make_df(cols, ind):
    data = {c : [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)

df = make_df('ABC', range(3))
# print(df)

# Repeat: Numpy arrays 的串接
# np.concatenate([array1[, array2 ... etc]])
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
# print(np.concatenate([x, y, z]))
a = [[1, 2], [3, 4]]
# print(np.concatenate([a, a], axis = 1)) # [[1, 2, 1, 2], [3, 4, 3, 4]] 1('col') -> 新增行
# print(np.concatenate([a, a], axis = 0)) # [[1, 2], [3, 4], [1, 2], [3, 4]] 0(row) -> 新增列


# 使用 pd.concat() 進行簡單的串接
# Parameter:
# pd.concat(objs, join = 'outer', join_axes = None, ignore_index = False, 
#           keys = None, levels = None, verify_integrity = False, copy = True)

# pd.concat() 可以使用在Series, DataFrame的串接上, 像是np.concatenate()單純的串接
ser1 = pd.Series(['A', 'B', 'C'], index = [1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index = [4, 5, 6])
# print(pd.concat([ser1, ser2]))
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
# print("DF1: \n", df1)
# print("DF2: \n", df2)
# print("pd.concat([df1, df2]): \n", pd.concat([df1, df2]))
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
# print("DF3: \n", df3)
# print("DF4: \n", df4)
# print("pd.concat([df3, df4], axis = 'col'): \n", pd.concat([df3, df4], axis = 1))

# 重複的索引
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index # 讓 y 索引和 x 重複
# print(pd.concat([x, y])) # 輸出上是沒有問題, 但不是我們想要的結果
# 把重複的索引當成是錯誤(異常)
# try:
#     pd.concat([x, y], verify_integrity = True) # verify_integrity 參數設定為 True
# except ValueError as e:
#     print(e) # Indexes have overlapping values: Int64Index([0, 1], dtype='int64')

# 忽略索引
# print(pd.concat([x, y], ignore_index = True)) # 索引使用新的Series的整數索引
# 加上多重索引鍵
# print(pd.concat([x, y], keys = ['x', 'y'])) # 替資料索引指定一個標籤, 則會產生階層式索引

# 使用 join, join_axes 參數進行串接
df5 = make_df('ABC', [1, 2])
df6 = make_df('CDE', [3, 4])
# print("DF5: \n", df5)
# print("DF6: \n", df6)
# print(pd.concat([df5, df6])) # 此種做法會有NaN值的產生
# print(pd.concat([df5, df6], join = 'inner')) # inner 交集, (default: outer聯集)
# print(pd.concat([df5, df6], join_axes = [df5.columns])) # 行合併 (df.index 列合併但需要索引值)

# Append() 方法
# df1.append(df2) 但是若資料量龐大會影響效率

# Reference: http://pandas.pydata.org/pandas-docs/stable/merging.html
