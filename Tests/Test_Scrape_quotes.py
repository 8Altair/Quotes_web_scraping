import time
import requests as req
import pytest

from Scrape_quotes import scrape_quotes


# Checks if scrape_quotes() returns a list
def test_scrape_quotes_returns_list():
    assert type(scrape_quotes()) == list


# Checks if each quote is a dictionary
def test_scrape_quotes_returns_dicts():
    for quote in scrape_quotes():
        assert type(quote) == dict


# Checks if each quote has the expected keys
def test_scrape_quotes_returns_expected_keys():
    expected_keys = {'text', 'author', 'bio_link'}
    for quote in scrape_quotes():
        assert set(quote.keys()) == expected_keys


# Checks if scrape_quotes() returns a non-empty list
def test_scrape_quotes_returns_non_empty_list():
    assert len(scrape_quotes()) > 0


# Checks if all bio_links start with '/author/'
def test_scrape_quotes_returns_valid_url():
    for quote in scrape_quotes():
        assert quote['bio_link'].startswith('/author/')


# Checks if scrape_quotes() does not raise any exceptions
def test_scrape_quotes_does_not_throw_exceptions():
    try:
        scrape_quotes()
    except Exception as e:
        pytest.fail(f"scrape_quotes() raised an exception: {e}")


# Checks if each quote has a 'text' key
def test_quotes_items_has_text_key():
    quotes = scrape_quotes()
    assert all("text" in q for q in quotes)


# Checks if each quote has an 'author' key
def test_quotes_items_has_author_key():
    quotes = scrape_quotes()
    assert all("author" in q for q in quotes)


# Checks if each quote has a 'bio_link' key
def test_quotes_items_has_bio_link_key():
    quotes = scrape_quotes()
    assert all("bio_link" in q for q in quotes)


# Checks if all quotes are unique based on text and author
def test_quotes_are_unique():
    quotes = scrape_quotes()
    assert len(quotes) == len(set((q["text"], q["author"]) for q in quotes))


# Checks if time.sleep() is called with expected delay
def test_sleep_called_with_expected_delay(monkeypatch):
    def mock_sleep(delay):
        assert delay == 2

    monkeypatch.setattr(time, "sleep", mock_sleep)
    scrape_quotes()


# Checks if scrape_quotes() handles case where no quotes are found
def test_handles_no_quotes(monkeypatch):
    mock_response = {
        "status_code": 200,
        "text": """
            <html>
                <head></head>
                <body>
                    <div class="container">
                        <h1>No quotes found</h1>
                    </div>
                </body>
            </html>"""}

    def mock_get(url):
        class MockResponse:
            def __init__(self, status_code, text):
                self.status_code = status_code
                self.text = text

        return MockResponse(mock_response["status_code"], mock_response["text"])

    monkeypatch.setattr(req, 'get', mock_get)
    quotes = scrape_quotes()
    assert quotes == []
