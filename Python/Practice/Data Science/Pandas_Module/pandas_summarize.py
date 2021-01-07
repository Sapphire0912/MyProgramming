import pandas as pd
import numpy as np
# 聚合計算和分組
# Pandas 聚合計算, 類似 Numpy 的簡單運算到以 groupby 概念的複雜運算
# 介紹 Seaborn 套件(http://seaborn.pydata.org) 行星資料
import seaborn as sns
planets = sns.load_dataset('planets')

# Pandas 中簡單的聚合運算
# Series下的聚合計算(和Numpy一樣)
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
# print(ser.sum())  # 求總和
# print(ser.mean()) # 求平均

# 在DataFrame下, 聚合計算會傳回每一行的結果
df = pd.DataFrame({'A':rng.rand(5), 'B':rng.rand(5)})
# print(df)
# print(df.mean()) # 預設axis = 0(rows) 每一行的結果
# print(df.mean(axis = 1)) # 每一列的結果(axis = 'columns')
# Pandas 的聚合計算和之前Numpy的聚合運算相同, 但是還有一個方便的方法 describe()

# describe()可以針對每一行進行幾種常見的聚合運算, 並以分列的方式傳回結果
# 以行星資料來測試
# print(planets.dropna().describe())
# 資料裡若有一NaN值則那一行就會被丟棄

# Pandas 聚合的常用方法
# count(): 計算資料項目的總數, first()/last(): 第一個/最後一個的資料項目
# mean()/median(): 平均數/中位數, min()/max(): 最小值/最大值
# std()/var(): 標準差/變異數, mad(): 平均絕對差, prod()/sum(): 所有資料項的積/和

# groupby 操作: 更有效率對於資料子集合進行聚合運算
# Groupby的組成: Split-Apply-Combine
# split: 依照相同的鍵值做切割重組一個dataframe
# apply: 在一個特定的分組計算某一種函數(通常是聚合計算, 轉換, 過濾)
# combine: 合併之前的運算結果, 變成一個輸出的陣列
# Ex.
df1 = pd.DataFrame({'key':['A', 'B', 'C', 'A', 'B', 'C'], 'data':range(6)}, columns = ['key', 'data'])
# print(df1)
# print(df1.groupby('key'))
# line 41: 
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001C32BB9DB00>

# 傳回是一個DataFrameGroupBy物件。在尚未設定聚合運算前, 它並不會執行真正的計算, 稱為惰性計算(lazy evaluation)
# 為了產生結果, 也就是執行groupby後面的apply-combine過程, 必須加上一個函數
# print(df1.groupby('key').sum())
# line 47:
#      data
# key
# A       3
# B       5
# C       7

# GroupBy物件
# 可以把GroupBy物件當成一個DataFrame的collection
# 聚合運算(aggregate), 過濾(filter), 轉換(transform), 套用(apply)是GroupBy重要的操作

# 欄索引(行標籤): 傳回值是一個修改過的groupby物件
# print(planets.groupby('method')) # 利用'method'標籤將相同性質的資料分組
# line 60: (每次執行都會在記憶體不同位置)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000025F1080A860>

# print(planets.groupby('method')['orbital_period']) # 在以分好組的資料, 取'orbital_period'
# line 64: (每次執行都會在記憶體不同位置)
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001BE35B16C88>

# print(planets.groupby('method')['orbital_period'].median()) # 取中位數(此時GroupBy物件才開始被計算)
# method
# Astrometry                         631.180000
# Eclipse Timing Variations         4343.500000
# Imaging                          27500.000000
# Microlensing                      3300.000000
# Orbital Brightness Modulation        0.342887
# Pulsar Timing                       66.541900
# Pulsation Timing Variations       1170.000000
# Radial Velocity                    360.200000
# Transit                              5.714932
# Transit Timing Variations           57.011000
# Name: orbital_period, dtype: float64

# 在群組中進行迭代: GroupBy物件支援直接在群組中迭代, 並把每一個群組的Series, DataFrame傳回
# for (method, group) in planets.groupby('method'):
#     print("{0:30s} shape = {1}".format(method, group.shape))
    # 格式化字符串{0}{1} 數字代表位置(格式化字符串可以使用位置, 關鍵字的方式傳入)
