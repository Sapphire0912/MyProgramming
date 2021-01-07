# 端到端的機器學習項目
# 假設今天你是一個房地產公司最新雇用的數據工程師, 那麼以下會是你經歷的主要步驟
# 1. 觀察大局
# 2. 獲得數據
# 3. 從數據探索和可視化獲得想法/靈感
# 4. 機器學習演算法的數據準備(數據預處理)
# 5. 選擇和訓練模型
# 6. 微調模型
# 7. 展示解決方案
# 8. 啟動, 監控和維護系統


# 2. 前置作業/獲得數據
# 先下載數據
# 因為是模擬專案開發, 原本應該要從網路加載數據, 但是要避免網路不良狀態, 先用下載的資料集 <- 之後再補上完整部分
# (也有下載到ML的DataSets裡面)

path = 'C:\\Users\\kotori\\Desktop\\MyProgramming\\Practice\\ML\\DataSet\\housing.csv'
import pandas as pd

def load_housing_data(housing_path = path):
    csv_path = pd.read_csv(path)
    return csv_path


# 大略看一下數據結構
# print(load_housing_data().head())
# 每一行都代表一個區, 並且有10種屬性
# load_housing_data().info() # info() 可查看數據的狀態和資訊
# 資料集總共有 20640 筆資料, 注意 total_bed 這個屬性只有20433個非空值, 後續處理資料要注意空值部分

# 因為 ocean_proximity 是 obj 對象, 且觀察數據結後它可能是一個分類屬性, 使用value_counts()查看
housing = load_housing_data()
# print(housing["ocean_proximity"].value_counts())

# 接著看看其他區域, 使用 describe() 查看
# print(housing.describe())
# 這裡計算時空值會被忽略

# 另一種方式, 是使用直方圖來查看
import matplotlib.pyplot as plt
# housing.hist(bins = 50, figsize = (20, 15))
# plt.show()

# 創建測試集
import numpy as np
from sklearn.model_selection import train_test_split as tts

def create_testdata(data, test_size = 0.2, random_state = 42):
    train_set, test_set = tts(data, test_size = test_size, random_state = random_state)
    return train_set, test_set

# train_set, test_set = create_testdata(housing)
# 根據題意, 查看收入中位數的直方圖
# housing["median_income"].hist(bins = 50)
# plt.show()

