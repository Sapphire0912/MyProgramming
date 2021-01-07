# 流形學習

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 本章節不適合用 class(太多函式相關)
# 流形學習是一種非監督式學習的評估器, 可以尋找用來描述資料集, 在高維度空間中內嵌的低維度多樣性.\n\
# 之前的PCA雖然具有彈性, 快速及容易解釋的優點, 但是資料集為非線性時效果就不是這麼顯著.\n\
# 在此示範幾種流形方法, MDS(multidimensional scaling), LLE(locally linear embedded),\n\
# Isomap(isometric mapping).
    
def make_hello(self, N = 1000, rseed = 42):
    '''畫一個HELLO圖形, 存成一個PNG檔'''
    path = '.\Practice\Data Science\MachineLearning\picture\ML_ManifoldLearning_hello.png'
    fig, ax = plt.subplots(figsize = (4, 1))
    fig.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1)
    ax.axis('off')
    ax.text(0.5, 0.4, 'HELLO', va = 'center', ha = 'center', weight = 'bold', size = 85)
    fig.savefig(path)
    plt.close(fig)

    # 開啟PNG檔, 然後從其中畫一些隨機點
    from matplotlib.image import imread
    data = imread(path)[::-1, :, 0].T
    rng = np.random.RandomState(rseed)
    X = rng.rand(4 * N, 2)
    i, j = (X * data.shape).astype(int).T
    mask = (data[i, j] < 1)
    X = X[mask]
    X[:, 0] *= (data.shape[0] / data.shape[1])
    X = X[:N]
    return X[np.argsort(X[:, 0])]
        
# 呼叫函式
X = make_hello(1000)
colorsize = dict(c = X[:, 0], cmap = plt.cm.get_cmap('rainbow', 5))
# plt.scatter(X[:, 0], X[:, 1], **colorsize)
# plt.axis('equal')
# plt.show()
# 上圖繪製了 HELLO 字元形狀由資料點所組成的, 這樣的資料形式可以幫助視覺上看出此演算法做的事

# MDS(multidimensional Scaling)
def rotate(X, angle):
    # theta 角度, R為旋轉角度
    theta = np.deg2rad(angle)
    R = [[np.cos(theta), np.sin(theta)],
         [-np.sin(theta), np.cos(theta)]]
    return np.dot(X, R)

# X2 = rotate(X, 20) + 5 # +5 為平移
# plt.scatter(X2[:, 0], X2[:, 1], **colorsize)
# plt.axis('equal')
# plt.show()
# 上圖可以得知, x y值不是此資料中最基本必須的關係, 每一個點和其他點之間的"距離"才是基本的關係

# 一個經常用來表達此種情況的方式是使用距離矩陣: 對於 N個資料點, 建立一個 N*N 陣列,
# 其中i, j包含第 i 點和 第 j 點的距離, 使用 Scikit-Learn 高效的 pairwise_distances
from sklearn.metrics import pairwise_distances
# D = pairwise_distances(X)
# print(D.shape) # (1000, 1000)
# N = 1000, 會得到 1000 * 1000 的矩陣. 把它視覺化
# plt.imshow(D, zorder = 2, cmap = 'Blues', interpolation = 'nearest')
# plt.colorbar()
# plt.show()
# 如果同樣的建構一個旋轉椅及平移過的資料之距離矩陣, 則可以看到同樣的內容
# D2 = pairwise_distances(X2)
# np.allclose(D, D2) # True
# np.allclose(a, b): 比對 a, b 是否相同, 相同回傳 True(前提是兩者的維度和空間大小必須一樣否則會報錯)
# 上面的測試得知, 距離矩陣不受任何平移及旋轉的影響.

# MDS的目標: 給予一個每點之間的距離矩陣, 它可以回複此資料的D維度座標表示法
# (Scikit-Learn 的 MDS)使用 precomputed 設定 dissimilarity 建立此模型, 然後把距離矩陣傳遞進去
from sklearn.manifold import MDS
# model = MDS(n_components = 2, dissimilarity = 'precomputed', random_state = 1)
# out = model.fit_transform(D)
# plt.scatter(out[:, 1], out[:, 0], **colorsize)
# plt.axis('equal')
# plt.show()
# 上圖從成對距離中計算的MDS嵌入
# MDS 演算法復原了資料中可能的二維座標表示法之一, 只使用了用來描述資料點之間關係的 N*N 距離矩陣