# 雖然內建的apply的功能會比較快, 但是這麼做操作彈性大

# 分派方法: 透過 Python 類別的分派方法 (Question Python 分派方法) <- skip
# print(planets.groupby('method')['year'].describe())

# 聚合計算(aggregate()), 過濾(filter()), 轉換(transform()), 套用(apply())
# 建立一個新的資料框
rng1 = np.random.RandomState(0)
df2 = pd.DataFrame({'key':['A', 'B', 'C', 'A', 'B', 'C'], 'data1':range(6),
                    'data2':rng1.randint(0, 10, 6)}, columns = ['key', 'data1', 'data2'])
# print(df2)

# 聚合計算(aggregate())
# print(df2.groupby('key').aggregate(['min', np.median, 'max'])) # 使用一個列表[函數1, ... etc.]
# print(df2.groupby('key').aggregate({'data1':'std', 'data2':'var'})) # 使用字典方式{行標籤:目標函數}

# 過濾(filter(target function))
# def filter_func(x):
#     return x['data2'].std() > 4
# print(df2.groupby('key').filter(filter_func))
# filter(function) 把資料傳給function並由function傳回一個布林值; function裡面放的是過濾條件

# 轉換(transform())
# print(df2.groupby('key').transform(lambda x: x - x.mean()))
# transform(function) 把資料傳給function, 並計算出值; 最後在用與輸入資料一樣的格式輸出結果

# apply(): 可以套用任何一個函式到群組結果; 輸入是一個DataFrame, 傳回一個Pandas物件, 合併後調整成適合輸出的型態
# def norm_by_data2(x):
#     # x is a DataFrame in the group
#     x['data1'] /= x['data2'].sum()
#     return x
# print(df2.groupby('key').apply(norm_by_data2)) # 被分好組的資料, 利用函數來計算出結果(其函數可以自定義)

# 指定分割鍵
# 做為分組鍵的 list, array, 序列數, index(但要符合dataframe的長度)
# L = [0, 1, 0, 1, 2, 0]
# print(df2.groupby(L).sum()) # 索引值 0,2,5一組; 1,3一組; 4一組 
# print(df2.groupby(df2['key']).sum()) # 和 df2.groupby('key').sum() 相同

# 利用 字典/序列 做為對應索引到群組
df3 = df2.set_index('key')
mapping = {'A':'vowel', 'B':'consonant', 'C':'consonant'}
# print(df3.groupby(mapping).sum()) # B,C 一組; A一組

# 任意Python函式
# print(df3.groupby(str.lower).mean()) # 按照小寫字母相等來分組
# 有效鍵的list
# print(df3.groupby([str.lower, mapping]).sum()) # 只要是可以使用的鍵, 就可以透過多索引合併到群組

# Example:
# 每10年中, 所發現新行星的方法
decade = 10 * (planets['year'] // 10) # 僅有年份的資料
decade = decade.astype(str) + 's'  # 轉換數據類型為str, 並在結尾+s
decade.name = 'decade' # 將 decade(DataFrame) 的名稱改為 'decade' (原本是'year')
print(planets.groupby(['method', decade])['number'].sum().unstack().fillna(0))
# line 140:
# decade                         1980s  1990s  2000s  2010s
# method
# Astrometry                       0.0    0.0    0.0    2.0
# Eclipse Timing Variations        0.0    0.0    5.0   10.0
# Imaging                          0.0    0.0   29.0   21.0
# Microlensing                     0.0    0.0   12.0   15.0
# Orbital Brightness Modulation    0.0    0.0    0.0    5.0
# Pulsar Timing                    0.0    9.0    1.0    1.0
# Pulsation Timing Variations      0.0    0.0    1.0    0.0
# Radial Velocity                  1.0   52.0  475.0  424.0
# Transit                          0.0    0.0   64.0  712.0
# Transit Timing Variations        0.0    0.0    0.0    9.0
# 將行星資料根據 'method'行 和 decade的排序 來進行分組; 取出'行標籤'為number的那行並計算總和;
# 將資料旋轉為列, 把NaN值填滿, 填為0