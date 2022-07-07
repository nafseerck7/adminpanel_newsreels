#converting the page to html
from distutils import text_file
import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
r = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')

print(soup.prettify())

data = soup.prettify()
text_file = open("static/convertedhtml/convertedpage.html", "w", encoding="utf-8")
n = text_file.write(data)
text_file.close()