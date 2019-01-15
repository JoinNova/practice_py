import re, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.request import Request,urlopen
import bs4
###naver_auto_search
'''
driver = webdriver.Chrome()
driver.get("https://www.naver.com")

query = ff_driver.find_element_by_id("query").send_keys("macbook pro")
driver.find_element_by_id("search_btn").click()
'''

###Tripadvisor 크롤링
name=input("TripAdvisor에서 검색을 원하시는 레스토랑을 입력해주세요.\n")



driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds
driver.get("https://www.tripadvisor.com/Restaurants-g294197-Seoul.html")
driver.find_element_by_id("taplc_masthead_search_0").click()
query = driver.find_element_by_id("mainSearch").send_keys(name)
driver.find_element_by_id("SEARCH_BUTTON").click()
driver.find_element_by_class_name("result-title").click()


elems = driver.find_elements_by_xpath("//a[@href]")
chk=0
for elem in elems:
    chk+=1
    #print(elem.get_attribute("href"))
    if chk==17:
        break

print(elem.get_attribute("href"))
front=elem.get_attribute("href")[:71]
print(front)
end=elem.get_attribute("href")[71:]
print(end)

source = urlopen(elem.get_attribute("href")).read()
source = bs4.BeautifulSoup(source, 'lxml')


file_ = open('18nov21_'+name+'.txt', 'w')
driver.implicitly_wait(10) # secconds

for i in range(10):
    review = source.find_all('p', class_='partial_entry')[i]
    review=review.get_text()    
    file_.write(review)
    #print(review)
    
try:
    for j in range(10,100,10):
        print(str(j))
        index = front+'or'+str(j)+'-'+end
        print(index)
        source = urlopen(index).read()
        source = bs4.BeautifulSoup(source, 'lxml')
        for i in range(10):
            try:
                review = source.find_all('p', class_='partial_entry')[i]
                review=review.get_text()    
                file_.write(review)
                print(review)
            except:
                pass
except:
    pass


file_.close()



