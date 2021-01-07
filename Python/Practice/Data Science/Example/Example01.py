# 美國總統的平均身高
# 用直方圖繪製出美國總統的身高分布
# file: president_heights.csv
# position: C:\Users\kotori\Desktop\Practice\Data Science\data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

file = 'C:\\Users\\kotori\\Desktop\\Practice\\Data Science\\data\\president_heights.csv'
data = pd.read_csv(file)
heights = data['height(cm)']
heights = np.array(heights)

plt.hist(heights, edgecolor = 'black')
plt.xlabel('height(cm)')
plt.ylabel('number')
plt.title('Height Distribution of US Presidents')
plt.xlim(160, 195)
plt.ylim(0, 12)
plt.show()