# 把 MDS 作為 ManifoldLearning
# 當距離矩陣可以被在 任一維度的資料中計算得出, 此種方法的用處就更加顯著
# 舉例來說, 我們使用以下的函式把它投影到3維上
def random_projection(X, dimension = 3, rseed = 42):
    assert dimension >= X.shape[1] # 斷言語句
    rng = np.random.RandomState(rseed)
    C = rng.randn(dimension, dimension)
    e, V = np.linalg.eigh(np.dot(C, C.T))
    return np.dot(X, V[:X.shape[1]])

# X3 = random_projection(X, 3)
# print(X3.shape) # (1000, 3)
# 把資料視覺化
from mpl_toolkits import mplot3d
# ax = plt.axes(projection = '3d')
# ax.scatter(X3[:, 0], X3[:, 1], X3[:, 2], **colorsize)
# ax.view_init(azim = 70, elev = 50)
# plt.show()

# 視覺化後, 把資料放入 MDS estimator 上, 計算距離矩陣
# model = MDS(n_components = 2, random_state = 1)
# out3 = model.fit_transform(X3)
# plt.scatter(out3[:, 1], out3[:, 0], **colorsize)
# plt.axis('equal')
# plt.show()
# 在此就是流形學習評估器本質上的目標: 給予一個高維度的內嵌資料, 它可以尋找一個可以保留資料裡面
# 之關係資訊的低維度表示法. 在這裡的 MDS 例子中, 它保存的內容是每一對資料點之間的距離



# 非線性嵌入(Nonlinear Embeddings): MDS不能應用的場合
# 前面的例子都是線性嵌入, 本質上就是旋轉, 平移和縮放資料到高維度的空間中,
# 若超過了這些簡單的集合, MDS並無法使用在非線性的嵌入中

# 考量以下的嵌入, 在三維空間中讓輸入變形成為S的形狀:
def make_hello_s_curve(X):
    t = (X[:, 0] - 2) * 0.75 * np.pi
    x = np.sin(t)
    y = X[:, 1]
    z = np.sign(t) * (np.cos(t) - 1)
    return np.vstack((x, y, z)).T

XS = make_hello_s_curve(X)
# ax = plt.axes(projection = '3d')
# ax.scatter3D(XS[:, 0], XS[:, 1], XS[:, 2], **colorsize)
# plt.show()
# 在三維空間中把資料內嵌一個非線性的內容

# 所有資料點之間的基本關係還是存在, 但是此時這些資料已經被使用非線性的方式轉換過了(變成S形狀)
# 若對此資料用 MDS 演算法, 看以下的結果
# model = MDS(n_components = 2, random_state = 2)
# outS = model.fit_transform(XS)
# plt.scatter(outS[:, 0], outS[:, 1], **colorsize)
# plt.axis('equal')
# plt.show()
# 圖為 MDS(mistake); 從圖可以看出是S形狀, 且資料無法復原成原本的結構



# 非線性流形(Nonlinear Manifolds): 區域線性嵌入(Locally Linear Embedding)
# 我們可以看到問題的來源是 MDS 在建構嵌入時, 試著去保留最遠的距離.
# 但如果讓它只保留比較近的點之間的距離, 結果比較接近我們想要的
# MDS: 會試著去保留在資料集中每一對資料點之間的距離
# LLE(Locally Linear Embedding)演算法: 不同於保留所有的距離, 只試著保留鄰接點的距離

# LLE 有許多不同的修改版本, 在此使用一個 modified LLE 演算法, 去復原這個內嵌的二維複本
# 以下例子
from sklearn.manifold import LocallyLinearEmbedding
model = LocallyLinearEmbedding(n_neighbors = 100, n_components = 2, method = 'modified', 
                               eigen_solver = 'dense')
out = model.fit_transform(XS)
# fig, ax = plt.subplots()
# ax.scatter(out[:, 0], out[:, 1], **colorsize)
# ax.set_ylim(0.15, -0.15)
# plt.show()
# 雖然還是有點變形, 但是至少有抓到此資料中最重要的關係了

# 關於流形學習的一些思考
# 相對於PCA的唯一明確的優點: 有能力去保留資料中的非線性關係