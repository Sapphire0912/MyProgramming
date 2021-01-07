# coding=utf8
# 運行 TensorFlow
# (這裡的代碼是使用 1.X 版本的指令, 到時做練習題時要改成 2.X 版本的指令)
import tensorflow as tf

tf.reset_default_graph() # 重置默認圖, 因為反覆執行同條命令會導致在同一個圖上添加許多重複節點

# 創建一個計算圖並在會話中執行
# x = tf.Variable(3, name = "x")
# y = tf.Variable(4, name = "y")
# f = x*x*y + y + 2
# 上面這些程式碼實際上並沒有執行任何計算, 僅僅創建一個計算圖而已(甚至變數都還沒初始化)
# 若要執行這個圖, 就需要打開一個 TensorFlow 的會話, 看以下程式碼
# with tf.Session() as sess:
#     x.initializer.run()
#     y.initializer.run()
#     result = f.eval()
#     print(result)
# 或者 先創建 tf.Session() 再用 sess.run() 執行變數初始化; 但是這樣做最後需要關閉會畫框 sess.close()
# 除了手動為每個變數調用初始化屬性外, 可以使用 global_variables_initializer()
# init = tf.global_variables_initializer() # 創建初始化節點(此時尚未替變數初始化)
# with tf.Session() as sess:
#     init.run()
#     result = f.eval()
#     print(result)
# tensorflow 程序可以分成兩個部分: 第一部分用來構建一個計算圖(展現 ML 訓練和 訓練所需的計算), 第二部分來執行這個計算圖

# 管理圖
# 我們所創建的所有節點都會自動添加到默認圖上(看以下例子)
# x1 = tf.Variable(1)
# print(x1.graph is tf.get_default_graph()) # True
# 若要管理互相不依賴的圖, 可以創建新的圖後 則用 with 來將它設置為默認圖
# graph = tf.Graph()
# with graph.as_default():
#     x2 = tf.Variable(2)
# print(x2.graph is graph, x2.graph is tf.get_default_graph()) # True False

# 節點值的生命週期
# 當求一個節點的值時, Tensorflow 會自動檢測該節點所依賴的節點, 並先對這些節點求值
# w = tf.constant(3)
# x = w + 2
# y = x + 5
# z = x * 3

# with tf.Session() as sess:
#     print(y.eval()) # 10
#     print(z.eval()) # 15
# 在圖的每次執行中, 所有節點值都會被丟棄, 但是變數的值不會; 因為變數的值是由會話維護的, 因此生命週期為 會話開始到執行結束
# 上面的代碼, 因為 Tensorflow 不會重複用上一步求值的結果, 所以 w, x 值會被計算兩次, 流程如下:
# w = 3 -> x = 3 + 2, x = 5 -> y = 5 + 5, y = 10; z = x * 3 -> x = w + 2 -> w = 3 -> x = 5 -> z = 5 * 3, z = 15

# 如果不想重複求值, 則必須在一次圖的執行中就完成 y, z 的求值
# with tf.Session() as sess:
#     y_val, z_val = sess.run([y, z])
#     print(y_val, z_val) # 10 15
# 注意: 單進程的 Tensorflow 即使它們共享一個計算圖, 多個會話之間依然互相隔離, 不共享任何狀態


# Tensorflow 中的線性回歸
# 計算 加州的住房數據線性回歸
# 要求:
#   1. 對所有訓練實例添加一個額外的偏移量(x0 = 1)
#   2. 創建兩個常量節點, x, y 以及 目標
#   另外用代碼創建 theta 求值, theta 的定義用的是正規方程(ch04有解釋)
#   正規方程: theta = inv(X.T.dot(X)).dot(X.T).dot(y)
# import numpy as np
# from sklearn.datasets import fetch_california_housing
# housing = fetch_california_housing()
# data, target = housing.data, housing.target

# 1.
# bias = np.ones((data.shape[0], 1))
# data_bias = np.c_[bias, data]
# print(data_bias)

# 2.
# X = tf.constant(data_bias, dtype = tf.float32, name = "X")
# y = tf.constant(target.reshape(-1, 1), dtype = tf.float32, name = "y")
# XT = tf.transpose(X)
# theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)

