import pytest
import requests as req

from Scrape_quotes import scrape_quotes


class MockResponse:
    def __init__(self, content):
        self.content = content
        self.text = content


class MockConnectionError:
    def __init__(self, *args, **kwargs):
        pass

    def raise_for_status(self):
        pass

    @property
    def text(self):
        return ""

    @property
    def content(self):
        return b""

    def json(self):
        return {}


def test_scrape_quotes():
    quotes = scrape_quotes()
    assert isinstance(quotes, list)
    assert len(quotes) > 0
    assert isinstance(quotes[0], dict)
    assert "text" in quotes[0]
    assert "author" in quotes[0]
    assert "bio_link" in quotes[0]


def test_scrape_quotes_error(monkeypatch, capsys):
    monkeypatch.setattr(req, 'get', lambda _: MockConnectionError)

    scrape_quotes()

    captured = capsys.readouterr()
    assert "Connection Error. Please check your internet connection and try again." in captured.out


def test_scrape_quotes_pagination(monkeypatch):
    base_url = "https://quotes.toscrape.com"
    url = base_url
    next_page_url = f"{base_url}/page/2/"
    sample_response = """
        <html>
          <body>
            <div class="quote">
              <span class="text">This is a sample quote</span>
              <span class="author">John Doe</span>
              <a href="/john-doe">More info</a>
            </div>
          </body>
        </html> """
    mock_responses = [MockResponse(sample_response)] * 10
    mock_responses.append(MockResponse(f'<html><li class="next"><a href="{next_page_url}">Next</a></li></html>'))

    def mock_get(url):
        return mock_responses.pop(0)

    monkeypatch.setattr(req, 'get', mock_get)

    quotes = scrape_quotes()

    assert len(quotes) > 0
    assert len(mock_responses) == 0
    assert all(q['bio_link'].startswith('/') for q in quotes)
    assert all(q['bio_link'].endswith('/') for q in quotes[:-1])
    assert quotes[-1]['bio_link'].endswith('/john-doe')


def test_scrape_quotes_no_quotes_found(monkeypatch):
    sample_response = """
        <html>
          <body>
          </body>
        </html> """

    monkeypatch.setattr(req, 'get', lambda _: MockResponse(sample_response))

    quotes = scrape_quotes()

    assert len(quotes) == 0
