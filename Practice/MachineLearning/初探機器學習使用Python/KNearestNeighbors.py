# KNN(K-最近鄰)
# 西雅圖的房屋估價
path = "C:\\Users\\kotori\\Desktop\\MyProgramming\\Practice\\MachineLearning\\DataSet\\king_county_data_geocoded.csv"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 使用 KNN 回歸( Scipy.spatial KDTree 建構 KNN 回歸 )
import random
import sys
from scipy.spatial import KDTree
from sklearn.metrics import mean_absolute_error

# print(sys.getrecursionlimit()) # <- 取得當前遞迴上限層數 默認: 3000
sys.setrecursionlimit(10000) # <- 設定遞迴上限層數

class Regression(object):
    """
    進行 KNN 回歸
    """
    def __init__(self):
        self.k = 5
        self.metric = np.mean
        self.kdtree = None
        self.houses = None
        self.values = None

    def set_data(self, houses, values):
        """
        設定房產相關資料
        :param houses: pandas.DataFrame with houses parameters
        :param values: pandas.DataFrame with houses values
        """
        self.houses = houses
        self.values = values
        self.kdtree = KDTree(self.houses)
    
    def regress(self, query_point):
        """
        以特定的參數計算房屋預估的價值
        :param query_point: pandas.Series with house parameters
        :return: house value
        """

        _, indexes = self.kdtree.query(query_point, self.k)
        value = self.metric(self.values.iloc[indexes])
        if np.isnan(value):
            raise Exception("Unexpected result")
        else:
            return value

# KNN 驗證(使用交叉驗證)
class RegressionTest(object):
    """
    採用 King County 房產資料來計算
    與描繪 KNN 回歸誤差率
    """

    def __init__(self):
        self.houses = None
        self.values = None
    
    def load_csv_file(self, csv_file, limit = None):
        """
        載入含有房地產資料的 CSV 檔案
        :param csv_file: CSV file name
        :param limit: number of rows of file to read
        """

        houses = pd.read_csv(csv_file, nrows = limit)
        self.values = houses['AppraisedValue']
        houses = houses.drop('AppraisedValue', 1)
        houses = (houses - houses.mean()) / (houses.max() - houses.min())
        self.houses = houses
        self.houses = self.houses[['lat', 'long', 'SqFtLot']]

    def tests(self, folds):
        """
        計算一連串測試項目的平均絕對誤差(mean absolute error)
        :param folds: how many times split the data 
        :return: list of error value
        """

        holdout = 1 / float(folds)
        errors = []
        for _ in range(folds):
            values_regress, values_actual = self.test_regression(holdout)
            errors.append(mean_absolute_error(values_actual, values_regress))
        
        return errors
    
    def test_regression(self, holdout):
        """
        計算樣本外資料的回歸
        :param holdout: part of the data for testing [0, 1]
        :return: tuple(y_regression, values_actual)
        """

        test_rows = random.sample(self.houses.index.tolist(), int(round(len(self.houses) * holdout)))
        train_rows = set(range(len(self.houses))) - set(test_rows)
        df_test = self.houses.loc[test_rows]
        df_train = self.houses.drop(test_rows)

        train_values = self.values.loc[train_rows]
        regression = Regression()
        regression.set_data(houses = df_train, values = train_values)

        values_regr = []
        values_actual = []

        for idx, row in df_test.iterrows():
            values_regr.append(regression.regress(row))
            values_actual.append(self.values[idx])
        
        return values_regr, values_actual

    def plot_error_rates(self):
        """
        描繪 MAE(平均絕對誤差) 與 folds
        """

        folds_range = range(2, 11)
        errors_df = pd.DataFrame({'max': 0, 'min': 0}, index = folds_range)
        for folds in folds_range:
            errors = self.tests(folds)
            errors_df['max'][folds] = max(errors)
            errors_df['min'][folds] = min(errors)
        errors_df.plot(title = "Mean Absolute Error of KNN over different folds_range")
        plt.xlabel('#folds_range')
        plt.ylabel('MAE')
        plt.show()

def main():
    regression_test = RegressionTest()
    regression_test.load_csv_file(path, 100)
    regression_test.plot_error_rates()

if __name__ == '__main__':
    main()