from selenium import webdriver
from time import sleep

url = 'http://opendata.epa.gov.tw/'
path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(path)
browser.maximize_window()
browser.get(url)

sleep(3)
browser.find_element_by_link_text("空氣品質指標(AQI)").click()
sleep(3)
browser.find_element_by_link_text("資料檢視").click()
sleep(2)
browser.find_element_by_link_text("JSON").click()
sleep(2)
browser.current_url
# Extend: 擷取json內容並顯示