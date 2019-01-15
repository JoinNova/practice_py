'''
from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) -
                   dt.strptime(input(), fmt)).total_seconds())))
'''
'''
from dateutil import parser

for _ in range(int(input())):
    d1 = parser.parse(input().strip())
    d2 = parser.parse(input().strip())
    print(abs(int((d2-d1).total_seconds())))
'''
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    from dateutil import parser

    d1 = parser.parse(t1.strip())
    d2 = parser.parse(t2.strip())
    result = (abs(int((d2-d1).total_seconds())))

    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
        #fptr.write(delta + '\n')
    #fptr.close()
'''
'''
from datetime import date
import calendar
T=int(input())
for x in range(T):
    t1=list(map(str,input().split(" ")))
    t2=list(map(str,input().split(" ")))
    hrs=int(''.join(list(t1[4])[0:2]))-(int(''.join(list(t2[4])[0:2])))
    mins=int(''.join(list(t1[4])[3:5]))-(int(''.join(list(t2[4])[3:5])))
    secs=int(''.join(list(t1[4])[6:]))-(int(''.join(list(t2[4])[6:])))
    hrtz1=int(''.join(list(t1[5])[1:3]))
    hrtz2=int(''.join(list(t2[5])[1:3]))
    mintz1=int(''.join(list(t1[5])[3:]))
    mintz2=int(''.join(list(t2[5])[3:]))
    month1=t1[2]
    month2=t2[2]
    d0=date(int(t1[3]),list(calendar.month_abbr).index(month1),int(t1[1]))
    d1=date(int(t2[3]),list(calendar.month_abbr).index(month2),int(t2[1]))
    delta=d0-d1
    dayz=delta.days
    if(str(list(t1[5])[0])== "-"):
        hrs=hrs+hrtz1
        mins=mins+mintz1
        
    if(str(list(t1[5])[0])== "+"):
        hrs=hrs-hrtz1
        mins=mins-mintz1
        
    if(str(list(t2[5])[0])=="-"):
        hrs=hrs-hrtz2    
        mins=mins-mintz2
        
    if(str(list(t2[5])[0])=="+"):
        hrs=hrs+hrtz2
        mins=mins+mintz2

    difference=dayz*86400 + hrs*3600 + mins*60+secs
    print(abs(difference))
'''
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    from datetime import datetime, timedelta
    s1=datetime.strptime(t1[0:24],'%a %d %b %Y %H:%M:%S')
    if t1[25]=='+':
        s1-=timedelta(hours=int(t1[26:28]),minutes=int(t1[28:]))
    elif t1[25]=='-':
        s1+=timedelta(hours=int(t1[26:28]),minutes=int(t1[28:]))

    s2=datetime.strptime(t2[0:24],'%a %d %b %Y %H:%M:%S')
    if t1[25]=='+':
        s2-=timedelta(hours=int(t2[26:28]),minutes=int(t2[28:]))
    elif t1[25]=='-':
        s2+=timedelta(hours=int(t2[26:28]),minutes=int(t2[28:]))
    result = (int(abs((s1-s2).total_seconds())))

    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
        #fptr.write(delta + '\n')
    #fptr.close()
'''
###Piling Up!
n=int(input())
result=[]
for i in range(n):
    l=int(input())
    cube=list(map(int,input().split()))
    #print(cube)
    chk=0
    if l%2==0:
        for j in range(int(l/2)):
            #print("j= %d"%j)
            if cube[j-1]<cube[l-j-1] :
                #print("dddddddddd")
                chk+=1
            elif cube[j-1]<cube[j]:
                #print("dddddddddd")
                chk+=1
            elif ((l-2)-j)!=(int(l/2)-1):
                if cube[(l-1)-j]<cube[(l-2)-j]:
                    #print(cube[l-j-2])
                    #print("dddddddddd")
                    chk+=1
        if chk==0:
            result.append('Yes')
        else :
            result.append('No')
    else :
        cube.insert(int((l+1)/2),1)
        #print(cube)
        for j in range(int(l/2)):
            if cube[j-1]<cube[l-j-1] :
                chk+=1
            elif cube[j-1]<cube[j]:
                chk+=1
            elif ((l-2)-j)!=(int(l/2)-1):
                if cube[(l-1)-j]<cube[(l-2)-j]:
                    #print(cube[l-j-2])
                    #print("dddddddddd")
                    chk+=1
        if chk==0:
            result.append('Yes')
        else :
            result.append('No')

for i in range(n):
    print(result[i])


'''
####Default Arguments
#def increment_by(n, increment=1):
#    return n + increment
class EvenStream(object):
    def __init__(self):
        self.current = 0
    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
class OddStream(object):
    def __init__(self):
        self.current = 1
    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())



queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream)
'''
