import requests
import re
from bs4 import BeautifulSoup as bs

# Load the webpage content
r = requests.get("https://champagneproxy.github.io/webscraping/example2.html")

# Convert to a beautiful soup object
soup = bs(r.content, features="html5lib")

# Pretty prints out our html
# print(soup.prettify())

#METHOD 1
# list = soup.find('ul', attrs={"class": "socials"})
# instagram = list.find('li', attrs={"class": "social instagram"})
# instagram_link = instagram.find('a')
# twitter = list.find('li', attrs={"class": "social twitter"})
# twitter_link = twitter.find('a')
# linkedin = list.find('li', attrs={"class": "social linkedin"})
# linkedin_link = linkedin.find('a')
# tiktok = list.find('li', attrs={"class": "social tiktok"})
# tiktok_link = tiktok.find('a')
# print(instagram_link['href'])
# print(twitter_link['href'])
# print(linkedin_link['href'])
# print(tiktok_link['href'])

#METHOD 2

# links = soup.select("ul > li")
#
# for link in links:
#     print(link.select("a"))

#METHOD 3

instagram = soup.select("li")
ig_link = instagram.select("a")
print(ig_link['href'])
