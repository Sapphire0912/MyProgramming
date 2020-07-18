import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22'
year = []
person = []
content = requests.get(url).text
parse = BS(content, 'html.parser')
data1 = parse.select("table[summary^='歷年戶數統計列表排版用']")[0] # In the first element of the list
# print(data1)
rows = data1.find_all("tr") # find the content is "tr" in the rows
for row in rows:
    cols = row.find_all("td") 
    # print(cols)
    if (len(cols) > 0):
        if cols[1].text != "─":
            year.append(cols[0].text[:-1]) # 不讀取"年"這個字
            person.append(cols[1].text)
# print(year)
# print(person)
plt.plot(year, person, linewidth = 3.0)
plt.title("桃園市大溪區歷年戶數")
plt.xlabel("年份")
plt.ylabel("戶數")
plt.show()