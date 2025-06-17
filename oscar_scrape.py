# This program taught me ...

# imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

possible_links = []

root = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year='



def main():
    print("\nWelcome to the Oscar Winning Films search tool! Browse through a database of films that have competed and won Oscars.")
    print("Program built by scraping the website https://www.scrapethissite.com/pages/ajax-javascript/, which queries a wikipedia database using AJAX requests.")

    while True:
        print("\nPlease choose one of the following years to retrieve oscar data from!\n")
        print("\t1) 2010")
        print("\t2) 2011")
        print("\t3) 2012")
        print("\t4) 2013")
        print("\t5) 2014")
        query = input("\t6) 2015\n\n")

        if not query.isdigit():
            print('\nError. Non integer input detected. Try again.')
        else:
            query = int(query)

            if query not in range(1, 7):
                print("\nError. Please choose from one of the valid options listed above. Try again.")
            else:
                pass

if __name__ == '__main__':
    main()