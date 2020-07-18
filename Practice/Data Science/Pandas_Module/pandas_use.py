import pandas as pd
import numpy as np
# Pandas 的資料結構 Series, DataFrame, Index

# Series 物件: 是一個被索引資料的一維陣列, 可以使用一個串列或陣列來建立
data = pd.Series([0.25, 0.5, 0.75, 1])
# print(data)

# Series裡面包含了值和索引, 可以使用values, index屬性來存取
# print("data.values: ", data.values)
# print("data.index: ", data.index) # RangeIndex(start=0, stop=4, step=1)

# 也可以利用Python的索引方式來取得data值
# print("data[0]: ", data[0])
# print("data[1:3]: \n", data[1:3])

# Numpy 裡面使用整數索引來存取值, PandasSeries則是要明確定義和值相關聯的索引
data = pd.Series([0, 25, 50, 100], index = ['a', 'b', 'c', 'd'])
# print("Data: \n", data)
# 取值方式和上面相同, 甚至可以使用非連續性的索引
# print("Data['a']: ", data['a'])

# 可以把Pandas當成一個Python的字典({key:value}), 執行上比Python字典更有效率
population = {'California' : 38332521, 'Texas' : 26448193, 
              'New York' : 19651127, 'Florida' : 19552860}
population = pd.Series(population)
# print(population)
# Series 支援陣列切片操作
# print("Slice:\n", population['California':'New York'])

# 建立Series物件 syntax: pd.Series(data[, index]) default index = [0, 1, 2, ...len(data)-1]
# 除了上述的方式外
# print(pd.Series({2:'a', 1:'b', 3:'c'}, index = [3, 2]))
# 只顯示index裡面的值和索引

# DataFrame 物件: 依照同一個索引值, 並把資料逐一對齊
area = {'California' : 423967, 'Texas' : 695662, 'New York' : 141297, 'Florida' : 170312}
area = pd.Series(area)
# print("Population: \n", population)
# print("Area: \n", area)

# 將上面兩種資料結合起來則用DataFrame物件
states = pd.DataFrame({'(name)population' : population, '(name)area' : area})
# print(states)

# DataFrame物件有 index(左邊直行的索引內容) 和 columns(上排橫列的標籤內容) 屬性
# print("Index: ", states.index) # Index(['California', 'Texas', 'New York', 'Florida'], dtype='object')
# print("Columns: ", states.columns) # Columns:  Index(['(name)population', '(name)area'], dtype='object')

# 取值方式和前面相同
# print("Area: \n", states['(name)area'])
# print("Area: \n", states['(name)area'][0]) # 標籤為(name)area這行的第0個元素

# 建立DataFrame物件(有多種建立方式)
# 1. 單一個Series物件建立
food = {'Favorite' : 'noodles', 'good' : 'rice', 'not bad' : 'pizza', 'not good' : 'vegetables'}
food = pd.Series(food)
foods = pd.DataFrame(food, columns = ['food'])
# print(foods)

# 2. 字典的list建立
math = [{'a' : i, 'b' : 2 * i} for i in range(4)]
math = pd.DataFrame(math)
# print(math)

less = [{'a' : 1, 'b' : 2}, {'b' : 3, 'c' : 4}]
less = pd.DataFrame(less)
# print(less) # 若有缺少的鍵, Pandas會用NaN來取代(Not a Number)

# 3. Series物件的字典建立
# 上面states就是此種方式

# 4. Numpy的二維陣列建立
num = np.random.rand(3, 2) # 3x2 (標籤x2, 索引x3)
df = pd.DataFrame(num, columns = ['foo', 'bar'], index = ['a', 'b', 'c'])
# print(df)

# 5. Numpy 結構陣列建立
A = np.zeros(3, dtype = [('A', 'i8'), ('B', 'f8')]) # 標籤A裡面的資料為int64, B則是float64
# print("Numpy: \n", A)
A = pd.DataFrame(A)
# print("DataFame: \n", A)

# Index 物件(和參數的index不同): 是一個不能修改值的陣列, 或是有序的集合
ind = pd.Index([2, 3, 5, 7, 11])
# print(ind) #Int64Index([2, 3, 5, 7, 11], dtype='int64')

# 把Index當成不可修改的陣列, 但是也可以去做切片取值
# print(ind[1])
# print(ind[::2])

# Index也有和Numpy相似的屬性
# print(ind.size, ind.shape, ind.ndim, ind.dtype)

# 不可以用一般賦值的方式去修改其值 (ex. ind[1] = 0; TypeError) 

# 把Index當成一個有序的集合
inda = pd.Index([1, 3, 5, 7, 9])
indb = pd.Index([2, 3, 5, 7, 11])
# print("交集: ", inda & indb)
# print("聯集: ", inda | indb)
# print("對稱補集: ", inda ^ indb)