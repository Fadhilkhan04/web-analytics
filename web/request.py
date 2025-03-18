#using request module

import requests


r = requests.get('https://github.com/fadhilkhan04')


print(r)

print(r.content)