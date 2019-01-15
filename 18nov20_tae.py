from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('http://www.google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[1]/input').click
driver.find_element_by_name('q').send_keys('제주 여행지')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()
driver.get('https://www.google.com/destination/map/topsights?q=%EC%A0%9C%EC%A3%BC+%EC%97%AC%ED%96%89%EC%A7%80&site=search&output=search&dest_mid=/m/01rffr&sa=X&ved=2ahUKEwjYuNLUhOLeAhUDzbwKHQA9CQsQzTooATAjegQIChAv')
driver.implicitly_wait(4)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
for i in range(10):
    namelist = soup.findAll("h2", {"class" : "NbdpWc"})[i]
    print(namelist)
