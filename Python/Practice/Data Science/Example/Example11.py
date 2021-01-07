import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

# p279. 假日對於美國出生人數之影響
# 檔案 ./data/birth.csv

births = pd.read_csv('./data/births.csv')

quartiles = np.percentile(births['births'], [25, 50, 75]) # 四分位數
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0]) 
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
# query 專門給資料框使用的, 平時可以用eval

births['day'] = births['day'].astype(int) # str 轉成 int

births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, 
                              format = '%Y%m%d')
births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
births_by_date.index = [pd.datetime(2012, month, day) for (month, day) in births_by_date.index]

fig, ax = plt.subplots(figsize = (12, 4))
births_by_date.plot(ax = ax)

# 在圖表加上標籤
# 可以使用 plt.text or ax.text
style = dict(size = 10, color = 'gray') 
# 此處作為字典傳參

# ax.text(x, y, string)
# ax.text('2012-1-1', 3950, "New Year's Day", **style)
# ax.text('2012-7-4', 4250, "Independence Day", ha = 'center', **style)
# ax.text('2012-9-4', 4850, "Labor Day", ha = 'center', **style)
# ax.text('2012-10-31', 4600, "Halloween", ha = 'right', **style)
# ax.text('2012-11-25', 4450, "Thanksgiving", ha = 'center', **style)
# ax.text('2012-12-25', 3850, "Christmas", ha = 'right', **style)

# 此處使用箭頭來註解
ax.annotate("New Year's Day", xy = ('2012-1-1', 4100), xycoords = 'data', 
            xytext = (50, -30), textcoords = 'offset points', 
            arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3, rad = -0.2"))

ax.annotate("Independence Day", xy=('2012-7-4', 4250),  xycoords='data',
            bbox=dict(boxstyle="round", fc="none", ec="gray"),
            xytext=(10, -40), textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle="->"))

ax.annotate('Labor Day', xy=('2012-9-4', 4850), xycoords='data', ha='center',
            xytext=(0, -20), textcoords='offset points')

ax.annotate('', xy=('2012-9-1', 4850), xytext=('2012-9-7', 4850),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', })

ax.annotate('Halloween', xy=('2012-10-31', 4600),  xycoords='data',
            xytext=(-80, -40), textcoords='offset points',
            arrowprops=dict(arrowstyle="fancy",
                            fc="0.6", ec="none",
                            connectionstyle="angle3,angleA=0,angleB=-90"))

ax.annotate('Thanksgiving', xy=('2012-11-25', 4500),  xycoords='data',
            xytext=(-120, -60), textcoords='offset points',
            bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=80,rad=20"))

ax.annotate('Christmas', xy=('2012-12-25', 3850),  xycoords='data',
             xytext=(-30, 0), textcoords='offset points',
             size=13, ha='right', va="center",
             bbox=dict(boxstyle="round", alpha=0.1),
             arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1))


# 在axes加上標籤
ax.set(title = 'USA births by day of year (1969 - 1988)', ylabel = 'average daily births')

# 把 x軸月份標籤 置中
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday = 15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))

# line 45 調整標籤位置 
# 其餘待查找

plt.show()