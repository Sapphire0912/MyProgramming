# Path: C:\Users\kotori\Desktop\Practice\Beginner Course\YT_dw
# The version of pytube module is 9.5.3
# Reference Link: https://python-pytube.readthedocs.io/en/latest/api.html

from pytube import YouTube

path = '.\Desktop\Practice\Beginner Course\ch09(GUI)\YT_dw'
# vurl = "https://www.youtube.com/watch?v=cvmQt-0pqWs"
vurl = "https://www.youtube.com/watch?v=UZpaHkHPNvk"
# 建立YouTube物件(影片連結網址)
yt = YouTube(vurl)

# print(yt.streams.all()) # 傳回streams的列表 
# print(yt.streams.first()) # 取得第一個串流

# 傳回經過filter條件篩選過後所有streams的列表
# progressive = True 為 漸進式下載流
# print(yt.streams.filter(progressive=True).all()) 

# adaptive = True 為 DASH流 (自適應串流)
# print(yt.streams.filter(adaptive=True).all())

# only_audio/video = True 查詢僅包含音軌/影像軌的串流
# print(yt.streams.filter(only_audio=True).all())

# file_extension = 'mp4' 查詢為 mp4 檔名的串流 (mp4 -> MPEG-4)
# print(yt.streams.filter(file_extension='mp4').all())
# 可以利用res, fps,...etc 等條件來查找所指定的串流 (res為解析度, fps為影格率)

# 利用itag來查詢串流
# print(yt.streams.get_by_itag('137')) # 查找itag=137的串流

# 字幕 / 字幕軌道
# print(yt.captions.all()) # 查找所有該影片字幕的串流(查找所有語言)

# yt.title 查找影片的標題名稱
# print(yt.title)

# yt.thumbnail_url 取得縮圖連結網址
# print(yt.thumbnail_url)

video = yt.streams.filter(file_extension = 'mp4', res = '1080p').first()
# download(path [,filename]) filename 可以給予檔案指定的名字,默認為影片標題
video.download(path,filename = "Letter song")