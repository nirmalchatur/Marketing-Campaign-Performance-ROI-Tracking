# webapp/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    """
    Scrape headlines from a given URL.
    Adjust selectors as per the target site structure.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Example: scrape all <h2> elements
        headlines = [h.get_text(strip=True) for h in soup.find_all("h2")]

        return headlines

    except Exception as e:
        return f"Scraping error: {e}"
