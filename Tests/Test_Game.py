from Game import get_hint, initializing


# A unit test for the get_hint function
def test_get_hint():
    bio_link = "/author/J-K-Rowling"        # Providing a sample bio_link as input
    hint = get_hint(bio_link)       # Calling the get_hint function and getting the output hint
    assert isinstance(hint, str)        # Asserting that the output is of string type
    assert len(hint) > 0        # Asserting that the length of output hint is greater than 0


# A unit test for the initializing function
def test_initializing():
    # Creating a sample list of quotes with text, author, and bio_link keys
    quotes = [{"text": "Quote 1", "author": "Author 1", "bio_link": "/author/Author-1"},
              {"text": "Quote 2", "author": "Author 2", "bio_link": "/author/Author-2"}]

    # Calling the initializing function with the sample quotes list as input
    random_quote, author, bio_link, hints, guesses_remaining = initializing(quotes)
    # Asserting that the random_quote output is a dictionary
    assert isinstance(random_quote, dict)
    # Asserting that the random_quote output contains text, author, and bio_link keys
    assert "text" in random_quote and "author" in random_quote and "bio_link" in random_quote
    # Asserting that the author output is of string type
    assert isinstance(author, str)
    # Asserting that the length of the author output is greater than 0
    assert len(author) > 0
    # Asserting that the bio_link output is of string type
    assert isinstance(bio_link, str)
    # Asserting that the length of the bio_link output is greater than 0
    assert len(bio_link) > 0
    # Asserting that the hints output is a list
    assert isinstance(hints, list)
    # Asserting that the length of the hints output is 3
    assert len(hints) == 3
    # Asserting that the first hint in the hints output is of string type
    assert isinstance(hints[0], str)
    # Asserting that the second hint in the hints output is of string type
    assert isinstance(hints[1], str)
    # Asserting that the third hint in the hints output is of string type
    assert isinstance(hints[2], str)
    # Asserting that the guesses_remaining output is equal to 4
    assert guesses_remaining == 4
