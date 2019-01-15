'''
###Word Order
from collections import OrderedDict
m=int(input())
a=OrderedDict()
n=[]
for i in range(0,m):
    b=input()
    n.append(b)
    if a[b]=n.count(b)

print(len(a))
for k in a.keys():
    print(a.values())

'''
'''
###Word Order
import re
def b(m) :
    a=[]
    n=[]
    for i in range(0,m):
        t=input()
        if a.count(t)==0 :
            a.append(t)
            n.append(1)
        else :
            j=a.index(t)
            n[j]=n[j]+1
    print(len(a))
    return re.sub("[,\[\]]", "", str(n))
if __name__=='__main__':
    m=int(input())
    print(b(m))
'''
'''
###Word Order
n=int(input())
a=dict()
l=[]
for i in range(0,n):
    t=input()
    if t in a:
        a[t]+=1
    else :
        a[t]=1
        l.append(t)
print(len(l))
for i in l:
    print(a[i],end=' ')
'''
'''
N=int(input())
dict={}
li=[]
for i in range(N):
    word=input()
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
        li.append(word)
print (len(li))      
for i in li:
    print (dict[i],end=' ')
'''
'''
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
'''

'''
#######Collections.deque()
from collections import deque
d = deque()
n=int(input())
for i in range(n):
    com=input().split()
    if com[0]=='append':
        d.append(com[1])
    elif com[0]=='appendleft':
        d.appendleft(com[1])
    elif com[0]=='clear':
        d.clear()
    elif com[0]=='extend':
        d.extend(com[1])
    elif com[0]=='extendleft':
        d.extendleft(com[1])
    elif com[0]=='count':
        d.count(com[1])
    elif com[0]=='pop':
        d.pop()
    elif com[0]=='popleft':
        d.popleft()
    elif com[0]=='remove':
        d.remove(com[1])
    elif com[0]=='reverse':
        d.reverse()
    elif com[0]=='rotate':
        d.rotate(com[1])
for i in range(len(d)):
    print(d[i],end=' ')
'''

'''
###Check Subset

n=int(input())
result=[]
for i in range(n):
    m=int(input())
    a=set(map(int,input().split()))
    m=int(input())
    b=set(map(int,input().split()))
    result.append(len(a.intersection(b))==len(a))
for i in range(n):
    print(result[i])
'''
'''
###Check Strict Superset
a=set(map(int,input().split()))
n=int(input())
result=True
for i in range(n):
    b=set(map(int,input().split()))
    if len(a.intersection(b))==len(a):
        result=False
    elif len(b.difference(a))>0:
        result=False

        
print(result)
'''

'''
###Array Mathematics
import numpy
n=input().split()
l=list()
for i in range(int(n[0])*2):
    l.append(input().split())
a=numpy.array(l,int)
#print(a)
if int(n[0])==1:
    for i in range(int(n[0])):
        print("[{0}]".format(numpy.add(a[i],a[i+int(n[0])])))
        print("[{0}]".format(numpy.subtract(a[i],a[i+int(n[0])])))
        print("[{0}]".format(numpy.multiply(a[i],a[i+int(n[0])])))
        print("[{0}]".format(a[i]//a[i+int(n[0])]))
        print("[{0}]".format(numpy.mod(a[i],a[i+int(n[0])])))
        print("[{0}]".format(numpy.power(a[i],a[i+int(n[0])])))
elif int(n[0])==2:
    print("[{0}\n {1}]".format(numpy.add(a[0],a[2]),numpy.add(a[1],a[3])))
    print("[{0}\n {1}]".format(numpy.subtract(a[0],a[2]),numpy.subtract(a[1],a[3])))
    print("[{0}\n {1}]".format(numpy.multiply(a[0],a[2]),numpy.multiply(a[1],a[3])))
    print("[{0}\n {1}]".format((a[0]//a[2]),(a[1]//a[3])))
    print("[{0}\n {1}]".format(numpy.mod(a[0],a[2]),numpy.mod(a[1],a[3])))
    print("[{0}\n {1}]".format(numpy.power(a[0],a[2]),numpy.power(a[1],a[3])))
'''
'''
import numpy

n,m=map(int,input().split())
A=numpy.array([list(map(int,input().split())) for i in range(n)])
B=numpy.array([list(map(int,input().split())) for i in range(n)])
print(A+B,A-B,A*B,A//B,A%B,A**B,sep='\n')
'''
'''
import numpy

n, m = [int(i) for i in input().strip().split()]
A, B = [],[]
for i in range(n) :
    A.append([int(k) for k in input().strip().split()])
    print(A)
for i in range(n) :
    B.append([int(k) for k in input().strip().split()])
A = numpy.array(A)
B = numpy.array(B)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
'''
'''
#########Floor, Ceil and Rint
import numpy
my = numpy.array(input().split(),float)
print(numpy.floor(my))
print(numpy.ceil(my))
print(numpy.rint(my))

'''
'''
import numpy

#numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
'''
'''
###Mod Divmod
a=int(input())
b=int(input())

print(a//b)
print(a%b)
print(divmod(a,b))
'''
'''
###Map and Lambda Function

cube = lambda x : x * x * x
def fibonacci(n):
    l=list()
    l=[0,1]
    k=0
    if n==0:
        l=[]
    elif n==1:
        l=[0]
    else:
        for i in range(2,n):
            k=l[i-2]+l[i-1]
            l.append(k)
    return l

if __name__=='__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
'''
'''
###Validating Email Addresses With a Filter
def fun(s):
    import re
    try:
        result=False
        regex_pattern = r"[@.]"
        chk=re.split(regex_pattern,s)
        if len(chk)==3:
            chk22=0
            for i in range(3):
                if i==0:
                    if chk[0]=='':
                        chk22+=1
                    for j in range(len(chk[0])):
                        regex_pattern = r"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\-_]"
                        chk2=re.split(regex_pattern,chk[0])
                        for j in range(len(chk2)):
                            if len(chk2[j])!=0:
                                chk22+=1
                elif i==1:
                    for j in range(len(chk[1])):
                        regex_pattern = r"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789]"
                        chk2=re.split(regex_pattern,chk[1])
                        for j in range(len(chk2)):
                            if len(chk2[j])!=0:
                                chk22+=1
                else :
                    if len(chk[2])>3:
                        chk22+=1
                    for j in range(len(chk[2])):
                        regex_pattern = r"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789]"
                        chk2=re.split(regex_pattern,chk[1])
                        for j in range(len(chk2)):
                            if len(chk2[j])!=0:
                                chk22+=1
        if chk22==0:
            result=True
        return result  
                    
    except:
        result=False
    return result

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

'''
'''
import re
lst = list()
for i in range(int(raw_input())):
    lst.append(raw_input())
print sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',x),lst)))
'''


###Zipped!

n, m=input().split()
slist=list()
for i in range(int(m)):
    slist.append(input().split())
alllist=list()
for i in range(len(slist)):
    s=slist[i]
    for j in range(len(s)):
        alllist.append(s[j])
#print(alllist)
alist=list()
for i in range(int(n)):
    s=0
    for j in range(i,int(n)*int(m),int(n)):
        s+=float(alllist[j])
    alist.append(float(s/int(m)))
for i in range(len(alist)):
    print("%0.1f"%alist[i])
