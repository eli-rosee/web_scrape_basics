# imports
import requests
from bs4 import BeautifulSoup

# use the python request tool to get the html version of the website and parse it with the lxml engine
html_text = requests.get('https://www.scrapethissite.com/pages/simple/').text
soup = BeautifulSoup(html_text, 'lxml')

# find all instances of h3, in which the country names are all stored
countries = soup.find_all('h3', class_='country-name')

names = []

# search through all the h3 tags and grab the text, aka the country name, store it in a list, and print it
for country in countries:
    new_country = country.get_text().strip()
    names.append(new_country)
    print(new_country)
