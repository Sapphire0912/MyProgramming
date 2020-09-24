# KNN Algorithm
# InputData: a Sample
# (one-dimension) process: 
# 量化資料 -> 特徵矩陣(two-dimension features array) -> 目標陣列(labels) # belong Datasets
# 輸入資料 -> KNN Algorithm -> 輸出預測結果
# OutputData: predict result(label)
# Ex x(a Sample) -> function(KNN Algorithm) -> y(result/label)

import numpy as np
from sklearn import preprocessing as pp

class KNN(object):
    def __init__(self, k_neighbors):
        self.k = k_neighbors
    
    def datasets(self, samples, feature, labels):
        le = pp.LabelEncoder()
        self.samples = le.fit_transform(samples)
        self.features = list(zip(self.samples, le.fit_transform(feature)))
        self.target = le.fit_transform(labels)
    
    def _distance(self, datas): # 對應sklearn的model.fit
        pass
    
    def predicts(self, textdata):
        self.result = _distance(textdata) # 先暫時把輸入資料設定為已量化的資料
        return self.result