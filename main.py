import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://www.youtube.com/c/garyvee/videos")
#print(r.content)

soup = bs(r.content, features="html5lib")

headers = soup.find_all("yt-formatted-string")
print(headers)

# paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# print(paragraph)

# body = soup.find('body')
# div = body.find('div')
# page = div.find('ytd-page-manager')
# header = div.find('h3')
# # title = header.find('a', attrs={"id": "video-title"})
# print(header)

#Pretty prints out our html
#print(soup.prettify())
