import cloudscraper
from bs4 import BeautifulSoup

URL = "https://www.bezrealitky.cz/vypis/nabidka-pronajem-byt"

def fetch():
    scraper = cloudscraper.create_scraper()
    results = []

    try:
        r = scraper.get(URL, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        for item in soup.select(".product"):
            title = item.select_one(".product__title")
            price = item.select_one(".product__price")
            locality = item.select_one(".product__location")
            link = item.select_one("a")

            results.append({
                "title": title.get_text(strip=True) if title else "",
                "price": price.get_text(strip=True) if price else "",
                "location": locality.get_text(strip=True) if locality else "",
                "url": "https://www.bezrealitky.cz" + link["href"] if link else ""
            })

        return results

    except Exception as e:
        print(f"[bezrealitky] Chyba: {e}")
        return []
