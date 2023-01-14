import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.cnn.com/')

soup = BeautifulSoup(req.content, "html.parser")

print(soup.get_text())