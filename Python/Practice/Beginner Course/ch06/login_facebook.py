from selenium import webdriver
from time import sleep
import os, getpass

fbac = input("輸入fb帳號: ")
fbpw = getpass.getpass("輸入fb密碼: ")

path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(path)
txt = ".\Desktop\Practice\Beginner Course\ch06\FBpw.txt"

url = 'http://www.google.com.tw'
browser.get(url)
sleep(2)
browser.find_element_by_xpath("//input[@class = 'gLFyf gsfi']").send_keys("facebook")
sleep(2)
browser.find_element_by_xpath("//input[@class = 'gNO89b']").click()
sleep(2)
browser.find_element_by_xpath("//span[@class = 'S3Uucc']").click()
sleep(3)

if os.path.exists(txt):
    with open(txt, 'r') as pw:
        pw.read()
with open(txt, 'w') as pw:
    pw.write(fbac)
    pw.write('\n')
    pw.write(fbpw)

sleep(2)
browser.find_element_by_xpath("//input[@type='email']").send_keys(fbac)
sleep(2)
browser.find_element_by_xpath("//input[@type='password']").send_keys(fbpw)
sleep(2)
browser.find_element_by_xpath("//input[@value = '登入']").click()