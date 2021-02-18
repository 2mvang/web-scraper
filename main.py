import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://champagneproxy.github.io/webscraping/example.html")
#print(r.content)

soup = bs(r.content, features="html5lib")

first_header = soup.find_all("h2")
print(first_header)

#Pretty prints out our html
#print(soup.prettify())
