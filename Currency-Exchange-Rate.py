# Import necessary libraries
from bs4 import BeautifulSoup  # Library for parsing HTML and XML documents
import requests as req  # Library for making HTTP requests

# Initialize an empty list to store currency information
currencies = []

# Fetch the HTML content of the x-rates homepage
page = req.get('https://www.x-rates.com/').text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

# Find all 'option' elements on the page and exclude the last 11 elements (not needed)
options = soup.find_all('option')[:-11]

# Loop through each 'option' element
for option in options:
    # Extract the currency abbreviation (short) and full name
    currency_short = option.text[:(option.text.find(" "))]
    currency_name = option.text[(option.text.find(" ") + 3):]
    # Create a dictionary with the currency's short name and full name
    current_element = {'name': currency_name, 'short': currency_short}
    # Add the dictionary to the list of currencies
    currencies.append(current_element)
    # Print the currency's position, full name, and short name
    print('{}. {} ({})'.format(len(currencies), current_element['name'],
                               current_element['short']))

# Prompt the user to enter the position number of their desired currency
currency_index = int(input('Enter your currency\'s position number: ')) - 1
# Get the selected currency from the list
currency = currencies[currency_index]
# Prompt the user to enter the amount of the selected currency
amount = input(
    '\033cEnter amount of {}s (if amount isn\'t integer, then write it with a dot, not comma): '
    .format(currency['name'].lower()))

# Construct the URL for the currency conversion table using the selected currency and amount
currencies_table_url = 'https://www.x-rates.com/table/?from={}&amount={}'.format(
    currency['short'], amount)

# Fetch the HTML content of the currency conversion table page
currencies_table_page = req.get(currencies_table_url).text

# Parse the HTML content of the conversion table page using BeautifulSoup
soup = BeautifulSoup(currencies_table_page, 'html.parser')

# Find all rows in the conversion table (excluding the header row)
table_rows = soup.findChild('table', attrs={
    'class': 'tablesorter'
}).findChildren('tr')[1:]

# Clear the console and print the conversion information header
print('\033cFor {} {}s you\'ll get:'.format(amount, currency['name'].lower()))

# Loop through each row in the conversion table
for table_row in table_rows:
    # Extract the data from each cell in the row
    row_data = table_row.findChildren('td')
    # Create a dictionary with the target currency and the converted amount
    exchange_rate = {
        'currency': row_data[0].text,
        'amount': float(row_data[1].text)
    }
    # Print the converted amount and the target currency
    print('{:.3f} {}s'.format(exchange_rate['amount'],
                              exchange_rate['currency']))
