import requests
from bs4 import BeautifulSoup
url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text,'html.parser')
# print(sp)
# print(sp.title)
# print(sp.text)
# print(sp.find('a'))
print(sp.find_all('a'))
# print(sp.select("b"))
