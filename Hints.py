import requests as req
from bs4 import BeautifulSoup as BS


def get_hint(bio_link):
    """
    This function takes a bio link and returns a hint about the author's birthdate and location.
    """
    url = "http://quotes.toscrape.com"
    response = req.get(f"{url}{bio_link}")
    soup = BS(response.text, "html.parser")
    birth_date = soup.find("span", {"class": "author-born-date"}).text
    birth_place = soup.find("span", {"class": "author-born-location"}).text
    return f"The author was born on {birth_date} {birth_place}."
