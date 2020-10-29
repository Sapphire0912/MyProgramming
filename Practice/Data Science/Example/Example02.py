# 計算下雨天數
# 使用西雅圖2014年的日降雨統計數據
# file: Seattle2014.csv
# position: C:\Users\kotori\Desktop\Practice\Data Science\data
# 使用直方圖畫出每日降雨量

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

file = 'C:\\Users\\kotori\\Desktop\\Practice\\Data Science\\data\\Seattle2014.csv'
data = pd.read_csv(file)
data = data['PRCP'].values # np.array 資料型態

inches = data / 254

ax = plt.axes()
plt.hist(inches, 40)
plt.xlim(0, 2)
plt.ylim(0, 250)
ax.xaxis.set_major_locator(plt.MaxNLocator(4)) # 必須有plt.axes()才有可以設定軸刻度的屬性
plt.show()