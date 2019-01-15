#print("Hello_World")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#s=pd.Series([1,3,5,np.nan,6,8])

#s= pd.Series(['A','B','C'])
#s=pd.Series(['Kor','Eng','Math'])

dates = pd.date_range('20181101', periods=6)

#df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#f=pd.DataFrame(np.random.randint(1,45,size=(6,6)),
#               index=dates,columns=list('ABCDEF'))
#print(f)

#print(s)
'''
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20181101'),
                    'C' : pd.Series(1, index = list(range(4)),
                                    dtype= 'float32'),
                    'D' : np.array([3] * 4, dtype = 'int32'),
                    'E' : pd.Categorical(["test", 'train',
                                          'test','train']),
                    'F' : 'foo'
                    })
print(df2)
'''
'''
#print(df2.dtypes)

#print(type(True))
#print(type('A'))
#print(type(1))
#print(type(3.14))
#print(type('abc'))

#print(df2.A)
#print(df2.C)

print(f.head(3))
print(f.tail(2))

print(f.index)

'''
'''
data = pd.read_csv("18nov06_pandas.csv",sep=',',dtype='unicode')
#print(data)
#print(data['상호명'])
#print(data['상호명'].values)
v1= data['상호명']
df=pd.DataFrame({"상호명":v1})
#print(df)
print(df.sort_index(axis=1, ascending=False))
#print(df.sort_values(by='상호명'))
'''



f=pd.DataFrame(np.random.randint(1,45,size=(6,6)),
               index=dates,columns=list('ABCDEF'))

#print(f.describe)
#print(f.T)
#print(f.sort_index(axis=0, ascending=False))
#print(f.sort_index(axis=1, ascending=False))
#print(f.sort_index(axis=1, ascending=True))
#print(f)
#print(f['B'])
#print(f[0:3])

print(f['20181101': '20181105'])