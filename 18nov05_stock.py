import bs4
import datetime as dt
from urllib.request import urlopen

#html_doc='https://finance.naver.com/sise/sise_index_day.nhn?code=KPI200'

#soup = urlopen(html_doc).read()
#soup = bs4.BeautifulSoup(soup, 'html.parser') #lxml       html.parser

index_code = '005930'
page_number = 1
naver_index = 'https://finance.naver.com/item/sise_day.nhn?code='+ \
                index_code + '&page=' + str(page_number)

source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')
#print(source.prettify())

span = source.find_all('span')
#print(len(span))

#value by config XPath
#/html/body/div/table[1]/tbody/tr[3]/td[1]
#print(source.find_all('table')[0].find_all('tr')[2].find_all('td')[0].text)
d=source.find_all('span', class_='tah p10 gray03')[0].text
#print(d)

yyyy = int(d.split('.')[0])
mm = int(d.split('.')[1])
dd = int(d.split('.')[2])
this_date = dt.date(yyyy,mm,dd)
#print(this_date)

#create function of express date
def date_format(d):
    d = str(d).replace('-','.')
    yyyy = int(d.split('.')[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])

    this_date = dt.date(yyyy, mm, dd)
    return this_date

#print(date_format(this_date))  #additional edit

this_close = source.find_all('tr')[2].find_all('td')[1].text
this_close = this_close.replace(',','')
this_close = float(this_close)
#print(this_close)


p = source.find_all('span', class_='tah p11')[0].text
#print(p)

dates = source.find_all('span', class_='tah p10 gray03')
price = source.find_all('span', class_='tah p11')
#print(len(dates))
#print(len(price))

for n in range(len(dates)):
    this_date = dates[n].text
    this_date = date_format(this_date)

    this_close = price[n*5].text
    #0,4,8 ....etc 4 multify
    this_close = this_close.replace(',','')
    this_close = float(this_close)
    print(this_close)

paging = source.find('td',class_='pgRR').find('a')['href']
#print(paging)
paging = paging.split('&')[1]
#print(paging)
paging = paging.split('=')[1]
#print(paging)

















#/html/body/div/table[1]/tbody/tr[3]/td[1]


#print(soup.head.text)

#get hyperlinks (finding 'a' = hyperlink tag code)
#print(soup.a)

#print(soup.find_all('a')[2])
#link =  soup.find_all('a')
