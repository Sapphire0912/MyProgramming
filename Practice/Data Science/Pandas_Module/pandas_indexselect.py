import pandas as pd
# 資料的索引和選擇

# Series 中選擇資料
data = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
# print("Data:")
# print(data)

# 把Series當成字典(可以使用Python字典的操作方法/表達式)
# print("data['b']: ", data['b'])
# print("'a' in data: ", 'a' in data)
# print("data.keys(): ", data.keys())
# print("data.items(): ", list(data.items()))
# 可以用字典的語法來對Series修改, data['e'] = 1.25
data['e'] = 1.25
# print("Data:")
# print(data)

# 把Series當成一維陣列(可以使用Numpy陣列的操作方式)
# 指定索引切片
# print("data['a':'c']: \n", data['a' : 'c'])
# 整數索引切片
# print("data[1:4]: \n", data[1:4])
# 遮罩(mask)
# print("data[(data > 0.4) & (data < 1.2)]: \n", data[(data > 0.4) & (data < 1.2)])
# fancy索引
# print("data[['a', 'e']]: \n", data[['a', 'e']])

# indexer: loc, iloc, ix
# 像是資料若使用整數當成每一列的標籤, 使用整數索引或指定索引會出現一些問題或混淆
# 因此Pandas提供了indexer屬性, 在Series使用了loc, iloc, ix三種屬性
data2 = pd.Series(['x', 'y', 'z'], index = [2, 3, 1])
# print("Data2:")
# print(data2)

# loc: 是讓索引和切片總是以明確的索引為主(每一列的標籤為主)
# print("data2[1]: ", data2[1]) # ('y' or 'z')可能會混淆, 避免數據龐大時造成不必要的錯誤
# print("data2.loc[1]: ", data2.loc[1]) # 'z'
# print("data2.loc[2:3]: \n", data2.loc[2:3]) # 第1 2列

# iloc: 讓索引和切片總是以整數索引的方式為主(Python型態的整數索引, 起始值為0)
# print("data2.iloc[0]: ", data2.iloc[0]) # 'x'
# print("data2.iloc[1:3]: \n", data2.iloc[1:3]) # 第2 3列

# ix是前兩者的混合, 在DataFrame效果比較顯著
# 在Python程式碼"明確>隱晦", 因此loc, iloc在維護簡潔和易讀十分有用(尤其在這個整數索引的例子)

# DataFrame中選取資料
area = pd.Series({'California' : 423967, 'Texas' : 695662, 'New York' : 141297,
                  'Florida' : 170312, 'Illinois' : 149995})
pop = pd.Series({'California' : 38332521, 'Texas' : 26448193, 'New York' : 19651127,
                 'Florida' : 19552860, 'Illinois' : 12882135})

data = pd.DataFrame({'Area' : area, 'Population' : pop})
# print("Data:")
# print(data)

# 把DataFrame當成字典
# print("data['Area']: \n", data['Area'])
# print("data.Population: \n", data.Population)
# 注意: 不要把DataFrame的屬性名稱, 和Python字典的屬性名稱弄在一塊
# 下面程式碼則是在DataFrame裡面新增一行
data['density'] = data['Population'] / data['Area']
print("Data:")
print(data)

# 把DataFrame當成二維陣列
# print("data.values: \n", data.values) # 取得DataFrame裡面的所有值(沒有標籤)
# print("data.T: \n", data.T) # 將DataFrame裡面的資料做轉置動作(Ex. 3x5 -> 5x3)

# print("data.values[0]: \n", data.values[0]) # 選取第一列的所有值(沒有標籤)
# print("data['Area']: \n", data['Area']) # 取得標籤為Area的所有資料(有標籤)
# print("data['California']: \n", data['California']) # KeyError
# line 73 (不能直接存取橫列的標籤) <- 因為使用Python字典語法(一鍵一值, 搜尋鍵)

# indexer此時派上用場了, 利用他們來索取DataFrame的資料
# print("data.iloc[:3, :2]: \n", data.iloc[:3, :2]) # 取得前3列和前2行的資料
# print("data.loc[:'New York', :'Population']: \n", data.loc[:'New York', :'Population'])
# line 77, 78是相同的結果; 且在上面有使用過, 接著使用ix

# ix是可以將兩種方式都混合起來使用(官方不推薦使用)
# print("data.ix[:3, :'Population']: \n", data.ix[:3, :'Population']) # 執行結果也和上述兩種相同
# 當然也可以使用Mask或者fancy indexing操作
# print("data.loc[data.density > 100, ['Population', 'density']]: \n", 
#        data.loc[data.density > 100, ['Population', 'density']]) 

# 在原本的操作方法中, 也可以直接使用slice, index, mask
print("data['Texas' : 'Illinois']: \n", data['Texas' : 'Illinois'])
print("data[1:5]: \n", data[1:5])
print("data[data.density >= 90]: \n", data[data.density >= 90])
# 這種似於Numpy操作雖然不能很精準符合Pandas的操作, 但實務上非常有用