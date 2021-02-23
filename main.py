import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://champagneproxy.github.io/webscraping/example.html")
#print(r.content)

soup = bs(r.content, features="html5lib")

# HTML SELECTION

# headers = soup.find_all(["h1","h2"])
# print(headers)

# paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# print(paragraph)

# body = soup.find('body')
# div = body.find('div')
# header = div.find('h1')
# print(header)

# bolded_paragraphs = soup.find_all("p", string=re.compile("bolded"))
# print(bolded_paragraphs)

# headers = soup.find_all("h2", string=re.compile("Header"))
# print(headers)

# headers_re = soup.find_all("h2", string=re.compile("(H|h)eader"))
# print(headers_re)

# CSS SELECTION

# content = soup.select("p")
# print(content)

# content = soup.select("div p")
# print(content)

# content = soup.select("body ~ p") # what does the ~ do?
# print(content)

# paragraphs = soup.select("body > p")
#
# for paragraph in paragraphs:
#     print(paragraph.select("i")) # only prints out the italisized stuff

# centered_stuff = soup.select("[align=middle]")
# print(centered_stuff)

# header = soup.find("h2")
# print(header)
# print(header.string) #pulls text only, no tags

# div = soup.find("div")
# print(div.get_text()) # prints all text in div

# link = soup.find("a")
# print(link['href'])

print(soup.body.div.h1.string) #print the string in the h1 located in the div which is located in thet

#Pretty prints out our html
#print(soup.prettify())
