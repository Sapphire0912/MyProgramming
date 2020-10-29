from bokeh.plotting import figure, show
from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22'
content = requests.get(url)
parse = BS(content.text, 'html.parser')

year = []
person = []
data1 = parse.select("table[summary^='歷年戶數統計列表排版用']")[0]
rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        year.append(cols[0].text[:-1])
        person.append(cols[1].text)

p = figure(width = 800, height = 400, title = "桃園市大溪區歷年戶數")
p.title.text_font_size = "24pt"
p.xaxis.axis_label = "年份"
p.yaxis.axis_label = "戶數"
p.line(year, person, line_width = 2)
show(p)
# Question: 調整x軸的數值寬度