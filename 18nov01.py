'''
####
import re
import time
import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
n=int(input())
result=[]
for i in range(n):
    gap=0    
    t1=input()
    t11=parse(t1[:24])
    h1=int(t1[26:28])
    m1=int(t1[28:])
    tt1=h1*3600+m1*60
    if t1[25]=='-':
        tt1=-tt1
##########################    
    t2=input()
    t22=parse(t2[:24])
    h2=int(t2[26:28])
    m2=int(t2[28:])
    tt2=h2*3600+m2*60
    if t2[25]=='-':
        tt2=-tt2
    gap=t22-t11
    gap2=tt2-tt1
    if gap.total_seconds()<0:
        gap=-gap
    #print(gap.total_seconds())
    #print(gap2)
    result.append(int(gap.total_seconds())+gap2)
for i in range(n):
    print(result[i])
    
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
    import time
    import datetime 
    from dateutil.parser import parse
    from dateutil.relativedelta import relativedelta
    t11=parse(t1[:24])
    h1=int(t1[26:28])
    m1=int(t1[28:])
    tt1=h1*3600+m1*60
    if t1[25]=='-':
        tt1=-tt1
    t22=parse(t2[:24])
    h2=int(t2[26:28])
    m2=int(t2[28:])
    tt2=h2*3600+m2*60
    if t2[25]=='-':
        tt2=-tt2
    gap=t22-t11
    gap2=tt2-tt1
    if gap.total_seconds()<0:
        gap=-gap
    result=float((gap.total_seconds())+gap2)
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
###Validating phone numbers
import re
n=int(input())
for i in range(n):
    try:
        t=input()
        t=int(t)+1-1
        t=str(t)
        if len(str(t))==10:
            #print(t[0])
            if int(t[0])>6 and int(t[0])<9.1 :
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    except:
        print("NO")
'''
'''
import re;
N = int(input());
for x in range(0,N):
    S = input();
    match = re.search('[789]\d+',S);    
    if match and len(match.group()) == 10:
        print("YES");        
    else:
        print("NO");
'''
'''
import re
for i in range(int(input())):
  print('YES' if re.match('^[7-9][0-9]{9}$', input()) else 'NO')
'''
'''
import re
for i in range(int(raw_input())):
    print 'YES' if re.search(r"^[789]\d{9}$",raw_input()) else 'NO'

'''
'''
#[789] : match a single digit 7,8 or 9. 
#\d{9} : match  digits.

###Validating and Parsing Email Addresses
import re
import email.utils
n=int(input())
for i in range(n):
    try :
        e=email.utils.parseaddr(input())
        chk=re.split(r"[@]",e[1])
        chk2=re.split(r"[.]",chk[1])
        user=chk[0]
        if len(chk2)==2 and str.isalpha(user[0])==True and str.isalpha(chk2[0])==True and str.isalpha(chk2[1]) and len(chk2[1])<=3:
            if len(re.sub(r"[\w\.\-\_]","",user))==0:
                print(email.utils.formataddr(e))
    except:
        continue
'''

import re

N = int(input())
for _ in range(N):
    tOrg = input().strip()

    e = re.search(r'<(.*)>', tOrg)
    if e == None:
        continue
    t = e.group(1).strip()

    if re.search(r'^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', t) != None:
        print(tOrg)
