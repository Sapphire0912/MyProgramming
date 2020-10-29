# 資料裝箱(Binning Data)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 假如有1000個值想要很快的找出他們分別落在陣列中的哪個箱子
# 使用ufunc.at
np.random.seed(42)
x = np.random.randn(1000)

# 手動計算直方圖
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
# 對每一個x找到適合的箱子
i = np.searchsorted(bins, x)
# 對著個箱子每一個加1
np.add.at(counts, i, 1)

# 把結果畫出來
# plt.plot(bins, counts, drawstyle = 'steps')
plt.hist(x, bins, histtype = 'step')
plt.show()