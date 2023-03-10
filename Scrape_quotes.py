import requests as req
from bs4 import BeautifulSoup as BS


def scrape_quotes():
    """
    This function scrapes the website for quotes and returns a list of dictionaries,
    where each dictionary contains the quote text, the name of the person who said the quote,
    and the href of the link to the person's bio.
    """
    url = "http://quotes.toscrape.com"
    quotes = []

    while url:
        response = req.get(url)
        soup = BS(response.text, "html.parser")
        quotes_div = soup.find("div", {"class": "quotes"})
        if quotes_div is not None:
            for quote in quotes_div.find_all("div", {"class": "quote"}):
                quotes.append({
                    "text": quote.find("span", {"class": "text"}).text,
                    "author": quote.find("span", {"class": "author"}).text,
                    "bio_link": quote.find("a")["href"]})

        next_page = soup.find("li", {"class": "next"})
        url = next_page.find("a")["href"] if next_page else None

    return quotes
