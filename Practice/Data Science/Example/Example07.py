# 出生率資料
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

file = 'C:\\Users\\kotori\\Desktop\\MyProgramming\\Practice\\Data Science\\data\\births.csv'
births = pd.read_csv(file)

# 使用樞紐分析表開始對資料做多一點的了解先加上一個10年欄, 把以10年為單位的男性/女性當成一個函數
births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index = 'decade', columns = 'gender', aggfunc = 'sum')

# 為了更清楚的展示, 把每十年改成每年
births.pivot_table('births', index = 'year', columns = 'gender', aggfunc = 'sum').plot()
plt.ylabel('total births per year')
plt.show()