import pandas as pd
import numpy as np

# 處理缺失資料 可以用Mask, sentinel value(哨兵值)來表示缺失資料的項目
# Mask 可以是一個布林陣列, 或者是在資料裡的其中一個bit 用此來表示資料的空值(Null)
# sentinel value 可以是特定資料慣例, 例如用一個極不常見的數值來取代缺失資料
# 不論哪種都會造成CPU, GPU計算或儲存的而外負擔
# 此時, 不同的程式語言就會和系統是用不同的慣例(Ex. R語言的NA <- 當成是哨兵值來表示缺失資料)

# Pandas 處理缺失資料的部分受限於 Numpy, 因為它並沒有提供NA值的表示法
# 但是 Pandas 若使用 Mask 的方法來表示空值, Numpy所支援的資料型態非常多,
# 因此處理不同型態的運算會造成很多的成本, 不只影響有效使用數值也犧牲 1bit 當成 Mask 做使用
# 所以, Pandas 選擇使用 哨兵值來表示缺失資料(NaN), 以及 Python 的 None 物件

# None : Python 的 缺失資料
# 第一種被使用哨兵值的是 Python 的 None, None是一個Python的物件(object),
# 但是不能被Numpy/Pandas所操作, 因此只能夠以資料型態(object)的方式放在陣列中

vals1 = np.array([1, None, 2, 3])
# print(vals1, "dtype = ", vals1.dtype)

# ipython 操作下(兩者的時間比較)
# In [6]: for dtype in ['object','int']:
#    ...:     print("dtype = ", dtype)
#    ...:     %timeit np.arange(1E6, dtype=dtype).sum() # 1E6 代表 1 * 10**6
#    ...:     print()
#    ...: 

# dtype =  object
# 100 ms ± 4.81 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
# dtype =  int
# 4.57 ms ± 248 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 結果上至少相差了快25倍(Python 的 object計算, Numpy 的 int 計算)

# 在陣列中使用Python物件, 若使用聚合運算的話(sum, min, max...) 會拋出 TypeError 異常
# 這也證明了 None 無法和實數進行任何運算

# NaN : 缺失的資料數值
# NaN 是一個特殊的浮點數值, 所有的系統使用IEEE浮點數表示法即可識別
vals2 = np.array([1, np.nan, 3, 4])
# print(vals2, "dtype =", vals2.dtype) # dtype = float64

# NaN 做運算
# print("1 + np.nan = ", 1 + np.nan)
# print("0 * np.nan = ", 0 * np.nan)
# 若不經過處理, NaN 做任何運算(包含聚合運算)時, 其值皆為NaN
# 在Numpy裡面有提供一些方式是可以忽略這些缺失值
# print("np.nansum(vals2): ", np.nansum(vals2))
# print("np.nanmin(vals2): ", np.nanmin(vals2))
# print("np.nanmax(vals2): ", np.nanmax(vals2))

# Pandas 的 Nan 和 None
a = pd.Series([1, np.nan, 2, None])
# print("a:")
# print(a) # dtype = float64

# 對於沒有可用的哨兵值來說, Pandas 會在 NA 值出現時自動轉換型態
# (Ex. 偵測到np.nan的值在整數陣列, 則會自動轉換為浮點數的型態以適應NA值)
x = pd.Series(range(2), dtype = int)
# print("Original x:")
# print(x)
x[0] = None
# print("Last x: ")
# print(x)

# Pandas 遇到 NA 值時所做出的變化[Format(type -> change type | sentinel value)]
# (float -> float | np.nan)、(object -> object | None, np.nan)
# (int -> float64 | np.nan)、(bool -> object | None, np.nan)
# Pandas 當中, 只要是字串資料(String)總是會以Object dtype的方式儲存

# 在 Null 值上的操作
# Pandas 資料結構中有許多方法來偵測, 移除或取代空值
# 1. isnull(): 產生一個布林遮罩以指示缺失的資料
# 2. notnull(): 和isnull()相反的操作
# 3. dropna(): 傳回一個過濾版本的資料   
# 4. fillna(): 傳回一個含有被填入或估算進缺失值的資料複本

# 偵測空值(使用上述的1, 2點)
data = pd.Series([1, np.nan, 'hello', None])
# print(data.isnull()) # boolmask 可以當成索引
# print(data[data.notnull()])
# 用在 DataFrame 也是產生類似的結果

# 拋棄空值(使用上述的3點)
df = pd.DataFrame([[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]])
# print(df)
# 我們不能從DataFrame中丟棄單一個值, 只能拋棄一整列或行
# print(df.dropna())
# print(df.dropna(axis = 'columns')) # 相當於axis = 1
# 但是這麼做, 我們可能會把一些需要的資料也一併刪除了

# dropna parameters: how, thresh; 可以選擇性地丟棄資料
# how: (default : 'any' 所有只要有一個包含NaN的資料就會移除)
df[3] = np.nan
# print(df)
# print(df.dropna(axis = 1, how = 'all')) # 全部都是空值才會被刪除

# thresh: 指定資料中非空值的個數有幾個, 該行/列才會被保留下來
# print(df.dropna(axis = 'rows', thresh = 3)) # 相當於axis = 0

# 填入空值(使用上述的4點)
# 把為NaN的資料插入一個數值
data2 = pd.Series([1, np.nan, 2, None, 3], index = list('abcde'))
# print(data2)
# print(data2.fillna(0)) # 補上0
# print(data2.fillna(method = 'ffill')) # 將NaN的資料和上一筆資料相同(Forward Fill)
# print(data2.fillna(method = 'bfill')) # 將NaN的資料和下一筆資料相同(Back Fill)

# 使用DataFrame 也可以達到相同的效果, 但是若前/後一筆資料是不可使用(包含NaN值)的則NaN會被保留
print(df)
print(df.fillna(method = 'ffill', axis = 1))
print(df.fillna(method = 'ffill', axis = 0)) 