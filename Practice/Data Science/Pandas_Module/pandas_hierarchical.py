import pandas as pd
import numpy as np
# 階層式索引(Hierarchical Indexing)
# Meaning: 一維的Series中透過使用多重索引去表示二維的資料
# 廣義上來說 每一層額外的層(Series)都可以透過多重索引進而顯示多維的資料

# 1個多重索引的Series
# 不好的方式:
index = [('California', 2000), ('California', 2010), 
         ('New York', 2000), ('New York', 2010), 
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index = index)

# print("pop:")
# print(pop)
# 但如果要從裡面取出2010年的所有資料, 會需要執行很多麻煩(可能更慢)的整合工作
# print("Summary:")
# print(pop[[i for i in pop.index if i[1] == 2010]])
# 確實可以產生結果, 但是對於更大的Data則很沒有效率

# 比較好的方式:
# Pandas MultiIndex
# 以 Tuple 為基礎的索引, 是多重索引的退化版; Pandas MultiIndex 提供了良好的運算型態
index = pd.MultiIndex.from_tuples(index)
# print(index, "\n", index.levels, "\n", index.labels)
# line 28:(O/P)
# MultiIndex([('California', 2000),
#             ('California', 2010),
#             (  'New York', 2000),
#             (  'New York', 2010),
#             (     'Texas', 2000),
#             (     'Texas', 2010)],
#            )
#  [['California', 'New York', 'Texas'], [2000, 2010]]
#  [[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]]

# 對已經排好的序列, 將它重新排序為符合index的排序方式: 使用reindex(arrange method)
pop = pop.reindex(index) # 將索引值重新排序, 符合index的排列方式
# print(pop)
# line 42: (O/P)
# California  2000    33871648
#             2010    37253956
# New York    2000    18976457
#             2010    19378102
# Texas       2000    20851820
#             2010    25145561

# 一樣, 若要取得2010年的所有資料
# print(pop[:, 2010]) 

# 多重索引當成是額外的維度
pop_df = pop.unstack() # 把多重索引(有重複的索引)變成列的標籤(資料旋轉為列)
# print(pop_df) 
# line 56: (O/P)
#                 2000      2010
# California  33871648  37253956
# New York    18976457  19378102
# Texas       20851820  25145561

# stack() 是相反的操作(資料旋轉為行) (O/P 同 line 42) 

# 若在新增每一洲每一年的18歲以下的人口統計資料, 使用MultiIndex 新增另一行資料是非常容易的
pop_df = pd.DataFrame({'total' : pop, 'under18' : [9267089, 9284094, 4687374, 4318033, 5906301, 6879014]})
# print(pop_df)
# line 67 (O/P) (資料使用原始資料pop, 也可以得到相同的結果)
#                     total  under18
# California 2000  33871648  9267089
#            2010  37253956  9284094
# New York   2000  18976457  4687374
#            2010  19378102  4318033
# Texas      2000  20851820  5906301
#            2010  25145561  6879014

# 計算以年度區分低於18歲人口比例 (ufuncs 可以在階層式索引下操作非常好)
f_u18 = pop_df['under18'] / pop_df['total']
# print(f_u18.unstack())
# line 79 (O/P)
#                 2000      2010
# California  0.273594  0.249211
# New York    0.247010  0.222831
# Texas       0.283251  0.273568

# MultiIndex 建立的方法(p134)
# 建立一個多索引的Series或是DataFrame最直接的方式, 傳遞1個或以上的多索引陣列的list當成建構子
df = pd.DataFrame(np.random.rand(4, 2), index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]], 
                  columns = ['data1', 'data2'])
# print(df)
# line 90 (O/P)
#         data1     data2
# a 1  0.053957  0.396452
#   2  0.388243  0.757625
# b 1  0.196178  0.779305
#   2  0.429974  0.648855

# 同樣, 如果使用一個正確的Tuple作為鍵的字典, Pandas會自動識別出來, (default: MultiIndex 建立)
data = {('California', 2000) : 33871648, ('California', 2010) : 37253956, 
         ('New York', 2000) : 18976457, ('New York', 2010) : 19378102,
         ('Texas', 2000) : 20851820, ('Texas', 2010) : 25145561}
# print(pd.Series(data)) # O/P 同 line 42
# 有時候明確的建立會很有用

