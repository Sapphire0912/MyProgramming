import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.tooopen.com/img/87.aspx'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'html.parser')

# 建立image目錄儲存圖片
image_dir = "image/"
if not os.path.exists(image_dir):
	os.mkdir(image_dir)

# 取得所有<a>, <img>標籤
all_link = sp.find_all(['a', 'img'])
for link in all_link:
	# 讀取src, href 屬性內容
	src = link.get('src')
	href = link.get('href')
	attrs = [src, href]
	# print(attrs)
	for attr in attrs:
		# 讀取.jpg, .png檔案
		if attr != None and ('.jpg' in attr or '.png' in attr):
			# 設定圖檔完整路徑
			full_path = attr
			filename = full_path.split('/')[-1] # 取得圖檔名
			print(full_path)
			# 儲存圖片
			try:
				image = urlopen(full_path)
				f = open(os.path.join(images_dir, filename), 'wb')
				f.write(image.read())
				f.close()
			except:
				print("{} 無法讀取!".format(filename))
# 回去換其他網址嘗試