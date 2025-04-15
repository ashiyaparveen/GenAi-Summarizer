# tools/real_time_web.py

import requests
from bs4 import BeautifulSoup

def fetch_article_summary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = [p.text for p in soup.find_all('p')]
    content = " ".join(paragraphs[:10])  # Limit length
    return content
