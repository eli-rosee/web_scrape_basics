from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# print("Title full tage: " + str(soup.title))
# print("soup.title.name: " + str(soup.title.name))
# print("soup.title.string: " + str(soup.title.string))
# print("soup.p: " + str(soup.p))
# print("soup.p['class']: " + str(soup.p['class']))
# print("soup.a: " + str(soup.a))
# print("soup.find_all('a'): " + str(soup.find_all('a')))
# print('soup.find(id="link3"): ' + str(soup.find(id="link3")))

# for link in soup.find_all('a'):
#     print(link.get('href'))

print(soup.get_text())

p = soup.p.string
print(p)
print(type(p))
print(str(p))
print(unicode(p))