# 在數據集中, 每一層都必須要有足夠的實例, 不然數據不足的層很可能會被錯估
# 篩選數據(利用ceil進行取整, 然後把>5的數據都歸類成5)
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace = True)
# 篩選完後, 可以根據收入類別進行分層抽樣, 使用 Scikit-Learn的 StratifiedShuffleSplit
from sklearn.model_selection import StratifiedShuffleSplit as SSS
split = SSS(n_splits = 1, test_size = 0.2, random_state = 42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# 查看數據是否為我們所需要的
# print(housing["income_cat"].value_counts() / len(housing))
# 補充: 分層抽樣和純隨機抽樣偏差比較, 可以得知分層抽樣與原本數據中的分布幾乎一致, 但隨機抽樣卻有重大偏差

# 現在可以把數據恢復原樣了, 刪除income_cat屬性
for sets in (strat_train_set, strat_test_set):
    sets.drop(["income_cat"], axis = 1, inplace = True)

# 花了一段時間在數據集的生成上, 這是機器學習極致重要的一部份. 接著要進入下一步驟了


# 3. 從數據探索和可視化獲得想法/靈感
# 目前我們只是快速的瀏覽數據, 因此本階段我們要更深入了解數據
# 首先, 把測試集放一邊, 能探索的只有訓練集; 如果訓練集非常龐大, 可以抽樣一個探索集, 這樣操作可以更簡單快捷
# 不過我們的數據集非常小, 完全可以直接在整個訓練集上操作.
# 讓我們先創建一個副本, 這樣可以隨便嘗試且不損害訓練集
housing_cp = strat_train_set.copy()

# 將地理數據可視化
# housing_cp.plot(kind = "scatter", x = "longitude", y = "latitude")
# 突出高密度區域的可視化
# housing_cp.plot(kind = "scatter", x = "longitude", y = "latitude", alpha = 0.1)

# 接著看看房價
# housing_cp.plot(kind = 'scatter', x = "longitude", y = "latitude", s = hosuing_cp["population"] / 100, 
#                 label = "population", alpha = 0.4, c = "median_house_value", 
#                 cmap = plt.get_cmap("jet"), colorbar = True)
# plt.legend()
# plt.show()
# 透過上圖可以發現房屋價格和地理位置以及人口密度息息相關.

# 尋找相關性
# 由於數據集不大, 可以使用 corr() 輕鬆計算出每對屬性之間的標準相關係數
corr_matrix = housing_cp.corr()
# 看看每個屬性與房屋中位數的相關性分別是多少
# print(corr_matrix["median_house_value"].sort_values(ascending = False))
# 相關係數的範圍[-1, 1]. 越接近1 表示有越強的正相關, 否則反之; 若越接近0, 代表兩者之間沒有線性的相關性
# 相關係數僅測量線性的相關性, 如果x上升/下降, y上升/下降. 所以有可能徹底遺漏非線性的相關性

# 另一種檢視屬性之間相關性的方法
from pandas.plotting import scatter_matrix
# attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
# scatter_matrix(housing_cp[attributes], figsize = (12, 8))
# plt.show()

# 從圖上可以看出最有潛力預測房價中位數的屬性是 收入中位數, 因此放大來看看其相關性的散點圖
housing_cp.plot(kind = 'scatter', x = 'median_income', y = 'median_house_value', alpha = 0.1)
# plt.show()
# 除了大於 500000 美元, 是一條清晰的水平線, 而且可以清楚看出上升的趨勢, 且點也不是太分散.
# 但是, 圖中還有顯示出不那麼明顯的直線, 45W, 35W, 28W等 隱約的有一條直線, 為了避免演算法學習之後重現
# 這些怪異的數據, 可能會嘗試刪除這些相應的地區

# 此外, 可以嘗試不同屬性的組合, 在準備給機器學習輸入數據之前, 最後一件事情應該是嘗試各種屬性的組合
# 雖然探索不見得要如此徹底, 關鍵是要快速取得對數據更深刻的理解

# 4. 機器學習演算法的數據準備
# 在此再創建一個數據副本, 並把預測集和標籤分開
housing_cp2 = strat_train_set.drop("median_house_value", axis = 1)
# drop 會創建一個數據副本, 但不影響原本數據
housing_labels = strat_train_set["median_house_value"].copy()

# 數據清理
# 大部分的機器學習演算法無法在缺失的特徵上工作
# 處理缺失值, 有三種方法: 放棄有缺失值的資料, 放棄有缺失值的標籤/屬性, 把缺失值用數字填補
# 在Scikit-Learn提供一個方法來處理缺失資料, imputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = "median") 
# 由於中位數只能在數值上運算, 因此要把obj對想給去除掉
# (為了慎重起見, 避免經過計算後的其他資料出現缺失值, 因此把它應用在所有標籤)
housing_num = housing_cp2.drop("ocean_proximity", axis = 1)
imputer.fit(housing_num)
# 結果會存在於statistics_屬性中
# print(imputer.statistics_)
# print(housing_num.median().values)

X = imputer.transform(housing_num)
# 轉換結過的X 是一個numpy數組, 以下是把Numpy數組放入dataframe
housing_tr = pd.DataFrame(X, columns = housing_num.columns)

# 處理文本和分類屬性
# 之前被排除的 ocean_proximity 是 obj對象/屬性, 無法計算它的中位數值
# 但是 大部分的機器學習演算法都易於使用數字計算, 所以我們把文本標籤轉換成數字
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
housing_cat = housing_cp2["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
# print(housing_cat_encoded)
# print(encoder.classes_)

# 獨熱編碼(One-Hot Encoder)
# 可以將整數分類值, 轉換成獨熱向量
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
# 需注意的是: 這裡的fit_transform參數必須是二維資料, 所以要把一維資料的housing_cat_encoded重塑
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1, 1))
# 補充: data.reshape(-1, 1) = data[:, np.newaxis] = data[:, None]
# print(housing_cat_1hot)
# 此時的輸出是一個Scipy稀疏矩陣, 並不是Numpy數組, 當資料有成千上萬的分組時, 此函數非常有用
# 因為當獨熱編碼完之後, 會得到一個幾千列的矩陣, 並且都是0, 每行僅有一個1; 但是儲存一堆0很浪費記憶體
# 所以稀疏矩陣選擇儲存1的位置. 若想要轉成Numpy數組, 只需要使用 toarray() 即可
# print(housing_cat_1hot.toarray())

