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

data = pd.read_csv('2013_baseball_kr.csv')
#print(data)

df=pd.DataFrame(data)
#print(df)
df2=df.filter(items=['선수명','홈런'])
#print(df2)
###1. 정렬 후 콘솔에 홈런타자 이름 순으로 출력합니다.
sortname=df2.sort_values(by='선수명')
print(sortname)
name=sortname['선수명']
homerun=sortname['홈런']

###2. y축 홈런 개수 x축 선수이름 인  Bar 차트 를 그리세요.
#print(type(list(name)))
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
###########
path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
fontprop = fm.FontProperties(fname=path, size=18)
#######333
objects =list(name)
y_pos = np.arange(len(objects))
performance = list(homerun)


rects=plt.bar(y_pos, performance, width=0.7, color='IndianRed', yerr=1, align='center', alpha=1)
plt.xticks(y_pos, objects,rotation=40, ha='right',fontproperties=fontprop)
plt.ylabel('홈런수',fontproperties=fontprop)
plt.xlabel('선수명',size=1,fontproperties=fontprop)
plt.title('KBO 홈런차트',fontproperties=fontprop)

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
plt.show()



###3. 홈런 순위가 표로만들어져 있는 파일을 만들어 웹서버에 올립니다.
sorthr=df2.sort_values(by='홈런',ascending=False)
#print(sorthr)
sorthr.index = range(1,len(sorthr)+1)
#print(sorthr)
hrdic={}
for i in range(len(sorthr)):
    hrdic['{0}'.format(i+1)]={sorthr['선수명'][i+1]:sorthr['홈런'][i+1]}
print(hrdic)  
    


#import glob
#from collections import defaultdict


# write to html
html = """
<html>
<table border="1">
<tr>
<th>순위<meta charset='utf-8'></th>
<th>선수명<meta charset='utf-8'></th>
<th>홈런<meta charset='utf-8'></th>
</tr>"""
for i in range(len(hrdic)):
    html += "<tr><td>{0}<meta charset='utf-8'></td><td>{1}<meta charset='utf-8'></td><td>{2}<meta charset='utf-8'></td>".format(i+1,list(hrdic['%d'%(i+1)].keys()),list(hrdic['%d'%(i+1)].values()))
    html += "</tr>"
html += "</table></html>"

#html = unicode( html, "utf-8" )
file_ = open('rankstable_kr.html', 'w')
file_.write(html)
file_.close()


