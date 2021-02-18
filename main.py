import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://champagneproxy.github.io/webscraping/example.html")
#print(r.content)

soup = bs(r.content, features="html5lib")

#Pretty prints out our html
print(soup.prettify())