# 若使用 LabelBinarizer 可以一次性的完成兩個轉換(從文本轉成整數再轉成獨熱向量)
from sklearn.preprocessing import LabelBinarizer
encoder = LabelBinarizer()
housing_cat_1hot = encoder.fit_transform(housing_cat)
# print(housing_cat_1hot)
# 此時的傳回值是一個 密集的 Numpy數組, 可以透過 sparse_output = True 調整, 則傳回稀疏矩陣

# 自定義轉換器
# 雖然 Scikit-Learn 提供了許多有用的轉換器, 但仍需要為一些自定義的清理和操作或組合特定屬性等來編寫自己的轉換器
# 現在需要創建一個類然後應用 fit(), transform(), fit_transform()方法.
# 如果使用 TransformerMixin 作為基類, 就可以直接得到最後一個方法;
# 若使用 BaseEstimator 作為基類(並在構造函數中避免 *args, **kargs)還可以使用兩種自動調整超參數的方法
# 見以下例子
from sklearn.base import BaseEstimator, TransformerMixin # 深入研究此兩種轉換器
rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # 超參數 add_bedrooms_per_room
        self.add_bedrooms_per_room = add_bedrooms_per_room
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
# attr_adder = CombinedAttributesAdder(False)
# housing_extra_attribs = attr_adder.transform(housing.values)

# 特徵縮放
# 此部分最重要也是最需要應用到數據上的轉換器, 輸入數值會影響到機器學習演算法的性能表現
# 注意: 目標值通常不需要縮放
# 同比例縮放所有屬性, 常用的兩種方式是: 最小-最大縮放 和 標準化
# 最小-最大縮放(歸一化): 將值重新縮放使其最終範圍落在 0~1 之間
# 做法: (data_value - minimum) / (maximum - minimum)
# Scikit-Learn 提供了 MinMaxScaler 轉換器, 超參數 feature_range 可以調整範圍值

# 標準化: 不將值設定在特定範圍
# 作法: (data_value - means) / variance(變異數)
# Scikit-Learn 提供了標準化的轉換器 StandardScaler 

# 轉換流水線(管線 pipeline)
# 許多數據轉換的步驟需要以正確的順序來執行, 而Scikit-Learn 的 Pipeline 支持這樣的轉換方式
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
# num_pipeline = Pipeline([('imputer', SimpleImputer(strategy = "median")), 
#                          ('attribs_adder', CombinedAttributesAdder()), 
#                          ('std_scaler', StandardScaler()),])
# housing_num_tr = num_pipeline.fit_transform(housing_num)

from sklearn.pipeline import FeatureUnion
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

