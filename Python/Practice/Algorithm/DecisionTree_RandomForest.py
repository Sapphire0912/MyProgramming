# 決策樹和隨機森林
# 判斷蘑菇是否有毒

# 定義以下類別
# MushroomProblem 實作 validation_data 用於驗證模型
# MushroomRegression 實作 回歸樹
# MushroomClassifier 針對分類問題的實用類別
# MushroomForest 實作 用於將蘑菇分類的隨機森林
# MushroomTree 實作用於將蘑菇分類的決策樹

# Pre
path = "C:\\Users\\kotori\\Desktop\\MyProgramming\\Practice\\MachineLearning\\DataSet\\agaricus-lepiota.data"
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from numpy.random import permutation
from numpy import array_split, concatenate
from sklearn.metrics import mean_squared_error 
import pandas as pd
import numpy as np

# 程式設計&測試
class MushroomProblem(object):
    """
    蘑菇分類問題
    """

    def __init__(self, data_file):
        """
        載入資料檔與參數資料
        :param data_file: CSV file name
        """
        self.data_frame = pd.read_csv(data_file)
        for k in self.data_frame.columns[1:]:
            self.data_frame[k], _ = pd.factorize(self.data_frame[k])
        
        categories = sorted(pd.Categorical(self.data_frame['class']).categories)
        self.classes = np.array(categories)
        self.features = self.data_frame.columns[self.data_frame.columns != 'class']

    @staticmethod
    def __factorize(data):
        y, _ = pd.factorize(pd.Categorical(data['class']), sort = True)
        return y

    def validation_data(self, folds):
        """
        針對已知的 #folds 執行資料分離、分類器訓練與預測
        :param folds: number of folds
        :return: list of numpy.array pairs(prediction, expected)
        """

        df = self.data_frame
        response = []

        assert len(df) > folds

        perms = array_split(permutation(len(df)), folds)

        for i in range(folds):
            train_idxs = list(range(folds))
            train_idxs.pop(i)
            train = []
            for idx in train_idxs:
                train.append(perms[idx])
            
            train = concatenate(train)

            test_idx = perms[i]

            training = df.iloc[train]
            test_data = df.iloc[test_idx]

            y = self.__factorize(training)
            classifier = self.train(training[self.features], y)
            predictions = classifier.predict(test_data[self.features])

            expected = self.__factorize(test_data)
            response.append([predictions, expected])

        return response

class MushroomRegression(MushroomProblem):
    """
    利用 sklearn.DecisionTreeRegressor
    處理蘑菇分類問題
    """

    def train(self, X, Y):
        """
        訓練分類器
        :param X: training input samples
        :param Y: target values
        :return: regressor
        """

        regressor = DecisionTreeRegressor()
        regressor = regressor.fit(X, Y)
        return regressor
    
    def validation(self, folds):
        """
        使用均方差估算分類器
        :param folds: number of folds
        :return: list of MSE per fold
        """

        responses = []
        
        for y_true, y_pred in self.validation_data(folds):
            responses.append(mean_squared_error(y_true, y_pred))
        
        return responses

class MushroomClassifier(MushroomProblem):
    """
    蘑菇分類問題的部分實作
    """

    def validation(self, folds):
        """
        使用混淆矩陣估算分類器
        :param folds: number of folds
        :return: list of confusion matrices per fold
        """

        confusion_matrices = []

        for test, training in self.validation_data(folds):
            confusion_matrices.append(self.confusion_matrix(training, test))
        
        return confusion_matrices
    
    @staticmethod
    def confusion_matrix(train, test):
        return pd.crosstab(test, train, rownames = ['actual'], colnames = ['preds'])
    
class MushroomForest(MushroomClassifier):
    """
    使用 sklearn.RandomForestClassifier
    處理蘑菇分類問題
    """

    def train(self, X, Y):
        """
        訓練分類器
        :param X: training input samples
        :param Y: target values
        :return: classifier
        """

        classifier = RandomForestClassifier(n_jobs = 2)
        classifier = classifier.fit(X, Y)
        return classifier

class MushroomTree(MushroomClassifier):
    """
    使用 sklearn.DecisionTreeClassifier
    處理蘑菇分類問題
    """

    def train(self, X, Y):
        """
        訓練分類器
        :param X: training input samples
        :param Y: target values
        :return: classifier
        """

        classifier = DecisionTreeClassifier()
        classifier = classifier.fit(X, Y)
        return classifier

# 測試
folds = 5
print("Calculating score for Decision Tree:")
tree = MushroomTree(path)
print(tree.validation(folds))

print("Calculating score for Random Forest:")
forest = MushroomForest(path)
print(forest.validation(folds))

print("Calculating score for Decision Tree Regression:")
regression = MushroomRegression(path)
print(regression.validation(folds))
