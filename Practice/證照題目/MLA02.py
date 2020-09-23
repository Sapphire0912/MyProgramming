from sklearn.datasets import make_blobs
X, y = make_blobs(200, 2, 4, cluster_std = 0.5, random_state = 0)
# print(X, y)

from sklearn.cluster import KMeans
n = []
for k in range(2, 200):
    kmean = KMeans(n_clusters = k, n_init = 15, max_iter = 200, random_state = 0)
    kmean.fit(X)
    if kmean.inertia_ >= 90:
        n.append((k, kmean.inertia_))
print(n) # [(2, 736.86391422994), (3, 304.9484842599343), (4, 94.02242630751765)] <- ?