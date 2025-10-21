import requests
from bs4 import BeautifulSoup
url="https://holamundo.day/"
response = requests.get(url)
#print(response.json)

soup= BeautifulSoup(response.text , 'html.parser')
quotes = []
quotex_boxes= soup.find_all('strong', class_='rt-Strong css-ksqtdq')
for quotes in quotex_boxes[4]:
    print(quotes)