'''
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for _ in attrs:
            print ('->',_[0],'>',_[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for _ in attrs:
            print ('->',_[0],'>',_[1])
            
n=int(input())
parser = MyHTMLParser()
for i in range(n):      
      parser.feed(input())

'''
'''

###HTML Parser - Part 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment\n{0}".format(data))
        else:
            print(">>> Single-line Comment\n{0}".format(data))
    def handle_data(self, data):
        if data!='\n':
            print(">>> Data\n{0}".format(data))  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
'''
'''
###Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print (tag)
        for _ in attrs:
            print ('->',_[0],'>',_[1])
            
    #def handle_endtag(self, tag):
        #print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for _ in attrs:
            print ('->',_[0],'>',_[1])
            
n=int(input())
parser = MyHTMLParser()
for i in range(n):      
      parser.feed(input())
'''
'''
###Validating UID

#It must contain at least 2 uppercase English alphabet characters.
#It must contain at least 3 digits (0-9).
#It should only contain alphanumeric characters (a-z,A-Z&0-9).
#No character should repeat.
#There must be exactly 10 characters in a valid UID.
import re

n=int(input())
for i in range(n):
    try:
        result='Invalid'
        uid=input()
        if len(uid)==10 :
            if uid.isalnum()==True:
                if len(re.findall(r'[0-9]',uid))>2:
                    if len(re.findall(r'[A-Z]',uid))>1:
                        if len(list(set(uid)))==10:
                            result='Valid'
        print(result)
    except :
        print('Invalid')
'''
'''
###Validating Credit Card Numbers
#► It must start with a 4,5  or 6.                   o
#► It must contain exactly 16 digits.                o
#► It must only consist of digits (0-9).             o
#► It may have digits in groups of 4, separated by one hyphen "-".        o
#► It must NOT use any other separator like ' ' , '_', etc.               o
#► It must NOT have 4 or more consecutive repeated digits.

import re

n=int(input())
for i in range(n):
    try:
        result='Invalid'
        cnum=input()
        chk=0
        if cnum[0]=='4' or cnum[0]=='5' or cnum[0]=='6' :
            chk1=re.sub(r'-','',cnum)
            #print(chk1)
            if len(chk1)==16 and chk1.isdigit()==True and len(cnum)<20:    
                hchk=re.sub(r'[0-9]','',cnum)
                if len(hchk)!=0:
                    chk2=re.split(r'-',cnum)
                    for _ in chk2:
                        if len(_)==4:
                            chk+=1
                    if chk==4:
                        chk=0
                        for i in range(13):
                            if chk1[i]==chk1[i+1]:
                                if chk1[i]==chk1[i+2]:
                                    if chk1[i]==chk1[i+3]:                                        
                                        chk=1
                        if chk!=1:                
                            result='Valid'
                else:
                    for i in range(13):                        
                        if chk1[i]==chk1[i+1]:
                            if chk1[i]==chk1[i+2]:
                                if chk1[i]==chk1[i+3]:
                                    chk=1
                    if chk!=1:
                        result='Valid'
        print(result)
    except :
        print('Invalid')
'''
'''
###Validating Postal Codes           이거 다시해야함 정규식 표현 
regex_integer_in_range = r"[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"

import re
P=input()
print(bool(re.match(regex_integer_in_range,P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
'''

###Matrix Script
import re
n, m = list(map(int,input().split()))
t=[]
for i in range(n):
    t.append(input())
nt=str()
for i in range(m):
    for j in range(n):
        tt=t[j]
        nt+=tt[i]
result=str()
ntt=re.sub(r'\b[^a-zA-Z0-9]+\b',' ', nt)

print(ntt)

'''
import re
n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))
'''
