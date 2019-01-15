'''
2013 야구성적을 이용하여 홈런타자 순서로 정렬해서 표현하세요.
1. 정렬 후 콘솔에 홈런타자 이름 순으로 출력합니다.
2. y축 홈런 개수 x축 선수이름 인  Bar 차트 를 그리세요.
3. 홈런 순위가 표로만들어져 있는 파일을 만들어 웹서버에 올립니다.
순위 이름 홈런수
1  홍길동 50
2  이순신 40
..
..
'''

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt

data = pd.read_csv('2013_baseball.csv')
#print(data)

df=pd.DataFrame(data)
#print(df)
df2=df.filter(items=['player','homerun'])
#print(df2)
###1. 정렬 후 콘솔에 홈런타자 이름 순으로 출력합니다.
sortname=df2.sort_values(by='player')
#print(sortname)
name=sortname['player']
homerun=sortname['homerun']

###2. y축 홈런 개수 x축 선수이름 인  Bar 차트 를 그리세요.
#print(type(list(name)))

objects =list(name)
y_pos = np.arange(len(objects))
performance = list(homerun)


rects=plt.bar(y_pos, performance, width=0.7, color='IndianRed', yerr=1, align='center', alpha=1)
plt.xticks(y_pos, objects,rotation=40, ha='right')
plt.ylabel('Amount')
plt.xlabel('Player')
plt.title('KBO HOMERUN CHART')

def autolabel(x, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects, "left")
#plt.show()



###3. 홈런 순위가 표로만들어져 있는 파일을 만들어 웹서버에 올립니다.
sorthr=df2.sort_values(by='homerun',ascending=False)
#print(sorthr)
sorthr.index = range(1,len(sorthr)+1)
#print(sorthr)
hrdic={}
for i in range(len(sorthr)):
    hrdic['{0}'.format(i+1)]={sorthr['player'][i+1]:sorthr['homerun'][i+1]}
#print(hrdic)  
    


#import glob
#from collections import defaultdict


# write to html
html = """
<html>
<table border="1">
<tr>
<th>ranks</th>
<th>players</th>
<th>homeruns</th>
</tr>"""
for i in range(len(hrdic)):
    html += "<tr><td>{0}</td><td>{1}</td><td>{2}</td>".format(i+1,str(list(hrdic['%d'%(i+1)].keys())),str(list(hrdic['%d'%(i+1)].values())))
    html += "</tr>"
html += "</table></html>"


file_ = open('rankstable.html', 'w')
file_.write(html)
file_.close()

