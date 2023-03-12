from Game import play_game

if __name__ == "__main__":
    to_scrape = input(str("Do you want to scrape the website or read the saved quotes if possible? (1/2) "))
    while to_scrape != "1" and to_scrape != "2":
        play_again = input(str("The answer is not valid. Please type '1' or '2':"))
    print()
    play_game(to_scrape)
