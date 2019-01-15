import pandas as pd
import numpy as np

#obj = pd.Series([1,2,3,4])
#obj = pd.Series([1,2,3,4])
#print(obj)
#print(obj.index)
#print(obj.dtype)

sdata1 = {'강호동':100,'유재석':200,
         '신동엽':300,'김제동':400}
sdata2 = {100:'강호동',200:'유재석',
         300:'신동엽',400:'김제동'}




#print(type(sdata))

obj1= pd.Series(sdata1)
obj2= pd.Series(sdata2)
#obj3= pd.Series(sdata3)
#print(obj2)
#print(type(obj2))
#print(obj1.index)
data = {'이름':['강호동','유재석','김재동','신동엽'],
        '사원번호':[100,200,300,400],
        '포인트':[1.1,2.2,3.3,4.4]
        }
#print(data)
#print(type(data))

df = pd.DataFrame(data)
#print(df)
#print(type(df))
#print(df.index)
#print(df.columns)
df.index.name = '순번'
df.columns.name = '컬럼'
#print(df)

df2 = pd.DataFrame(data, columns=['이름','사원번호','포인트'],
                   index=[1,2,3,4])
print(df2)
print(df2.describe)
df2['점수'] = np.arange(4)
print(df2)
print(df2.loc[2:4])
