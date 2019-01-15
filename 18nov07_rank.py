import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
#idx='1'
base = "https://www.hackerrank.com/leaderboard?page=1&track=python&type=practice"

source = urlopen(base).read()
source = bs(source, 'lxml')
#print(source)
kor=source.find_all('span')
for _ in kor:
    print(_)
