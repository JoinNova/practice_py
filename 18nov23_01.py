# -*- coding: utf-8 -*-

"""
@author: shha
"""
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#가져올 인터넷 주소를 적으세요.
url = 'http://news.naver.com'

#<class 'http.client.HTTPResponse'> 텍스트가 아닙니다.
html = urlopen(url)
print(type(html))
#BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
#<class 'bs4.BeautifulSoup'>
print(type(soup))
#str타입으로 변환
soup = soup.text
#print(soup)
print(type(soup))

#한자리 이상의 한글 문자들만 추출
pattern = re.compile('[가-힣]+')
result = pattern.findall(soup)
print(result)
print(type(result))
'''
'''
import re                                            ##____문자열 다루는 re라이브러리 호출
from urllib.request import urlopen                   ##____html소스 가져오는 리퀘스트라이브러리 호출

source = urlopen('https://news.naver.com').read()    ##____html소스 가져와서 저장하기
source = source.decode('euc-kr')                     ##____16진수로 표현되는 byte문자열 한글(euc-kr)을 유니코드문자열로 디코딩하기

source=re.sub(r'[^가-힣]+','',str(source))  ##____기본적으로 키보드상에있는 문자들 삭제
#source=re.sub(r'[~!@#$%^&*()_+`\-=]','',source)      ##____키보드상에있는 기호들 삭제
#source=re.sub(r'[ ]','',source)                      ##____유닉스용 줄구분명령 삭제
#source=re.sub(r'[\n\r\\]','',source)                 ##____윈도용 줄구분명령 삭제
#source=re.sub(r'[\[\]\  ]','',source)                ##____그밖에 가로들 삭제
#source=re.sub(r'[㎞℃⑧②①◆▶＇¨〃？！“”’…·‘ㆍ]','',source)    ##____윈도용 한자변환으로 만든 기호들 삭제
#source=re.sub(r'[小雪韓美父朴男野委株北日車中親開門發文非企毒勞南]','',source)   ##____윈도용 한자들 삭제
print(source)
'''


import re                                            ##____문자열 다루는 re라이브러리 호출
from urllib.request import urlopen                   ##____html소스 가져오는 리퀘스트라이브러리 호출
from bs4 import BeautifulSoup


url = 'http://www.korcham.net/nCham/Service/Main/appl/Main.asp'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
soup = soup.text
pattern = re.compile('[A-z]+@[A-z]+.[A-z]{3}?')
result = pattern.findall(soup)
print(result)
