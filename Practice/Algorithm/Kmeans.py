# Kmeans Clustering Algorithm
# Unsupervised Learning (Cluster)

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def example1():
    pass

def example2():
    iris = datasets.load_iris()
    # print(iris.data.shape) # (150, 4)

    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    # print(df.head())

    df['flower'] = iris.target
    # print(df.head(7))

    km = KMeans(n_clusters = 3)
    yp = km.fit_predict(df)
    # print(yp)

    df['cluster'] = yp
    # print(df.head(10))
    # print(df.cluster.unique()) # 尋找唯一的資料

    df1 = df[df.cluster == 0]
    df2 = df[df.cluster == 1]
    df3 = df[df.cluster == 2]

    # plt.scatter(df1["petal length (cm)"], df1["petal width (cm)"], color = 'blue')
    # plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], color = 'green')
    # plt.scatter(df3["petal length (cm)"], df3["petal width (cm)"], color = 'yellow')

    # Elbow Plot
    sse = []
    for k in range(1, 10):
        km = KMeans(n_clusters = k)
        km.fit(df)
        sse.append(km.inertia_)

    plt.xlabel('K')
    plt.ylabel('Sum of square error')
    plt.plot(range(1, 10), sse)
    plt.show()

def example3():
    flower = datasets.load_sample_image('flower.jpg')
    # can be any picture with high resulotion image
    # ax = plt.axes(xticks = [], yticks = [])
    # ax.imshow(flower)
    # print(flower.shape) # (length pixel, width pixel, n_dimension)

    data = flower / 255 # reshape 0 - 255, between 0 and 1
    data = data.reshape(427 * 640, 3)
    # print(data.shpae) # (273200, 3)

    def plot_pixels(data, title, colors = None, N = 10000):
        if colors is None:
            colors = data
        
        # choose a random subset
        rng = np.random.RandomState(0)
        i = rng.permutation(data.shape[0])[:N]
        
        # permutation method:
        # np.random.permutation(): 隨機排列
        # Ex. np.random.permutation([i for i in range(10)])

        colors = colors[i]
        R, G, B = data[i].T
        fig, ax = plt.subplots(1, 2, figsize = (16, 6))
        ax[0].scatter(R, G, color = colors, marker = '.')
        ax[0].set(xlabel = 'Red', ylabel = 'Green', xlim = (0, 1), ylim = (0, 1))

        ax[1].scatter(R, B, color = colors, marker = '.')
        ax[1].set(xlabel = "Red", ylabel = "Blue", xlim = (0, 1), ylim = (0, 1))

        fig.suptitle(title, size = 20)
    
    # plot_pixels(data, title = "Input color space: 16 million possible colors")
    from sklearn.cluster import MiniBatchKMeans
    import warnings
    warnings.simplefilter("ignore") # Fix numpy issue
    kmeans = MiniBatchKMeans(16)
    kmeans.fit(data)
    new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

    plot_pixels(data, colors = new_colors, title = "Reduced color space: 16 colors")

    plt.show()

example3()