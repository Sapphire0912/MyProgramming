# 正規表達式 re 模組
# 用法很多, 可以參照網路或書上的資料(常用常看就記熟了)

# re module 的方法
# re.match(pattern, string, flags)
# pattern 是 正規表示法, string 表示要符合的字串, flags 控制正規表示法的比對方式(例如是否區分大小寫或多行等)
# example 1
import re
# test = "I like Python."
# if re.match(r'[A-Za-z0-9]', test):
#     # [A-Za-z0-9] 比對任意字母及數字
#     print("True")
# else:
#     print("Failed")

# match 比對成功會傳回一個 match 物件, 否則傳回 None
test = '0912-345678'
# \d 匹配任意數字, {n}重複匹配4次(想成取四個字元), \- 匹配特殊字符必須加上'\'的符號, $ 代表結尾
result = re.match(r'\d{4}\-\d{6}$', test)
# <re.Match object; span=(0, 11), match='0912-345678'>
test2 = '0912345678'
result = re.match(r'\d{4}\-\d{6}$', test2)
# None
# print(result)

# match 物件的 屬性和方法
# example 2
t = "09:47:36"
# ^ 代表開頭(記得括號, 有優先順序的問題)
m = re.match(r'^(\d\d)\:(\d\d)\:(\d\d)$', t)
# print("m.string: ", m.string)
# print("m.re: ", m.re)
# print("m.pos: ", m.pos)
# print("m.endpos: ", m.endpos)
# print("m.lastindex: ", m.lastindex)
# print("m.lastgroup: ", m.lastgroup)
# print("m.group(0): ", m.group(0))
# print("m.group(1,2): ", m.group(1, 2))
# print("m.groups(): ", m.groups())
# print("m.groupdict(): ", m.groupdict())
# print("m.start(2): ", m.start(2))
# print("m.end(2): ", m.end(2))
# print("m.span(2): ", m.span(2)) # span(2) -> (start(2), end(2))

# 分組
# group(0) 永遠是原始字串, 接著由優先匹配到的字串開始為 group(1), group(2)...
# example 3
number = "07-12345678"
n = re.match(r'^(\d{2})\-(\d{7,8})$', number)
# print(n.group(0)) # 07-12345678
# print(n.group(1)) # 07
# print(n.group(2)) # 12345678

# 切分字串
# 用正規標示法切分字串 比 Python 的字串切割還要靈活
# example 4
str1 = "a b    c"
# print(str1.split(' ')) # ['a', 'b', '', '', '', 'c']
# \s 匹配任何空白字元(包含 空格 定位字元 換頁符等 = [\f\n\r\t\v])
# print(re.split(r'\s+', str1))  # ['a', 'b', 'c']
# print(re.split(r'[\s\,]+', 'a,b, c,  d')) # ['a', 'b', 'c', 'd']
# print(re.split(r'[\s\,\;]+', 'a,b;; c;  ;d')) # ['a', 'b', 'c', 'd']

# search() findall() 方法
# match 方法 總是從字串的開頭去比對, 若要比對非開頭的部分就會傳回 None
# 若要從任意位置比對就要使用 search() 和 findall() 方法
str2 = "Hello World!"
# print(re.match(r'World', str2)) # None
# print(re.search(r'World', str2)) # <re.Match object; span=(6, 11), match='World'>

# re.search() 會只會傳回"第1個"符合字串的物件
str3 = "what is your name? I am iris."
# print(re.search(r'is', str3)) # <re.Match object; span=(5, 7), match='is'>
# print(re.findall(r'is', str3)) # ['is', 'is']
# re,findall() 會傳回 所有符合匹配字串的結果



# 中文分詞
# 英文的單字之間是以空格作為區分, 但是中文只有句子和段有明顯的符號來區別, 詞沒有一個形式上的分段符號
# 中文分詞是網頁分析索引的基礎, 分詞的準確性對於搜尋引擎十分重要, 因此十分講究效率及準確性
# jieba 是一個支援中文分詞, 高準確, 效率 的 Python 中文分片語件, 支援繁體分詞和自訂字典, 
# 並支援三種分詞模式: 精確模式, 全模式, 搜尋引擎模式

import jieba
# jieba 提供了 cut()方法用於分詞, cut() 方法接受兩個輸入參數
# 第一個參數是為需要分詞的字串, cut_all 參數用來控制分詞模式
# jieba.cut() 傳回的結構是一個可反覆運算的產生器, 可以使用 for 來取得分詞後的每個詞語, 或用 list 轉化成列表
# example 5
seg_list = jieba.cut("我正在學Python程式語言", cut_all = True) # 全模式
# print("Full Mode: ", '/'.join(seg_list)) # Full Mode:  我/正在/學/Python/程式/語/言
# 全模式: 把句子中所有可以成詞的詞語都掃描出來, 速度非常快卻無法解決問題的問題

seg_list = jieba.cut("我正在學Python程式語言", cut_all = False) # 精確模式
# print(type(seg_list)) # <class 'generator'>
# print("Default Mode: ", '/'.join(seg_list)) # Default Mode:  我/正在/學/Python/程式/語言
# 精確模式: 試圖將句子最精確的切開, 適合文字分析

