import numpy as np
# Numpy的結構化陣列, 紀錄陣列, 通常會用在Pandas DataFrame上

# 建立一個簡單的陣列敘述
# x = np.zeros(4, dtype = int)

data = np.zeros(5, dtype = {'names' : ('name', 'age', 'weight'), 
                            'formats': ('U10', 'i4', 'f8')}) 
# print("data type: ", data.dtype) # [('name', '<U10'), ('age', '<i4'), ('weight', '<f8')]
# U10 代表: 最大長度是10的Unicode字串, i4為 4bytes的int, f8為 8bytes的float

name = ['Alice', "Eric", "Sapphire", "Lily", 'Iris']
age = [25, 19, 20, 16, 22]
weight = [48.0, 51.2, 49.3, 43.6, 45.1]

data['name'] = name
data['age'] = age
data['weight'] = weight
print("Data: \n", data) # 此時資料被放置於便於存取的記憶體區塊中

# 取得所有的name
# print("All name: ", data['name'])
# 取得第一項資料和最後一列的name
# print("First Data: ", data[0], " Last Name: ", data[-1]['name'])
# 布林遮罩
# 取得 age 小於 22 的 name
# print("Age less than 22: ", data[data['age'] < 22]['name'])

# 建立結構陣列
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype = tp)
print(X[0])
print(X['mat'][0])
# 為甚麼要建立結構化陣列? 因為Numpy的dtype對應到C的結構定義, 在該緩衝區包含的這些陣列內容可以直接被C程式碼存取 

# 紀錄陣列 (np.recarray) 可以讓字典鍵變成屬性來使用(但效率比字典鍵存取低卻比較方便)
# 原本的方式 data['name'] 使用字典鍵來存取
data_rec = data.view(np.recarray)
print("Age: ", data_rec.age)
print("Name: ", data_rec.name)
print("weight: ", data_rec.weight)

# 結構化陣列資料Pandas套件會是更好的選擇
# Numpy 主要增進Python的迭代列表問題和更加靈活運用多維陣列的計算和操作