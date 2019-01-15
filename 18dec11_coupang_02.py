
from bs4 import BeautifulSoup
import requests
from re import findall as f
from re import sub

###git_hub소스
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html
###

URL = "https://www.coupang.com/np/search?component=&q=tv&channel=user"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')
#l = soup.find_all("div",class_='search-content search-content-with-feedback ')

chk=0;
###상품명
product=[]
l = soup.find_all("div",class_='name')
for _ in l:
    _=str(_)
    _=sub(r'[a-z,<>"=/]','',_)[1:20]
    #print(_)
    product.append(_.strip().replace(' ','_'))
    
    #chk+=1

###가격
l = soup.find_all("strong",class_='price-value')
for _ in l:
    _=str(_)
    _=sub(r'[a-z,<>"=/\- ]','',_)
    #print(_)
    product.insert(2*chk+1,_)
    
    chk+=1

chk=0
###사진저장하기
import urllib.request
###사진바이너리형식으로
import base64

photo=[]


###
###사진경로
l = soup.find_all("dt",class_='image')
for _ in l:
    _=str(_)
    _=f(r'\w+.\w+.\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+/\w+-\w+-\w+-\w+-\w+.jpg',_)
    _=str(_)[2:-2]
    #print('https://'+_)
    _='https://'+_

   
    ###사진저장하기
    ur = _
    savename = product[2*chk+chk]+".png"
    try:
       urllib.request.urlretrieve(ur, savename)
       print("saved")
       ###사진파일 바이너리 파일로 전환하기
       with open("/home/nova/bigdata/python/today/%s"%savename, "rb") as imageFile:
          bi = base64.b64encode(imageFile.read())
          print(bi)
          photo.append(bi)
    except:
       print(str(chk)+"fail")
       photo.append('Null')
       pass
   
    product.insert(3*chk+2,_)
    chk+=1
#print(chk,chk2)    
#print(product)
#//thumbnail12.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2018/08/21/3539743483/33355327-e776-4aec-939a-426c68938947.jpg


###csv파일 만들기
result=''
result+='"제품명","가격","이미지주소","이미지파일"\n'
#result+='ProductName'+','+'ImgAddress'+'\n'
for i in range(len(product)//3):
    #print(product[i*2]+','+product[i*2+1])
    result+='"'+str(i+1)+'"'+','+'"'+product[i*3]+'"'+','+'"'+product[i*3+1]+'"'+','+'"'+product[i*3+2]+'"'+','+'"'+str(photo[i])+'"'+'\n'
file_ = open('18dec12_coupangTV.csv', 'w')
file_.write(result)
file_.close()

###blob.c


###mysql에 넣기
import pymysql

# Open database connection
db = pymysql.connect("localhost","root","1234","coupang" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE coupangTV (
   Id int not null,
   ProductName  varchar(100),
   Price  varchar(200),  
   ImageAddress varchar(1000),
   Photo longblob);"""

cursor.execute(sql)


#sql = """LOAD DATA LOCAL INFILE '/home/nova/bigdata/python/today/18dec12_coupangTV.csv'
#INTO TABLE coupang.coupangTV
#FIELDS TERMINATED BY ',' ENCLOSED BY '"'
#LINES TERMINATED BY '\n'
#IGNORE 1 ROWS;"""

#cursor.execute(sql)

# disconnect from server
db.close()

####blob 저장공간만들기




'''
import csv
import pymysql
import pandas as pd

cnx = pymysql.connect(user='root', password='1234', host='localhost', database='coupang')
cursor = cnx.cursor()
#csv_data = read.csv('/home/nova/bigdata/python/today/18dec12_coupangTV.csv') 
with open('/home/nova/bigdata/python/today/18dec12_coupangTV.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         data=str(row)[2:-2].split(',')
         cursor.execute("INSERT INTO coupang.coupangTV(ProductName,Price,ImageAddress,Photo) VALUES(\'%s\',\'%s\',\'%s\',\'%s\');" %(data[0],data[1],data[2],data[3]))
     #print(str(row))
#for row in csv_data.iterrows():
#    list = row[1].values
#    cursor.execute("INSERT INTO coupang.coupangTV(ProductName,Price,ImageAddress) VALUES(\'%s\',\'%d\',\'%s\');" % tuple(list))

cursor.close() 
cnx.close() 
'''