# 明確指定MultiIndex建構子
# s = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
# t = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
# d = pd.MultiIndex.from_product([['a', 'b'], [1, 2]]) # 使用笛卡兒積
# 或者可以使用levels, labels來建立, line 37, 38 的格式
# 上述這幾種方式得到的結果都相同

# 多重索引的階層名稱
# 使用names參數在建構前新增, 或者建構後使用index.names的方式
# 這裡使用建構後的pop
pop.index.names = ['State', 'Year']
# print(pop)
# line 116 (O/P)
# State       Year
# California  2000    33871648
#             2010    37253956
# New York    2000    18976457
#             2010    19378102
# Texas       2000    20851820
#             2010    25145561
# dtype: int64

# 行的 MultiIndex
index2 = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names = ['Year', 'Visit'])
columns2 = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], 
                                         names = ['Subject', 'Type'])
# 新增一些資料
# round(x[,n]): 將x四捨五入取到小數第n位
# randn: 常態分布, 以0為平均值, 1為標準差; 記為N(0, 1) rand normal -> normal(預設為avg=0, SD=1)
data2 = np.round(np.random.randn(4, 6), 1) # 相當於np.round(np.random.normal(0, 1, (4, 6)), 1)
data2[:, ::2] *= 10 # 每一列都取, 每隔兩行取一個
data2 += 37

# 建立DataFrame
health_data = pd.DataFrame(data2, index = index2, columns = columns2)
# print(health_data)
# print(health_data.unstack().iloc[0]) # 取得2013年的資料
# print(health_data['Guido']) # 取得名字為Guido的資料

# MultiIndex的索引和切片
# 多重索引的Series
# print(pop['California', 2000]) # 藉由多個名詞存取單一元素
# print(pop['California']) # 也支援單一索引
# print(pop.loc['California':'New York']) # 只要MultiIndex是已排序的過的就可以這麼使用
# print(pop[:, 2000]) # 尋找所有符合第二層級的資料
# print(pop[pop > 22000000]) # Bool Mask
# print(pop[['California', 'Texas']]) # fancy 索引

# 多重索引的DataFrame
# print(health_data['Guido', 'HR']) # 和Series一樣的方式
# print(health_data.iloc[:2, :2]) # 使用Indexer屬性
# print(health_data.loc[:, ('Bob', 'HR')]) # 可以傳入一個多重索引的tuple

# 切片
idx = pd.IndexSlice # Python 內建的 Slice() 函數, 建議使用 Pandas 的 IndexSlice 物件
# print(health_data.loc[idx[:, 1], idx[:, 'HR']]) # 所有人的每一年的第一筆資料和HR

# 重排列多重索引 (許多情況下, 索引若未排序在很多的切片操作下容易出錯)
# 已排序和未排序的索引
# 建立一個未排序(未依照字典順序)的多重索引資料
index3 = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data3 = pd.Series(np.random.rand(6), index = index3)
data3.index.names = ['Char', 'Int']
# print(data3) 
# 嘗試做切片
# try:
#     data3['a':'b']
# except KeyError as e:
#     print(type(e)) # <class 'pandas.errors.UnsortedIndexError'>
#     print(e) # Key length (1) was greater than MultiIndex lexsort depth (0)
# 未按照字典排序的MultiIndex報出這種錯誤

# Pandas 排序
# DataFrame 的方法有 sort_index(), sortlevel()
data3 = data3.sort_index()
# print(data3)
# print(data3['a':'b']) # 此時切片已經沒有問題了

# 索引的stacking, unstacking
# print(pop.unstack(level = 0))
# print(pop.unstack(level = 1)) # default: level = 1(when total level = 2)
# print(pop.unstack().stack()) # 回復原來的序列
# print(pop.stack()) # AttributeError: 'Series' object has no attribute 'stack'

# 索引的設定與重設
# 一個重排列階層資料的方式把索引標籤轉換成每一行的標籤, 使用reset_index()
pop_flat = pop.reset_index(name = 'population')
# print(pop_flat)
pop_flat = pop_flat.set_index(['State', 'Year'])
# print(pop_flat)

# 在多重索引上的聚合處理
# print(health_data)
# 計算每一年2次量測的平均值
data_mean = health_data.mean(level = 'Year')
# print(data_mean)
# 每一年所有人平均的 HR 和 Temp
data_mean = data_mean.mean(axis = 1, level = 'Type')
# print(data_mean)