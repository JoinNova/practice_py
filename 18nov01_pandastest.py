import csv
import pip
import matplotlib.pyplot
import pandas as pd


#f = open('/home/nova/Downloads/datadata/bigstoreutf.csv','r')
file_path = '/home/nova/Downloads/datadata/bigstoreutf.csv'
df = pd.read_csv(file_path)
df.head(5)
df.head(10)
df.info()
df.drop(['상가업소번호','지점명','상권업종대분류코드','상권업종중분류코드',
         '상권업종중분류명','상권업종소분류코드','상권업종소분류명','표준산업분류코드',
         '표준산업분류명','시도코드','시군구코드','행정동코드',
         '행정동명','법정동코드','법정동명','지번코드','대지구분코드',
         '대지구분명','지번본번지','건물부번지','지번부번지','지번주소','도로명코드',
         '도로명','건물본번지','건물관리번호','건물명','도로명주소','구우편번호',
         '신우편번호','동정보','층정보','호정보'],axis=1,inplace=True)


df.columns.values

df.to_csv("18nov02_sleepseoul.csv")
#rdr = csv.reader(f)
#for line in rdr:
#    mydata.append(line[12])
    #mydata.append(line[4])1
    #mydata.append(line[15])13,38,39

#f.close()
#print(mydata)

#pandas.value_counts(mydata).plot(kind='pie')
#matplotlib.pyplot.show()
