import pymysql,ast,hashlib,os,requests
from bs4 import BeautifulSoup
# 課本以SQLite操作 此處以MySQL操作

# 建立資料庫連接
DB = pymysql.connect('localhost', 'root', 'a123456', charset = 'utf8mb4')
cur = DB.cursor()

cur.execute('create database if not exists PM25;')
cur.execute('use PM25;')

command = '''
create table if not exists TablePM25 (\
NO int primary key NOT NULL AUTO_INCREMENT unique,\
SiteName text NOT NULL,\
PM25 int)
'''

cur.execute(command)

url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?\
$orderby=SiteName&$skip=0&$top=1000&format=json"

# 讀取網頁原始碼
html = requests.get(url).text.encode('utf-8-sig')

# 判斷網頁是否更新
md5 = hashlib.md5(html).hexdigest()
old_md5 = ""
if os.path.exists('old_md5.txt'):
	with open('old_md5.txt', 'r') as f:
		old_md5 = f.read()

with open('old_md5.txt', 'w') as f:
	f.write(md5)

if md5 != old_md5:
	print('資料已更新...')
	sp = BeautifulSoup(html, 'html.parser')
	# print(sp.text)
	# 將網頁內是dict的元素轉換成list,list
	jsondata = ast.literal_eval(sp.text)
	# 刪除表的內容
	cur.execute("delete from TablePM25;")
	# 將結果傳到資料庫
	DB.commit()

	n = 1
	for site in jsondata:
		SiteName = site["SiteName"]
		if site["PM2.5"] == "":
			PM25 = 0
		else:
			PM25 = int(site["PM2.5"])
		print("站名: {}\tPM2.5 = {}".format(SiteName, PM25))
		# 新增一筆紀錄到資料庫
		sqlstr = "insert into TablePM25 \
		values({},'{}',{});".format(n,SiteName,PM25)
		cur.execute(sqlstr)
		n += 1
		DB.commit()  # 主動更新
else:
	print("資料未更新，從資料庫讀取...")
	cur.execute("select * from TablePM25;")
	rows = cur.fetchall()
	for row in rows:
		print("站名: {}\tPM2.5 = {}".format(SiteName, PM25))
cur.close()
DB.close()
# pymysql.err.InternalError: (1366, "Incorrect string value:~~)
# 遇到上述問題解法如下()
# alter table TablePM25 convert to character set utf8mb4;

# ValueError: invalid literal for int() with base 10: 'ND'
# tomorrow^