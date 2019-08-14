import requests
from bs4 import BeautifulSoup

response=requests.get('http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O0204&sub=1O&search_open_yr_trm=20182#')
aaa=response.text
soup = BeautifulSoup(aaa,"html.parser")

for elem in soup.find_all(class_='th5'):
    print(elem.string)

#print(soup.prettify())


print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.name)
# u'title'

print(soup.title.string)    ;print(soup.title.text)
# u'The Dormouse's story'

print(soup.title.parent.name)
# u'head'

print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])
# u'title'

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print('-----')

print(soup.find(id="link3"))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

for aa in soup.find_all('a'):
    print(aa['href'])

print(type(soup.find('div').find('p')))

print(soup.head.title)
#print(soup.html.contents)
