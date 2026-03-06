import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")

for book in books:
    title = book.find("a")["title"]
    print(title)