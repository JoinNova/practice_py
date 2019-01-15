from bs4 import BeautifulSoup
from urllib.request import urlopen

html_doc = """
<html><head><title>Beautiful Soup</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#전제소스출력
print(soup.prettify())

#태그까지 포함한 문장
for link in soup.find_all('a'):
   print(link)

#태그삭제한 문장
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())


with open("abc.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup)

soup = BeautifulSoup("<html>data</html>", 'html.parser')

print(soup)

'''
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))

print(tag.name)

tag.name = "blockquote"
print(tag)


print(tag['class'])

print(tag.attrs)
'''
