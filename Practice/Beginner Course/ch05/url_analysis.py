from urllib.parse import urlparse
url = "http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1"
o = urlparse(url)
print(o)