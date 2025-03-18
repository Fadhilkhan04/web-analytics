#using beautiful soup extract useful info
#finding elements by class

import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://github.com/fadhilkhan04')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='entry-content')
content = soup.find_all('h1')

print(content)
