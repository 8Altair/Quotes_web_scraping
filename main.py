from Game import play_game


def choice() -> str:
    """
        Asks the user if they want to scrape a website or read saved quotes, and returns their choice.

        Returns:
        - A string representing the user's choice: either "1" to scrape a website or "2" to read saved quotes.

        Raises:
        - ValueError if the user inputs an invalid choice more than 5 times.
    """
    to_scrape = input(str("Do you want to scrape the website or read the saved quotes if possible? (1/2) "))
    counter = 0
    while to_scrape != "1" and to_scrape != "2":
        counter += 1
        if counter == 5:
            raise ValueError("Invalid input!")
        to_scrape = input(str("The answer is not valid. Please type '1' or '2':"))
    print()
    return to_scrape


if __name__ == "__main__":
    play_game(choice())
