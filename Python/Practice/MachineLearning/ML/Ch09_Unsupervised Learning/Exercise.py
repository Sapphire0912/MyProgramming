from sklearn.datasets import fetch_olivetti_faces
olivetti = fetch_olivetti_faces()
# print(olivetti.DESCR) # 關於 olivetti 的描述 

from sklearn.model_selection import StratifiedShuffleSplit as SSS
# 訓練驗證集 和 測試集
data_split = SSS(n_splits = 1, test_size = 40, random_state = 42)
train_valid_idx, test_idx = next(data_split.split(olivetti.data, olivetti.target))
X_train_valid, y_train_valid = olivetti.data[train_valid_idx], olivetti.target[train_valid_idx]
X_test, y_test = olivetti.data[test_idx], olivetti.target[test_idx]

# 把訓練驗證集 拆成 訓練集 驗證集
data_split = SSS(n_splits = 1, test_size =  80, random_state = 43)
train_idx, valid_idx = next(data_split.split(X_train_valid, y_train_valid))
X_train, y_train = X_train_valid[train_idx], y_train_valid[train_idx]
X_valid, y_valid = X_train_valid[valid_idx], y_train_valid[valid_idx]

# print(X_train.shape, y_train.shape) # (280, 4096) (280,)
# print(X_valid.shape, y_valid.shape) # (80, 4096) (80,)
# print(X_test.shape, y_test.shape) # (40, 4096) (40,)

from sklearn.decomposition import PCA
pca = PCA(0.99)
X_train_pca = pca.fit_transform(X_train)
X_valid_pca = pca.transform(X_valid)
X_test_pca = pca.transform(X_test)
# print(pca.n_components_) # 199

from sklearn.cluster import KMeans
k_range = range(5, 150, 5)
kmeans_per_k = []
for k in k_range:
    # print("k={}".format(k))
    kmeans = KMeans(n_clusters = k, random_state = 42).fit(X_train_pca)
    kmeans_per_k.append(kmeans)

from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib as mpt
import matplotlib.pyplot as plt
silhouette_scores = [silhouette_score(X_train_pca, model.labels_) for model in kmeans_per_k]
best_index = np.argmax(silhouette_scores) # 傳回最大值的索引值
best_k = k_range[best_index]
best_score = silhouette_scores[best_index]

# plt.figure(figsize = (8, 3))
# plt.plot(k_range, silhouette_scores, 'bo-')
# plt.xlabel("$k$", fontsize = 14)
# plt.ylabel("Silhouette score", fontsize = 14)
# plt.plot(best_k, best_score, "rs") # red square
# plt.show()

# print(best_k) # 100
inertias = [model.inertia_ for model in kmeans_per_k]
best_inertias = inertias[best_index]

# plt.figure(figsize = (8, 3.5))
# plt.plot(k_range, inertias, "bo-")
# plt.xlabel("$k$", fontsize = 14)
# plt.ylabel("Inertia", fontsize = 14)
# plt.plot(best_k, best_inertias, "rs")
# plt.show()

best_model = kmeans_per_k[best_index]

def plot_faces(faces, labels, n_cols = 5):
    n_rows = (len(faces) - 1) // n_cols + 1
    plt.figure(figsize = (n_cols, n_rows * 1.1))
    for index, (face, label) in enumerate(zip(faces, labels)):
        plt.subplot(n_rows, n_cols, index + 1)
        plt.imshow(face.reshape(64, 64), cmap = "gray")
        plt.axis("off")
        plt.title(label)
    plt.show()

for cluster_id in np.unique(best_model.labels_):
    # print("Cluster", cluster_id)
    in_cluster = best_model.labels_ == cluster_id
    faces = X_train[in_cluster].reshape(-1, 64, 64)
    labels = y_train[in_cluster]
    # plot_faces(faces, labels)

from sklearn.ensemble import RandomForestClassifier as RFC
# rfc = RFC(n_estimators = 150, random_state = 42)
# rfc.fit(X_train_pca, y_train)
# print(rfc.score(X_valid_pca, y_valid)) # 0.9


X_train_reduced = best_model.transform(X_train_pca)
X_valid_reduced = best_model.transform(X_valid_pca)
X_test_reduced = best_model.transform(X_test_pca)
rfc = RFC(n_estimators = 150, random_state = 42)
rfc.fit(X_train_reduced, y_train)
# print(rfc.score(X_valid_reduced, y_valid)) # 0.75

from sklearn.pipeline import Pipeline
for n_clusters in k_range:
    pipeline = Pipeline([
        ("kmeans", KMeans(n_clusters = n_clusters, random_state = n_clusters)),
        ("forest_clf", RFC(n_estimators = 150, random_state = 42))
    ])
    pipeline.fit(X_train_pca, y_train)
    # print(n_clusters, pipeline.score(X_valid_pca, y_valid))

X_train_extended = np.c_[X_train_pca, X_train_reduced]
X_valid_extended = np.c_[X_valid_pca, X_valid_reduced]
X_test_extended = np.c_[X_test_pca, X_test_reduced]

rfc = RFC(n_estimators = 150, random_state = 42)
rfc.fit(X_train_extended, y_train)
# print(rfc.score(X_valid_extended, y_valid)) # 0.825


from sklearn.mixture import GaussianMixture as GM
gm = GM(n_components = 40, random_state = 42)
y_pred = gm.fit_predict(X_train_pca)

n_gen_faces = 20
gen_faces_reduced, y_gen_faces = gm.sample(n_samples = n_gen_faces)
gen_faces = pca.inverse_transform(gen_faces_reduced)
# plot_faces(gen_faces, y_gen_faces)

n_rotated = 4
rotated = np.transpose(X_train[:n_rotated].reshape(-1, 64, 64), axes = [0, 2, 1])
rotated = rotated.reshape(-1, 64*64)
y_rotated = y_train[:n_rotated]

n_flipped = 3
flipped = X_train[:n_flipped].reshape(-1, 64, 64)[:, ::-1] # x[:, ::-1] <- 每一列倒序
flipped = flipped.reshape(-1, 64*64)
y_flipped = y_train[:n_flipped]

n_darkened = 3
darkened = X_train[:n_darkened].copy()
darkened[:, 1:-1] *= 0.3
darkened = darkened.reshape(-1, 64*64)
y_darkened = y_train[:n_darkened]

X_bad_faces = np.r_[rotated, flipped, darkened] # np.c_ 按照 列 連接兩個矩陣, np.r_ 按照 行 連接兩個矩陣
y_bad = np.concatenate([y_rotated, y_flipped, y_darkened])
# plot_faces(X_bad_faces, y_bad)
X_bad_faces_pca = pca.transform(X_bad_faces)
# print(gm.score_samples(X_bad_faces_pca))
# print(gm.score_samples(X_train_pca[:10]))

def reconstruction_errors(pca, X):
    X_pca = pca.transform(X)
    X_reconstructed = pca.inverse_transform(X_pca)
    mse = np.square(X_reconstructed - X).mean(axis = -1)
    return mse
print(reconstruction_errors(pca, X_train).mean())
print(reconstruction_errors(pca, X_bad_faces).mean())
# plot_faces(X_bad_faces, y_gen_faces)
X_bad_faces_reconstructed = pca.inverse_transform(X_bad_faces_pca)
# plot_faces(X_bad_faces_reconstructed, y_gen_faces)
