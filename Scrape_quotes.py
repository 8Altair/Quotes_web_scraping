from time import sleep

import requests as req
from bs4 import BeautifulSoup as BS


def scrape_quotes():
    """
    This function scrapes the website for quotes and returns a list of dictionaries,
    where each dictionary contains the quote text, the name of the person who said the quote,
    and the href of the link to the person's bio.
    """
    base_url = "https://quotes.toscrape.com"
    url = base_url
    quotes = []

    while url:
        try:
            response = req.get(url)
        except req.exceptions.ConnectionError as e:
            print("Connection Error. Please check your internet connection and try again.")
            print(e)
            exit(1)
        soup = BS(response.text, "html.parser")
        q = soup.find_all(class_="quote")
        if q is not None:
            for quote in q:
                quotes.append({"text": quote.find(class_="text").get_text(),
                               "author": quote.find(class_="author").get_text(),
                               "bio_link": quote.find("a")["href"]})

        next_page = soup.find("li", {"class": "next"})
        url = base_url + next_page.find("a")["href"] if next_page else None

        sleep(2)
    return quotes
