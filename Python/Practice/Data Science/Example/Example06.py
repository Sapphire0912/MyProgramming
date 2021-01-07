# 美國聯邦州的資料

# Pre:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 載入資料
position = 'C:\\Users\\kotori\\Desktop\\Practice\\Data Science\\data\\'

pop = pd.read_csv(position + 'state-population.csv')
areas = pd.read_csv(position + 'state-areas.csv')
abbrevs = pd.read_csv(position + 'state-abbrevs.csv')

# 先查看每個檔案的頭幾筆資料
# print(pop.head())
# print(areas.head())
# print(abbrevs.head())

# 計算美國各州及地區根據2010年人口密度的排名
# 首先, 先合併資料
merged = pd.merge(pop, abbrevs, how = 'outer', left_on = 'state/region', right_on = 'abbreviation')
merged = merged.drop('abbreviation', 1) # 去除重複的標籤
# print(merged.head())

# 查找含有Null資料的內容
# print(merged.isnull().any())

# 查找缺少的詳細內容
# print(merged.loc[merged['state'].isnull(), 'state/region'].unique())
# ['PR' 'USA']

# 把缺少的內容 用值給替換掉
# 注意: 判斷式要放在前面
merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'

# 處理好state的資料不會有Null後, 接著就合併區域資料
final = pd.merge(merged, areas, on = 'state', how = 'left')

# 查找缺失資料
# print(final.isnull().any())

# 查找缺少的詳細內容
# print(final['state'].loc[final['area (sq. mi)'].isnull()].unique())
# ['United States']

# 把缺少的內容刪掉, 因為計算人口密度有NaN值, 即使用任何東西取代也沒有意義, 畢竟也不是真實的人口密度
final.dropna(inplace = True)
# 補充: inplace = True, 直接對原本的數據修改; = False, 傳回修改後的結果但不更改原數據

# 計算結果
data2010 = final.query("year == 2010 & ages == 'total'")
data2010.set_index('state', inplace = True)
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending = False, inplace = True)
print(density)
# 補充: ascending = True, 升序排列; = False, 降序排列