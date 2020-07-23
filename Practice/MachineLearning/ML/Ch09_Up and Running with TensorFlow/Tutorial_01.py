# coding=uft8
# 運行 TensorFlow
import tensorflow as tf

# 創建一個計算圖並在會話中執行
x = tf.Variable(3, name = "x")
y = tf.Variable(4, name = "y")
f = x*x*y + y + 2
# 上面這些程式碼實際上並沒有執行任何計算, 僅僅創建一個計算圖而已(甚至變數都還沒初始化)
# 若要執行這個圖, 就需要打開一個 TensorFlow 的會話, 看以下程式碼
with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()
    print(result)
