import pandas as pd
import numpy as np

# 合併資料集: Merge 以及 Join
# Pandas 提供高效能記憶體內 join and merge 操作
# pd.merge() 使用關聯式代數(relational algebra)的子集合, 實作了許多基本建構方塊(join方法)
# Join 類別; 在pd.merge裡面有許多型式的join: 1 to 1, multi to 1, multi to multi 
# 此3種 join 方式可以透過同一個pd.merge()來存取, 以輸入資料的型式來決定執行哪種型式的join

# 1 to 1 join
df1 = pd.DataFrame({'employee' : ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group' : ['Accouting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee' : ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date' : [2004, 2008, 2012, 2014]})
# print("DF1:")
# print(df1)
# print("DF2:")
# print(df2)
# 將資料合併成單一個DataFrame, 使用 pd.merge()
df3 = pd.merge(df1, df2)
# print("DF3:")
# print(df3) # 即使被合併的資料框的順序不同, 一般來說這種方式會讓索引值被丟棄

# multi to 1
df4 = pd.DataFrame({'group' : ['Accouting', 'Engineering', 'HR'],
                    'supervisor' : ['Carly', 'Guido', 'Steve']})
# print("DF4:")
# print(df4)
# print("After Merge:")
# print(pd.merge(df3, df4)) # 產生新的一行, 那行的內容會依據輸入資料而產生重複的項目
# line 30:
# After Merge:
#   employee        group  hire_date supervisor
# 0      Bob    Accouting       2008      Carly
# 1     Jake  Engineering       2012      Guido
# 2     Lisa  Engineering       2004      Guido
# 3      Sue           HR       2014      Steve

# multi to multi 
df5 = pd.DataFrame({'group':['Accouting', 'Accouting', 'Engineering', 'Engineering', 'HR', 'HR'],
                    'skill':['math', 'spreadsheets', 'coding', 'linux', 'spreadsheets', 'organization']})
# print(pd.merge(df5, df1)) # 合併資料集裡面的資料交換, 只會影響順序不會影響結果
# line 42:
#          group         skill employee
# 0    Accouting          math      Bob
# 1    Accouting  spreadsheets      Bob
# 2  Engineering        coding     Jake
# 3  Engineering        coding     Lisa
# 4  Engineering         linux     Jake
# 5  Engineering         linux     Lisa
# 6           HR  spreadsheets      Sue
# 7           HR  organization      Sue

# pd.merge() Parameter
# on 參數
# print(pd.merge(df1, df2, on = 'employee'))
# 明確 指定keyboard 來 '指定特定行標籤' 的名稱, 用來當作要處理的那一行
# 這個參數要兩個DataFrame都要擁有, '一樣的keyboard'才可以正常工作

# left_on and right_on
df6 = pd.DataFrame({'name':['Bob', 'Jake', 'Lisa', 'Sue'], 'salary': [70000, 80000, 120000, 90000]})
# print(df1.merge(df6, left_on = 'employee', right_on = 'name'))
# 若產生的結果有冗於的行, 可以使用drop('label name'[,axis])來刪除(axis = 1為行標籤)
# print(df1.merge(df6, left_on = 'employee', right_on = 'name').drop('name', axis = 1))

# left_index and right_index
# 除了合併欄位, 也可以使用索引. 指定特定的索引值來當成合併資料的條件
# 首先, 先讓df1, df2的employee行變成資料框的索引值
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
# print(df1a)
# print(df2a)
# print(df1a.merge(df2a, left_index = True, right_index = True))
# print(df1a.join(df2a)) <- 可以做到(line 73)一樣的結果(join預設就是以索引值來合併)

# left_on, right_on with left_index, right_index 
# print(df1a.merge(df6, left_index = True, right_on = 'name')) 

# Reference: http://pandas.pydata.org/pandas-docs/stable/merging.html

# 在 Join 中指定集合算術運算
df7 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'], 'food': ['fish', 'beans', 'bread']},
                    columns = ['name', 'food'])
df8 = pd.DataFrame({'name': ['Mary', 'Joseph'], 'drink' : ['wine', 'beer']},
                    columns = ['name', 'drink'])
# print(df7)
# print(df8)
# print(pd.merge(df7, df8)) # A 交集 B <- 也是代表 內部連接(inner join)
# line 88:
#    name   food drink
# 0  Mary  bread  wine

# 用 how 參數 來決定集合的用算方式(default: how = 'inner')
# how = 'outer'(A 聯集 B) <- outer join(外部連接); 缺失值會填入 NaN
# print(pd.merge(df7, df8, how = 'outer'))
# how = 'left' or 'right' <- 左連結(left join) 右連結(right join)
# 分別以 左/右 的項目為主的外連結
# print(pd.merge(df7, df8, how = 'left'))  # 以 df7 為主
# print(pd.merge(df7, df8, how = 'right')) # 以 df8 為主

# 重疊的欄位名稱, 使用 suffixes 參數
# 在 2個 DF 中, 若有重複的欄位(行標籤)名稱
df9 = pd.DataFrame({'name' : ['Bob', 'Jake', 'Lisa', 'Sue'], 'rank' : [1, 2, 3, 4]})
df10 = pd.DataFrame({'name' : ['Bob', 'Jake', 'Lisa', 'Sue'], 'rank' : [3, 1, 4, 2]})
# print(pd.merge(df9, df10, on = 'name'))
# line 105: 
#    name  rank_x  rank_y
# 0   Bob       1       3
# 1  Jake       2       1
# 2  Lisa       3       4
# 3   Sue       4       2
# 若有重複的欄名, merge函數預設會自動加上_x, _y來區別, 則suffixes參數就是來修改預設值
# print(pd.merge(df9, df10, on = 'name', suffixes = ["_L", "_R"]))
# line 114:
#    name  rank_L  rank_R
# 0   Bob       1       3
# 1  Jake       2       1
# 2  Lisa       3       4
# 3   Sue       4       2