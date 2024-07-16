import os
import json
import requests
from bs4 import BeautifulSoup

URL = "https://nostarch.com/catalog/programming"

def startScraper():
    book_data = []
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    element = soup.findAll("div", {'class': "col-xs-6 col-sm-6 col-md-6 col-lg-6 with-padding-bottom nostrach-views-row"})
    for div in list(element):
        link = div.findChild('h2').findChild('a')['href']
        name = div.findChild('h2').findChild('a').text
        author = div.findChild('div', {'class': "field field-name-field-author field-type-text field-label-hidden"}).findChild('div', {'class':"field-item even"}).text

        data = {}
        data['link'] = "https://nostarch.com/" + link
        data['name'] = name
        data['author'] = author

        book_data.append(data)

    with open('scraper_results.json', 'w') as f:
        json_str = json.dumps(book_data)
        f.write(json_str)

startScraper()