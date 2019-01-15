'''
import bs4
from urllib.request import Request,urlopen


req = Request('https://www.coupang.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#src = urlopen('https://www.coupang.com/np/search?component=&q=tv&channel=user').read()
webpage = bs4.BeautifulSoup(webpage, 'lxml')
print(webpage)

#review = webpage.find_all('td', class_='p-nick') 
#review=review.get_text()    
#print(review)
'''




import re, os                                                    ##____문자열가공모듈인 re함수 호출 
from selenium import webdriver                                   ##____마우스역할하는 셀레니움 속 웹드라이브 함수 호출 
from selenium.webdriver.support.ui import WebDriverWait          ##____웹 완성까지 기다리는 웨이팅 함수 호출 
#from selenium.webdriver.support import expected_conditions as EC ##____이번엔 사용하지않았지만 path를 활용하는 함수임. 
#from selenium.webdriver.common.by import By                     ##____이번엔 사용하지 않았지만 다른기능시 유용한 함수임. 
from urllib.request import Request,urlopen                       ##____url분석에 유용한 리퀘스트 함수 호출 
import bs4                                                       ##____url파싱에 유용한 뷰티풀soup 
 
 
###Tripadvisor 크롤링 
#name=input("TripAdvisor에서 검색을 원하시는 레스토랑을 입력해주세요.\n==> : ") 
driver = webdriver.Chrome()                                          ##____셀레니움으로 구글드라이브 Turn on 
driver.implicitly_wait(10)                                           ##____사진자료가 열릴때까지 기다리는 함수 10초 
driver.get("https://www.coupang.com/")   ##____첫 시작할 홈페이지는 지정해주세요. 
driver.find_element_by_id("headerSerchKeyword").click()         ##____식당검색을 위한 검색창 생성부분 클릭
query = driver.find_element_by_id("headerSerchKeyword").send_keys('tv')      ##____식당검색부분에 식당이름 입력 
driver.find_element_by_id("SEARCH_BUTTON").click()                   ##____식당검색부분의 검색버튼 클릭 
driver.find_element_by_class_name("result-title").click()            ##____검색된 식당들중 가장 첫번째 식당 클릭 
 
 
elems = driver.find_elements_by_xpath("//a[@href]")                  ##____링크설정되있는것들 크롤링 

 
 
source = urlopen(elem.get_attribute("href")).read()       ##____리퀘스트로 웹소스 리딩 
source = bs4.BeautifulSoup(source, 'lxml')                ##____뷰티풀soup으로 웹소스 파싱   
