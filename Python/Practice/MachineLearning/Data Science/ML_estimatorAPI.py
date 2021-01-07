# Scikit-Learn API 是依照以下原則來設計的
# https://arxiv.org/abs/1309.0238
# 一致性(Consistancy):
# 所有的物件共享一個共同的介面, 該介面來自於方法的一個有限集合
# 可觀察(Inspection):
# 所有指定的參數值都被當作是公用的屬性
# 有限的個體階層(Limited object hierarchy):
# 只有演算法被以 Python 類別表示(Numpy, Pandas DataFrame, Scipy稀疏矩陣), 參數名稱使用標準Python字串
# 合成的(Composition):
# 許多ML的工作可以被表示成一系列更基本的演算法, 而Scikit-Learn盡可能用此種方式
# 合理的預設值(Sensible defaults):
# 當模型需要使用者指定的參數時, 程式庫會定義一個適當的預測值

# API 使用基礎
# Step1: 從 Scikit-Learn estimator 匯入適合的模型
# Step2: 藉由指定資料值來實體化類別, 以選擇模型的超參數(hyperparameters)
# Step3: 把資料安排到特徵矩陣(features matrix)以及目標向量(label)
# Step4: 藉由呼叫執行實例的 fit() 方法, 把資料擬合出一個模型
# Step5: 套用此模型到新的資料, 如果是SL通常使用predict(), UL則使用transform() or predict()

def LR_Example():
    # Supervised Learning for Example: Simple Linear Regression
    # 線性回歸, 使用一條線擬合到(x, y)資料的例子
    import matplotlib.pyplot as plt
    import numpy as np

    rng = np.random.RandomState(42)
    x = 10 * rng.rand(50)
    y = 2 * x - 1 + rng.randn(50) # normal distribution

    # Step1: 匯入線性回歸模型
    from sklearn.linear_model import LinearRegression as LR

    # Step2: 選擇模型的超參數
    # ! 模型的類別不等於模型的執行實例
    # 選項設定往後會詳細討論(這裡使用fit_intercept 超參數去實例化LR類別以及指定擬合的截距)
    model = LR(fit_intercept = True)
    print(model)
    # line39 O/P: LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

    # Step3: 安排資料到特徵矩陣和目標向量
    # 把資料x變成一個大小是[n_samples, n_features]的矩陣
    x = x[:, np.newaxis]

    # Step4: 擬合模型
    model.fit(x, y)
    # print("斜率= ", model.coef_) # 大概1.776
    # print("截距= ", model.intercept_) # 大概 -0.90

    # Step5: 預測未知資料的標籤
    xfit = np.linspace(-1, 11) # 新資料
    xfit = xfit[:, np.newaxis]

    yfit = model.predict(xfit)
    # 把資料視覺化
    # plt.scatter(x, y)
    # plt.plot(xfit, yfit)

    # plt.show()

def SL_Iris_Example():
    # Supervised Learning: Iris classification
    # Que: 給予一個針對部分鳶尾花訓練過的模型, 用在預測剩餘的標籤之表現會有多好? 
    import seaborn as sns
    iris = sns.load_dataset('iris')
    X_iris = iris.drop('species', axis = 1)
    y_iris = iris['species']

    # 根據問題, 將採用一個極簡單的生成模型, 也就是 Gaussian naive Bayes
    # Gaussian naive Bayes 藉由己設每個類別都是從一個軸對齊(axis-aligned)高斯分布進行的
    # 速度快而且不需要選用超參數, Gaussian naive Bayes 經常是作為基線分類方法一個不錯的模型
    # 單純貝氏分類器(Naive Bayes Classifiers)

    # 在還沒有見過的資料上評估模型, 因此將把資料分成訓練集(training set)和測試集(testing set)
    # 使用 train_test_split 函式
    from sklearn.model_selection import train_test_split as tts
    X_train, X_test, y_train, y_test = tts(X_iris, y_iris, random_state = 1)

    # 資料排列好後, 就進行一開始所講述的5步驟
    from sklearn.naive_bayes import GaussianNB # Step1 選擇模型類別
    model = GaussianNB()  # Step2 實體化模型
    model.fit(X_train, y_train) # Step3 對資料擬合此模型
    y_model = model.predict(X_test) # 對新資料進行預測

    # 檢視正確率
    from sklearn import metrics
    print("Accuracy: ", metrics.accuracy_score(y_test, y_model))
    # Accuracy:  0.9736842105263158 
    # 正確率高達 97% 

def UL_Iris_Example():
    # Unsupervised Learing: Iris classification
    # 降維的目的: 是否有合適的較低維度表示方法可以保留資料中重要的特徵
    # 降維 經常被使用在以視覺化為目標的情況

    # 主成分分析(Principal Component Analysis): 快速的線性維度降低的方法
    # 要求此模型傳回2個成分(Component)

    import seaborn as sns
    import matplotlib.pyplot as plt
    iris = sns.load_dataset('iris')
    X_iris = iris.drop('species', axis = 1)
    y_iris = iris['species']

    # 同樣依照上面的5個步驟
    from sklearn.decomposition import PCA
    model = PCA(n_components = 2)
    model.fit(X_iris) # PCA 模型的 y 不需要設定
    X_2D = model.transform(X_iris)  # 把資料轉換成兩個維度

    iris['PCA1'] = X_2D[:, 0]
    iris['PCA2'] = X_2D[:, 1]

    sns.lmplot("PCA1", "PCA2", hue = 'species', data = iris, fit_reg = False)
    plt.show()

