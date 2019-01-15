import re                                            ##____문자열 다루는 re라이브러리 호출
from urllib.request import urlopen                   ##____html소스 가져오는 리퀘스트라이브러리 호출
 
source = urlopen('https://news.naver.com').read()    ##____html소스 가져와서 저장하기
source = source.decode('euc-kr')                     ##____16진수로 표현되는 byte문자열 한글(euc-kr)을 유니코드문자열로 디코딩하기
print(source[:1000])
'''
source=re.sub(r'[A-Z,a-z,0-9,~!@#$%&*()_+-=|\'>?"{}]','',str(source))  ##____기본적으로 키보드상에있는 문자들 삭제
source=re.sub(r'[~!@#$%^&*()_+`\-=]','',source)      ##____키보드상에있는 기호들 삭제
source=re.sub(r'[	]','',source)
source=re.sub(r'[ ]','',source)                      ##____유닉스용 줄구분명령 삭제
source=re.sub(r'[\n\r\\]','',source)                 ##____윈도용 줄구분명령 삭제
source=re.sub(r'[\[\]\	\	]','',source)                ##____그밖에 가로들 삭제 
source=re.sub(r'[㎞℃⑧②①◆▶＇¨〃？！“”’…·‘ㆍ]','',source)    ##____윈도용 한자변환으로 만든 기호들 삭제 
source=re.sub(r'[小雪韓美父朴男野委株北日車中親開門發文非企毒勞南]','',source)   ##____윈도용 한자들 삭제
print(source)
'''
