### Hex Color Code
'''
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
###Hex Color Code
import re
n=int(input())
slist=[]
#chk=0
for i in range(n):
      #chk+=1
      #print("====%d==="%chk)
      text=input()
      t=re.findall(r"#[0-9a-fA-F]{3,6}[;),]",text)
      #print(t)
      if len(t)!=0:
            for s in t:
                  print(s[:len(s)-1])
            #slist.append(re.findall(r"[#\w{3,6}[;),]",text))
#print("=======")
#for s in slist:
      #print(s)
'''
'''
####HTML Parser - Part 1
                  
from html.parser import HTMLParser
import re

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        #print(attrs)
        #print(type(attrs))
        #print(len(attrs))        
        if len(attrs)!=0:
              #print(attrs[0])
              #print(type(attrs[0]))
              l=list(attrs)
              for i in range (len(l)):
                    d=l[i]
                    print("-> %s > %s"%(d[0],d[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        #print(attrs)
        #print(type(attrs))
        #print(len(attrs))        
        if len(attrs)!=0:
              #print(attrs[0])
              #print(type(attrs[0]))
              l=list(attrs)
              for i in range (len(l)):
                    d=l[i]
                    print("-> %s > %s"%(d[0],d[1]))

# instantiate the parser and fed it some HTML
n=int(input())
parser = MyHTMLParser()
for i in range(n):      
      parser.feed(input())
'''

'''
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
n=int(input())
parser = MyHTMLParser()
for i in range(n):      
      parser.feed(input())
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

