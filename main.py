from Game import play_game


def choice():
    to_scrape = input(str("Do you want to scrape the website or read the saved quotes if possible? (1/2) "))
    counter = 0
    while to_scrape != "1" and to_scrape != "2":
        counter += 1
        if counter == 5:
            raise "Invalid input!"
        to_scrape = input(str("The answer is not valid. Please type '1' or '2':"))
    print()
    return to_scrape


if __name__ == "__main__":
    play_game(choice())
