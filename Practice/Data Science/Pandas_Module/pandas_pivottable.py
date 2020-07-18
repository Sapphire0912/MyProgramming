import numpy as np
import pandas as pd
# 樞紐分析表(pivot table): 常見於電子試算表, 和其他以表格為操作方式的程式中. 
# 以行(欄)為主的資料當作輸入, 並把這些項目分組到二維表格中; 
# 可以把它當成是多重維度的GroupBy聚合計算

# 激發樞紐分析法(使用鐵達尼號旅客的資料)
import seaborn as sns
titanic = sns.load_dataset('titanic')
# print(titanic.head())
#  survived  pclass     sex   age  sibsp  parch     
#  fare embarked  class    who  adult_male deck  
#  embark_town alive  alone  <- titanic資料裡擁有上述的這些"行標籤"   

# 手動製作樞紐分析表
# print(titanic.groupby('sex')[['survived']].mean())
# ['survived']
# sex
# female    0.742038
# male      0.188908
# [['survived']]
#         survived
# sex
# female  0.742038
# male    0.188908
# print(titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack())

# 樞紐分析表的語法
# DataFrame.pivot_table(index, columns, aggfunc='mean',...etc) 
# print(titanic.pivot_table('survived', index = 'sex', columns = 'class'))
# 此種作法同樣也可以得到 line 26 的結果

# 多層的樞紐分析表
# 猶如groupby裡, pivot_table中區分群組可以使用多層指定, 裡面也有多個參數可以使用
age = pd.cut(titanic['age'], [0, 18, 80])
# print(titanic.pivot_table('survived', ['sex', age], 'class'))
fare = pd.qcut(titanic['fare'], 2) 
# print(titanic.pivot_table('survived', ['sex', age], [fare, 'class']))
# 額外選項之後補充