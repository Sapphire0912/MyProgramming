import numpy as np
import pandas as pd
import numexpr as npr
import time as t

# PyData 堆疊的威力建立在 Numpy, Pandas 讓運算使用直覺的語法進入C的能力,
# Ex. Numpy vectorized, broadcasting 這些抽象概念非常有效率, 但是經常依賴中間暫存的物件上
# 造成運算時間以及記憶體使用的過度成本

# Pandas 包含了一些實驗工具允許直接存取C等級的速度運算, 而不會產生中間值陣列的配置
# eval(), query()函式, 屬於 Numexpr 套件
# Reference: https://gitnub.com/pydata/numexpr

# query(), eval() 複合敘述式
# Ex.
# mask = (x > 0.5) & (y < 0.5)
# 在 Numpy 執行 line 16 的複合敘述時, 會變成
# tmp1 = x > 0.5
# tmp2 = y < 0.5
# mask = tmp1 & tmp2
# 一般Numpy在計算複合敘述時, 會變得比較沒有效率, 因為在計算的每一個步驟都被暫存於記憶體中

# Numexpr 的優點, 不需要建立全部的暫存陣列, 因此相對於Numpy會更加有效率
# 使用 pandas.eval()函式使用字串敘述式高效率的計算使用了 DataFrame 的操作
nrows, ncols = 100000, 100
rng = np.random.RandomState(42)
df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows, ncols)) for i in range(4))
# 傳統的作法(若要算4個資料框的總和)
start = t.time()
df1 + df2 + df3 + df4
end = t.time()
# print("Traditional Cost time: %4f" % ((end - start) * 1000), "ms") # 157.656431 ms
# 使用pd.eval()計算
start = t.time()
pd.eval("df1 + df2 + df3 + df4")
end = t.time()
# print("pd.eval() Cost time: %4f" % ((end - start) * 1000), "ms") # 83.536625 ms
# 經過多次實驗結果, 大約快了50%, 而且使用比較少的記憶體
# print(np.allclose(df1 + df2 + df3 + df4, pd.eval("df1 + df2 + df3 + df4")))
# np.allclose() : 比較兩個物件是否相同, 默認誤差值1e-05

# 支援pd.eval()的操作: 算術, 比較, 位元, 物件屬性和索引
# 比較複雜的例如函式呼叫, 條件敘述, 迴圈等等複雜結構尚未實裝 可以使用原本的 Numexpr函式庫

# 使用DataFrame.eval()進行逐欄操作
df = pd.DataFrame(rng.rand(1000, 3), columns = ['A', 'B', 'C'])
# print(df.head())
result1 = (df['A'] + df['B']) / (df['C'] - 1)
result2 = pd.eval("(df.A + df.B) / (df.C - 1)")
result3 = df.eval('(A + B) / (C - 1)')
# np.allclose(result1, result2) # True
# np.allclose(result1, result3) # True
# np.allclose(result2, result3) # True

# DataFrame.eval()中的賦值運算
# 可以使用df.eval()來建立一個新的欄'D'
# print(df.eval('D = (A + B) / C', inplace = True))
# print(df.head())
# 用同樣的方式, 任何已經存在的欄也可以被修改
# print(df.eval('D = (A - B) / C', inplace = True))
# print(df.head())

# DataFrame.eval() 的本地端(局域)變數 -> local variables
# DataFrame.eval() 支援一個語法可以操作本地端的Python變數
column_mean = df.mean(1)
result1 = df['A'] + column_mean
result2 = df.eval('A + @column_mean')
# print(np.allclose(result1, result2))

# DataFrame.query() 方法
result1 = df[(df.A < 0.5) & (df.B < 0.5)]
# result2 = pd.eval('df[(df.A < 0.5) & (df.B < 0.5)]')
result2 = df.query('A < 0.5 and B < 0.5')
# print(np.allclose(result1, result2))
# line 73, 74: 可以得到相同的結果

Cmean = df['C'].mean()
result1 = df[(df.A < Cmean) & (df.B < Cmean)]
result2 = df.query('A < @Cmean and B < @Cmean')
# print(np.allclose(result1, result2))

# 效能: 在甚麼時候使用這些函式
# 有2個主要的考量點, 運算時間和記憶體的使用
# 記憶體使用 是最需要預測的考量點
# 如果暫時的DF 對於可用的記憶體比較起來是非常顯著的, 此時使用eval(), query()敘述是一個好主意
# 可以透過 df.values.nbytes 檢查陣列的大小

# 參考資料: http://pandas.pydata.org/pandas-docs/dev/enhancingperf.html
# Pandas 線上說明文件: http://pandas.pydata.org/
# 時間系列工具(Python for Data Analysis): http://bit.ly/python-for-data-analysis
# Pandas 在 Stack Overflow: https://stackoverflow.com/questions/tagged/pandas
# Pandas 在 PyVideo : https://pyvideo.org/search?q=pandas