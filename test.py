import requests
from bs4 import BeautifulSoup

url = 'https://www.listafirme.ro/media-expres-srl-15052199/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('text-right').text
print(title)