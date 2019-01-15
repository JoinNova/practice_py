#import pandas as pd
#cctv=pd.read_csv('cctv.csv',encoding='utf-8')
#print(cctv.head())
a=0;c=0
for _ in 'a'*10:
 b=a;a+=int(input())
 if a>100 and c==0:
  if 100-b<a-100:c=b
  else:c=a
 elif a==100:c=a
if c==0:print(a)
else:print(c)
