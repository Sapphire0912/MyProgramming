# 取得台灣彩券威力彩開獎結果
import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'html.parser')
# html.text 去除所有HTML標籤後的網頁文字內容

data1 = sp.select("#rightdown")
# 讀取id = rightdown內容
# 讀取id要加"#, 讀取class要加"."

# print(data1)
data2 = data1[0].find('div', {'class' : 'contents_box02'})
# print(data2)
# contents_box02 為威力彩的開獎結果

data3 = data2.find_all('div', {'class' : 'ball_tx'})
# print(data3)

date = data2.find('div', {'class' : 'contents_mine_tx02'})

print(date.text)
# 威力彩開獎號碼
print("開出順序: ",end = ' ')
for n in range(6):
	print(data3[n].text, end = ' ')
print()

print("大小順序: ", end = ' ')
for n in range(6,len(data3)):
	print(data3[n].text, end = ' ')
print()

# 第二區
red = data2.find('div', {'class' : 'ball_red'})
print("第二區: {}".format(red.text))