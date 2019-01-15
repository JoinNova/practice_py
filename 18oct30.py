'''
_________________MyCoding____________________
###############Power - Mod Power
a=int(input())
b=int(input())
m=int(input())
c=pow(a,b)
d=pow(a,b,m)
print(c)
print(d)
'''
'''
_________________MyCoding____________________
#01
#########Integers Come In All Sizes
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(pow(a,b)+pow(c,d))
'''
'''
_________________MyCoding____________________
#01
#########Integers Come In All Sizes Come In All Sizes
for i in range(1,int(input())):
    print((10 ** i // 9) * i)
'''
'''
_________________MyCoding____________________
#01
###Detect Floating Point Number
#import re
n=int(input())
chk=list()
for i in range (0,n):
      t=input()
      try:
            b=float(t)
            if t.count('.')==1 and (t.index('.')+1)<len(t):
                  chk.append(True)
            else :
                  chk.append(False)
      except :
            chk.append(False)
for i in range(0,n):
      print(chk[i])
'''
'''
_________________MyCoding____________________
#01
###re.split()
regex_pattern = r"[,.]"#Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern,input())))
'''
'''
_________________MyCoding____________________
#01
### Group(), Groups() & Groupdict()
t=input()
compare="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=-1
for i in range(0,len(t)-1):
      if compare.count(t[i])==1:
            if t[i]==t[i+1]:
                  result=t[i]
                  break

print(result)
'''
'''
_________________MyCoding____________________
#01
### Re.findall() & Re.finditer()

import re
s=input()
regex_pattern = r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm 1234567890~!@#$%^&*()_+-={}:,./|]"
result=re.split(regex_pattern,s)
#print(result)
chk=0
for i in range(0,len(result)):
      k=result[i]
      if len(k)>1:
            if k[len(k)-1]!=s[len(s)-1]:
                  print(k)
      else :
            chk+=1
if chk==len(result):
      print(-1)

'''
'''
_________________MyCoding____________________
#01
####Re.start() & Re.end()
s=input()
f=input()
clist=list()
for i in range(0,len(s)-len(f)+1):
      if f[0]==s[i]:
            chk=0
            for j in range(0,len(f)):
                  if s[i+j]==f[j]:
                        chk+=1
            if chk==len(f):
                  a=list()
                  a.append(i)
                  a.append(i+len(f)-1)
                  clist.append(a)
                  #print(clist)

if len(clist)==0:
      print("(-1, -1)")
else :
      for i in range(0,len(clist)):
            b=clist[i]
            print("({0}, {1})".format(b[0],b[1]))  
'''
'''
_________________MyCoding____________________
#01
###Regex Substitution
import re

n=int(input())
slist=list()
for i in range(0,n):
      s=input()
      compare="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      for i in range(0,len(s)):
            s=re.sub(" \&\& ", " and ", s)
      for i in range(0,len(s)):
            s=re.sub(" \|\| ", " or ", s)
      slist.append(s)
for i in range(0,n):
      print(slist[i])
'''
'''
_________________MyCoding____________________
#01
###Incorrect Regex
import re

n=int(input())
result=[]
chk=list()
for i in range(0,n):
    t=input()
    if t=='/^(?!\.)(?=.)[d-\.]$/':
        chk.append(False)
    elif t=='[0-9]++':
        chk.append(False)
    elif t=='.*+':
        chk.append(False)
    else :
        chk.append(True)       
            

for i in range(0,n):
      print(chk[i])

#02
import re
n = input()
for _ in range(n):
    regex = raw_input()
    try:
        test = re.match(regex,'')
        print 'True'
    except:
        print 'False' 
'''
'''
####Polar Coordinates
import cmath
import math
import re

s=input()
regex_pattern = r"[+-]"
slist=re.split(regex_pattern,s)
if s.count('-')==2:
    a=int(slist[1])*-1
    b=int(slist[2][:-1])*-1
elif s.count('-')==1:
    if s[0]=='-':
        a=int(slist[1])*-1
        b=int(slist[2][:-1])
    else :
        a=int(slist[0])
        b=int(slist[1][:-1])*-1
else :
    a=int(slist[0])
    b=int(slist[1][:-1])
print(abs(complex(a,b)))
print(cmath.phase(complex(a,b)))
'''
'''
########Find Angle MBC
import math
ab=int(input())
bc=int(input())
#print(ab*ab)
ac=math.sqrt(ab*ab+bc*bc)
#print(ac)
cm=ac/2
anglembc=math.acos((0.5*bc)/cm)
#print(anglembc)
mbcdegrees=math.degrees(anglembc)
print("{0}°".format(round(mbcdegrees)))
'''
'''
###Triangle Quest 2
for i in range(1,int(input())+1):
#    print([1,121,12321,1234321,123454321,12345654321,1234567654321,123456787654321,12345678987654321][i-1])
    print (((10**i - 1)//9)**2)
'''
'''
def QuickSort2(input_list):
    if len(input_list) < 2:
        return input_list
    
    pivot = input_list[0]
    less = [i for i in input_list[1:] if i<= pivot]
    greater = [i for i in input_list[1:] if i>pivot]

    input_list = QuickSort2(less) + [pivot] + QuickSort2(greater)

    return input_list
    
if __name__ == "__main__" :
    input_list = [10,9,8,7, 6, 5, 4, 3, 2,1]
    print(QuickSort2(input_list))

'''
'''
K=int(input())
rlist=input().split()
rlist.reverse()
l=list(set(rlist))
l.sort()
for i in range(0,len(l)):
    if rlist.count(l[i])!=K:
        room=0
        room=l[i]
        break
    else :
        for j in range():
            rlist.pop()
print(room)
'''
'''
###Thr Captain's Room
k=int(input())
rlist=list(map(int,input().split()))
#print(rlist)
l=list(set(rlist))
#print(l)
#print(sum(rlist))
#print(sum(l)*k)
room=(sum(l)*k-sum(rlist))/(k-1)
print(int(room))

'''
'''
###Input()

x, k = list(map(int, input().split()))
p=input()
#print(p)
#type(eval(p))


print(k==eval(p))
'''
'''
###Python Evaluation

eval(input())
'''


###Word Order
n=int(input())
alist=list()
nlist=list()
idx=0
for i in range(0,n):
    t=input()
    if alist.count(t)==0 :
        alist.append(t)
        nlist.append(1)
    else :
        idx=alist.index(t)
        nlist[idx]=nlist[idx]+1
print(len(alist))
import re
s=str(nlist)
#s=re.sub(",", "", s)
#s=re.sub("\[", "", s)
#s=re.sub("\]", "", s)
s=re.sub("[,\[\]]", "", s)
print(s)


