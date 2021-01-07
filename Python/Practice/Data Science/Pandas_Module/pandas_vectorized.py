import numpy as np
import pandas as pd

# Pandas 透過 Pandas Series 的 str 特性, 以及包含字串的Index 物件解決向量化字串的操作
# 且可以正確的處理缺失資料

data = ['peter', 'Paul', 'None', 'MARY', 'gUIDO']
# 在 Numpy 下(資料中若有 缺失資料就會報錯(AttributeError))
# print([s.capitalize() for s in data]) # s.capitalize()首字大寫其餘小寫

# 在 Pandas 下
name = pd.Series(data)
# print(name)
# print(name.str.capitalize())

# Pandas 字串方法的表格
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle',
                   'Terry Jones', 'Michael Palin'])
# 基本上 Python 的所有字串方法 都有對應到 Pandas str 向量化方法(p186)
# print(monte.str.len())
# print(monte.str.lower())
# print(monte.str.startswith('T'))
# print(monte.str.split())
# 與Python 字串處理用法大同小異

# 使用正規表達式(Regular Expression)的方法(p187)
# Pandas str方法 和 Python re 模組的對應
# print(monte.str.extract('([A-Za-z]+)'))
# print(monte.str.findall(r'^[^AEIOU].*[^aeiou]$'))
# line 30: 匹配 首字 非AEIOU 非'\n' 非包含aeiou任意字符的結尾

# Re module:(待補充, 複習)
# re.match(pattern, string[, flag = 0]) 
# re.extract(pattern)
# re.findall()
# re.replace()
# re.contains()
# re.count()
# re.split()
# re.rsplit()

# 雜項方法(其他Pandas 字串方法)
# get() 索引每一個元素
# slice() 切片每一個元素
# slice_replace() 使用傳進去的值取代在每一個元素的切片
# cat() 串接字串
# repeat() 重複值
# normalize() 傳回Unicode格式的字串
# pad() 在字串的左, 右或是兩邊加上空白
# wrap() 把長字串分割成多列, 每一列不超過給定的寬度
# join() 每Series 中的每一個元素以傳入的分隔符號串連成字串
# get_dummies() 把虛擬變數提取出來變成一個DataFrame

# 向量化項目的存取和切片: get(), slice()
# print(monte.str.slice(0, 3)) # 等同於 df.str[0:3]
# print(monte.str.split().str.get(-1)) # 等同於 df.split()[-1]

# 指示符變數: get_dummies(), 當資料中有一個欄位包含了一些編碼過的指示符時就很好用了(p189)
# 例如如果有一個資料集包含某一型式編碼的資訊
# Ex: A = [born in America], B = [born in the United Kingdom], 
#     C = [likes cheese], D = [likes spam]
full_monte = pd.DataFrame({'name': monte, 'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C', 'B|C|D']})
# print(full_monte)
# 把指示符切割出來變成一個DataFrame
print(full_monte['info'].str.get_dummies('|'))