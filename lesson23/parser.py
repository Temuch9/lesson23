import requests
from bs4 import BeautifulSoup

url='https://dedmorozural.ru/'
response = requests.get(url)
print(response.status_code)
print(response.text)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

print(soup.a)
print(soup.a.string)

a_tags = soup.find_all('a')
for a_tags in a_tags:
    print(a_tags)

big_body_div = soup.find( 'div', class_ = 'modulebody1')
print(big_body_div)