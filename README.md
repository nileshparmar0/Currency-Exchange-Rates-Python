# Currency-Exchange-Rates-Python

Project Description:

This project is a web scraping tool designed to fetch and display currency exchange rates from the x-rates website. The script allows users to select a base currency and input an amount to convert, then retrieves the equivalent amounts in various other currencies based on the current exchange rates.

How the Project Works:
1. Fetch Homepage Content: The script begins by making an HTTP request to the x-rates homepage to fetch the HTML content.
2. Parse HTML Content: Using BeautifulSoup, the script parses the HTML content to find all available currency options on the page.
3. Display Currency Options: The script displays a list of available currencies along with their position numbers.
4. User Input: The user is prompted to enter the position number of their desired currency and the amount they wish to convert.
5. Fetch Conversion Table: The script constructs a URL for the currency conversion table based on the selected currency and amount, then fetches the HTML content of this page.
6. Parse Conversion Table: Using BeautifulSoup again, the script parses the conversion table to extract the equivalent amounts in various other currencies.
7. Display Results: The script displays the conversion results, showing the equivalent amounts in other currencies.

How to Run the Project:
1. Install Dependencies: Ensure you have Python installed, then install the required libraries using pip:
         pip install requests beautifulsoup4
2. Run the Script: Execute the script using Python:
         python currency_scraper.py

Example Usage:
1. The script displays a list of currencies:
    US Dollar (USD)
    Euro (EUR)
    British Pound (GBP)
...
2. User enters the position number of their desired currency:
   Enter your currency's position number: 1
3. User enters the amount to convert:
   Enter amount of US Dollars (if amount isn't integer, then write it with a dot, not comma):      100
4. The script displays the conversion results:
   For 100 US Dollars you'll get:
   85.000 Euros
   75.000 British Pounds

...


Author: Created by Nilesh Parmar For any questions or suggestions, feel free to contact me at https://www.linkedin.com/in/nilesh-parmar-/



