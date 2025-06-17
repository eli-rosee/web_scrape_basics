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

    def print_frames(self):
        if len(self.scraped_tables) > 1:
            print(pd.concat(self.scraped_tables, ignore_index=True).to_markdown())
        elif len(self.scraped_tables) == 1:
            print(self.scraped_tables[0].to_markdown())
        else:
            print("Error. No search results found. Try again!")

    def scrape_link(self, search):
        html_text = requests.get(search).text
        soup = BeautifulSoup(html_text, 'lxml')

        self.table_scrape(soup)

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
        df_hockey = pd.DataFrame(data, index=range(len(data)), columns=Search.column_index)

        # adds the dataframe into the class variable
        self.scraped_tables.append(df_hockey)

    # scrapes the website for a specific search.
    # passing an empty search_query will result in the default table output getting scraped
    def search_link(self, search_query):
        self.scraped_tables.clear()
        search = Search.root + "?q=" + search_query
        links = [search]

        html_text = requests.get(search).text
        soup = BeautifulSoup(html_text, 'lxml')

        pages = soup.find('ul', class_='pagination')
        page_nums = pages.find_all("a")

        if len(page_nums) != 0:
            links.clear()
            page_length = len(page_nums)

            for i in range(1, page_length + 1):
                search = Search.root + '?page_num=' + str(i) + '&q=' + str(search_query)
                links.append(search)

        for link in links:
            self.scrape_link(link)

def main():

    search = Search()

    print("\nWelcome to the Hockey Teams search tool! Browse through a database of NHL team stats since 1990 using custom searches.")
    print("Program built by scraping the website https://www.scrapethissite.com/pages/forms/, which has an existing database.")

    while True:
        query = input("\n\nPlease input a search prompt for the hockey database! A table will be printed containing the search results of your query.\nHint: Leave field blank for an exhaustive search of the database!\n\n")
        search.search_link(query)
        search.print_frames()

if __name__ == '__main__':
    main()