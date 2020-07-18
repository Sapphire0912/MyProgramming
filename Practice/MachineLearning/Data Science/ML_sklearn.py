# Introducing Scikit-Learn 
# Reference: http://scikitlearn.org

# Scikit-Learn 的資料表示法
# 把資料當成表格(Data as table)
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
# print(iris.head())
# 在這裡面的資料, 每一列都代表是單一朵被觀察的花, 而列的數目就是在此資料集中所有花的數量
# 也就是說, 這個matrix裡面的所有列都稱為樣本(Sample), n_samples為列的總數
# 而每一欄都是用來描述sample的部分量化資訊, 稱為特徵(features), n_features為欄的總數

# 特徵矩陣(Feature matrix)
# 表格排列的樣子使得資訊可以想成一個二維陣列, 此種表格稱為特徵矩陣
# 通常特徵矩陣被儲存在一個叫做 X 的變數中, 此特徵矩陣的形狀被視為 [n_samples, n_features]的二維陣列

# 樣本(資料的每一列): 通常對應到的是資料集所描述的獨立個體
# Ex. 樣本可能是一朵花, 一個人, 一份文件, 一張影像, 一個聲音檔, 一段影片, 一個可被描述觀測的謎之X物體, etc.
# 特徵(資料的每一欄): 總是被視為獨特的觀察, 此觀察以數值的方式去描述每一個樣本
# 特徵通常都是實數的數值, 但是在有些情況下也可以是布林值或是離散的資料

# 目標陣列: 使用標籤(label)或者目標陣列慣例上通常會把它叫做 "y"
# 目標陣列通常都是一維的, 它的長度是 n_samples, 可以是連續的數值或是離散的類別/標籤
# 目標陣列通常是我們 "想要從資料去預測的值" 

sns.set()
# sns.set() default parameters setting
# sns.set(    
    # context='notebook',
    # style='darkgrid',  
    # palette='deep',  
    # font='sans-serif',
    # font_scale=1,     
    # color_codes=True, 
    # rc=None,
# )

# sns.pairplot(iris, hue = 'species', height = 1.5)  # 成對圖表

X_iris = iris.drop('species', axis = 1)  # axis 為橫列, drop為刪除資料框, 刪除每一列標籤為species的資料
# print(iris.shape)  # (150, 5)
# print(X_iris) # (150, 4)

Y_iris = iris['species']
# print(Y_iris)
# print(Y_iris.shape) # (150, ) -> (150, 1)的意思 

# 此時的 X_iris 為 features matrix; Y_iris 為 target array(label)
# 當資料被正確格式化後, 就可以開始來考慮 Scikit-Learn 的 estimator API 了
plt.show()