# Result:
# with tf.Session() as sess:
#     theta_val = theta.eval()
#     print(theta_val)
# [[-3.7225266e+01]
#  [ 4.3568176e-01]
#  [ 9.3872147e-03]
#  [-1.0598953e-01]
#  [ 6.3939309e-01]
#  [-4.1104349e-06]
#  [-3.7780963e-03]
#  [-4.2437303e-01]
#  [-4.3785891e-01]]


# Tensorflow 實現 梯度下降法(ch04)
# 注意: 使用梯度下降法之前, 要記得先對輸入的特徵向量歸一化
# pre: 先進行歸一化
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaled_data = StandardScaler().fit_transform(data_bias, target[:, None])

# 手工計算梯度(之後回來驗證這個值是否正確)
# n_epochs = 1000
# learning_rate = 0.01
# X2 = tf.constant(scaled_data, dtype = tf.float32, name = "X2")
# y2 = tf.constant(target[:, None], dtype = tf.float32, name = "y2")
# theta2 = tf.Variable(tf.random_uniform([data.shape[1] + 1, 1], -1.0, 1.0), name = "theta2")
# y_pred = tf.matmul(X2, theta2, name = "predictions")
# error = y_pred - y2
# mse = tf.reduce_mean(tf.square(error), name = "mse")
# gradients = 2/data.shape[0] * tf.matmul(tf.transpose(X2), error) # 原本的數學算法
# gradients = tf.gradients(mse, [theta2])[0] # 在 Tensorflow 使用自動微分
# training_op = tf.assign(theta2, theta2 - learning_rate * gradients)

# init = tf.global_variables_initializer()

# with tf.Session() as sess:
#     sess.run(init)

#     for epoch in range(n_epochs):
#         if epoch % 100 == 0:
#             print("Epoch: ", epoch, "MSE:", mse.eval())
#         sess.run(training_op)
    
#     best_theta2 = theta2.eval()
#     print(best_theta2)

# 使用優化器
# 把上面原本的 gradients = ... 和 training_op = ... 改成
# optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)
# training_op = optimizer.minimize(mse)
# 或者其他類型的優化器, 只需要把 GradientDescentOptimizer 改成 MomentumOptimizer 即可 <- 後面會詳細介紹


# 給訓練算法提供數據
# 這裡只介紹 tf.placeholder() 方法
# A = tf.placeholder(tf.float32, shape = (None, 3))
# B = A + 5
# with tf.Session() as sess:
#     B_val1 = B.eval(feed_dict = {A: [[1, 2, 3]]})
#     B_val2 = B.eval(feed_dict = {A: [[1, 2, 3], [7, 8, 9]]})
#     print(B_val1, B_val2)

# 保存和恢復模型
# 在會話框開啟的時間, 使用 save() 和 restore() 
# arr1 = tf.Variable(tf.random_normal(shape = [2]), name = 'arr1')
# arr2 = tf.Variable(tf.random_normal(shape = [5]), name = 'arr2')
# init = tf.global_variables_initializer()
# savepath = ".\\Ch09_Up and Running with TensorFlow\\save"
# saver = tf.train.Saver()
import os
# with tf.Session() as sess:
#     sess.run(init)
#     if not os.path.exists(savepath):
#         os.mkdir(savepath)
#     saver.save(sess, savepath + '\\test')

# with tf.Session() as sess:
#     load = tf.train.import_meta_graph(savepath + "\\test.meta")
#     load.restore(sess, tf.train.latest_checkpoint(savepath))
#     sess.run(tf.global_variables_initializer())
#     print(sess.run('arr1:0'))

# 載入流程 -> 載入網路結構(L.161) -> 載入最後一次的checkpoint(L.162) -> 初始化(L.163) -> 執行(L.164)


# 使用 TensorBoard 來可視化圖 和 命名作用域
# (這裡的程式用 深度學習快速入門 那本書 單元: 如何使用 Tensorboard)
# 另外 可以參考<<DeepLearning 設計下一代人工智慧演算法 第三章>>
# print(os.getcwd()) # 獲取當前的工作路徑

# from datetime import datetime
# now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
# root_logdir = "./Ch09_Up and Running with Tensorflow/tf_logs"
# logdir = "{}/run-{}/".format(root_logdir, now)

# 命名空間域
# with tf.name_scope("const") as const:
#     a = tf.constant(10, name = "a")
#     b = tf.constant(90, name = "b")
# with tf.name_scope("variable") as vari:
#     y = tf.Variable(a + b * 2, name = "y")
# model = tf.global_variables_initializer()

