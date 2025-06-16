import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.scrapethissite.com/pages/simple/').text
soup = BeautifulSoup(html_text, 'lxml')

countries = soup.find_all('h3', class_='country-name')

names = []
for country in countries:
    names.append(country.get_text().strip())

for name in names:
    print(name)