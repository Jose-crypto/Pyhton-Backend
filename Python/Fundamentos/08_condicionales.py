import requests
from bs4 import BeautifulSoup
response = requests.get(url="https://holamun7do.day/")



try:
    soup= BeautifulSoup(response.text , 'html.parser')
    print(soup)
except:
     print("An exception occurred")
     raise f"Error : {response.status_code}"