# with tf.Session() as sess:
#     merged = tf.summary.merge_all()
#     writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
#     sess.run(model)
#     print(sess.run(y))
#     print(a.op.name) # const/a
#     print(b.op.name) # const/b
#     print(y.op.name) # variable/y


# 模塊化
# 假如我們要創建一個計算兩個修正線性單元(Rectified Linear Unit, ReLU)之和的圖
# 公式: h_w,b(X) = max(X.dot(w)+b, 0); 通常的定義是 f(x) = max(0, x) <- 斜坡函數
# (在神經網路中會再加以介紹)
n_features = 3
# X = tf.placeholder(tf.float32, shape = (None, n_features), name = "X")

# w1 = tf.Variable(tf.random_normal((n_features, 1)), name = "weights1")
# w2 = tf.Variable(tf.random_normal((n_features, 1)), name = "weights2")
# b1 = tf.Variable(0.0, name = "bias1")
# b2 = tf.Variable(0.0, name = "bias2")

# z1 = tf.add(tf.matmul(X, w1), b1, name = "z1")
# z2 = tf.add(tf.matmul(X, w2), b2, name = "z2")

# relu1 = tf.maximum(z1, 0, name = "ReLU1")
# relu2 = tf.maximum(z2, 0, name = "ReLu2")

# output = tf.add(relu1, relu2, name = "output")
# 上面這段代碼可以完成 ReLU 的動作, 但是這種程式容易出錯且不好維護
# 事實上, 此代碼包含了 cut-and-paste(重複的 剪切和貼上) 的錯誤, 把資料流圖形可視化會更清楚
# testpath = "./Ch09_Up and Running with TensorFlow/test_relu"
# count = 1
# log_dir = "{}/relu{}/".format(testpath, count)
# writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())

# 一旦要添加多個 ReLU 就會變得非常複雜, Tensorflow 會保持著不重複的原則: 用一個 ReLU 的函數來構建
# def ReLU(X):
#     with tf.name_scope("relu"):
#         w_shape = (int(X.get_shape()[1]), 1)
#         w = tf.Variable(tf.random_normal(w_shape), name = "weights")
#         b = tf.Variable(0.0, name = "bias")
#         z = tf.add(tf.matmul(X, w), b, name = "z")
#         return tf.maximum(z, 0, name = "relu")

# n_features = 3
# X = tf.placeholder(tf.float32, shape = (None, n_features), name = "X")
# relus = [ReLU(X) for i in range(5)]
# output = tf.add_n(relus, name = "output")
# # 圖形化(沒有使用命名作用域)
# count = 2
# log_dir = "{}/relu{}/".format(testpath, count)
# writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())
# Tensorflow 會發現此種規律性, 將其歸類到一組避免介面混亂, 另外使用命名作用域又可以更加清晰
# count = 3
# log_dir = "{}/relu{}/".format(testpath, count)
# writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())


# 共享變量
# 有非常多種做法: 可以利用函數傳參, 或著建立字典, 創建一個class等等
# 在 Tensorflow 所提供的是先透過 get_variable() 來創建共享變量(如果共享變量不存在, 反之覆用該共享變量)
# 期望的行為是 透過 variable_scope() 來控制(創建或者覆用), 看以下例子
def relu(X):
    with tf.variable_scope("relu", reuse = tf.AUTO_REUSE):
        threshold = tf.get_variable("threshold") # 取得變數
        with tf.name_scope("relu"):
            w_shape = (int(X.get_shape()[1]), 1)
            w = tf.Variable(tf.random_normal(w_shape), name = "weights")
            b = tf.Variable(0.0, name = "bias")
            z = tf.add(tf.matmul(X, w), b, name = "z")
            return tf.maximum(z, threshold, name = "max")
X = tf.placeholder(tf.float32, shape = (None, n_features), name = "X")

with tf.variable_scope("relu"):
    threshold = tf.get_variable('threshold', shape = (), initializer = tf.constant_initializer(0.0)) # 創建變數

relus = [relu(X) for relu_index in range(5)]
output = tf.add_n(relus, name = "output")

# print(os.getcwd())
testpath = "./Tensorflow/Ch09_Up and Running with TensorFlow/test_relu"
count = 4
log_dir = "{}/relu{}/".format(testpath, count)
writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())


# 這個章節學完後 看一下其他書比較然後再熟悉一下