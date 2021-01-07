# coding = utf8

# urllib 介紹
# urllib.request: 用來讀取和開啟 URL
# urllib.error: 包含一些由 urllib.request 產生的錯誤, 可以使用 try 進行捕捉處理
# urllib.parse: 包含一些解析 URL 的方法
# urllib.robotparser: 用來解析 robots.txt, 另外提供一個單獨的 RobotFileParser 類別, 透過該類別提供的 can_fetch() 方法測試爬蟲是否可以下載一個頁面

# 取得網頁資訊: urllib.request.urlopen(url[, data[, proxies]])
# urlopen() 的一些屬性
# info(): 傳回一個httplib.HTTPMessage物件, 表示遠端伺服器傳回的標頭資訊
# getcode(): 傳回 HTTP 狀態碼, 200 表示請求成功, 404 表示網址未找到
# geturl(): 傳回請求的 URL

# Example
from urllib import request
if __name__ == '__main__':
    response = request.urlopen("https://www.google.com")
    html = response.read()
    html = html.decode("utf8")
    # print(html)
    # 若要查找網頁用何種編碼方式, F12 -> <head>標籤底下的 charset

# 若要把檔案下載到本機 使用 request.urlretrieve(url, filename)

# 取得伺服器回應資訊
# status 屬性傳回請求 HTTP 後的狀態; reason 屬性非常重要, 可以獲取未被回應的原因
# 使用 getheaders() 傳回 HTTP 回應的標頭資訊
# Example
f = request.urlopen("https://www.google.com")
# data = f.read()
# print("Status: ", f.status, f.reason)
# for k, v in f.getheaders():
#     print("%s: %s" % (k, v))
# 同樣可以使用 Response 物件的方法來取得相關的 URL
# print("geturl(): %s" % (f.geturl()))
# print("-----")
# print("info(): %s" % (f.info()))
# print("-----")
# print("getcode(): %s" % (f.getcode()))

# 向伺服器發送資料
# 使用 urlopen() 函數中的 data 參數向伺服器發送資料
# get 和 post 皆可以傳送資料, 前者在 data 沒有設定時的默認值; 後者沒有對提交內容的長度做限制
# data 參數有自己的格式, 可以使用 urllib.parse.urlencode() 函數將字串自動轉換成相符的格式

# 使用 User Agent(UA) 隱藏身分
# UA 儲存於 headers 中, 伺服器透過檢視 headers 中的 UA 來判斷是誰在存取
# 若 Python 不設定 User Agent 程式將使用預設的參數, 那麼此時 UA 就有 Python 的字樣
# 若 伺服器檢查 UA, 那沒有設定 UA 的 Python 將無法正常存取網站

# 設定 User Agent 的方式有兩種
# 在建立 Request 物件的時候填入 headers 參數(參數要求為字典); 或者在建立完成後用 add_header() 來增加
# Example:
url = "http://www.csdn.net/"
head = {}
# 寫入 UA 資訊(Method 1)
# head['User-Agent'] = "Monzilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/ JRO03D) AppleWebKit/539.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19"
# req = request.Request(url, headers = head)
# (Method 2)
# req = request.Request(url)
# req.add_header('User-Agent', 'Monzilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/ JRO03D) AppleWebKit/539.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19')

response = request.urlopen(url)
html = response.read().decode("utf=8")
# print(html)
