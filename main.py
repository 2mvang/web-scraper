import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://www.youtube.com/c/garyvee/videos")
#print(r.content)

soup = bs(r.content, features="html5lib")

#headers = soup.find_all(["h1", "h2"])
#print(headers)

paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)

#Pretty prints out our html
#print(soup.prettify())
