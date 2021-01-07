# 高斯混合模型(Gaussian Mixture Models)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()

class GaussianMixtureModels(object):
    '''之前的KMeans模型簡單也相對容易理解, 但是也使得它面臨應用實務上的一些挑戰.\n\
       因此, 此處將檢視高斯混合模型, 它可以被看作是隱藏KMeans背後概念的延伸, 卻可以\n\
       成為比簡單的集群評估更強力的工具.\n'''

    def introduce(self):
        '''先來看KMeans的一些弱點, 然後思考如何改進集群模型的方向.'''
        # 例如, 有組簡單的資料, KMeans 可以快速為那些群組上標籤, 找出相近的配對
        # 產生一些資料
        from sklearn.datasets import make_blobs
        X, y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)
        X = X[:, ::-1] # 翻轉軸以更好地繪圖

        # 繪出 KMeans 的資料標籤
        from sklearn.cluster import KMeans
        kmeans = KMeans(4, random_state = 0)
        labels = kmeans.fit(X).predict(X)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 40, cmap = 'viridis')
        # plt.show()
        # 上圖對於資料簡單的KMeans標籤

        # 上圖, 直觀來說可以預期對於某些點的集群設定會比其他點來的明顯;
        # 例如, 有些點看起來會在兩個中間群組有些重疊, 重疊的資料點我們可能沒有信心把它們歸類
        # 於某個群組, 不幸的是, KMeans 模型對於機率或是群組設定的不確定性沒有一個基本的衡量
        # 方式(雖然有機會使用一個 bootstrap 方法去評估此種不確定性), 針對此點, 必須要思考到
        # 關於模型的一般化.

        # 其中, 關於KMeans模型思考方向就是在每一群中心放置一個圓(如果是在高維度, 是一個超球面)
        # , 加上一個由此群中最遠的那一點所界定的半徑. 此半徑在訓練資料集中做為一個嚴格斷面: 
        # 任一個在此圓之外的點都不被認為是此群的一員, 透過以下的函式視覺化出這個集群模型
        from scipy.spatial.distance import cdist
        def plot_kmeans(kmeans, X, n_clusters = 4, rseed = 0, ax = None):
            labels = kmeans.fit_predict(X)

            # 繪出輸入的資料
            ax = ax or plt.gca()
            ax.axis('equal')
            ax.scatter(X[:, 0], X[:, 1], c = labels, s = 40, cmap = 'viridis', zorder = 2)

            # 繪出平均模型的表示方法
            centers = kmeans.cluster_centers_
            radii = [cdist(X[labels == i], [center]).max() for i, center in enumerate(centers)]
            for c, r in zip(centers, radii):
                ax.add_patch(plt.Circle(c, r, fc = '#CCCCCC', lw = 3, alpha = 0.5, 
                             zorder = 1, edgecolor = 'black'))
            plt.show()        
        # kmeans = KMeans(n_clusters = 4, random_state = 0)
        # plot_kmeans(kmeans, X)

        # 對於 KMeans 一個重要的觀察是, 這些集群模型必須是圓形的: KMeans沒有內建的方法用來處理
        # 橢圓的群. 例如, 如果拿到了同樣的資料並把它進行轉換, 則此集群就會亂掉了
        # 看以下的例子
        rng = np.random.RandomState(13)
        X_stretched = np.dot(X, rng.randn(2, 2))

        # kmeans = KMeans(n_clusters = 4, random_state = 0)
        # plot_kmeans(kmeans, X_stretched)
        # 上圖表現出對於不是圓形的集群, KMeans的表現不佳. 
        # KMeans有兩個缺點: 1. 缺乏在群組形狀上的彈性. 2. 缺乏機率集群的指定
        # 代表 在許多資料集(特別是低維度的資料)並沒有辦法像我們期待的執行這麼好

    def normalEM(self):
        '''一般化E-M: 高斯混合模型(Gaussian Mixture Models)\n\
           高斯混合模型(GMM)嘗試去尋找一個多維度高斯機率分布的混合體, 讓它可以最佳化形塑任一輸入之資料集\n\
           在一個簡單的例子中, GMM可以被使用在像是KMeans一樣的方法以找出群組.\n\
           高斯混合模型非常類似於KMeans: 它使用最大期望算法方式, 而其量化的行為如下:\n\
                1. 選擇一開始猜測的位置和形狀\n\
                2. 重複直到收斂\n\
                    a. E-Step: 對於每一個點, 找出權重以用來編碼在每一個群之中為其成員的機率\n\
                    b. M-Step: 對於每一個群, 以所有資料點為基礎, 利用這些權重更新它的位置、\n\
                               常規化、以及形狀。\n\
           (可和KMeans所使用的E-M流程做比對)\n'''
        # 沿用前面的資料集
        from sklearn.datasets import make_blobs
        X, y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)
        X = X[:, ::-1]

        from sklearn.mixture import GaussianMixture as GMM 
        gmm = GMM(n_components = 4).fit(X)
        labels = gmm.predict(X)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 40, cmap = 'viridis')
        # plt.show()
        # 上圖為高斯混合標籤用的資料

        # 因為GMM的內部包含了機率模型, 它也可能被用來找出指定群組的機率
        # 使用 Scikit-Learn predict_proba方法來執行, 傳回值為 [n_samples, n_clusters] 的矩陣
        # 它測量了任一個資料點屬於某一給定之群組的機率
        probs = gmm.predict_proba(X)
        # print(probs[:5].round(3)) # 取前面5組資料, 取到小數第三位

        # 使用每個點的比例大小標示出預測的確定性來視覺化出此種不確定性質
        size = 50 * probs.max(1) ** 2 # 平方差可強調差值 <- 讓視覺化更清楚
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = size, cmap = 'viridis')
        # plt.show()
        # GMM的機率標籤: 使用機率反映在點的尺寸

        # 執行之後的結果, 每一個群所結合的就不只是一個嚴格的球面, 而是一個平滑的高斯模型
        # 但如同之前所提的, 此EM演算法有時候可能會失去整體最佳化, 但是實務上有多個隨機模型可以使用於此

        # 以下建立一個函式, 讓此函式藉由畫出以 gmm 輸出為基的橢圓
        from matplotlib.patches import Ellipse
        def draw_ellipse(position, covariance, ax = None, **kwargs):
            """給一個位置和covariance(共變異數), 即可畫出一個橢圓"""
            ax = ax or plt.gca()

            # 把 covariance 轉換到主軸
            if covariance.shape == (2, 2):
                U, s, Vt = np.linalg.svd(covariance) # 奇異值分解
                angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
                width, height = 2 * np.sqrt(s)
            else:
                angle = 0
                width, height = 2 * np.sqrt(covariance)
            
            # 畫出橢圓
            for nsig in range(1, 4):
                ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))
        
        def plot_gmm(gmm, X, label = True, ax = None):
            ax = ax or plt.gca()
            labels = gmm.fit(X).predict(X)
            if label:
                ax.scatter(X[:, 0], X[:, 1], c = labels, s = 40, cmap = 'viridis', zorder = 2)
            else:
                ax.scatter(X[:, 0], X[:, 1], s = 40, zorder = 2)
            ax.axis('equal')

            w_factor = 0.2 / gmm.weights_.max()
            for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
                draw_ellipse(pos, covar, alpha = w * w_factor)
            plt.show()

        # gmm = GMM(n_components = 4, random_state = 42)
        
        # 同樣地, 也可以使用 GMM 的方法去擬合延展過的資料集, 設定covariance_type = 'full', 
        # 此模型可以擬合到非常延展拉伸的群上
        rng = np.random.RandomState(13)
        X_stretched = np.dot(X, rng.randn(2, 2))

        gmm = GMM(n_components = 4, covariance_type = 'full', random_state = 42)
        plot_gmm(gmm, X_stretched)
        # 此標記很清楚地顯示, GMM可以解決之前我們在KMeans所遇到的2個主要實務上的問題

        # 選用 covariance 類型
        # covariance_type 選項, 控制每一個集群形狀的自由度(在面對任何問題時, 要小心設定)
        # 此選項的預設值是: covariance_type = "diag", 意思是群組的大小在每一個維度可以被獨立地設定,
        # 則結果的橢圓形會被限制在對齊的軸線上. 一個稍微簡單且快速的模型是 covariance_type = "spherical",
        # 它限制讓群組的形狀在所有的維度中都是相同的.
        # 然而, 此結果的群組將會和 KMeans 有類似的特性, 卻並不完全等價. 有一個更複雜, 且會花上非常多
        # 計算成本的模型(尤其是維度增加非常大時), 是使用 covariance_type = 'full', 此類型讓每個群組
        # 可以在任意方向被形塑成橢圓形.
        # 參考圖片: ML_GMM_covariance_option.png 

    def density_estimation(self):
        '''GMM雖然經常被歸類到集群演算法, 但是它基本上是一個用來做密度計算的演算法\n\
           也就是說, GMM擬合的結果在技術上不是一個集群模型, 而是一個用來描述資料分\n\
           佈的生成機率模型(generative probabilistic model).\n'''
        # 以下的例子
        from sklearn.datasets import make_moons
        Xmoon, ymoon = make_moons(200, noise = 0.05, random_state = 0)
        # plt.scatter(Xmoon[:, 0], Xmoon[:, 1])
        # plt.show()

        # 若使用 2種成分 GMM當作是集群模型去擬合此資料, 會發現結果沒有特別用處
        from sklearn.mixture import GaussianMixture as GMM
        gmm2 = GMM(n_components = 2, covariance_type = 'full', random_state = 0)

        from matplotlib.patches import Ellipse
        def draw_ellipse(position, covariance, ax = None, **kwargs):
            """給一個位置和covariance(共變異數), 即可畫出一個橢圓"""
            ax = ax or plt.gca()

            # 把 covariance 轉換到主軸
            if covariance.shape == (2, 2):
                U, s, Vt = np.linalg.svd(covariance) # 奇異值分解
                angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
                width, height = 2 * np.sqrt(s)
            else:
                angle = 0
                width, height = 2 * np.sqrt(covariance)
            
            # 畫出橢圓
            for nsig in range(1, 4):
                ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))

        def plot_gmm(gmm, X, label = True, ax = None):
            ax = ax or plt.gca()
            labels = gmm.fit(X).predict(X)
            if label:
                ax.scatter(X[:, 0], X[:, 1], c = labels, s = 40, cmap = 'viridis', zorder = 2)
            else:
                ax.scatter(X[:, 0], X[:, 1], s = 40, zorder = 2)
            ax.axis('equal')

            w_factor = 0.2 / gmm.weights_.max()
            for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
                draw_ellipse(pos, covar, alpha = w * w_factor)
            # plt.show()
        # plot_gmm(gmm2, Xmoon)

        # 若使用更多的成分來取代, 並忽略群組的標籤, 則可以找到一個更接近輸入資料的擬合結果
        gmm16 = GMM(n_components = 16, covariance_type = 'full', random_state = 0)
        # plot_gmm(gmm16, Xmoon, label = False)
        # 上圖的結果使用了16個成分並不是為了要找出資料分隔用的群組, 但卻形塑了此輸入資料整體
        # 的分布狀態. 代表GMM是一個分布的生成模型, 給我們一個產生和輸入資料相似, 新的隨機資
        # 料分布步驟. 

        # 需要多少個成分(component)
        # GMM 實際上是一個生成模型, 給一個資料集, 它給我們一個自然的方法決定元件的最佳數目.
        # 一個生成模型是承襲自資料集的機率分布, 因此可以簡單的評估在模型之下資料的可能性, 
        # 使用交叉驗證以避免過度擬合, 另外一個修正過度擬合的方法是使用一些分析的規範, 像是
        # AIC, BIC去調整模型的可能性. Scikit-Learn 裡面 GMM 評估器實際上也包含了內建模型
        n_component = np.arange(1, 21)
        models = [GMM(n, covariance_type = 'full', random_state = 0).fit(Xmoon)
                  for n in n_component]

        # plt.plot(n_component, [m.bic(Xmoon) for m in models], label = 'BIC')
        # plt.plot(n_component, [m.aic(Xmoon) for m in models], label = 'AIC')
        # plt.legend(loc = 'best')
        # plt.xlabel('n_components')
        # plt.show()
        # 根據上圖可以發現最佳的群組數目大約在8~12之間, 也就是AIC/BIC最小值
        # 另一個重要的點: component數目的選擇衡量了GMM當作是一個密度評估器表現的好壞
        # 而不是當作一個集群演算法的好壞, 建議把GMM想成是一個密度評估器, 只有確實是在
        # 簡單的資料集中才把它當作是集群方法來用


gmm = GaussianMixtureModels()
# gmm.introduce() # 使用 GMM 的動機, KMeans的弱點
# gmm.normalEM() # 一般化E-M: 高斯混合模型(Gaussian Mixture Models)
gmm.density_estimation()