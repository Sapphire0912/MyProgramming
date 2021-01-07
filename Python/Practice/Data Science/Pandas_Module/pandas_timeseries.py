import numpy as np
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import BDay

# Pandas 在財務模型領域中也包含了相當多的工具, 可以來操作 dates, times, time-indexed
# Time stamps: 表示時間中某一個特定的時刻(2020/02/28 AM7:00)
# Time interval/periods: 表示某一個時刻開始到結束的時間長度, periods表是一個時間間隔通常不會重疊且固定長度
# Time deltas|durations: 表是一個時間長度

# Python的data, time: time, datetime

# 時間的定型陣列: Numpy datetime64
# Numpy datetime64 的陣列是單一型態, 比Python使用datetime物件更快被執行(numpy ufuncs)
date = np.array('2019-09-12', dtype = np.datetime64)
# print(date) 
# print(date + np.arange(12)) # 有了格式化的日期就可以快速地進行向量化的操作

# 可以自行設定要使用哪個時間為單位
# print(np.datetime64('2019-09-12')) # 以天為單位
# print(np.datetime64('2019-09-12 09:20')) # 以分為單位
# print(np.datetime64('2019-09-12 08:33:40.75', 'us')) # 以微秒為單位

# 在 Pandas 中的 Timestamp 物件: 結合了Python datetime, dateutil易用性 和Numpy datetime64儲存效率和向量化
date2 = pd.to_datetime("4th of July, 2019")
# print(date2)
# print(date2.strftime("%A")) # 可以直接輸出某一天是星期幾
# print(date2 + pd.to_timedelta(np.arange(12), 'D'))
# 關於pd.to_timedelta的用法: https://www.cjavapy.com/article/525/

# Pandas時間系列: 使用時間當作索引
index = pd.DatetimeIndex(['2017-09-12', '2019-10-02', '2019-09-12', '2017-10-02'])
data = pd.Series([0, 1, 2, 3], index = index)
# print(data)
# print(data['2017-09-12':'2019-09-12']) # 以時間間隔為切片
# print(data['2019'])  # 以年份當成切片(取出2019的所有資料)

# Pandas時間系列資料結構
# Time stamps -> pandas Timestamp物件 對應索引結構為 DatetimeIndex
# Time periods -> pandas Period物件 對應索引結構為 PeriodIndex
# Time delta|durations -> pandas Timedelta 對應索引結構為 TimedeltaIndex
# 最基本的是 Timestamp 和 DatetimeIndex 物件, 雖然可以直接被呼叫, 但通常使用 pd.to_datetime()
# pd.to_datetime() 可以解析非常多種格式, 且會產生一個Timestamp, 傳遞一串日期會產生DatetimeIndex
dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015', 
                        '2015-Jul-6', '07-07-2015', '20150708']) 
# print(dates)
# 任何一個DatetimeIndex可以透過to_period()函式加上一個頻率單位編碼, 轉換成PeriodIndex
# print(dates.to_period('D')) 
# 當一個日期做運算時, 會產生一個 TimedeltaIndex
# print(dates - dates[0])

# 規則性的序列: pd.date_range(), pd.period_range(), pd.timedelta_range()
# print(pd.date_range('2020-09-12', '2020-09-22'))
# print(pd.date_range('2020-09-12', periods = 8))
# print(pd.date_range('2020-09-12', periods = 8, freq = 'H')) # 以每小時為間隔, 重複8次
# print(pd.period_range('2020-09', periods = 6, freq = 'M')) # 以月為單位
# print(pd.timedelta_range(0, periods = 10, freq = 'H')) # 每次增加1小時的duration序列
# line 56: 0代表從"00:00:00"開始, 參數可使用時間格式

# 頻率和位移植
# Pandas 頻率編碼(freq參數)
# D , W , M , Q , A , H , T , S , L ,    U ,   N , B 
# 天, 週, 月, 季,  年, 時, 分, 秒, 毫秒, 微秒, 奈秒, 工作天  
# BM, BQ, BA, BH (工作 月/季/年 結束點/小時)
# MS, BMS, QS, BQS, AS, BAS (月, 工作月, 季, 工作季, 年, 工作年/ 開始點) (有加S代表開始點)
# 另外也可以在頻率編碼後面加上 任何季|年|月|週 的編碼
# Ex. Q-JAN(從1月開始每一個季結束點), BQ-FEB(從2月開始每一季工作日)...etc
# print(pd.date_range('2020', periods = 5, freq = 'Q-JAN'))
# print(pd.date_range('2020', periods = 5, freq = 'BQ-FEB'))
# print(pd.date_range('2020-10', periods = 7, freq = 'W-MON'))

# 另外編碼也可以以數字來指定頻率, 建立一個2小時30分的頻率, 
# Ex.
# print(pd.timedelta_range(0, periods = 9, freq = '2H30T'))

# 上面這些實例包含在 pd.tseries.offsets 模組裡面
# print(pd.date_range('20450101', periods = 10, freq = BDay()))

# 重新取樣, 偏移, 窗口設定


# Reference: http://pandas.pydata.org/pandas-docs/stable/timeseries.html