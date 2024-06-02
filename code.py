import requests
from bs4 import BeautifulSoup

# Replace with the actual URL of the page you want to scrape
url = "https://en.wikipedia.org/wiki/Data_extraction"

# Send a request to fetch the page content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the title (assuming it's in an <h1> tag)
title = soup.find('h1')

# Locate the div with the class "td-post-content tagdiv-type"
article = soup.find('div', class_='mw-content-ltr mw-parser-output')

# Extract and print the title
if title:
    article_title = title.get_text(separator=' ', strip=True)
    print("Title:", article_title)
else:
    print("Title not found")

# Extract and print the article content
if article:
    article_text = article.get_text(separator=' ', strip=True)
    print("Content:", article_text)
else:
    print("Article content not found")
