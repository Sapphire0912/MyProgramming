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
# 首先用 urllib 來模擬瀏覽器造訪網站的行為, 由指定的 url 獲得對應網頁的 html 並以字串傳回
# 接著用 re 函式庫 在字串中比對圖片連結的小字串, 傳回一個 list
# 最後 遍歷列表, 根據連結將圖片儲存到本機
# example 3
import re
def getHtmlCode(url):
    headers = {
        'User-Agent': 'Monzilla/5.0 (Linux; Android 6.0; Nexus 7 Build/ JRO03D) AppleWebKit/539.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
    }

    urll = urllib.request.Request(url, headers = headers)
    page = urllib.request.urlopen(urll).read()
    page = page.decode('utf-8') # 字串解碼
    return page

def getImg(page):
# 此方法傳入 html 原始碼, 經過擷取其中的 img 標籤, 將圖片儲存到本機
    imglist = re.findall(r'(http:[^\s]*?(jpg|png|gif))', page)
    
    x = 0
    for imgurl in imglist:
        try:
            print("正在下載: %s " % imgurl[0])
            urllib.request.urlretrieve(imgurl[0], 'C:\\Users\\iris2\\Desktop\\MyProgramming\\Project\\教學\\Ch06 爬蟲應用_抓取圖片\\test_rushia%d.png' % x)
            x += 1
        except:
            continue

# if __name__ == '__main__':
#     # 暫時找不到想要的url
#     url = 'anyurl'
#     page = getHtmlCode(url)
#     getImg(page)



# BeautifulSoup 函數庫概述
# 基本使用方式
# example 4
from bs4 import BeautifulSoup
doc = [
    '<html><head><title> The story of Monkey </title></head>',
    '<body><p id="firstpata" align="center">This is one paragraph</p>',
    '<p id="secondpara" align="center">This is two paragraph</p>',
    '</html>'
]
# doc 可以是 html 內容的字串, 這裡是 list 因此要轉換成 str
soup = BeautifulSoup(''.join(doc), "html.parser")
# print(soup.prettify()) # 格式化輸出 Beautiful 物件的內容

# 1. 導入 bs4 裡的 BeautifulSoup 
# 2. 建立 BeautifulSoup 物件 soup = BeautifulSoup(html)
# 2-1. 也可以使用本機的 html 檔案 soup = BeautifulSoup(open(index.html), "html.parser")
# 2-2. 使用網址的 url 取得 html
#       res = request.urlopen(url)
#       html = res.read()
#       html = html.decode('utf-8')
#       soup = BeautifulSoup(html, "html.parser")

# BeautifulSoup 物件
# 1. tag 物件: html 中的一個標籤 <title>, <a> 等開頭的所包含的內容就是 tag
#              (使用 type 可以確認此物件類型)
# 使用 BeautifulSoup 取得 Tags
# print(soup.title) # <title> The story of Monkey </title>
# print(soup.head) # <head><title> The story of Monkey </title></head>
# 注意: 這裡所尋找的標籤是所有內容中的第一筆符合要求資料

# tag 物件有兩個重要的屬性
# print(soup.name) # [document] <- soup 物件的名字
# print(soup.head.name) # head <- soup 物件 裡的 head 標籤的名字
# print(soup.p.attrs) # 輸出 p 標籤的所有屬性 -> {'id': 'firstpata', 'align': 'center'}

# 若想取得單獨某個屬性: 例如取得 它的 ID
# print(soup.p['id']) # firstpata
# print(soup.p.get('id')) # 結果同上

# 接著也可以對這些屬性的內容修改或刪除
# soup.p['class'] = "newClass"
# del soup.p['class']

# 2. NavigableString
# Tag 物件 是取得標籤內容, NavigableString 即可以取得內容
# print(soup.title.string) # The story of Monkey <- 取得 title 標籤內容 

# 3. BeautifulSoup 物件(其實就是soup本身, 用 type 即可知道)
# 表示是一個文件的全部內容 

# 4. Comment 物件: 是一種註釋物件是一個特殊類型的 NavigableString 物件, 若不妥善處理可能會對文字處理造成意想不到的影響



# 用 BeautifulSoup 函數庫操作解析 HTML 文件樹
# 1. 檢查文件樹
# 使用 contents, children 屬性取得 直接子節點
# print(soup.body.contents) # 以下為輸出結果
# [<p align="center" id="firstpata">This is one paragraph</p>, <p align="center" id="secondpara">This is two paragraph</p>]
# 輸出是一個 list 因此可以用 list 操作來取得元素

# 另外, children 屬性傳回的不是一個 list 而是一個 迭代器(用 for 可以取出元素)
# for child in soup.body.children:
#     print(child)

# 使用 descendants 屬性取得所有子孫節點(傳回是一個 迭代器)
# for child in soup.descendants:
#     print(child) # 所有的節點都被列印出來

# 使用 string 屬性取得標籤內容, 前提是標籤底下沒有標籤了, 否則會傳回 None
# print(soup.title.string)  # 輸出 <title> 標籤裡面的內容 -> The story of Monkey
# print(soup.body.string) # <body> 標籤包含了多個子節點, 所以輸出 None -> None

# 使用 parent 屬性可以取得父節點

# 2. 搜尋文件樹
# find_all(name, attrs, recursive, text, **kwargs)
# find_all 方法: 搜索目前 Tag 的所有子節點, 並判斷是否符合篩檢程式的條件

# name 參數: 可以尋找所有名字為 name 的標籤
# print(soup.find_all('p')) # 輸出所有 <p> 的標籤
# 若 name 參數傳入 正規表達式, BeautifulSoup 會透過 正規表示法的match()來比對內容
# for tag in soup.find_all(re.compile('^h')):
#     print(tag.name, end = " ") # html head

# attrs 參數: 按照 tag 標籤屬性值檢索, 需要列出屬性名稱和值, 採用字典形式
# soup.find_all('p', attrs = {'id': "firstpara"})

# recursive 參數: 在呼叫 Tag 的 find_all() 方法時, BeautifulSoup 會檢索目前 Tag 的所有子孫節點, 若只想搜尋子節點, 則 recursive = False

# text 參數: 透過 text 參數可以搜索文件中的字串內容
# print(soup.find_all(text = re.compile("paragraph")))
# ['This is one paragraph', 'This is two paragraph']
# re.compile(target): 回傳所有符合 target 字符串的結果

# limit 參數: find_all() 可以搜索全部符合條件的結果, 但資料龐大相對耗時, 因此 limit 可以限制搜索幾條資料即可
# print(soup.find_all('p', limit = 1))

# 另外, find() 只會傳回匹配符合的第一條結果

# 3. CSS 選擇器篩選元素
# CSS 在寫的時候 標籤名稱 可以不加任何修飾, 類別名稱加點('.'), ID前加'#'
# 使用 soup.select() 是透過類似的方法來篩選元素, 此方法傳回的類型是列表
# soup.select('title') # 選取 title 標籤元素
# soup.select('.firstpara') # 選取 class 是 firstpara 的元素
# soup.select_one('.firstpara') # 尋找 class 是 firstpara 的第一個元素
# soup.select("#firstpara") # 選取 id 是 firstpara 的元素
# 上面這些方式, 都傳回一個列表, 若要取得元素內容可以使用 get_text() 



# requests 函式庫教學