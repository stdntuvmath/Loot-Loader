import bs4 as bty
import requests
import datetime
import os
import LLLib_Charles_Schwab as lib

def Parse_WebPage_Delisted():

    try:

        webPage = 'https://stockanalysis.com/actions/delisted/'

        getPage = requests.get(webPage)

        if getPage.status_code != 200:
            print(f"Error: Unable to fetch the page. Status code: {getPage.status_code}")
        #print(getPage)    
        soup = bty.BeautifulSoup(getPage.text, 'html.parser')
        #print(soup.prettify())

        tbody = soup.find('tbody')

        aTags = tbody.find_all('a')
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        
        #print(aTag)
        for tag in aTags:
           
            filename="{}_WebScraped_Data_Delisted.txt".format(todaysDate)

            f = open(filename, "a")
            f.write(tag.text + "\f")

    except Exception as e:
        print(f"An error occurred with the webscraper:{webPage}\r{e}")
        lib.Logging.error("{webPage}\r{e}")


def Parse_WebPage_Listed():

    try:

        webPage = 'https://stockanalysis.com/actions/listed/'

        getPage = requests.get(webPage)

        if getPage.status_code != 200:
            print(f"Error: Unable to fetch the page. Status code: {getPage.status_code}")
        #print(getPage)    
        soup = bty.BeautifulSoup(getPage.text, 'html.parser')
        #print(soup.prettify())

        tbody = soup.find('tbody')

        aTags = tbody.find_all('a')
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        
        #print(aTag)
        for tag in aTags:
           
            filename="{}_WebScraped_Data_Listed.txt".format(todaysDate)

            f = open(filename, "a")
            f.write(tag.text + "\f")

    except Exception as e:
        print(f"An error occurred with the webscraper:{webPage}\r{e}")
        lib.Logging.error("{webPage}\r{e}")


def Parse_WebPage_Splits():

    try:

        webPage = 'https://stockanalysis.com/actions/splits/'

        getPage = requests.get(webPage)

        if getPage.status_code != 200:
            print(f"Error: Unable to fetch the page. Status code: {getPage.status_code}")
        #print(getPage)    
        soup = bty.BeautifulSoup(getPage.text, 'html.parser')
        #print(soup.prettify())

        tbody = soup.find('tbody')

        aTags = tbody.find_all('a')
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        
        #print(aTag)
        for tag in aTags:
           
            filename="{}_WebScraped_Data_Splits.txt".format(todaysDate)

            f = open(filename, "a")
            f.write(tag.text + "\f")

    except Exception as e:
        print(f"An error occurred with the webscraper:{webPage}\r{e}")
        lib.Logging.error("{webPage}\r{e}")


def Parse_WebPage_Spinoffs():

    try:

        webPage = 'https://stockanalysis.com/actions/spinoffs/'

        getPage = requests.get(webPage)

        if getPage.status_code != 200:
            print(f"Error: Unable to fetch the page. Status code: {getPage.status_code}")
        #print(getPage)    
        soup = bty.BeautifulSoup(getPage.text, 'html.parser')
        #print(soup.prettify())

        tbody = soup.find('tbody')

        aTags = tbody.find_all('a')
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        
        #print(aTag)
        for tag in aTags:
           
            filename="{}_WebScraped_Data_Spinoffs.txt".format(todaysDate)

            f = open(filename, "a")
            f.write(tag.text + "\f")

    except Exception as e:
        print(f"An error occurred with the webscraper:{webPage}\r{e}")
        lib.Logging.error("{webPage}\r{e}")


def Parse_WebPage_Acquisitions():

    try:

        webPage = 'https://stockanalysis.com/actions/acquisitions/'

        getPage = requests.get(webPage)

        if getPage.status_code != 200:
            print(f"Error: Unable to fetch the page. Status code: {getPage.status_code}")
        #print(getPage)    
        soup = bty.BeautifulSoup(getPage.text, 'html.parser')
        #print(soup.prettify())

        tbody = soup.find('tbody')

        aTags = tbody.find_all('a')
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        
        #print(aTag)
        for tag in aTags:
           
            filename="{}_WebScraped_Data_Acquisitions.txt".format(todaysDate)

            f = open(filename, "a")
            f.write(tag.text + "\f")

    except Exception as e:
        print(f"An error occurred with the webscraper:{webPage}\r{e}")
        lib.Logging.error("{webPage}\r{e}")


def Parse_WebPage_Bankruptcies():

    try:

        webPage = 'https://stockanalysis.com/actions/bankruptcies/'

        getPage = requests.get(webPage)

        if getPage.status_code != 200:
            print(f"Error: Unable to fetch the page. Status code: {getPage.status_code}")
        #print(getPage)    
        soup = bty.BeautifulSoup(getPage.text, 'html.parser')
        #print(soup.prettify())

        tbody = soup.find('tbody')

        aTags = tbody.find_all('a')
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        
        #print(aTag)
        for tag in aTags:
           
            filename="{}_WebScraped_Data_Bankruptcies.txt".format(todaysDate)

            f = open(filename, "a")
            f.write(tag.text + "\f")

    except Exception as e:
        print(f"An error occurred with the webscraper:{webPage}\r{e}")
        lib.Logging.error("{webPage}\r{e}")



os.system("CLS")

print("Web Scraper started...")


Parse_WebPage_Delisted()
Parse_WebPage_Listed()
Parse_WebPage_Splits()
Parse_WebPage_Spinoffs()
Parse_WebPage_Acquisitions()
Parse_WebPage_Bankruptcies()

print("Web Scraper finished...")