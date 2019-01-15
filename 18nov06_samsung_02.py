import matplotlib.pyplot as plt
import bs4
import datetime as dt
from urllib.request import urlopen
#%matplotlib inline
import pandas as pd
from tkinter import *
import re





##################3

##################
index_code = '005930'
alldate=[]
alldata=[]
#for i in range(12,0):
page_number = 12 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############11
page_number = 11 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############10
page_number = 10 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############09
page_number = 9 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############08
page_number = 8 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############07
page_number = 7 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############06
page_number = 6 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############05
page_number = 5 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############04
page_number = 4 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############03
page_number = 3 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############02
page_number = 2 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)
###############01
page_number = 1 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata.append(sortprice)


######result
#aldate=[]
#aldata=[]
#pl=[]
#for i in range(len(alldata)):
    #resultd=alldate[i]
    #resultp=alldata[i]
    #for j in range(len(resultd)):
        #print(resultd[j], "  ",resultp[j])
        #aldate.append(resultd[j])
        #aldata.append(resultp[j])
        #pl.append((resultd[j],resultp[j]))

#print(pl)

#df = pd.DataFrame(pl)
#print(df)
################################hynics
#import matplotlib.pyplot as plt
#import bs4
#import datetime as dt
#from urllib.request import urlopen
#%matplotlib inline
#import pandas as pd
#from tkinter import *
#import re





##################
index_code = '000660'
alldate=[]
alldata2=[]
#for i in range(12,0):
page_number = 12 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############11
page_number = 11 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############10
page_number = 10 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############09
page_number = 9 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############08
page_number = 8 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############07
page_number = 7 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############06
page_number = 6 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############05
page_number = 5 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############04
page_number = 4 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############03
page_number = 3 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############02
page_number = 2 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)
###############01
page_number = 1 
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+index_code + '&page=' + str(page_number) 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')

dates = source.find_all('span', class_='tah p10 gray03')
prices = source.find_all('span', class_='tah p11')
#print(dates)
joo=list(re.findall(r"\d+.\d+.\d+",str(dates)))
joo.sort()
alldate.append(joo)
#print(prices)
price=list(re.findall(r"\d+,\d+",str(prices)))
sortprice=[]
for i in range(len(price)-5,-1,-5):
    #print(price[i])
    sortprice.append(price[i])
alldata2.append(sortprice)


######result
#aldate2=[]
aldata2=[]
aldata=[]
pl=[]
for i in range(len(alldata)):
    resultd=alldate[i]
    resultp=alldata[i]
    resultp2=alldata2[i]
    for j in range(len(resultd)):
        #print(resultd[j], "  ",resultp[j])
        #aldate.append(resultd[j])
        #aldata.append(resultp[j])
        #aldata2.append(resultp2[j])
        pl.append((resultd[j],resultp[j],resultp2[j]))

#print(pl)

df = pd.DataFrame(pl)
print(df)










import numpy as np

# Data for plotting


fig, ax = plt.subplots()
ax.plot(df[0], df[1], df[2])

ax.set(xlabel='date(day)', ylabel='price(won)',
       title='About Samsung & Hynix')
ax.grid()
labels = ["Samsung","Hynix"]
ax.legend(labels = ["Samsung","Hynix"],loc='upper left')
fig.savefig("test.png")
plt.show()

'''
x = df[0]
y1 = df[1]
y2 = df[2]

y = np.vstack([y1,y2])

labels = ["Samsung","Hynix"]

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, labels=labels)
ax.legend(loc='upper left')
plt.show()
'''

'''

########################### 
plt.figure(figsize=(10,5))
plt.plot(df[1])
plt.legend(loc=0)
plt.grid(True, color='0.7', linestyle=':', linewidth=1) #그리드 설정
plt.show()
'''
