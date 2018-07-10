import requests
from bs4 import BeautifulSoup
import sys
url = 'https://www.python.org/'

page = requests.get(url).text

soup = BeautifulSoup(page, "html.parser")

print(soup.find("div", {'class':'medium-widget event-widget last'}).text)