def UL_Iris_Example2():
    # Supervised Learning: Iris Clustering
    # 集群演算法: 嘗試在對於任何標籤均沒有任何參考的情況下分成不同的群組
    # GMM (Gaussian mixture model) 高斯混合模型

    import seaborn as sns
    import matplotlib.pyplot as plt
    iris = sns.load_dataset('iris')
    X_iris = iris.drop('species', axis = 1)
    y_iris = iris['species']

    from sklearn.mixture import GaussianMixture as GMM
    model = GMM(n_components = 3, covariance_type = 'full')
    model.fit(X_iris)
    y_gmm = model.predict(X_iris)


    from sklearn.decomposition import PCA
    model = PCA(n_components = 2)
    model.fit(X_iris)
    X_2D = model.transform(X_iris)
    
    iris['cluster'] = y_gmm
    iris['PCA1'] = X_2D[:, 0]
    iris['PCA2'] = X_2D[:, 1]

    sns.lmplot("PCA1", "PCA2", hue = 'species', data = iris, col = 'cluster', fit_reg = False)
    plt.show()

# LR_Example()
# SL_Iris_Example()
# UL_Iris_Example()
# UL_Iris_Example2()

def writting():
    # 應用: 探索手寫字元
    # 光學辨識問題中的 手寫字元辨識
    # 使用Scikit-Learn 已經經過預處理的字元集

    # 載入資料和視覺化
    from sklearn.datasets import load_digits
    digits = load_digits()
    print(digits.images.shape) # (1797, 8, 8)
    # 代表這筆資料是一個three-dimensional array
    # 共有 1797個樣本, 每一個樣本都是由 8x8 格的像素所組成的

    # 繪製前100個
    import matplotlib.pyplot as plt
    # fig, axes = plt.subplots(10, 10, figsize = (8, 8), subplot_kw = {'xticks': [], 'yticks': []},
    #                          gridspec_kw = dict(hspace = 0.1, wspace = 0.1))

    # for i, ax in enumerate(axes.flat):
        # enumerate(): 對於一個可迭代的對象, enumerate()將對象組成索引序列, 可以同時取得索引和值
        # Reference: https://www.cnblogs.com/lemonbit/p/6238402.html
        # axes.flat: 屬於numpy.ndarray.flat 
        # Ex:
            # import numpy as np 
            # a = np.array([[2,3], [4,5], [6,7]])
            # for i in a.flat: 
            #     print(i) # 2 3 4 5 6 7
        
        # 這裡的 i 為 索引值, ax 為值
        # ax.imshow(digits.images[i], cmap = 'binary', interpolation = 'nearest')
        # ax.text(0.05, 0.05, str(digits.target[i]), transform = ax.transAxes, color = 'green')
    # plt.show()

    # 為了要讓資料可議在 Scikit-Learn 工作, 必須轉換成 特徵矩陣:[n_samples, n_features]
    # 可以透過把每一個在影像中的像素當成一個特徵, 把像素平面化(8x8 -> 64x1)
    # 接著 目標陣列 代表每一個數字元的標籤, 分別被放在 data, target屬性裡面

    X = digits.data
    print(X.shape) # (1797, 64)
    y = digits.target
    print(y.shape) # (1797,)

def UL_digits_RD():
    # Unsupervised Learning: Reduing dimensional
    # 使用 流形學習演算法(manifold learning algorithm)
    from sklearn.datasets import load_digits
    digits = load_digits()

    from sklearn.manifold import Isomap
    iso = Isomap(n_components = 2)
    iso.fit(digits.data)
    data_projected = iso.transform(digits.data)
    print(data_projected.shape) # (1797, 2)
    # 已經把資料降成2維了

    # 把資料畫出來看是否從結構中學習到甚麼
    import matplotlib.pyplot as plt
    # plt.scatter(data_projected[:, 0], data_projected[:, 1], c = digits.target, 
    #             edgecolor = 'none', alpha = 0.5, cmap = plt.cm.get_cmap('twilight', 10))
    # plt.colorbar(label = 'difit label', ticks = range(10))
    # plt.clim(-0.5, 9.5)

    # plt.show()

    # 數字元的分類
    from sklearn.model_selection import train_test_split as tts
    Xtrain, Xtest, ytrain, ytest = tts(digits.data, digits.target, random_state = 0)

    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(Xtrain, ytrain)
    y_model = model.predict(Xtest)

    # 檢查正確率
    from sklearn.metrics import accuracy_score
    print(accuracy_score(ytest, y_model))
    # Accuracy: 0.8333333333333334

    # 單純只有正確率無法得知是哪裡出錯了, 所以使用混淆矩陣(confusion matrix)來計算
    from sklearn.metrics import confusion_matrix
    import seaborn as sns
    mat = confusion_matrix(ytest, y_model)

    # sns.heatmap(mat, square = True, annot = True, cbar = False)
    # plt.xlabel('predicted value')
    # plt.ylabel('true value')
    # 這裡的圖形可以顯示出 錯誤的地方(此處以數據呈現)
    # plt.show()

    # 用視覺化的方式檢視(用前100筆資料)
    fig, axes = plt.subplots(10, 10, figsize = (8, 8), subplot_kw = {'xticks': [], 'yticks': []},
                             gridspec_kw = dict(hspace = 0.1, wspace = 0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(digits.images[i], cmap = 'binary', interpolation = 'nearest')
        ax.text(0.05, 0.05, str(digits.target[i]), transform = ax.transAxes, 
                color = 'green' if (ytest[i] == y_model[i]) else 'red')
    plt.show()

# writting()
UL_digits_RD()