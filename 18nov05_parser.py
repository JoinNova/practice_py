#print('Hello_World!')
#import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

html_doc='http://www.4irsw.com'

soup = urlopen(html_doc).read()
soup = BeautifulSoup(soup, 'html.parser') #lxml       html.parser

#print(soup.prettify())

#print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.text)
# u'title'

#print(soup.title.string)
# u'The Dormouse's story'

#get hyperlinks (finding 'a' = hyperlink tag code)
#print(soup.a)
#print(soup.find_all('a')[2])
#link =  soup.find_all('a')
#for i in link:
    #print(i.text)
#for link in soup.find_all('a'):
    #print(link.get('href'))
