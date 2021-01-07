# 貝氏分類器
# 是一種非常快速且簡單的分類演算法, 經常適用於非常高維度的資料
# 因為此演算法非常快而且可調的參數非常少, 常被拿來當作針對某一分類問題應急用的基線時非常實用

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

class BayesianClassification():
    def introduce(self):
        '''Naive Bayes分類器建立在 Bayesian分類法之上.\n\
               它所依賴的Bayes定理, 是用來描述統計量條件機率關係的等式. \n\
               若已經給了一些觀察過的特徵標籤之機率寫成 P(L|features), 貝氏定理可以使用可計算的量來表達. \n\
               \tP(L|features) = P(feature|L) * P(L) / P(features)\n\
               # supplement: P(L|features) = P(L∩features)/P(features)  ∩表示交集.\n\
               若我們嘗試在2個標籤之間做決定, 假設2個標籤分別為L1, L2, \n\
               \tP(L1|features) / P(L2|features) = P(features|L1) * P(L1) / P(features|L2) * P(L2)\n\
               現在我們需要的就是可以對每一個標籤計算 P(features|L1)的模型, 此模型稱為生成模型(generative model),\n\
               因為它指定了產生這些資料的假定隨機程序;對於每個標籤指定一個生成模型是貝氏分類器的主要部分.\n\
               貝氏分類器的不同型態依賴在關於資料不同的單純假設, 以下會有一些例子.\n
            '''
    
    def GaussianNaiveBayes(self):
        '''此分類器是假設每一個標籤的資料都是來自於一個簡單的高斯分布(simple Gaussian distribution)'''
        # 假如有以下的資料
        from sklearn.datasets import make_blobs
        x, y = make_blobs(100, 2, centers = 2, random_state = 2, cluster_std = 1.5)
        plt.scatter(x[:, 0], x[:, 1], c = y, s = 50, cmap = 'RdBu')
        # plt.show()

        # 建立一個簡單的模型, 並預測其標籤
        explanation = "在此分類中可以稍微看到一個彎曲的邊界. 一般而言, 高斯樸素貝氏的邊界都是二次方程式"
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        model.fit(x, y)
        rng = np.random.RandomState(0)
        xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
        ynew = model.predict(xnew)
        # plt.scatter(x[:, 0], x[:, 1], c = y, s = 50, cmap = 'RdBu')
        lim = plt.axis()
        plt.scatter(xnew[:, 0], xnew[:, 1], c = ynew, s = 20, cmap = 'BrBG', alpha = 0.1)
        plt.axis(lim)
        # print(explanation)
        # plt.show()

        # 貝氏定理其中一個不錯的點是, 在本質上允許機率分類, 使得可以利用predict_proda方法來進行計算
        yprod = model.predict_proba(xnew)
        print(yprod[-8:].round(2))
        # [[0.89 0.11]
        # [1.   0.  ]
        # [1.   0.  ]
        # [1.   0.  ]
        # [1.   0.  ]
        # [1.   0.  ]
        # [0.   1.  ]
        # [0.15 0.85]]

        # 上面這些欄的內容列出了第一個和第二個的後驗機率. 如果在尋找分類中對於不確定性的評估, 
        # 像這樣的貝氏方式是很有用的方法.
        # 但是, 最終分類將只會和模型假設所推導的一樣好, 這也是為什麼高斯樸素貝氏經常沒有辦法產生非常好的結果
        # 然而, 在許多的情況中, 這個假設不至於讓高斯樸素貝氏不能成為一個好用的方法

    def MultinomialNaiveBayes(self, s = None):
        '''多項式樸素貝氏, 它的特徵被假設是從一個簡單的多項式分佈產生而來的\n\
           多項式分佈描述在一個數量的類別中觀察到的次數之頻率, 而使得此種多項式樸素貝式非常適合於其特徵是\n\
           代表次數或計次比率的地方.\n\
           這個概念和上一個一樣, 原本資料分佈是使用最適高斯, 而改為使用最適多項式分佈來取代資料分佈.'''

        # Example: 文字的分類
        # 多項式樸素貝氏經常會被用到的地方是文字的分類工作, 其中特徵是和要被分類的文件中文字出現的次數或頻率相關的
        # 在此將從20個新聞群組語料庫中使用稀疏文字計數特徵, 以展示可以如何把這些簡短的文件分類

        from sklearn.datasets import fetch_20newsgroups
        data = fetch_20newsgroups()
        # print(data.target_names)
        
        # 為了簡單起見, 選用少部分的類別, 接著下載訓練和測試資料集
        categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space', 'comp.graphics']
        train = fetch_20newsgroups(subset = 'train', categories = categories)
        test = fetch_20newsgroups(subset = 'test', categories = categories)
    
        # 以下是從資料中所得到的其中一個項目的代表性內容
        # print(train.data[5])

        # 為了使用這些資料進行機器學習, 首先要把每個字串的內容轉換成數值向量, 使用TF-IDF
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.pipeline import make_pipeline

        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(train.data, train.target)
        labels = model.predict(test.data)

        # 使用測試資料完成預測標籤後, 使用混淆矩陣來驗證, 顯示真實結果與預測之間以了解評估器的效能
        from sklearn.metrics import confusion_matrix
        mat = confusion_matrix(test.target, labels)
        sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False, 
                    xticklabels = train.target_names, yticklabels = train.target_names)
        plt.xlabel('true label')
        plt.ylabel('predicted label')
        # plt.show()

        # 現在有一個工具可以判斷任意字串的類別, 使用在這個管線中的predict()方法
        if s != "None":
            pred = model.predict([s])
            return train.target_names[pred[0]]


    def summary(self):
        '''貝氏分類器優點: 不管訓練or預測都非常快速; 提供了直接的機率預測; 易於解讀; 可調變參數少\n\
           但是一般而言它在更複雜的模型上並不一定執行一樣好.\n\
           通常在以下情況時會表現得特別好: 當樸素(naive)的假設正好符合資料時; 區分非常好的類別來說\n\
           , 模型的複雜度顯得不是這麼重要; 對於非常高維度的資料, 模型複雜度也比較不重要.'''

NBC = BayesianClassification()
help(NBC.introduce)
# NBC.GaussianNaiveBayes() # 用 help 可以查看函數的解說
# NBC.MultinomialNaiveBayes() # 用 help 可以查看函數的解說

s = 'sending a payload to the ISS'
# print(NBC.MultinomialNaiveBayes(s)) # sci.space
# help(NBC.MultinomialNaiveBayes)
# help(NBC.summary)