class MyLabelBinarizer(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = LabelBinarizer(*args, **kwargs)

    def fit(self, x, y = 0):
        self.encoder.fit(x)
        return self

    def transform(self, x, y = 0):
        return self.encoder.transform(x)


num_pipeline = Pipeline(
    [
        ('selector', DataFrameSelector(num_attribs)),
        ('imputer', SimpleImputer(strategy = "median")), 
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ]
)

cat_pipeline = Pipeline(
    [
        ('selector', DataFrameSelector(cat_attribs)),
        ('label_binarizer', MyLabelBinarizer()),
    ]
)

full_pipeline = FeatureUnion(transformer_list = [
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
    ]
)

# 運行整條管線
housing_prepared = full_pipeline.fit_transform(housing_cp2)
# print(housing_prepared)
# print(housing_prepared.shape) # (16512, 16)


# 5. 選擇和訓練模型
# 首先, 經過最開始的評估結果, 要選用監督式學習的回歸模型, 所以在此使用 LR 模型
from sklearn.linear_model import LinearRegression as LR
lr = LR()
lr.fit(housing_prepared, housing_labels)
# 查看預測結果(使用前幾個資料測試)
# some_data = housing_cp2.iloc[:5]
# some_labels = housing_labels.iloc[:5]
# some_prepared = full_pipeline.transform(some_data)
# print("Predictions: ", lr.predict(some_prepared))
# print("Original Labels: ", list(some_labels))
# 可以看出預測結果差的離譜(代表資料的擬合不足 underfitting)

# 透過 Scikit-Learn mean_squared_error 來計算整個訓練資料上回歸模型的RMSE
from sklearn.metrics import mean_squared_error
housing_predictions = lr.predict(housing_prepared)
# lr_mse = mean_squared_error(housing_labels, housing_predictions)
# rmse = np.sqrt(lr_mse)
# print("RMSE: ", rmse) # 預測誤差 68628.19819848923 美元

# 因此對於擬合不足的模型, 可以選用更強大的模型或是提供更好的特徵, 減少限制等等
# 這裡則更換更強大的模型 DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor as DTR
tree_reg = DTR()
tree_reg.fit(housing_prepared, housing_labels)
predicted = tree_reg.predict(housing_prepared)
# mse = mean_squared_error(housing_labels, predicted)
# rmse = np.sqrt(mse)
# print("RMSE: ", rmse) # RMSE:  0.0
# 這裡的結果正確率是100%, 但要考慮是否過度擬合 Overfitting

# 因此, 要使用交叉驗證來進行更好的評估模型
from sklearn.model_selection import cross_val_score as cvs
scores = cvs(tree_reg, housing_prepared, housing_labels, scoring = "neg_mean_squared_error", cv = 10)
rmse_scores = np.sqrt(-scores)
# Scikit-Learn 交叉驗證更傾向於效用函數(越大越好), 而不是成本函數(越小越好), 所以計算分數實際上是負的MSE
# 來查看結果
def display_score(scores):
    print("Score: ", scores)
    print("Mean:", scores.mean())
    print("Stardard deviation: ", scores.std())

# display_score(rmse_scores)
# Mean: 71227.31692492112
# Stardard deviation:  2926.49161963209

# 和LR的交叉驗證評分做個比較
lr_scores = cvs(lr, housing_prepared, housing_labels, scoring = "neg_mean_squared_error", cv = 10)
lr_rmse = np.sqrt(-lr_scores)
# display_score(lr_rmse)
# Mean: 69052.46136345083
# Stardard deviation:  2731.6740017983425

# 明顯兩者比較出來的結果, 決策樹回歸已經嚴重的過度擬合了導致比線性回歸還差

# 所以來嘗試最後一個模型 RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor as RFR
rfr = RFR()
# rfr.fit(housing_prepared, housing_labels)
# housing_predicted = rfr.predict(housing_prepared)
# rmse = np.sqrt(mean_squared_error(housing_labels, housing_predicted))
# print("RMSE: ", rmse) # RMSE:  18620.70199601925
# rfr_scores = cvs(rfr, housing_prepared, housing_labels, scoring = "neg_mean_squared_error", cv = 10)
# rfr_rmse = np.sqrt(-rfr_scores)
# display_score(rfr_rmse)
# Mean: 50243.380660403775
# Stardard deviation:  1997.2178724397745
# 結果仍然過度擬合了, 因為訓練分數(rmse)遠低於驗證分數(rfr_rmse)
# 注意: 千萬別花太多時間調整超參數, 我們的目的是篩選幾個(2~5)有效的模型, 緊接著微調就可以了

# 6. 微調模型
# 格狀搜尋 GridSearch
# 使用 Scikit-Learn GridSearchCV
from sklearn.model_selection import GridSearchCV
param_grid = [{'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]}, 
              {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]}]
forest_reg = RFR()
grid_search = GridSearchCV(forest_reg, param_grid, cv = 5, scoring = 'neg_mean_squared_error')
grid_search.fit(housing_prepared, housing_labels)
# print(grid_search.best_params_) # {'max_features': 6, 'n_estimators': 30}

# 也有評估分數
cvres = grid_search.cv_results_
# for meanscore, params in zip(cvres["mean_test_score"], cvres["params"]):
#     print(np.sqrt(-meanscore), params)
    # 49992.059040823806 {'max_features': 6, 'n_estimators': 30} best_params_

# 分析最佳模型及其錯誤
# 進行準確預估時, RandomForestRegressor 可以指出每個屬性的相對重要程度
features_importances = grid_search.best_estimator_.feature_importances_
# print(features_importances)
extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
cat_one_hot_attribs = list(encoder.classes_)
attributes = num_attribs + extra_attribs + cat_one_hot_attribs
# print(sorted(zip(features_importances, attributes), reverse = True))
# 上面的結果可以嘗試刪除一些不太有用的特徵, 分析就如同前面的特徵關聯矩陣

# 通過測試集來評估系統
final_model = grid_search.best_estimator_

X_test = strat_test_set.drop("median_house_value", axis = 1)
y_test = strat_test_set["median_house_value"].copy()

X_test_prepared = full_pipeline.transform(X_test)
final_predictions = final_model.predict(X_test_prepared)
final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
# print(final_rmse) # 48430.496180618604


# 7. 展示解決方案(簡報/講稿內容)
# 8. 啟動監控和維護系統(書上重點)