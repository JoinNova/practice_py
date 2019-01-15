'''
n=int(input())
nl=0
for i in range(1,n):
    if n%i==0:
        nl+=i
if nl==n:
    print('yes')
else:
    print('no')
'''
'''
import math
n=int(input())
print(math.factorial(n))
'''
'''
n=int(input())
f=1
for i in range(1,n+1) :
    f*=i
print(f)   
'''
'''
n=int(input())
i=1
result=1
while (i<(n+1)):
    result*=i
    i+=1

print(result)

#6 = 중간수입니다 i=2
#35 = 중간수입니다 i=14                   #35/6=5.83333333
#204 = 중간수입니다 i=84                  #204/35=5.8285714
#1189 = 중간수입니다 i=492                #1189/204=5.82843137
#6930 = 중간수입니다 i=2870               #6930/1189=5.8284272498
#40391 = 중간수입니다 i=16730 41.42%      #40391/6930=5.8284271284
#235416 = 중간수입니다 i=97512

'''

#6.52초(10,000까지)
#2분19초(50,000까지)
#9분53초(100,000까지)
n=0
s=0
chk=0
rank=0
while n!=-1:
    n+=1
    if chk == 1:
        chk=0
        n=int(n*5.8284271247)-5 
    m=0
    s=sum(range(n))
    i=0
    k=0
    while s>k:
        i+=1
        m+=i
        k=i*n+m
        if s==k:
            rank+=1
            print('{0} = {1}번째 중간수입니다'.format(n,rank))
            chk=1

'''
#FOR문
#6.82초(10,000까지)
#2분12초(50,000까지)
#8분52초(100,000까지)

for n in range(1,235500):
    print(n,end='_')
    chk=0
    s=sum(range(n))
    kk=0
    for i in range(1,int(n*0.4143)+1):
        chk+=i
        kk=i*n+chk
        if s==kk:
            print('\n{0} = 중간수입니다'.format(n))
            
'''



