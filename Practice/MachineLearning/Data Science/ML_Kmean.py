# K-平均集群法(K-Mean Clusters)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


class K_Means(object):
    '''另一種非監督式學習模型: 集群演算法, 集群演算法從資料的特性中尋找以學習一個最佳的分布\n\
       或是一組資料點的離散標籤.\n\
       KMeans: 在一個為標籤的多為資料中搜尋一個預先定義數目的群組.它藉由使用一個簡單的最佳化\n\
       集群看起來的樣子之概念來完成.\n\
           群組中心: 是所有同一群組中的所有點之算術平均; 群組中的每一個點都比其他群組的點還要\n\
           更接近群組中心.\n\
       這兩個假設是KMeans模型的基礎.\n'''

    def introduce(self):
        from sklearn.datasets import make_blobs
        X, y_true = make_blobs(n_samples = 500, centers = 4, cluster_std = 0.60, random_state = 0)
        # plt.scatter(X[:, 0], X[:, 1], s = 50)
        # plt.show()
        # 上圖可以很清楚的觀察到資料被分成4個部分. 
        # KMeans演算法可以自動做這件事, 使用Scikit-Learn典型的評估器API
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters = 4)
        kmeans.fit(X)
        y_kmeans = kmeans.predict(X)
        # plt.scatter(X[:, 0], X[:, 1], c = y_kmeans, s = 50, cmap = 'viridis')
        centers = kmeans.cluster_centers_ # 群組中心
        # plt.scatter(centers[:, 0], centers[:, 1], c = 'black', s = 200, alpha = 0.5)
        # plt.show()
        # 上圖, 使用Scikit-Learn可以一下子就把4個區域給分出來了
        # KMeans典型研究包含了一個直覺的迭代嘗試: 最大期望算法(expectation-maximization)

    def expectation_maximization(self):
        '''最大期望算法(E-M): 是一個具有威力的演算法, 應用在DS的許多不同領域中.\n\
           KMeans是一個特別簡單而且容易理解的演算法應用, 而我們將在此簡要的執行一遍\n\
           最大期望算法是由以下的幾個程序組成的: \n\
           1. 猜測一些群組的中心\n\
           2. 重複一直到收斂\n\
              a. E-Step: 指定一些點到最近的群組中心\n\
              b. M-Step: 設定群組中心為平均值\n\
           E-Step 包含了更新我們對於每一個點屬於的群組之期望;\n\
           M-Step 包括最大化一些適應函數(fitness function)這些函數定義了群組中心的位置\n\
           在上面的介紹例子當中, 最大化藉由取得每一個群組中資料點的簡單平均來完成.\n'''

        # 沿用之前的資料
        from sklearn.datasets import make_blobs
        X, y_true = make_blobs(n_samples = 500, centers = 4, cluster_std = 0.60, random_state = 0)

        # KMeans演算法可以用幾行程式碼完成
        from sklearn.metrics import pairwise_distances_argmin
        def find_clusters(X, n_clusters, rseed = 2):
            # 1. 選擇隨機群組
            rng = np.random.RandomState(rseed)
            i = rng.permutation(X.shape[0])[:n_clusters]
            centers = X[i]

            while True:
                # 2a. 基於最近的中心設定標籤
                labels = pairwise_distances_argmin(X, centers)
                
                # 2b. 從點的平均找出新的中心
                new_centers = np.array([X[labels == i].mean(0) for i in range(n_clusters)])

                # 2c. 檢查是否收斂
                if np.all(centers == new_centers):
                    break
                centers = new_centers

            return centers, labels

        # centers, labels = find_clusters(X, 4)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 50, cmap = 'viridis')
        # plt.show()
        # 上圖使用KMeans加上標籤的資料

        # 最大期望算法的一些警示
        # 1. 全體最佳化的結果可能無法達到
        # 即使E-M-Step保證在每一步改善其結果, 但無法保證可以達成全體的最佳化. 如果上面的例子, 
        # 使用一個不同的隨機種子在我們的簡單程序中, 有些特定的猜測將會導致很差的結果. 基於這個
        # 情況, 此演算法經常被使用多個不同的起始猜測執行多次, 實際上, Scikit-Learn 在預設的情
        # 況下就會這麼做(以 n_init 參數來設定次數, 默認是10).
        # centers, labels = find_clusters(X, 4, rseed = 60)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 50, cmap = 'viridis')
        # plt.show()
        # 這裡測試過了10組(都有完好的分類...)

        # 2. 必須事先設定群組的數目
        # KMeans 必須先設定預期的群組數目: 它沒辦法從資料中學習到群組的數目.例如, 如果我們要求
        # 此演算法識別出6個群組, 它會開心的很快找出最佳的6個群組
        from sklearn.cluster import KMeans
        # labels = KMeans(n_clusters = 6, random_state = 0).fit_predict(X)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 50, cmap = 'viridis')
        # plt.show()
        # 上圖的結果為當群組數設定不佳的時候
        # 對於結果是否有意義是一個很難明確定義的問題, 但是我們可以使用更複雜的, 對於每一個群組
        # 數目有較佳的適應量化量測的集群演算法(例如: 高斯混合模型), 或是可以先選用一個合適的群
        # 組數目(例如: DBSCAN, mean-shift, affinity propagation, 這些都在sklearn.cluster中)

        # 3. KMeans被限制在線性群組邊界
        # KMeans的基本模型假設(資料點比在其他群組中的點更接近自己的中心)代表此演算法在遇到複雜
        # 的幾何形狀的群組時經常是無效的, 尤其是KMeans的群組邊界都是線性的, 以下參考例子
        from sklearn.datasets import make_moons
        X, y = make_moons(200, noise = .05, random_state = 0)
        labels = KMeans(2, random_state = 0).fit_predict(X)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 50, cmap = 'viridis')
        # plt.show()

        # 但是我們可以像之前的 KSVM(把資料投影到一個更高維度讓線性分割變得可能), 使用相同的技巧
        # 以讓 KMeans 可以找出非線性的邊界.
        # 其中一個核化版本的KMeans被實作在 Scikit-Learn 的 SpectralClustering estimator,
        # 它使用最近鄰圖(gragh of nearest neighbors)去計算一個資料的更高維度表示.
        from sklearn.cluster import SpectralClustering
        model = SpectralClustering(n_clusters = 2, affinity = 'nearest_neighbors', 
                                   assign_labels = 'kmeans')
        labels = model.fit_predict(X)
        # plt.scatter(X[:, 0], X[:, 1], c = labels, s = 50, cmap = 'viridis')
        # plt.show()

        # 4. 大量的樣本會讓 KMeans 執行變慢
        # 因為 KMeans 每一次的迭代都必須存取資料集中的每一個點, 此演算法相對來說就會在資料量
        # 龐大時變慢, 但是"在每一個迭代中使用每一個點"這個需求是可以被放寬的, 例如: 可能只要
        # 使用資料的一個子集合更心在每一個步驟中的群組中心, 這是 batch-based k-means演算法
        # 它被實作在 sklearn.cluster.MiniBatchKMeans 中, 介面和標準的 KMeans 一樣, 接下來
        # 將看實作例子

    def example01(self):
        # 在數字元上使用KMeans
        from sklearn.datasets import load_digits
        digits = load_digits()
        # print(digits.data.shape) # (1797, 64)

        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters = 10, random_state = 0)
        clusters = kmeans.fit_predict(digits.data)
        # print(kmeans.cluster_centers_.shape) # (10, 64)

        # 視覺化群組
        # fig, ax = plt.subplots(2, 5, figsize = (8, 3))
        # centers = kmeans.cluster_centers_.reshape(10, 8, 8)
        # for axi, center in zip(ax.flat, centers):
        #     axi.set(xticks = [], yticks = [])
        #     axi.imshow(center, interpolation = 'nearest', cmap = plt.cm.binary)
        # plt.show()
        # 上圖可以看出即使沒有標籤也能夠被KMeans辨別出群組中心, 但是因為KMeans對於如何分別群組
        # 沒有任何了解, 所以可能不會按照 0~9 的順序排列
        # 在此可以透過把每一個學習到的群組, 從它們之中找出實際標籤做配對來修正此種情況:
        from scipy.stats import mode
        labels = np.zeros_like(clusters)
        for i in range(10):
            mask = (clusters == i)
            labels[mask] = mode(digits.target[mask])[0]

        # 檢查正確率
        from sklearn.metrics import accuracy_score
        # print(accuracy_score(digits.target, labels)) # 0.7952142459654981

        # 透過混淆矩陣來檢查具體出錯的情況
        from sklearn.metrics import confusion_matrix
        mat = confusion_matrix(digits.target, labels)
        # sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False, 
        #             xticklabels = digits.target_names, yticklabels = digits.target_names)
        # plt.xlabel('true label')
        # plt.ylabel('predicted label')
        # plt.show()

        # 結果就和前面視覺化群組中心所預期的, 會混淆的主要是8和1, 但是依然可以使用KMeans建立一個數字元分類器
        # 以下再使用t-SNE演算法(讓它在進行KMeans前先預處理這些資料)
        # t-SNE 是一個非線性的內嵌演算法, 特別是可以被用在保留群組中的資料點
        from sklearn.manifold import TSNE
        # 投影資料
        tsne = TSNE(n_components = 2, init = 'pca', random_state = 0)
        digits_proj = tsne.fit_transform(digits.data)

        # 計算此群
        kmeans = KMeans(n_clusters = 10, random_state = 0)
        clusters = kmeans.fit_predict(digits_proj)

        # 排列標籤
        labels = np.zeros_like(clusters)
        for i in range(10):
            mask = (clusters == i)
            labels[mask] = mode(digits.target[mask])[0]
        
        # 計算正確率
        print(accuracy_score(digits.target, labels)) # 0.9398998330550918

    def example02(self):
        # 在色彩壓縮使用KMeans
        # 對於大部分的影像, 大部分的顏色是沒有被用到的, 而且許多影像中的點具有相類似, 甚至一模一樣
        from sklearn.datasets import load_sample_image
        china = load_sample_image("china.jpg")
        # ax = plt.axes(xticks = [], yticks = [])
        # ax.imshow(china)
        # plt.show()

        # 這張影像本身是以三維的陣列尺寸(高, 寬, RGB)儲存, 並包含從0~255整數表示顏色的資料值
        # print(china.shape) # (427, 640, 3)

        # 其中一個可以檢視此像素集合之方法: 把它當作是三維顏色空間中的資料點集合
        # 把資料重塑成[n_samples * n_features], 然後把顏色的值重新調整到 0~1 之間
        data = china / 255.0
        data = data.reshape(427 * 640, 3)
        # print(data.shape) (273280, 3)

        # 視覺化像素點(因效率所以只採用10000個像素點)
        def plot_pixels(data, title, colors = None, N = 10000):
            if colors is None:
                colors = data

            # 隨機選一個子集合
            rng = np.random.RandomState(0)
            i = rng.permutation(data.shape[0])[:N]
            colors = colors[i]
            R, G, B = data[i].T

            fig, ax = plt.subplots(1, 2, figsize=(16, 6))
            ax[0].scatter(R, G, color = colors, marker = '.')
            ax[0].set(xlabel = 'Red', ylabel = 'Green', xlim = (0, 1), ylim = (0, 1))

            ax[1].scatter(R, B, color = colors, marker = '.')
            ax[1].set(xlabel = 'Red', ylabel = 'Blue', xlim = (0, 1), ylim = (0, 1))
            fig.suptitle(title, size = 20)
            plt.show()
        # plot_pixels(data, title = 'Input color space: 16 million possible colors')
        # 圖中為RGB顏色空間中各像素點的分布

        # 現在使用 KMeans, 在像素空間中把這些 16,000,000 個顏色減少成16色
        # 因為資料集龐大, 使用 迷你批次KMeans(mini batch kmeans), 在資料的子集合中運作,
        # 結果會比標準的 KMeans 快
        from sklearn.cluster import MiniBatchKMeans
        kmeans = MiniBatchKMeans(16)
        kmeans.fit(data)
        new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

        # plot_pixels(data, colors = new_colors, title = 'Reduced color space: 16 colors')
        # 圖中的結果為對原始像素點的重新上色, 其中每一個像素均被指定為最接近它的群組中心顏色

        # 用新的顏色構圖和原始圖的對比可以看出演算法的效能
        china_recolored = new_colors.reshape(china.shape)

        fig, ax = plt.subplots(1, 2, figsize = (16, 6), 
                               subplot_kw = dict(xticks = [], yticks = []))
        fig.subplots_adjust(wspace = 0.05)
        ax[0].imshow(china)
        ax[0].set_title('Original Image', size = 16)
        ax[1].imshow(china_recolored)
        ax[1].set_title('16-color Image', size = 16)
        plt.show()
        # 右邊的圖中損失了一些細節, 但是整體上影像仍然容易辨識(而且還達到了100萬倍的壓縮率)
        # 雖然在影像壓縮上有更好的方法, 但是此例子展現出像是KMeans這樣的非監督式方式跳脫框架之外的其他能力

kmean = K_Means()
# help(kmean)
# kmean.introduce()
# kmean.expectation_maximization()
# kmean.example01()
kmean.example02()