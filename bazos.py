import cloudscraper
from bs4 import BeautifulSoup

URL = "https://reality.bazos.cz/pronajem/"

def fetch():
    scraper = cloudscraper.create_scraper()
    results = []

    try:
        r = scraper.get(URL, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        for item in soup.select(".inzeraty .inzeratynadpis"):
            title = item.get_text(strip=True)
            link = item.get("href")

            price_el = item.find_next("span", class_="cena")
            price = price_el.get_text(strip=True) if price_el else ""

            location_el = item.find_next("span", class_="velikost")
            location = location_el.get_text(strip=True) if location_el else ""

            results.append({
                "title": title,
                "price": price,
                "location": location,
                "url": "https://reality.bazos.cz" + link if link else ""
            })

        return results

    except Exception as e:
        print(f"[bazos] Chyba: {e}")
        return []

