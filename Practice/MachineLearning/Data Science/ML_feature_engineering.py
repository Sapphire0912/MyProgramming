# 特徵工程
# 在實務上, 運用機器學習的其中一個重要的步驟就是特徵工程.
# 不論要處理的問題所包含的資訊是甚麼, 取出這些資訊並轉成可用的數字, 藉此建立特徵矩陣(Feature Matrix)

# 一些常見的特徵工程任務的例子: 類別資料(categorical data), 文字(text), 影像(image)的特徵...etc.
# 在此也將討論增加模型複雜度的推導特徵(derived feature), 和缺失資料的補值(imputation).
# 這些處理的過程通常被稱為向量化(vectorization), 也就是把任何資料轉換成可用向量表示的過程.

# 分類特徵
# 假如, 你在探索關於房價的資料, 它們會包含數值特徵比如價格,房間數, 附近鄰居的相關資訊...etc
data = [{'price' : 850000, 'rooms' : 4, 'neighborhood' : 'Queen Anne'},
        {'price' : 700000, 'rooms' : 3, 'neighborhood' : 'Fremont'},
        {'price' : 650000, 'rooms' : 3, 'neighborhood' : 'Wallingford'},
        {'price' : 600000, 'rooms' : 2, 'neighborhood' : 'Fremont'}
    ]

# 但是若純粹只是把資料歸納在程式上並不具有任何意義
# 因此, 有一種被驗證過的技巧是使用 one-hot encoding 它建立了額外的欄位.
# 使用 0/1 代表 有/沒有 出現某類別. 使用 Scikit-Learn DictVectorizer
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse = False, dtype = int)
output = vec.fit_transform(data)
# print(output)
# 在此, 鄰居被擴展成3個欄位代表3個鄰居的標籤, 而1就代表它有這個鄰居
# 把類別特徵進行此種編碼, 就可以使用一般的程序來擬合一個Scikit-Learn模型

# 若要檢視每個欄的意義, 可以觀察此特徵的名稱:
name = vec.get_feature_names()
# print(name)

# 這種方式會有一個缺點, 如果分類中有許多可能的值, 會讓資料集增加非常多.
# 然而, 因此編碼的資料中包含的內容大部份都是0, 使用稀疏輸出(sparse output)是非常有效的解決方案
vec = DictVectorizer(sparse = True, dtype = int)
output = vec.fit_transform(data)
# print(output)
# Scikit-Learn 評估器當在擬合和評估模型時接受此稀疏型態的輸入


# 文字特徵
# 把文字轉換成可表示數值資料的集合, 其中一種方式是字數的計算
# 拿取任一個文字片段, 計算其中每一個字出現的次數並把結果放在表格中
sample = ['problem of evil', 'evil queen', 'horizon problem']

# 把資料向量化
# 雖然也可以手動完成(Ex. re模塊), 但是使用Scikit-Learn 的 CountVectorizer可以比較簡單
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
X = vect.fit_transform(sample)
# print(X)
# 上面的結果是紀錄每一個字出現次數的稀疏矩陣, 若轉換成DataFrame的型態再加上欄名稱會更好觀察
import pandas as pd
output = pd.DataFrame(X.toarray(), columns = vect.get_feature_names())
# print(output)
# line 53(O/P):
#    evil  horizon  of  problem  queen
# 0     1        0   1        1      0
# 1     1        0   0        0      1
# 2     0        1   0        1      0
# 然而這種方法有一些問題: 原始的字數計算會導致特徵被放太多的權重在非常高頻出現的字上, 
# 因此在一些分類演算法中會比較沒有那麼好. 修正的方法是(TF-IDF), 計算文字出現的頻率來加權文字出現的次數
from sklearn.feature_extraction.text import TfidfVectorizer
vecT = TfidfVectorizer()
Y = vecT.fit_transform(sample)
output2 = pd.DataFrame(Y.toarray(), columns = vecT.get_feature_names())
# print(output2)
# line65(O/P):
#        evil   horizon        of   problem     queen
# 0  0.517856  0.000000  0.680919  0.517856  0.000000
# 1  0.605349  0.000000  0.000000  0.000000  0.795961
# 2  0.000000  0.795961  0.000000  0.605349  0.000000

