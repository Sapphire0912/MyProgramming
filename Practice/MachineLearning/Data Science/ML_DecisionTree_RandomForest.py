# 決策樹&隨機森林
# 匯入模塊SOP
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

class RandomForests(object):
    '''隨機森林是一個無母數的演算法.\n\
       隨機森林是整體(ensemble)方法的一個例子, 它是藉由蒐集來自於較簡單評估器結果的方法.\n\
       它的總和會比部分的結果還要更好, 也就是說, 來自於多數評估器的投票結果會形成比任一\n\
       單獨的評估器還要好的結果'''
    
	# 視覺化資料
    def visualize_classifier(self, model, X, y, ax = None, cmap = 'rainbow'):
        ax = ax or plt.gca()

		# 繪出訓練資料點
        ax.scatter(X[:, 0], X[:, 1], c = y, s = 30, cmap = cmap)
        ax.axis('tight')
        ax.axis('off')
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        # 擬合一個評估器
        model.fit(X, y)
        xx, yy = np.meshgrid(np.linspace(*xlim, num = 200), 
                                np.linspace(*ylim, num = 200))
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        # *xlim = (a, b) xx = 從 a 到 b 分割成 num參數值 等分
        # xx.ravel() -> n維度 轉換成 1維
        # c_[a, b]: 把a, b的每個點 個別對應[a1, b1],[a2, b2]...形成一個新列表

        # 建立結果的色彩圖形
        n_classes = len(np.unique(y))
        contours = ax.contourf(xx, yy, Z, alpha = 0.3, levels = np.arange(n_classes + 1) - 0.5,
                               cmap = cmap)
        ax.set(xlim = xlim, ylim = ylim)
        plt.show()


    def DecisionTree(self):
        '''隨機森林是建立在決策樹上的一個整體學習法, 基於這個理由, 將從討論決策樹開始.\n\
           決策樹是用在分類或進行標籤非常直覺的方法: 可以從0開始詢問一連串設計過的問題\n\
           來分類. 例如, 想要建立一個用來分類在健行時遇到某種動物的決策樹, 直覺的想法\n\
           是用二分法(兩條腿/四條腿?)來讓它有效率, 在一個建構良好的決策樹, 每個問題近乎\n\
           可以把資料做對半分割. 在ML實作中, 問題通常是沿軸方式分割資料, 也就是每一個樹\n\
           中的節點會使用其中一種特徵值把資料分成2組. 見以下例子\n'''
        
        # 建立一個決策樹
        # 考慮有一個二維資料, 其中共有4個標籤
        from sklearn.datasets import make_blobs
        X, y = make_blobs(n_samples = 300, centers = 4, random_state = 0, cluster_std = 1.0)
        # plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'rainbow')
        # plt.show()

        # 依據此資料建立簡單決策樹反覆沿著一軸或其他的軸, 根據某一個量值分割資料
        # 而在每一層資料中依據其中每一點多數票對一個新區域設定標籤
        # 使用 Scikit-Learn 的 DecisionTreeClassifier estimator
        from sklearn.tree import DecisionTreeClassifier as DTC
        tree = DTC().fit(X, y)
        self.visualize_classifier(DTC(), X, y)
        # 參考: 決策樹與過度擬合的問題及解決(使用交叉驗證是其中一種方法)

    def RandomForest(self):
        '''把多個過度擬合的評估器合併起來可以減少此過度擬合的影響, 集成評估器的基礎概念就稱為bagging集成方法.\n\
           bagging 使用一些平行運行的評估器的一個集成, 它們每一個都過度擬合了資料, 而其平均結果去可以是較好\n\
           的分類結果. 其中一種使用隨機決策樹的方法, 就是隨機森林.\n'''
        # 沿用先前的資料
        from sklearn.datasets import make_blobs
        X, y = make_blobs(n_samples = 300, centers = 4, random_state = 0, cluster_std = 1.0)

        # 可以透過 Scikit-Learn 的 BaggingClassifier estimator
        from sklearn.tree import DecisionTreeClassifier as DTC
        from sklearn.ensemble import BaggingClassifier

        tree = DTC()
        bag = BaggingClassifier(tree, n_estimators = 100, max_samples = 0.8, random_state = 1)

        bag.fit(X, y)
        # self.visualize_classifier(bag, X, y)
        # 上圖用來進行邊界決策的一個整體隨機決策樹

        # 在此例中, 把資料隨機擬合到每一個評估器, 其中每一個隨機子集合訓練資料點的80%(max_samples參數值)
        # 實務上, 在選用要分割的內容時, 加入一些隨機性會讓決策樹更有效率;
        # 例如, 當決定以哪一個特徵分割時, 此種隨機樹可能會從上面的幾個特徵來選擇(參考說明文件)

        # Scikit-Learn 中, 最佳化的隨機決策樹整體被以 RandomForestClassifier 評估器來實作,
        # 它會自動處理關於隨機程序的所有細節, 只要選擇評估器的數量, 會以平行運算的方式擬合出所有樹的集成
        from sklearn.ensemble import RandomForestClassifier as RFC
        models = RFC(n_estimators = 100, random_state = 0)
        # self.visualize_classifier(models, X, y)
        # 上圖以 random forest 進行邊界決策, 它是一個最佳化過隨機決策樹的集成
        # 透過對超過100個隨機擾動模型的平均, 所得到的最終模型更接近我們直覺上所認為這些資料應該如何被分割的樣子

        # 隨機森林回歸
        # 使用 Scikit-Learn RandomForestRegressor
        rng = np.random.RandomState(42)
        x = 10 * rng.rand(200)
        def model(x, sigma = 0.3):
            fast_oscillation = np.sin(5 * x)
            slow_oscillation = np.sin(0.5 * x)
            noise = sigma * rng.randn(len(x))

            return slow_oscillation + fast_oscillation + noise
        y = model(x)
        plt.errorbar(x, y, 0.3, fmt = 'o')
        # plt.show()
        # 上圖是要使用在隨機森林回歸的資料

        # 使用 RandomForestRegressor
        from sklearn.ensemble import RandomForestRegressor as RFR
        forest = RFR(200)
        forest.fit(x[:, None], y)

        xfit = np.linspace(0, 10, 1000)
        yfit = forest.predict(xfit[:, None])
        ytrue = model(xfit, sigma = 0)

        plt.errorbar(x, y, 0.3, fmt = 'o', alpha = 0.5)
        plt.plot(xfit, yfit, '-r')
        plt.plot(xfit, ytrue, '-k', alpha = 0.5)
        plt.show()
        # 在此, 真實的模型被以平滑的曲線來呈現, 而隨機森林模型則以鋸齒狀的曲線表示
        # 無母體隨機森林模型的彈性足以擬合多段的資料, 而且不需要去指定一個多段的模型

    def summary(self):
        '''包含了集成評估器的概念, 尤其是隨機森林模型, 它是一個隨機決策樹的集成.\n\
           包含了以下的幾個優點:\n\
           1. 因為基礎是決策樹, 所以不論是訓練還是預測非常快速. 另外, 每棵個別的樹都是獨立的,\n\
              所以每一項工作都可以直接被平行處理.\n\
           2. 多棵樹允許使用機率上的分類: 在所有的評估器進行過半數投票, 具有機率上的評估.\n\
              (在 Scikit-Learn 以 predict_proba() 方法存取)\n\
           3. 無母樹的模型具有彈性, 因此可以被執行在那些其他評估器擬合不足的工作上.\n\
           缺點: 隨機森林主要的缺點是結果不容易被解釋; 若打算從分類模型中描繪其意義與結論,\n\
                 此模型將不是最佳選擇.\n'''
rf = RandomForests()
# help(rf)
# help(rf.DecisionTree)
# rf.DecisionTree()
# rf.RandomForest()
help(rf.summary)