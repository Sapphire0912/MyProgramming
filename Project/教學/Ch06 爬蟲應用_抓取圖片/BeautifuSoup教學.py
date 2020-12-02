# 一般來說 爬蟲需要分成以下步驟
# 1. 分析需求
# 2. 分析網頁原始程式碼和網頁結構
# 3. 撰寫正規表示法 或 XPath 運算式
# 4. 正式撰寫 Python 爬蟲程式
# 這裡按照這些步驟實現 按關鍵字爬取 Google 圖片

# 若要把相對應的圖片下載到本機
# 使用 request.urlretrieve(url, filename)
# example 1
from urllib import request
path = 'C:\\Users\\iris2\\Desktop\\MyProgramming\\Project\\教學\\Ch06 爬蟲應用_抓取圖片\\test_rushia.jpg'
url = 'https://frm-wows-sg.wgcdn.co/wows_forum_sg/monthly_2019_12/Rushia.png.6a3517347aae21389f391533fcfbb166.png'
# request.urlretrieve(url, path)

# 使用 Python 檔案操作函數 write() 寫入檔案
# example 2
import urllib
from urllib import request
path = 'C:\\Users\\iris2\\Desktop\\MyProgramming\\Project\\教學\\Ch06 爬蟲應用_抓取圖片\\test_rushia02.png'
url = 'https://static.miraheze.org/hololivewiki/thumb/0/02/Uruha_Rushia_-_Portrait_NSS.png/260px-Uruha_Rushia_-_Portrait_NSS.png'
urll = urllib.request.Request(url) # Request() 函數將 url 增加到表頭, 模擬瀏覽器存取
# print(type(urll)) # <class 'urllib.request.Request'>
page = urllib.request.urlopen(urll).read() # 將 url 頁面的原始程式碼儲存成字串
# print(type(page)) # <class 'bytes'>
# open(filename, method).write(target)
# open(path, 'wb').write(page) # 方法原始, 且很有效


# 爬取指定網頁中的圖片
