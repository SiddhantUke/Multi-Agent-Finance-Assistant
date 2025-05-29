import requests
from bs4 import BeautifulSoup

def scrape_earnings_news():
    url = "https://www.reuters.com/markets/earnings/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.select("article h3 a")
    return [a.get_text() for a in articles[:5]]