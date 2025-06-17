# imports
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# defining a class to be able to scrape and search the website
class Search:

    # static variable listing the column names
    column_index = ['Team Name ',
                    'Year',
                    'Wins',
                    'Losses',
                    'OT Losses',
                    'Win %',
                    'Goals For (GF)',
                    'Goals Against (GA)',
                    '+ / -']

    # static variable listing the root website address
    root = 'https://www.scrapethissite.com/pages/forms/'

    def __init__(self):
        self.scraped_tables = []

    # scrapes the site for the table outputted and puts it in a pandas dataframe
    def table_scrape(self, soup):

        # finds the html tag for each row for each column
        name = soup.find_all('td', class_='name')
        year = soup.find_all('td', class_='year')
        wins = soup.find_all('td', class_='wins')
        losses = soup.find_all('td', class_='losses')
        ot_losses = soup.find_all('td', class_='ot-losses')
        win_percentages = soup.find_all('td', class_=['pct text-success', 'pct text-danger'])
        goals_for = soup.find_all('td', class_='gf')
        goals_against = soup.find_all('td', class_='ga')
        plus_minus = soup.find_all('td', class_=['diff text-success', 'diff text-danger'])

        data = []

        # iterates through the tags and pulls the strings from them
        for i in range(len(name)):
            data.append([name[i].string.strip(),
                           year[i].string.strip(),
                           wins[i].string.strip(),
                           losses[i].string.strip(),
                           ot_losses[i].string.strip(),
                           win_percentages[i].string.strip(),
                           goals_for[i].string.strip(),
                           goals_against[i].string.strip(),
                           plus_minus[i].string.strip()])

        # turns the data into a pandas dataframe
        df_hockey = pd.DataFrame(data, index=range(1, len(data) + 1), columns=Search.column_index)

        # adds the dataframe into the class variable
        self.scraped_tables.append(df_hockey)

    # scrapes the website for a specific search.
    # passing an empty search_query will result in the default table output getting scraped
    def search_link(self, search_query):
        pass

def main():
    # table scrape test case
    html_text = requests.get('https://www.scrapethissite.com/pages/forms/').text
    soup = BeautifulSoup(html_text, 'lxml')
    search = Search()
    search.table_scrape(soup)
    print(search.scraped_tables[0].to_markdown())

if __name__ == '__main__':
    main()