seg_list = jieba.cut_for_search("我正在學Python程式語言") # 搜尋引擎模式
# print("Search Mode: ", '/'.join(seg_list)) # Search Mode:   我/正在/學/Python/程式/語言
# 搜尋引擎模式: 在精確模式的基礎上對長詞再次切分, 加強召回率, 適合用於搜尋引擎分詞
# 另外, jieba.cut_for_search() 僅有一個參數, 為分詞的字串, 該方法適用於搜尋引擎建置的倒排索引分詞

seg_list = jieba.cut("我正在學Python程式語言")
# 用 for 迴圈 遍歷所有字詞
# for word in seg_list:
#     print(word, end = '')



# 為 jieba 增加自訂字典
# 有些專有名詞可能因為分詞而分開
# example 6
string1 = "故宮的著名景點及物品包含乾清宮、太和殿和翠玉白菜等"
seg_list_f = jieba.cut(string1, cut_all = True) # 故/宮/的/著名/景/點/及/物品/包含/乾/清/宮/、/太和/太和殿/和/翠玉/白菜/等
# print('/'.join(seg_list_f))
seg_list_d = jieba.cut(string1, cut_all = False) # 故宮/的/著名/景點/及/物品/包含/乾清宮/、/太和殿/和/翠玉/白菜/等
# print('/'.join(seg_list_d))
# 明顯 翠玉白菜是一個物品卻被切開了

# 因此在 jieba 分詞有支援開發者使用自定義的辭典, 以便包含 jieba 詞庫裡沒有的詞語
# 用法如下: jieba.load_userdict(file_name)
# 辭典的格式:  
# 一個詞佔一行; 每行分三個部分: 詞語, 詞頻, 詞性(可略); 三個部分接用空格隔開
# 補充: ns 為地點名詞, nz 為其他專有名詞, a 為形容詞, v 為動詞, d 為副詞(詞性標記方式和 ICTCLAS 的標記方法相同)
# example 7
path = 'C:\\Users\\iris2\\Desktop\\MyProgramming\\Project\\教學\\Ch05 校園網搜尋引擎\\dict.txt'
jieba.load_userdict(path)
seg_list_de = jieba.cut(string1, cut_all = False)
# print("新增自定義辭典後: ", '/'.join(seg_list_de)) # 故宮/的/著名/景點/及/物品/包含/乾清宮/、/太和殿/和/翠玉白菜/等
# 可以看到 翠玉白菜 被識別成專有名詞了

# 文字分類的關鍵字分析
# 當文字在分類時, 在建置 VSM(向量空間模型)的過程中 把文字轉換成數學形式的計算中需要運用到 關鍵字分析技術
# jieba關鍵字分析技術的基本用法: jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())
# 首先先 import jieba.analyse
import jieba.analyse

# 其中 sentence 為待分析的文字, topK 為傳回幾個 TF/IDF 加權最大的關鍵字(default = 20), withWeight 為是否一併傳回關鍵字加權值(default = False)
# allowPOS 只僅包含指定詞性的詞(default = () <- 不進行篩選)
# example 8
string2 = "今天我搭公車去了學校, 學校教了程式語言, 那門課讓我很有興趣, 因此今天在學校的收穫很大" 
seg_list_str = jieba.cut(string2, cut_all = False) # 精確模式
# print('/'.join(seg_list_str)) # 分詞結果
# 今天/我/搭/公車/去/了/學校/,/ /學校/教/了/程式/語言/,/ /那門/課/讓/我/很/有/興趣/,/ /因此/今天/在/學校/的/收/穫/很大

tags = jieba.analyse.extract_tags(string2, topK = 5, withWeight = True)
# print(tags)  # [('學校', 2.988691875725), ('公車', 0.9962306252416666), ('語言', 0.9962306252416666), ('那門', 0.9962306252416666), ('興趣', 0.9962306252416666)]

# 關鍵字分析所使用的逆向檔案頻率(IDF) 
# jieba.analyse.TFIDF(idf_path = None) # 新增 TF/IDF 實例, idf_path 為 IDF 頻率檔案(放路徑)
# 關鍵字分析所使用的停止詞
# jieba.analyse.set_idf_path(file_name) # file_name 為自訂語料庫的路徑



# deque(double-ended queue) 雙向佇列 位於 Python 標準函式庫 collections 中
# 提供了兩端都可以操作的序列, 表示在序列的前後皆可以執行增加或刪除操作
from collections import deque
# example 9
d = deque() # 建立雙向序列
d.append(3) # 新增元素
d.append(4.5)
d.append(1) 
# print(d) # deque([3, 4.5, 1])

# deque 支援從任意一端增加元素, append() 加在最右邊, appendleft() 則加在最左邊
# pop(), popleft() 同理

# 限制 deque 長度
d = deque(maxlen = 20)
for i in range(30):
    d.append(i)
# print(d) # 若超出範圍則會從另一邊的先刪除
# Q. 用 高科大校務系統 爬蟲