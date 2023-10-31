"""
This is a web scraping script that allows you to scrape google
news about technology.

author: Fernando Arroliga
created: 2023-10-30 
version: 1.0
"""

# ------------- Importing the Useful Libraries and Modules
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# --------------- Functions for the Main Program --------------------

def get_title_of_articles(soup):
    """

    This function gets the title of the articles
    in the html file of google news webpage.

    Parameters
    ----------
    soup : soup object
        soup object with html content.

    Returns
    -------
    list
        A list containing the title of articles.
    """
    title_of_the_articles = []
    article_tags = soup.find_all("article")

    for article in article_tags:
        
        h3_tag = article.find("h3")
        h3_content = h3_tag.text
        title_of_the_articles.append(h3_content)

    return title_of_the_articles


def get_link_of_articles(soup):
    """

    This function gets the links of the articles
    in the html file of google news webpage.

    Parameters
    ----------
    soup : soup object
        soup object with html content.

    Returns
    -------
    list
        A list containing the links of the articles.
    """
    links = []
    article_tags = soup.find_all("article")

    for article in article_tags:
        h3_tag = article.find("h3")

        for a in h3_tag:
            
            a_link = h3_tag.find("a")
            href_value = a_link.get("href")
            href_link = href_value[1:]
            link = "https://news.google.com" + href_link

            links.append(link)

    return links

def get_current_date():
    """

    This function gets the current date.
    
    Returns
    -------
    str
        A string containing the current date with
        the format: Tuesday_20.
    """
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%A_%d")

    return formatted_date


# ----------------  Variables ----------------------------------------

# Url of the website
url = "https://news.google.com/search?q=technology&hl=en-US&gl=US&ceid=US%3Aen"

# Html Content 
response = requests.get(url)

# Soup Object
soup = BeautifulSoup(response.content, 'html.parser')

# Headlines
headlines = {
    title: link for title, link in zip(
        get_title_of_articles(soup),
        get_link_of_articles(soup))
    }

# Day of the Scraping
day_of_scraper = get_current_date() + ".txt"


# --------------- Main Program -------------------------------

if __name__ == "__main__":

    # Creating the txt file with the articles
    with open(day_of_scraper, "w") as file:
        
        for key, value in headlines.items():
            
            file.write(f"Title of Article:\n{key} \nLink of article:\n{value}\n\n")


    print("The scraper program worked good!")


















