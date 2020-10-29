from selenium import webdriver
from time import sleep
import getpass, os

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
url = 'http://www.google.com.tw'
txt = 'pw.txt'

email = input("輸入email帳號: ")
password = getpass.getpass("輸入密碼: ")

if os.path.exists(txt):
    with open(txt, 'r') as pw:
        pw.read()

with open(txt, 'w') as pw:
    pw.write(password)

browser = webdriver.Chrome(path)
browser.maximize_window()
browser.get(url)

# 在HTML裡面 登入按鈕的id是gb_70 (.click()代表點下登入按鈕)
browser.find_element_by_id('gb_70').click()
# 輸入email的id 為 identifierId (.send_keys(...)輸入信箱)
browser.find_element_by_id('identifierId').send_keys(email)
sleep(2)
# 輸入完成後 點選繼續的按鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
sleep(2)
# 接著輸入密碼
browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
sleep(2)
# 點下繼續的按鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
sleep(3)

# Extend: 在google搜尋fb並且登入fb帳號 