# 支援向量機(SVMs)
# 不論是在分類或是回歸中都特別具有威力以及彈性的監督式演算法

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
sns.set()


class SVMs(object):
    def introduce(self):
        '''之前的貝氏分類法是使用了一個簡單的模型來描述每一個類別的分佈,\n\
        而且使用生成模型對於一個新的資料點以機率來決定它的標籤, 也就是生成分類法.\n\
        在此, 我們將考慮取代為判別分類法: 我們找出一條直線或曲線(>1的維度), 讓他們\n\
        可以和其他的類別分開.\n\n
        此分類器成功的其中一個關鍵是, 關於擬合只有那些支持向量的位置是相關的: \n\
            任一邊比邊界遠的資料點並不會影響你和結果, 技術上來說, 因為這些點\n\
            並不會對於使用在擬合此模型的損失(loss function)函數有任何的貢獻,\n\
            所以只要不跨越邊界, 它們的位置和數目並不重要.\n\
            (詳情見FitSVMs).\n'''

    def SupportVectorMachine(self):
        # 考慮一個分類工作的簡單情況, 所有的點有2個類別, 而且分隔得很清楚
        from sklearn.datasets import make_blobs
        X, y = make_blobs(n_samples = 50, centers = 2, random_state = 0, cluster_std = 0.60)
        # plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')
        # plt.show()

        # 一個線性的判別分類器, 可以嘗試去畫出一條直線把這些資料分隔為2個集合, 從而建立一個可以用來分類的模型
        # 但是上述的資料會發現一個問題, 有多於一個可能的線條存在, 可以用來完美的辨別這兩類
        # 嘗試把線條畫出來
        xfit = np.linspace(-1, 3.5)
        # plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')
        # plt.plot([0.6], [2.1], 'x', color = 'red', markeredgewidth = 2, markersize = 10)

        # for m, b in [(1, 0.65), (0.5, 1.6), (-0.2, 2.9)]:
        #     plt.plot(xfit, m * xfit + b, '-k')
        # plt.xlim(-1, 3.5)
        # plt.show()

        # 圖上有三條不一樣的分割器, 都可以完美的區分出這些樣本點; 但是圖中標記的X會因為採取不一樣的模型,
        # 而被分類為不一樣的標籤, 因此在類別間只畫一條線是不夠用的, 還需要再深入一些

        # SVM: 最大化邊界
        # SVM 提供了一個改良上述問題的方式, 直覺式的想法, 我們可以在每一條線上畫上具有寬度的邊界, 直到最近的點.
        xfit = np.linspace(-1, 3.5)
        # plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')

        # for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
        #     yfit = m * xfit + b
        #     plt.plot(xfit, yfit, '-k')
        #     plt.fill_between(xfit, yfit - d, yfit + d, edgecolor = 'none', 
        #                      color = 'Yellow', alpha = 0.4)
        # plt.xlim(-1, 3.5)
        # plt.show()

        # 在SVM中, 能夠最大化邊界的線條會被選用來當做是最佳的模型.
        # SVMs 就是此種最大化邊界的一個例子

    # 為了要讓視覺圖表現得更好, 先建立一個方便的函式畫出SVM決策邊界
    # 接著的兩個例子, 都會需要用到所以寫在外面
    def plot_svc_decisionfunction(self, model, ax = None, plot_support = True):
        '''畫出二維的SVC決策函數'''
        if ax is None:
            ax = plt.gca() # <- 取得當前的軸給ax變數
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        # 建立grid以評估模型
        x = np.linspace(xlim[0], xlim[1], 30)
        y = np.linspace(ylim[0], ylim[1], 30)
        Y, X = np.meshgrid(y, x) # <- 建立多維矩陣(y * x的大小) 類似broadcasting
        xy = np.vstack([X.ravel(), Y.ravel()]).T
        P = model.decision_function(xy).reshape(X.shape)

        # 繪出決策邊界
        ax.contour(X, Y, P, colors = 'k', levels = [-1, 0, 1], alpha = 0.5, 
                   linestyles = ['--', '-', '--'])
            
        # 繪出支持向量
        if plot_support:
            ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], 
                       s = 300, linewidth = 1, facecolor = 'none', edgecolor = 'black')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        # plt.show()

    def FitSVMs(self):
        # 沿用上一個例子的資料
        from sklearn.datasets import make_blobs
        X, y = make_blobs(n_samples = 50, centers = 2, random_state = 0, cluster_std = 0.60)

        # 使用 Scikit-Learn 的 support vector classifier 來訓練一個模型
        # 目前暫且使用一個線性核心, 並先把 C 參數設定一個很大的數目
        from sklearn.svm import SVC # <- SupportVectorClassifier
        model = SVC(kernel = 'linear', C = 1E10)
        model.fit(X, y) 

        plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')
        plot_svc_decisionfunction(model)

        # 圖上的輸出結果是在兩組資料點鐘具有最大邊界的分隔線
        # 注意有少許的訓練資料剛好觸碰到邊界, (黑色圈起來的資料點), 這些點是擬合的關鍵元素,
        # 也被稱為支持向量(support vector)的元素; 在Scikit-Learn中, 
        # 這些點的內容被儲存在分類器的support_vectores_屬性中 <- line. 103
        # print(model.support_vectors_)
        # [[0.44359863 3.11530945]
        # [2.33812285 3.43116792]
        # [2.06156753 1.96918596]]

    def KernelSVM(self):
        '''把SVM結合核心後就會變得非常具有威力. 在基函數回歸中已經看過其中一個版本的核心,\n\
           那時透過多項式和高斯基函數把資料投影到更高維度的空間中, 讓我們可以在線性分類器,\n\
           中擬合非線性關係.\n'''
        
        # 在SVM模型中, 可以使用同樣概念的版本, 為了激發核心的需要, 先來看一些非線性分隔的資料
        from sklearn.datasets import make_circles
        from sklearn.svm import SVC
        X, y = make_circles(100, factor = .1, noise = .1)
        # clf = SVC(kernel = 'linear').fit(X, y)

        # plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')
        # self.plot_svc_decisionfunction(clf, plot_support = False)
        # 上面的結果, 很明顯無法使用線性函數就區分這些資料

        # 我們可以藉由LR學到的方式, 把線性分類器投影到更高的維度
        # 例如使用簡單的投影方法計算以這些點為中心的半徑基函數(random basis function)
        r = np.exp(-(X ** 2).sum(1))

        # 使用3度空間的圖形視覺化這個額外的資料維度
        from mpl_toolkits import mplot3d

        def plot_3D(elev = 30, azim = 30, X = X, y = y):
            ax = plt.subplot(projection = '3d')
            ax.scatter3D(X[:, 0], X[:, 1], r, c = y, s = 50, cmap = 'autumn')
            ax.view_init(elev = elev, azim = azim)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('r')
            plt.show()
        # plot_3D(elev = [-90, 90], azim = (-180, 180), X = X, y = y)
        # line145: TypeError: can't multiply sequence by non-int of type 'float' <- 尚未找到問題
        # 網路上下載圖片: ~Result01.png

        # 第二種方法是以這些資料集的每一個點為中心計算基函數, 然後讓SVM過濾這些結果
        # 此種形態被稱為核轉換(Kernel transformation), 也就是基於每一對資料點之間的相似關係(指核心)
        # 此作法(投影N個點到N個維度)的一個問題是當N越大就需要耗費非常大的計算, 然而
        # 因為叫做核心技巧(Kernel trick)的簡潔小程序, 在核轉換資料可以被隱含完成,
        # 也就是說, 甚至不需要建構全部核心投影之N維度表示

        # 在 Scikit-Learn 中可以套用核計算過的SVM, 藉由改變線性核心到一個RBF核心
        # 使用 kernel 超參數
        clf = SVC(kernel = 'rbf', C = 1E6)
        clf.fit(X, y)
        self.plot_svc_decisionfunction(clf)
        plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')
        plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
                    s = 300, lw = 1, edgecolor = 'black', facecolor = 'none')
        # plt.show()
        # 有問題: 輸出結果無法非常完整, 只能顯示1/4

        # 使用核計算過的SVM, 常被用在機器學習中, 用來轉換快速線性方法成為快速非線性方法,
        # 特別是對於那些可以使用核技巧的模型

    def softening(self):
        '''到目前為止, 我們的資料集都有著可以非常完美的可決定邊界存在的資料集,\n\
           但是若資料中有重疊的部分呢? 看以下例子.\n'''
        from sklearn.svm import SVC
        from sklearn.datasets import make_blobs
        X, y = make_blobs(n_samples = 100, centers = 2, random_state = 0, cluster_std = 1.2)
        # plt.scatter(X[:, 0], X[:, 1], c = y , s = 50, cmap = 'autumn')
        # plt.show()
        # 上圖的資料有部分重疊了
        # 要處理這種情形, SVM實作有一些模糊因子(fudge-factor)可以用來柔化邊界,
        # 也就是說它允許一些資料點可以蔓延進入邊界以讓擬合的結果較好, 邊界的銳利程度是由'C參數'來調整
        # 對於非常大的 C 邊界很銳利, 以至於資料點不能在邊界上; 反之允許邊界成長到包含一些資料點

        X, y = make_blobs(n_samples = 100, centers = 2, random_state = 0, cluster_std = 0.8)
        fig, ax = plt.subplots(1, 2, figsize = (16, 6))
        fig.subplots_adjust(left = 0.0625, right = 0.95, wspace = 0.1)
        for axi, C in zip(ax, [10.0, 0.1]):
            model = SVC(kernel = 'linear', C = C).fit(X, y)
            axi.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')
            self.plot_svc_decisionfunction(model, axi)
            axi.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
                        s = 300, lw = 1, edgecolor = 'black', facecolor = 'none')
            axi.set_title('C = {0:.1f}'.format(C), size = 14)
        # plt.show()
        # C 參數最佳的值由資料集來決定, 可以透過交叉驗證或類似的程序來調整

    def summary(self):
        '''SVM依賴相對少的支持向量, 表示它們是非常精簡的模型, 而且只使用很少的記憶體.\n\
           一旦模型訓練完成, 預測階段的速度非常快.\n\
           因為SVM只有被接近邊界的點有影響, 因此對於高維度的資料中運作的很好, 甚至包括在\n\
           維度比樣本數還多的資料中, 這些對於其他的演算法是一個挑戰.\n\
           與核方法(KSVM)整合非常多樣化, 能夠適應到許多型態的資料.\n\n\
           缺點: \n\
           關於樣本數N的執行效能估計, 最糟時是 O(N^3), 有效率的實作則是O(N^2)\n\
           對於非常大的訓練樣本來說, 計算成本可能就會變得太高了.\n\
           SVM的結果非常依賴柔化參數C的選擇, 這個值必須小心藉由交叉驗證來選取, 在資料集變大之後, 成本會非常昂貴.\n\
           SVM的結果沒有一個直接的機率學理解釋, 可以從一個內部的交叉驗證(參考SVC的機率參數), 但需要額外成本.\n\
           結論: 通常只有在其他更簡單, 更快速以及較少極需調整的方法已經確定不夠用時, 才會轉用SVM.\n\
           (除非, 有足夠的CPU效能可以在資料上用來訓練和交叉驗證SVM, 這樣就可以得到很傑出的結果)\n'''

svm = SVMs()
# help(svm.introduce)
# svm.SupportVectorMachine() # SVM 的基礎介紹和原理
# svm.FitSVMs() # <- 擬合支持向量機
svm.KernelSVM() # <- 超越線性邊界 (核心SVM) # 3D有問題
# svm.softening() # <- 調整SVM 柔化邊界
# help(svm.summary) # SVM 摘要
