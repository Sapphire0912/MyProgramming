import itertools
import matplotlib.pyplot as plt
import numpy as np

# itertools 模組內有 permutations() 方法, 可以列出元素所有可能位置的組合
x = ["1", "2", "3"]
perm = itertools.permutations(x)
for i in perm:
    print(i)

# 時間複雜度比較
# 執行次數(n) n 為 1到10時繪製時間關係圖
n = np.linspace(1, 10, 10)
O_1 = n / n
O_log_n = np.log2(n)
O_n = n
O_nlog_n = np.log2(n) * n
O_nn = n * n

plt.xlabel("execution times")
plt.ylabel("execution time")
plt.plot(n, O_1, '-o', label="O(1)")
plt.plot(n, O_log_n, '-o', label="O(log n)")
plt.plot(n, O_n, '-o', label="O(n)")
plt.plot(n, O_nlog_n, '-o', label="O(nlog n)")
plt.plot(n, O_nn, '-o', label="O(n*n)")
plt.xticks(np.linspace(2, 10, 5))
plt.yticks(np.linspace(0, 100, 6))
plt.legend(loc="best")
plt.show()
