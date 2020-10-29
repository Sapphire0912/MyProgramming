# Kernel Density Estimation(KDE 核密度估計)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

class kde(object):
    '''KDE在某種意義上是使用一個高斯混合想法的演算法, 使用每一個資料點的一個高斯元件的混合\n\
       產生出一個本質上是無母體的密度評估器結果.'''
    def use(self):
        '''KDE使用動機: 直方圖, 密度評估器是一個演算法, 它找出一個可以生成資料集之模型化機率分布.'''
        def make_data(N, f = 0.3, rseed = 1):
            rand = np.random.RandomState(rseed)
            x = rand.randn(N)
            x[int(f * N):] += 5
            return x
        
        x = make_data(1000)
        # hist = plt.hist(x, bins = 30, normed = True)
        # normd 參數: 正規化直方圖, 是把y軸座標顯示成機率分布而不是出現次數
        # plt.show()

        # 因為選用了正規化, 因此直方圖的全部面積等於1, 可用以下方式來確認
        # density, bins, patches = hist
        # width = bins[1:] - bins[:-1]
        # print((density * width).sum()) # 1.0

        # 使用直方圖當成密度評估器其中一個問題是籃子大小以及位置的選擇, 可能會導致表現出來的樣子在
        # 質方面不同的特徵. 例如, 如果檢視此資料的其中一個只有20個資料點版本的情況, 考慮以下例子
        x = make_data(20)
        bins = np.linspace(-5, 10, 10)
        # fig, ax = plt.subplots(1, 2, figsize = (12, 4), sharex = True, sharey = True, 
        #                        subplot_kw = {'xlim':(-4, 9), 'ylim':(-0.02, 0.3)})
        # fig.subplots_adjust(wspace = 0.5)
        # for i, offset in enumerate([0.0, 0.6]):
        #     ax[i].hist(x, bins = bins + offset, normed = True)
        #     ax[i].plot(x, np.full_like(x, -0.01), '|k', markeredgewidth = 1)
        # plt.show()
        # 可以看出兩邊的直方圖使用同樣的資料但卻有不一樣的結果

        # 若我們退回去看, 把直方圖想成是一個區塊的堆疊, 每一個籃子中在每一個資料點的上方堆一個區塊
        # fig, ax = plt.subplots()
        bins = np.arange(-3, 8)
        # ax.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth = 1)
        # for count, edge in zip(*np.histogram(x, bins)):
        #     for i in range(count):
        #         ax.add_patch(plt.Rectangle((edge, i), 1, 1, alpha = 0.5))
        # ax.set_xlim(-4, 8)
        # ax.set_ylim(-0.2, 8)
        # plt.show()

        # 兩個籃子間的間隔問題來自於一個事實, 那就是區塊堆疊的程度通常反映出的不是此資料點附近實際的密度
        # 而是此籃子在資料點鐘如何對齊的巧合. 在資料點之間出現誤對齊的情況, 則它們的區塊就有可能會造成像
        # 是我們看到的, 不佳的直方圖問題. 但是如果我們不讓這些區塊和籃子對齊, 而是依照資料點實際表現出的
        # 樣子堆疊這些區塊, 那麼這些區塊就不會被對齊, 在它們在每一個位置上沿著X軸新增分布形成的結果
        x_d = np.linspace(-4, 8, 2000)
        # density = sum((abs(xi - x_d) < 0.5) for xi in x)
        # plt.fill_between(x_d, density, alpha = 0.5)
        # plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth = 1)
        # plt.axis([-4, 8, -0.2, 8])
        # plt.show()
        # 雖然結果有些雜亂, 但是可以比標準的直方圖更強固反映出實際資料的特性
        # 把粗略的邊緣使用高斯平滑函數來取代

        from scipy.stats import norm
        x_d = np.linspace(-4, 8, 1000)
        density = sum(norm(xi).pdf(x_d) for xi in x)
        plt.fill_between(x_d, density, alpha = 0.5)
        plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth = 1)
        plt.axis([-4, 8, -0.2, 8])
        plt.show()
        # 上圖是使用高斯核心的核密度估計
    
    def application(self):
        '''核密度估計一些可以使用的參數包含(核心 kernel), 也就是用來指定每一個點所放置的分布形狀\n\
           , 以及核心帶寬(kernel bandwidth), 用來控制每一個點的核心大小.\n\
           實務上, 核密度估計中有許多核心可以使用, 在 Scikit-Learn KDE 實作中支援了6個核心中的\n\
           一種, 可以查看說明文件. 在Scikit-Learn 的 KDE 評估器中, 因為KDE會使用相當大的運算資\n\
           料, 所以在 sklearn 中背後以樹狀為基礎的演算法, 可以透過atol, rtol 參數的設定在正確率\n\
           和計算資源之間做些取捨, 我們可以決定核心帶寬, 也是一個自由設定的參數, 使用Scikit-Learn\n\
           的標準交叉驗證.\n'''

        def make_data(N, f = 0.3, rseed = 1):
            rand = np.random.RandomState(rseed)
            x = rand.randn(N)
            x[int(f * N):] += 5
            return x
        
        x = make_data(20) # 前面的資料集
        x_d = np.linspace(-4, 8, 1000)

        # 看以下的例子
        from sklearn.neighbors import KernelDensity

        # 實體化和擬合KDE模型
        kde = KernelDensity(bandwidth = 1.0, kernel = 'gaussian')
        kde.fit(x[:, None])

        # 傳回機率密度的log
        logprob = kde.score_samples(x_d[:, None])
        # plt.fill_between(x_d, np.exp(logprob), alpha = 0.5)
        # plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth = 1)
        # plt.ylim(-0.02, 0.22)
        # plt.show()
        # 上面的結果是經過正規化的, 所以曲線下的面積等於1
        
        # 經由交叉驗證選用帶寬
        # 帶寬的選擇在尋找一個合適的密度評估時極端重要, 而且它是一個可調整的旋鈕, 可以在核密度估計中,
        # 控制誤差-變異(bias-variance)之間的取捨, 太過窄化帶寬會造成高變異的估計(Overfitting), 單一
        # 個點的有無就會造成很大的差異. 太過寬的帶寬則會導致一個高誤差的估計(underfitting), 在資料中的
        # 結果會被過寬的核心所淘汰. 
        # 在 Scipy 以及 StatModels 套件的KDE實作, 將會看到基於這些規則中一些實作內容

        # 在 Scikit-Learn 中的 KernelDensity estimator 被設計來讓他們可以被直接使用在 
        # Scikit-Learn 的標準格狀搜尋工具, 使用 GridSearchCV 去最佳化之前資料集的帶寬

        from sklearn.model_selection import GridSearchCV
        from sklearn.model_selection import LeaveOneOut

        bandwidths = 10 ** np.linspace(-1, 1, 100)
        grid = GridSearchCV(KernelDensity(kernel = 'gaussian'), {'bandwidth': bandwidths}, 
                                          cv = LeaveOneOut())
        grid.fit(x[:, None])
        print("Best parameters: ", grid.best_params_) # {'bandwidth': 1.1233240329780276}

KDE = kde()
# KDE.use()
KDE.application()