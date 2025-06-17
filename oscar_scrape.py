# This program taught me how to handle backend api requests to bypass the html and how to use json objects with pandas

# imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# root link that will remain unchanged
root = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year='

def main():
    # welcoming text
    print("\nWelcome to the Oscar Winning Films search tool! Browse through a database of films that have competed and won Oscars.")
    print("Program built by scraping the website https://www.scrapethissite.com/pages/ajax-javascript/, which queries a wikipedia database using AJAX requests.")

    # main program loop, will continue to run and feed requests from user through the logic
    while True:

        # initial list the user sees, gains input from user
        print("\nPlease choose one of the following years to retrieve oscar data from!\n")
        print("\t1) 2010")
        print("\t2) 2011")
        print("\t3) 2012")
        print("\t4) 2013")
        print("\t5) 2014")
        query = input("\t6) 2015\n\n")
        print('\n')

        # error checks the input for being a digit
        if not query.isdigit():
            print('Error. Non integer input detected. Try again.')
        else:
            # makes query integer so logic can be performed correctly
            query = int(query)

            # checks to see if the query is in the correct range
            if query not in range(1, 7):
                print("Error. Please choose from one of the valid options listed above. Try again.")
            else:
                # grabs the text from the json object from the backend api and turns it into json ob
                text_ob = requests.get(root + str(2009 + query)).text
                json_ob = json.loads(text_ob)

                # uses pandas json_normalize to turn the json ob into a dataframe
                df_oscars = pd.json_normalize(json_ob)
                print(df_oscars.to_markdown())
                print('\n')

if __name__ == '__main__':
    main()