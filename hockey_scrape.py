# This program taught me how to deal with pagination and searches while web scraping

# imports
import requests
import pandas as pd
from bs4 import BeautifulSoup

# defining a class to be able to scrape and search the website
class Scrape:

    # static variable listing the column names
    column_index = ['Team Name',
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

    # initialization scrape
    def __init__(self):
        self.scraped_tables = []

    # prints all dataframes stored in self.scraped_tables
    def print_frames(self):
        print('\n')

        # if there are more than one dataframes stored, they are concatenated
        if len(self.scraped_tables) > 1:
            print(pd.concat(self.scraped_tables, ignore_index=True).to_markdown())
        elif len(self.scraped_tables) == 1:
            print(self.scraped_tables[0].to_markdown())
        else:
            print("Error. No search results found. Try again!")
        print('\n')

    # scrapes soup from search link and calls table scrape to convert it into a dataframe
    def scrape_link(self, link):
        html_text = requests.get(link).text
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
        df_hockey = pd.DataFrame(data, index=range(len(data)), columns=Scrape.column_index)

        # adds the dataframe into the class variable
        self.scraped_tables.append(df_hockey)

    # scrapes the website for a specific search.
    # passing an empty search_query will result in the default table output getting scraped
    def search_link(self, search_query):
        # dataframe repo is cleared for every new search
        self.scraped_tables.clear()

        # base search is built
        search = Scrape.root + "?q=" + search_query
        links = [search]

        # initial soup is scraped for page catalogue
        html_text = requests.get(search).text
        soup = BeautifulSoup(html_text, 'lxml')

        # soup is searched for pagination
        pages = soup.find('ul', class_='pagination')
        page_nums = pages.find_all("a")

        # if there are pages, a new search is built
        if len(page_nums) != 0:
            links.clear()
            page_length = len(page_nums)

            # iterates over all pages detected and stores every link in the links list
            for i in range(1, page_length):
                search = Scrape.root + '?page_num=' + str(i) + '&q=' + str(search_query)
                links.append(search)

        # iterates over the links list and scrapes every one
        for i, link in enumerate(links, 1):
            print('Scraping page ' + str(i) + '/' + str(len(links)))
            self.scrape_link(link)

def main():

    # initializes the scrape class
    scrape = Scrape()

    # welcoming text
    print("\nWelcome to the Hockey Teams search tool! Browse through a database of NHL team stats since 1990 using custom searches.")
    print("Program built by scraping the website https://www.scrapethissite.com/pages/forms/, which has an existing database.")
    print("Hint: Leave field blank for an exhaustive search of the database!")

    # main input program loop for custom search queries
    while True:
        # gets input from user
        query = input("\nPlease input a search prompt for the hockey database! A table will be printed containing the search results of your query.\n\n")

        # checks to see if input is blank or not
        if not query:
            print("\nSuccessfully entered empty query! Scraping website...\n")
        else:
            print(f'\nSuccessfully inputted query={query}! Scraping website...\n')

        # scrapes and prints based on query
        scrape.search_link(query)
        scrape.print_frames()

if __name__ == '__main__':
    main()
