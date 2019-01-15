'''
#This is String
n=input()
print(type(n))
for _ in n:
    print(_)
    print(type(n))


print("=======================")

#This is String
n=input().split()
print(type(n))
for _ in n:
    print(_)
    print(len(n))
    print(type(_))

print("=======================")


#This is String
n=input().split()

for _ in n:
    for i in _ :
        print(i)
        print(len(_))
        print(type(_))
    print("=======================")

'''
'''
'''
#Detect HTML Tags, Attributes and Attribute Values
HTML="""
<head>
    <title>HTML</title> 
    </head>
    <object type="application/x-flash" 
        data="your-file.swf"
        width="0" height="0">
        <!-- <param name="movie" value="your-file.swf" /> -->
        <param name="quality" value="high"/> 
    </object>
"""

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print (tag)
        for _ in attrs:
            print ('->',_[0],'>',_[1])
            
      
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for _ in attrs:
            print ('->',_[0],'>',_[1])
            
#n=int(input())
parser = MyHTMLParser()
parser.feed(HTML)




    

    
