import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://champagneproxy.github.io/webscraping/example.html")
#print(r.content)

soup = bs(r.content, features="html5lib")

headers = soup.find_all(["h1", "h2"])
print(headers)

#Pretty prints out our html
#print(soup.prettify())
