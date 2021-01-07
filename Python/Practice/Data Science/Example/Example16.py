# 在SVM章節的例子
# 人臉辨識
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people(min_faces_per_person = 60)
# print(faces.target_names)
# ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
#  'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
# print(faces.images.shape)  # (1348, 62, 47)

# 先畫出其中的一些人臉看看接下來會用到的資料內容
# fig, ax = plt.subplots(3, 5)
# for i, axi in enumerate(ax.flat):
#     axi.imshow(faces.images[i], cmap = 'bone')
#     axi.set(xticks = [], yticks = [], xlabel = faces.target_names[faces.target[i]])
# plt.show()

# 每一張圖像都包含了[62x47], 將近3000多個像素點. 可以直接使用每個像素點來當成特徵
# 使用PCA 萃取150個基礎成分並匯入到SVM分類器中
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline

pca = PCA(n_components = 150, whiten = True, random_state = 42, svd_solver = 'randomized')
svc = SVC(kernel = 'rbf', class_weight = 'balanced')
model = make_pipeline(pca, svc)

# 因為需要測試此分類器的輸出, 所以要把資料分成訓練集和測試集
from sklearn.model_selection import train_test_split as tts
Xtrain, Xtest, ytrain, ytest = tts(faces.data, faces.target, random_state = 42)

# 最後使用一個格狀搜尋交叉驗證來探索參數的組合
from sklearn.model_selection import GridSearchCV
param_grid = {'svc__C': [1, 5, 10, 50], 'svc__gamma': [0.0001, 0.0005, 0.001, 0.005]}
grid = GridSearchCV(model, param_grid)
grid.fit(Xtrain, ytrain)
# print("Best Param: ", grid.best_params_) # {'svc__C': 10, 'svc__gamma': 0.001}
# 最佳值剛好落在中間, 如果是落在邊界上, 就需要拓展格子以確保找到是真的最佳值

# 現在有了交叉驗證模型, 就可以預測這個模型還沒有見過的測試資料標籤
model = grid.best_estimator_
yfit = model.predict(Xtest)

# 視覺化
# fig, ax = plt.subplots(4, 6)
# for i, axi in enumerate(ax.flat):
#     axi.imshow(Xtest[i].reshape(62, 47), cmap = 'bone')
#     axi.set(xticks = [], yticks = [])
#     axi.set_ylabel(faces.target_names[yfit[i]].split()[-1], 
#                    color = 'black' if yfit[i] == ytest[i] else 'red')
# fig.suptitle('Predicted Names; Incorrect Labels in Red', size = 14)
# plt.show()

# 透過分類報告來判讀評估器的效能(可以看出在小樣本中, 此最佳的評估器只有標錯1張)
from sklearn.metrics import classification_report
print(classification_report(ytest, yfit, target_names = faces.target_names))

# 也可以顯示在這些類別之間的混淆矩陣
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(ytest, yfit)
sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False,
            xticklabels = faces.target_names, yticklabels = faces.target_names)
plt.xlabel("True label")
plt.ylabel("Predicted label")
plt.show()

# 在真實世界的人臉辨識工作, 相片並不會被切割成這麼完美的方格, 此種情況下在面部分類的方法上
# 唯一的差別就是特徵的選取: 需要使用更複雜的演算法去找到這些臉, 以及獨立於像素之外去萃取特徵.
# 例如: OpenCV(http://opencv.org), 它包含了經過訓練的最佳化影像特徵萃取工具, 不論在一般的
# 使用或特別是在人臉辨識上都很好