# 影像特徵
# 後續會介紹(因為較複雜)

# 推導的特徵(Derived Features)
# 從輸入特徵中, 以數學的方式推導來的, 當從輸入資料建構多項式特徵時, 
# 可以藉由轉換輸入而不是改變模型來把線性回歸轉變成多項式回歸, 這有時候就是基礎函數回歸
import numpy as np
import matplotlib.pyplot as plt

# 以下這筆資料很明顯無法使用一條直線完美的描述
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
# plt.scatter(x, y)

# 即使這樣, 還是可以使用LinearRegression去擬合一條直線且取得最佳的結果
from sklearn.linear_model import LinearRegression as LR
X = x[:,np.newaxis]
model = LR().fit(X, y)
yfit = model.predict(X)
# plt.scatter(x, y)
# plt.plot(x, yfit)
# 一個不好的直線擬合

# 需要更複雜的模型來描述x,y的關係; 藉由轉換資料可以增加額外的特徵欄位
# 例如: 把多項式特徵加到資料中
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 3, include_bias= False)
X2 = poly.fit_transform(X)
# print(X2)
# X2 output:
# [[  1.   1.   1.]
#  [  2.   4.   8.]
#  [  3.   9.  27.]
#  [  4.  16.  64.]
#  [  5.  25. 125.]]

# 延伸的輸入中計算線性回歸可以得到一個非常接近的資料擬合
model2 = LR().fit(X2, y)
yfit2 = model2.predict(X2)
# plt.scatter(x, y)
# plt.plot(x, yfit2)

# 此種不是藉由更換模型, 而是藉由轉換輸入來改良模型的想法, 是許多更強大機器學習方法的基礎
# plt.show()


# 缺失資料的插補
# 特徵工程中另一種常見的需求是處理缺失資料
# For example:
data2 = np.array([[np.nan, 0, 3],
                  [3, 7, 9], [3, 5, 2],
                  [4, np.nan, 6], [8, 8, 1]])
ydata = np.array([14, 16, -1, 8, -5])
# 若要把有缺失值的資料套用在ML的模型上, 就需要對缺失資料插補(imputation)
# 做法可以簡單的(把NaN資料用該欄的平均值取代), 複雜的(使用矩陣完成或是更強健模型來處理)
from sklearn.impute import SimpleImputer as Imputer
imp = Imputer(strategy = 'mean') # 使用平均值取代NaN
data3 = imp.fit_transform(data2)
# print(data2)
# print(data3)
# data2:
# [[nan  0.  3.]
#  [ 3.  7.  9.]
#  [ 3.  5.  2.]
#  [ 4. nan  6.]
#  [ 8.  8.  1.]]
# data3:
# [[4.5 0.  3. ]
#  [3.  7.  9. ]
#  [3.  5.  2. ]
#  [4.  5.  6. ]
#  [8.  8.  1. ]]

model = LR().fit(data3, ydata)
op = model.predict(data3)
# print(op)
# line 147(o/p): [13.14869292 14.3784627  -1.15539732 10.96606197 -5.33782027]

# 特徵管線
# 在之前的例子, 手動執行轉換會變得非常繁瑣. 尤其把多個步驟串接一起
# For example:
# 1. 使用平均值替補缺失資料(imputation)
# 2. 轉換特徵成為二階方程式(derived features)
# 3. 擬合線性回歸(LR)
# 若要處理上述的步驟, Scikit-Learn 提供了pipeline物件, 可以並行處理
from sklearn.pipeline import make_pipeline
model = make_pipeline(Imputer(strategy = 'mean'), PolynomialFeatures(degree = 2),
                      LR())
model.fit(data2, ydata)
print("ydata: \n", ydata)
print(model.predict(data2))