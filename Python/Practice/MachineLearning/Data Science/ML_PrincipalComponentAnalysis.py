# PCA 主成分分析
# 匯入模塊SOP
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

class PrincipalComponentAnalysis(object):
    '''之前已深入探討監督式學習評估器, 這些評估器利用已經標好標籤的訓練資料為基礎來預測標籤,\n\
       接著來開始檢視幾個非監督式評估器, 它們可以在沒有任何已知標籤的情況下標示出對於資料的\n\
       一些面向.\n\
       主成分分析(PCA)基本上是一種降維演算法, 但是也可以用來進行視覺化, 雜訊過濾, 特徵擷取\n\
       與工程的好用工具.\n'''
    def __init__(self):
        rng = np.random.RandomState(1)
        self.X = X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T

    def Principal_introduce(self):
        '''PCA是一個快速且具有彈性, 用來對資料進行降維的非監督式學習方法, 以下透過檢視一個二維資料\n\
           集是最容易視覺化其行為的方法, 考慮有200個資料點.\n'''
        
        
        # plt.scatter(self.X[:, 0], self.X[:, 1])
        # plt.axis('equal')
        # plt.show()
        # 上圖可以很清楚的辨識出在x, y之間有個近乎線性的關係, 但是之前提到的LR是從x的值來預測y,
        # 在非監督式學習是嘗試去學習關於在 x, y之間的關係

        # 在 PCA 中, 先找出資料中主要軸(principal axes)的一個串列來量化這些關係, 
        # 並且使用這些軸來描述這個資料集, 藉由 Scikit-Learn 的 PCA estimator
        from sklearn.decomposition import PCA
        pca = PCA(n_components = 2)
        pca.fit(self.X)
        # print(pca) # PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
                     #     svd_solver='auto', tol=0.0, whiten=False)

        # 此擬合學習了一些來自於資料的量, 最重要的是成分(components)以及已解釋的變異量(explained variance)
        # print("components: ", pca.components_)
        # [[-0.94446029 -0.32862557]
        #  [-0.32862557  0.94446029]]
        # print("explained_variance: ", pca.explained_variance_) # [0.7625315 0.0184779]
        # 上面這些數字, 可以當成是在輸入資料上的向量加以視覺化, 使用成分來定義向量的方向;
        # 而已解釋變異量則用來定義向量的平方長度

        def draw_vector(v0, v1, ax = None):
            ax = ax or plt.gca()
            arrowprops = dict(arrowstyle = '->', linewidth = 2, shrinkA = 0, shrinkB = 0, color = 'black')
            ax.annotate('', v1, v0, arrowprops = arrowprops)
            
            
        # 繪出資料
        plt.scatter(self.X[:, 0], self.X[:, 1], alpha = 0.3)
        for length, vector in zip(pca.explained_variance_, pca.components_):
            v = vector * 3 * np.sqrt(length)
            draw_vector(pca.mean_, pca.mean_ - v)
        plt.axis('equal')
        # plt.show()
        # 向量表示資料的主要軸, 長度則是描述這個資料的分布時, 該軸的重要程度
        # 更精確的說, 這是一個用來衡量當資料被投射到此軸時的變異量,
        # 每一個投射到主軸上的資料點就是此資料的主要成分(principal component)

        # 從資料軸到主要軸的轉換是一個混合線性二維轉換(affine transformation), 基本上是由
        # 平移, 旋轉, 等比例縮放所組合成的轉換

    def ReduingDimension(self):
        '''使用PCA進行降維: 把一個或數個最小的主要成分移除, 結果就會是可以保留最大資料變異量的\n\
           較低維度之投影, 詳見以下例子.\n'''
        # 沿用初始設定好的資料
        from sklearn.decomposition import PCA
        pca = PCA(n_components = 1)
        pca.fit(self.X)
        X_pca = pca.transform(self.X)
        # print("Original shape:  ", self.X.shape)  # (200, 2)
        # print("transformed shape: ", X_pca.shape) # (200, 1)

        # 為了要清楚降維動作的影響, 把被降維的資料進行反轉換, 並和原始資料畫在一起
        X_inverse = pca.inverse_transform(X_pca)
        plt.scatter(self.X[:, 0], self.X[:, 1], color = 'red', alpha = 0.3)
        plt.scatter(X_inverse[:, 0], X_inverse[:, 1], color = 'blue', alpha = 0.6)
        plt.axis('equal')
        # plt.show()
        # 上圖可以清楚的看到PCA降維後的意義, 把最不重要的主軸移除, 留下來的只有用有高變異的資料成分
        # 變異量小的被切除之後大約可以做為一個衡量在此降維運算中, 有多少資訊被丟棄的情況

    def Application_digitmath(self):
        '''降維的用處並不會只有在二維才那麼明顯, 也讓我們在關注高維度資料時可以更加清晰.'''
        # 以下使用 數字資料
        from sklearn.datasets import load_digits
        digits = load_digits()
        # print(digits.data.shape) # (1797, 64)
        
        from sklearn.decomposition import PCA
        pca = PCA(n_components = 2)  # 把 64維度 降成 2 維度
        projected = pca.fit_transform(digits.data)
        # print(digits.data.shape) # (1797, 64)
        # print(projected.shape)  # (1797, 2)

        # plt.scatter(projected[:, 0], projected[:, 1], c = digits.target, edgecolor = 'None', 
        #             alpha = 0.5, cmap = plt.cm.get_cmap('nipy_spectral', 10))
        # plt.xlabel('component 1')
        # plt.ylabel('component 2')
        # plt.colorbar()
        # plt.show()
        # 完整的資料是一個64個維度由點所組成的雲, 而這些點是每一個資料點沿著最大變異量方向之投影,
        # 在 64維度空間中最佳的延展和旋轉, 可以看出這些數字元(資料集)在二維平面的排列, 
        # 以上是使用非監督式的方法所完成, 在沒有任何參考標籤下所進行的

        # 選擇成分的數量
        # 實務上使用PCA一個非常重要的部分, 是可以有能力去評估要用來描述資料需要多少的成分.
        # 可以藉由檢視把累積的"已解釋變異量比例", 當做是一個成分數量函數來決定
        pca2 = PCA().fit(digits.data)
        plt.plot(np.cumsum(pca2.explained_variance_ratio_))
        plt.xlabel('number of components')
        plt.ylabel('cumulative explained variance')
        plt.show()
        # 透過累積已解釋變異量, 可以用來評量PCA保留資料內容的好壞程度
        # 檢視曲線圖形, 可以幫助我們了解在多次觀察之後降維度程度的表現

    def noisy(self):
        '''使用PCA做雜訊過濾, 若任一個成分的變異量遠大於雜訊的影響, 則相對不容易被雜訊所影響.\n\
           所以, 如果只使用主要成分的最大子集合來重建資料, 則應該要優先保留訊號而丟棄掉那些雜訊.\n\
           以下有個例子.\n'''

        from sklearn.datasets import load_digits
        digits = load_digits()

        def plot_digits(data):
            fig, axes = plt.subplots(4, 10, figsize = (10, 4), 
                                     subplot_kw = {'xticks' : [], 'yticks' : []}, 
                                     gridspec_kw = dict(hspace = 0.1, wspace = 0.1))
            for i, ax in enumerate(axes.flat):
                ax.imshow(data[i].reshape(8, 8), cmap = 'binary', interpolation = 'nearest', 
                          clim = (0, 16))
            plt.show()

        # 先畫出沒有雜訊的輸入資料
        # plot_digits(digits.data)

        # 現在, 加上一些隨機的雜訊以建立雜訊資料訊, 然後再重畫一次
        np.random.seed(42)
        noisy = np.random.normal(digits.data, 4)
        # plot_digits(noisy)

        from sklearn.decomposition import PCA
        # 在充滿雜訊的資料上訓練一個PCA, 並保留50%的變異量
        pca = PCA(0.50).fit(noisy)
        # print("pca.n_components = ", pca.n_components_) # 12

        # 在此, 50%變異量需要12個主要成分; 現在可以計算這些成分, 並使用它們來反轉那些轉換已重建且過濾後的數字元
        components = pca.transform(noisy)
        filtered = pca.inverse_transform(components)
        plot_digits(filtered)
        # 此種訊號保留且雜訊去除的特性, 使得PCA成為一個非常有用的特徵選擇程序
        # 例如: 與其在一個非常高維度的資料中訓練一個分類器, 不如在較低維度的資料中訓練這個分類器,
        # 將會自動的為我們過濾掉在輸入時的隨機雜訊

    def summary(self):
        '''本節討論PCA降維使用在對於高維度資料的視覺化, 雜訊過濾, 以及高維度資料特徵選擇的應用上.\n\
           因為PCA的可解釋特性以及多面性, 已經在許多領域以及學門上非常有效且廣泛的運用.\n\
           PCA主要的缺點, 容易被資料中的異常值所高度影響, 因此發展了許多PCA變形, 這些變形中有許\n\
           多是重複丟棄不太能被初始成分所描述的資料點; Scikit-Learn 包含了一些PCA變形: \n\
           如: RandomizedPCA, SparsePCA, 此兩者都在 sklearn.decomposition中; 前者使用一個非\n\
           決定性方法在非常高維的資料中, 以快速的近似前面幾個主要成分, 後者則引入一個正規化術語\n\
           (regularization term) <- LR, 用來提供強化成分的稀疏特性.'''


mypca = PrincipalComponentAnalysis()
# help(pca)
# mypca.Principal_introduce()
# mypca.ReduingDimension()
# mypca.Application_digitmath()
# mypca.noisy()
# help(mypca.summary)