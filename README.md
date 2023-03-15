Quote Scraper
This is a simple Python program that scrapes quotes from a website and stores them in a list of dictionaries. Each dictionary contains the quote text, the name of the person who said the quote, and the href of the link to the person's bio.

Requirements
To run this program, you'll need:

Python 3.x
requests library
beautifulsoup4 library
pytest library (for running tests)
You can install these libraries using pip by running:

shell
Copy code
pip install requests beautifulsoup4 pytest
Usage
To use this program, simply run the main.py file using Python:

shell
Copy code
python main.py
The program will ask you if you want to scrape the website or read saved quotes. Enter 1 to scrape the website or 2 to read saved quotes. If you choose to scrape the website, the program will scrape quotes from the website and store them in a file called quotes.json.

Tests
To run the tests, simply run the pytest command:

shell
Copy code
pytest
This will run all the test cases in the tests directory.

Contributing
If you find a bug or have a feature request, please open an issue in the GitHub repository. If you want to contribute to the project, feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
