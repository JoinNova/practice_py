import re
from urllib.request import urlopen

source = urlopen('https://news.naver.com').read()
source = source.decode('euc-kr')

source=re.sub(r'[A-Z,a-z,0-9,~!@#$%&*()_+-=|\'>?"{}]','',str(source))
source=re.sub(r'[~!@#$%^&*()_+`\-=]','',source)
source=re.sub(r'[ ]','',source)
source=re.sub(r'[\n\r\\]','',source)
source=re.sub(r'[\[\]\	]','',source)
source=re.sub(r'[㎞℃⑧②①◆▶＇¨〃？！“”’…·‘ㆍ]','',source)
source=re.sub(r'[小雪韓美父朴男野委株北日車中親開門發文非企毒勞南]','',source)
print(source)

