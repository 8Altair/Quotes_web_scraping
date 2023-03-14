from Game import get_hint, initializing


def test_get_hint():
    bio_link = "/author/J-K-Rowling"
    hint = get_hint(bio_link)
    assert isinstance(hint, str)
    assert len(hint) > 0


def test_initializing():
    quotes = [{"text": "Quote 1", "author": "Author 1", "bio_link": "/author/Author-1"},
              {"text": "Quote 2", "author": "Author 2", "bio_link": "/author/Author-2"}]

    random_quote, author, bio_link, hints, guesses_remaining = initializing(quotes)
    assert isinstance(random_quote, dict)
    assert "text" in random_quote and "author" in random_quote and "bio_link" in random_quote
    assert isinstance(author, str)
    assert len(author) > 0
    assert isinstance(bio_link, str)
    assert len(bio_link) > 0
    assert isinstance(hints, list)
    assert len(hints) == 3
    assert isinstance(hints[0], str)
    assert isinstance(hints[1], str)
    assert isinstance(hints[2], str)
    assert guesses_remaining == 4
