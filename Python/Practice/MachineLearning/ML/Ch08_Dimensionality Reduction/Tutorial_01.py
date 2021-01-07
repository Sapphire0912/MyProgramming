# 降維
# 維度詛咒: 許多ML問題涉及訓練實例的幾千幾百萬個特徵, 會導致訓練非常緩慢也難找到好的解決辦法
# 但對於現實世界的問題, 一般可以大量減少特徵的數量, 也不至於丟失太多的訊息
# 注意: 降維數據確實會失去一些訊息, 雖然可以加速訓練, 但也會輕微降低系統性能, 且同時會讓流水線更複雜, 維護難度上升
# 所以訓練太慢, 首先應該考慮的是 嘗試繼續使用原始數據, 然後再考慮降維

# 除了加快訓練, 降維對於數據可視化也是非常有用的, 通過可視化來檢測常常可以獲得十分重要的資訊(比如聚類)
# 本章節討論 維度詛咒, 大致了解高維度空間會發生的事情, 以及介紹兩種主要的數據降維方式(投影, 流形學習),
# 並學習現在最流行的三種數據降維技術(PCA, KernelPCA LLE)

# 維度詛咒
# 高維度數據集很大可能是非常稀疏的(代表 訓練實例彼此相距很遠), 導致新的訓練實例很可能遠離任何一個訓練實例,
# 導致預測跟低維度相比更加不可靠(這裡可以得知, 若有一個 X 模型擬合了超高維度模型, 很大的機率是過度擬合),
# 換句話說, 訓練集的維度越高, 過度擬合的風險越大 
# 理論上來說, 通過增大訓練集, 使訓練實例達到足夠的密度, 是可以逃出維度詛咒的; 
# 實際上, 達到足夠的密度是隨著維度增加呈現指數上升, 是不可能做到的

# 數據降維的主要方法
# 投影
# 大多數現實世界的問題, 訓練實例在所有維度上並不是均勻分布
# 許多特徵幾乎是不變的, 也有許多特徵是高度相關的(因此高維空間的所有實例受一個低維子空間所影響)
# 但是在許多情況下, 子空間可能會彎曲或轉動, 導致投影並不是降維的最佳方法

# 流形學習
# d 維流形是 n 維空間的一部分(d < n), 許多降維演算法通過對訓練實例進行流形建模實現的
# 它依賴於流形假設, 認為大多數現實世界高維度的數據集存在一個低維度的流形來重新表示(而這個假設通常是憑經驗觀察)
# 流行假設伴隨著一個前提, 如果能用低維空間的流形表示, 任務(分類或回歸)將變得簡單
# 但是這個前提實際上不會總是成立, 此前提取決於數據集, 有時候降維反而讓決策邊界更難處理


# 流行的三種降維方式
# 1. PCA(主成分分析)
# 迄今為止最流行的降維演算法, 它是先識別出最接近數據的超平面然後將數據投影其上

# 保留差異性
# 選擇保留最大差異性的軸(比丟失原始訊息還少), 或者比較原始數據與軸上的投影之間的均方距離(歐式距離的平均值)
# 此均方距離最小的軸是最合理的選擇, 也是 PCA 背後簡單的思想

# 主成分
# PCA 可以在訓練集中識別出哪條軸對差異性貢獻度最高, 維度數量與軸的數量相同
# 若要找到訓練集的主成分, 有一種標準矩陣分解技術(奇異值分解, SVD <- 線性代數內容)
# SVD 將訓練集矩陣 X 分解成 三個矩陣的點積 U.dot(sigma).dot(V.T), 其中 V.T 正包含所有主成分
# 以下用 Python 實現 SVD(自定義資料)
import numpy as np
rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T

X_centered = X - X.mean(axis = 0)
U, s, V = np.linalg.svd(X_centered)
c1 = V.T[:, 0]
c2 = V.T[:, 1]
# print(c1, c2) # [0.94446029 0.32862557] [ 0.32862557 -0.94446029]
# 注意: PCA 假設數據圍繞原點集中, 所以如果要使用自定義PCA, 或者其他模塊, 要記得先把數據集中

# 低維度投影
# 一旦確定了所有主成分, 就可以將數據集投影到前 d 個主成分定義的超平面上
# 把訓練集投影到超平面上, 計算 訓練集矩陣 X 和 矩陣 W 的點積即可(W 是包含前 d 個主成分的矩陣 <- 由 V.T 的前 d 列組成的矩陣)
# 公式: X_d-proj = X.dot(W_d)
# 以下用剛才的資料 以 Python 代碼來實現
W2 = V.T[:, :2] # <- 因為這個資料是 2 維的 (透過 X.shape 可得知)
X2D = X_centered.dot(W2)
# print(W2)

# 使用 Scikit-Learn 的 PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X2D_sklearn = pca.fit_transform(X)
# print(pca.components_.T) # <- 和前面的 W2 一樣, 但執行結果差了一個負號

