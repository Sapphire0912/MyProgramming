# K-Nearnest Neighbors
# Supervised Learning (Cluster)

def explain():
    s = '''
    # KNN 演算法
    # K-Nearest Neighbor
    # KNN 在 ML(Machine Learn) 裡十分常用的演算法, 同時也非常易理解
    # KNN 屬於ML監督式學習的一種

    # 一個輸入樣本(K), 根據投票的方式來把輸入樣本分類
    # K盡量是個偶數, 而不要取奇數, 以免當票數相同時, 不知如何做分類

    # 自定義數據集(定義特徵Feature)
    # 有 weather and temp and 標籤play
    # 假設天氣如何, 溫度如何, 我們是否出去玩

    # weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny',
    #            'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']

    # temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 
    #       　'Mild', 'Mild', 'Mild', 'Hot', 'Mild']

    # play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

    # from sklearn import preprocessing

    # 創建 LabelEncoder
    # le = preprocessing.LabelEncoder()

    # 把字串轉換成數字
    # weather_encoded = le.fit_transform(weather)
    # print(weather_encoded)
    # temp_encoded = le.fit_transform(temp)
    # print(temp_encoded)
    # label = le.fit_transform(play)
    # print(label)

    # 把特徵(weather, temp)變成元組列表 
    # features = list(zip(weather_encoded, temp_encoded))
    # print(features)

    # 補充: zip(): 把可迭代對象逐一打包成一個元組, 元素個數與最短的長度一致
    # Ex. a = [1, 2, 3], b = [4, 5, 6], c = [4, 5, 6, 7, 8]
    # zip(a, b); result: [(1, 4), (2, 5), (3, 6)]
    # zip(a, c); result: [(1, 4), (2, 5), (3, 6)]

    # 在此使用 Scikit-Learn 裡面的 KNN 模型來操作
    # from sklearn.neighbors import KNeighborsClassifier

    # model = KNeighborsClassifier(n_neighbors = 3) # k = 3 的意思

    # 使用訓練集合來訓練模型
    # model.fit(features, label) 

    # 預測輸出
    # 假設 天氣陰天 溫度涼風 是否可以出去玩
    # predicted = model.predict([[0, 2]]) # 0: Overcast, 2: Mild
    # 內部順序由ASCII碼排列(由小到大) 
    # print(predicted) # 0: No, 1: Yes

    # model2 = KNeighborsClassifier(n_neighbors = 5)
    # model2.fit(features, label)
    # predicted = model2.predict([[2, 2]])
    # print(predicted) # 0



    # 使用sklearn 的 datasets
    # from sklearn import datasets

    # 載入資料庫
    # wine = datasets.load_wine()
    # print(dir(wine)) # 顯示wine的目錄 
    # line 68 O/P: ['DESCR', 'data', 'feature_names', 'target', 'target_names']

    # print(wine.data[0:3]) # data 前三條紀錄
    # line 71 O/P: 
    #  [[1.423e+01 1.710e+00 2.430e+00 1.560e+01 1.270e+02 2.800e+00 3.060e+00
    #   2.800e-01 2.290e+00 5.640e+00 1.040e+00 3.920e+00 1.065e+03]
    #  [1.320e+01 1.780e+00 2.140e+00 1.120e+01 1.000e+02 2.650e+00 2.760e+00
    #   2.600e-01 1.280e+00 4.380e+00 1.050e+00 3.400e+00 1.050e+03]
    #  [1.316e+01 2.360e+00 2.670e+00 1.860e+01 1.010e+02 2.800e+00 3.240e+00
    #   3.000e-01 2.810e+00 5.680e+00 1.030e+00 3.170e+00 1.185e+03]]

    # print(wine.target)
    # line 80 O/P:
    # [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    #  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    #  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    #  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    #  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2]

    # print(wine.feature_names)
    # line 88 O/P :
    # ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids',
    #  'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 
    #  'proline']

    # print(wine.target_names)
    # line 94 O/P:
    # ['class_0' 'class_1' 'class_2']

    # print(wine.data.shape) # (178, 13) <- (target, feature_names)

    # from sklearn.model_selection import train_test_split as tts
    # train_test_split() 用於將矩陣隨機劃分為 訓練子集和測試子集, 
    # 並返回劃分好的(訓練集,測試集)樣本和(訓練集,測試集)標籤
    # x_train, x_test, y_train, y_test = tts(wine.data, wine.target, test_size = 0.3)
    # test_size = 0.3 代表 70% 訓練資料 和 30% 測試資料

    # 假設 k = 5
    # knn = KNeighborsClassifier(n_neighbors = 11)
    # knn.fit(x_train, y_train)
    # y_pred = knn.predict(x_test)
    # print(y_pred)

    # 評估KNN預測的準確性 使用如下:
    # from sklearn import metrics

    # 計算出KNN預測的準確性
    # print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
    # 正確率: 77.77777777777778%(k = 5)
    # 不同的K值 會影響準確率

    # KNN的優缺點
    # 優點: 與其他演算法相比, KNN的訓練階段快很多, 沒有必要訓練模型進行泛化
    #       KNN在非線性數據的情況下非常有用, 它可以與回歸問題一起使用
    # 缺點: KNN 在測試時間和記憶體方面比較慢且成本高
    #       它需要大容量存儲器來儲存整個數據集以進行預測
    #       KNN需要縮放數據, 因為使用兩個數據點之間的歐基里德平面對幅度敏感
    #       具有高幅度的特徵要比低幅度的特徵更重, 所以KNN不適合大數據

    # 改善KNN:
    # 對數據進行標準化 (normalizing data), 將數據範圍設定在 0 ~ 1 之間
    # KNN 不適合大數據, 因此要進行降維來改善性能. 處理缺失值也助於改善結果
    '''
    return s

def situation1():
    # situation 1:
    # 自定義資料集(用來預測)
    weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny',
               'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']

    temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 
            'Mild', 'Mild', 'Mild', 'Hot', 'Mild']

    play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    weather_encoded = le.fit_transform(weather)
    temp_encoded = le.fit_transform(temp)
    labels = le.fit_transform(play)
    
    features = list(zip(weather_encoded, temp_encoded))

    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(features, labels)
    predicted = model.predict([[0, 2]])
    print(predicted)

def situation2():
    from sklearn import datasets
    wine = datasets.load_wine()
    from sklearn.model_selection import train_test_split as tts
    x_train, x_test, y_train, y_test = tts(wine.data, wine.target, test_size = 0.3)
    # print("x_train data: \n", x_train)
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 5)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    # print(y_pred)
    from sklearn import metrics 
    accuracy = metrics.accuracy_score(y_test, y_pred)
    # print("Accuracy: %.3f %%" % (accuracy * 100))


# print(explain())
# situation1()
situation2()