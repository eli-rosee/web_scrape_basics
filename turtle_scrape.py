# This program taught me how to deal with iframes while webscraping

# imports
import requests
from bs4 import BeautifulSoup

def main():
    # define the root link in which all information is kept in iframes
    root = 'https://www.scrapethissite.com/pages/frames/?frame=i'

    # get the html code from the main iframe page and parse it into a beautiful soup ob
    html_text = requests.get(root).text
    soup = BeautifulSoup(html_text, 'lxml')

    # locate all the names listed in the html and append them to the names list
    names = []
    family_names = soup.find_all('h3', class_='family-name', string=True)
    for name in family_names:
        names.append(name.string)

    # introductory text
    print("\nWelcome to the Turtle Species fun facts tool! Browse through a database of turtles that and request fun facts about them.")
    print("Program built by scraping the website https://www.scrapethissite.com/pages/frames/, which scrapes a wikipedia table for its information.")

    # main program loop to keep asking for input for turtle fun facts
    while True:
        # list out all the options available for the user to pick
        print("\nChoose one of the following turtle species to learn more about!\n")
        for i, name in enumerate(names, 1):
            print(str(i) + ') ' + name)

        # gain input from user
        ans = input('\n')
        print('\n')

        # check and see if the user inputted a valid int
        if ans.isdigit():
            ans = int(ans)

            # check and see if the user inputted a value in the correct range
            if ans in range(1, len(names) + 1):
                # get the html text from the individual page and scrape it into a beautifulsoup ob
                html_text = requests.get(root + '&family=' + names[ans - 1]).text
                soup = BeautifulSoup(html_text, 'lxml')

                # search the soup for the tag in which the fun fact is located
                fact_tag = soup.find(class_='lead')
                fact = ''

                # search through all the strings in the fun fact tag and append them
                for string in fact_tag.strings:
                    fact = fact + string

                # remove whitespace and print
                fact = fact.strip()
                print(fact)

            else:
                print("Error. Invalid input. Please select a value from the list.")
        else:
            print("Error. Invalid input. Please input an integer.")

if __name__ == '__main__':
    main()