# 方差解釋率(通過屬性 explained_variance_ratio_ 取得)
# 表示每個主成分軸對整個數據集的方差貢獻度
# print(pca.explained_variance_ratio_) # [0.97634101 0.02365899]
# 上面的結果代表 第一條主成分(c1) 97.6% 的數據集方差來自於它, 第二條(c2) 2.3% 為第二條軸

# 選擇正確數量的維度
# 通常來說, 更好的做法是將靠前主成分的方差解釋率依次相加到 95% , 這時的維度數量是一個很好的選擇
# 除非為了數據可視化, 才降成2D/3D
# 以下的代碼是 計算若要保留訓練集方差的 95% 所需要最低維度的數量
# 作法 1. 
# pca2 = PCA()
# pca2.fit(X)
# cumsum = np.cumsum(pca2.explained_variance_ratio_) # <- np.cumsum 累加
# print(cumsum) # [0.97634101 1.        ]
# d = np.argmax(cumsum >= 0.95) + 1 # <- d 就是再次訓練PCA 並設置 n_components = d

# 作法 2.
# pca3 = PCA(n_components = 0.95) # <- 0.0 ~ 1.0 之間, 直接輸入方差比即可

# PCA 壓縮
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784')
X, y = mnist["data"], mnist["target"]

# pca = PCA(n_components = 154)
# X_mnist_reduced = pca.fit_transform(X)
# X_mnist_recovered = pca.inverse_transform(X_mnist_reduced)
# PCA 逆轉換, 回到原始維度: X_recovered = X_d-proj.dot(W_d.T)
# 但是經過降維過後又逆轉換的數據和原始數據會有小小的誤差, 稱為重建誤差(原始數據和重建數據的均方距離)

# 增量 PCA
# 增量主成分分析(IPCA): 把訓練集分成一個個小批量, 一次給IPCA算法一個(也可以應用於 在線應用PCA)
# 以下代碼是將 MNIST 數據集分成 100 個小批量(使用 Numpy array_split()), 將數據集降到 154維
# 注意: 必須為每個小批量調用 partial_fit(), 而不是 fit()
from sklearn.decomposition import IncrementalPCA
# n_batches = 100
# inc_pca = IncrementalPCA(n_components = 154)
# for X_batch in np.array_split(X, n_batches):
#     inc_pca.partial_fit(X_batch)
# X_mnist_reduced = inc_pca.transform(X)
# 也可以使用 Numpy memmap(), 允許操控一個儲存在磁碟二進制文件裡的大型數組
# X_mm = np.memmep(filname, dtype = "float32", mode = "readonly", shape = (m, n))
# batch_size = m // n_batches
# inc_pca = IncrementalPCA(n_components = 154, batch_size = batch_size)
# inc_pca.fit(X_mm)

# 隨機 PCA, 是一種隨機算法: 計算複雜度是 O(m*d^2)+O(d^2), 所以當 d << n , 算法要快很多
# 簡單的例子(僅大概架構)
# rnd_pca = PCA(n_components = 154, svd_solver = 'randomized')
# X_reduced = rnd_pca.fit_transform(X)


# 核主成分分析
# kPCA 擅長投影後保留實例的資料集群, 甚至也能超展開近似一個扭曲流型的數據集
from sklearn.decomposition import KernelPCA
# rbf_pca = KernelPCA(n_components = 2, kernel = "rbf", gamma = 0.4)
# X_reduced = rbf_pca.fit_transform(X)

# 選擇核函數和調整超參數
# 由於 kPCA 是一種非監督的學習算法, 降維通常是監督式學習任務,  網格搜尋找出最佳核超參數
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# clf = Pipeline([
#     ("kpca", KernelPCA(n_components = 2)),
#     ("log_reg", LogisticRegression())
# ])

# param_grid = [{
#     "kpca__gamma": np.linspace(0.03, 0.05, 10),
#     "kpca__kernel": ["rbf", "sigmoid"]
# }]

# grid_search = GridSearchCV(clf, param_grid, cv = 3)
# grid_search.fit(X, y)
# 透過核超參數可以通過變量 best_params_ 取得
# print(grid_search.best_params_)

# LLE(局部線性嵌入)
# 另一種非常強大的非線性降維(NLDR), 它屬於一種流形學習技術
# LLE 首先測量每個算法如何與最近鄰居線性相關, 然後為訓練集尋找一個能最大程度保留局部關係的低維表示
# LLE 擅長展開彎曲的流形, 特別是沒有太多噪聲時
# 使用 Scikit-Learn LocallyLinearEmbedding
from sklearn.manifold import LocallyLinearEmbedding
# lle = LocallyLinearEmbedding(n_components = 2, n_neightbors = 10)
# X_reduced = lle.fit_transform(X)
# 但是此方法很難擴大到 大型數據集(公式部分在課本上)


# 其他降維技巧
# 有些可以在 Scikit-Learn 找到 以下還有幾個流行的降維技術
# MDS, Isomap, t-SNE, LDA(SVM分類器, LDA是一個不錯的降維手段)