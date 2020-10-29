# What is Machine Learning ?
# ML 經常被分類為 AI 的子領域, 但是ML方法於資料科學的應用上, ML是建構資料的模型

# Categories of Machine Learning
# Two main type:
# supervised learning, unsupervised learning
# supervised learning:
# 包含某種方式去塑模(modeling)量測到的資料特徵(feature)以及一些與資料結合的標籤(label)之間的關係
# 一旦決定了這個模型(model), 可以被用來套用標籤到新的, 未知的資料
# 更進一步可再區分為分類(classification)和回歸(regression)工作
# classification的標籤是離散的類別, regression 是連續的量

# unsupervised learning:
# 包含了沒有參考任何標籤的資料集特徵的塑模, 常被形容成""讓資料自己說話""
# 這些模型包括集群(clustering)以及維度降低(dimensionality reduction)
# (Algorithm)clustering會識別出資料中不同的群組, 而dimensionality reduction則會搜尋更簡潔的資料表示方法

# In addition, semi-supervised learning method
# 半監督學習方法在資料不具備完整標籤的情況下是非常有用的

# 圖表的來源: httpsL//github.com/jakevdp/PythonDataScienceHandBook
# 接下來的內容從課本上看到p358(程式碼和圖表 在上面的連結看的到)

# Summary:
# Supervised Learning: 基於已經標上標籤的資料, 建立模型來預測標籤data
# Classification: 建立可以把2個或是更多的獨立的類別標上標籤的模型
# Regression: 建立可以用來預測連續標籤的模型
# Unsupervised Learning: 建立在未標上標籤的資料中識別出結構的模型
# Clustering: 建立在資料中偵測並識別出不同的群組之模型
# Dimensionality reduction: 建立在比較高維度的資料中可以偵測及識別出較低維度型

# Overfitting(過度擬合): 
# 在ML演算法中, 對於已知的資料驗證率非常精確但在新資料的驗證率不精確的情形, 稱為Overfitting