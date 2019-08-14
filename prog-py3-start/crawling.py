import requests

response=requests.get('http://computer.knu.ac.kr/main/')

html=response.text
print(html)


a=requests.get('http://www.google.com').text

print('aaaaaaaaa',a)