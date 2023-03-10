import random as rand

from Hints import get_hint
from Scrape_quotes import scrape_quotes


def play_game():
    """
    This function starts the game and asks the user to guess the author of a random quote.
    """
    quotes = scrape_quotes()
    random_quote = rand.choice(quotes)
    author = random_quote["author"]
    bio_link = random_quote["bio_link"]
    hints = [get_hint(bio_link), f"The author's first name starts with '{author[0]}'",
             f"The author's last name has {len(author.split()[-1])} letters"]
    rand.shuffle(hints)

    print(random_quote["text"])
    print("Who said this quote?")
    guesses_remaining = 4
    while guesses_remaining > 0:
        guess = input(f"You have {guesses_remaining} guesses remaining. ")
        if guess.lower() == author.lower():
            print("Congratulations! You guessed correctly.")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() == "y":
                play_game()
            else:
                print("Thanks for playing!")
            return
        else:
            guesses_remaining -= 1
            print(f"Sorry, that's incorrect. {hints.pop(0)}")
    print(f"Sorry, you're out of guesses. The author was {author}.")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")
