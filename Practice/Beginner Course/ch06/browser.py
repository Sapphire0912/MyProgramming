from selenium import webdriver
from time import sleep
path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(path)

urls = ['http://www.google.com', 
        'http://www.taiwanlottery.com.tw', 
        'http://www.facebook.com', 
        'https://opendata.epa.gov.tw']

for url in urls:
    browser.get(url)
    sleep(5)
# browser.quit()
browser.close()
