
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

base = "https://sports.news.naver.com/kbaseball/index.nhn"

source = urlopen(base).read()
source = bs(source, 'lxml')

w=29
d='-'

print("순위-팀명--경기--승--무--패---승률---승차".rjust(w,d))
for i in range(1,11):
    print(' ',i,end='')
    for j in range(0,7):        
        w = source.find_all('tr')[i].find_all('td')[j].find_all('span')
        w = re.sub(r'[meoit_bu<span class=""></span>]','',str(w))
        w = re.sub(r'[\[\]]','-',str(w))
        print(w,end='')
    print('\n')

'''
import bs4
import datetime as dt
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
 
 
naver_index = "https://sports.news.naver.com/kbaseball/index.nhn"
 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')
 
teamlist = []
totlist = []
viclist = []
drawlist = []
loselist = []
vplist = []
game = []
 
for i in range(2,12,1):
    t=source.find_all('span', class_='name')[i].text
    teamlist.append(t)
 
#print(teamlist)
 
for i in range(1,11,1):
    p=source.find_all('tr')[i].find_all('td')[1].text
    totlist.append(p)
 
#print(totlist)
     
for i in range(1,11,1):
    v=source.find_all('tr')[i].find_all('td')[2].text
    viclist.append(v)
 
#print(viclist)
     
for i in range(1,11,1):
    d = source.find_all('tr')[i].find_all('td')[3].text
    drawlist.append(d)
 
#print(drawlist)
     
for i in range(1,11,1):
    l = source.find_all('tr')[i].find_all('td')[4].text
    loselist.append(l)
 
#print(loselist)
     
for i in range(1,11,1):
    vp = source.find_all('tr')[i].find_all('td')[5].text
    vplist.append(vp)
 
#print(vplist)
 
for i in range(1,11,1):
    g = source.find_all('tr')[i].find_all('td')[6].text
    game.append(g)
 
#print(game)
     
df = pd.DataFrame({'a:team' : teamlist,
                   'b:tot': totlist,
                   'c:win': viclist,
                   'd:draw': drawlist,
                   'e:lose': loselist,
                   'f:wr' : vplist,
                   'g:game' : game,
                    })
     
print(df)
'''
