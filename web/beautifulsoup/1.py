import requests
from bs4 import BeautifulSoup


#get request from the website using url with request module
r = requests.get('https://github.com/fadhilkhan04')


print(r)


#parse the content using beautiful soup
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
