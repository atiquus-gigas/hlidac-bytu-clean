# sources/idnes.py
from bs4 import BeautifulSoup
import re

def fetch(scraper):
    url = "https://reality.idnes.cz/nabidky/pronajem-bytu/praha"
    html = scraper.get(url)
    soup = BeautifulSoup(html, "html.parser")

    offers = []

    items = soup.select("div.b-product")
    for item in items:
        try:
            titulek = item.select_one("h3").get_text(strip=True)
            cena = item.select_one(".b-price").get_text(strip=True)
            lokalita = item.select_one(".b-location").get_text(strip=True)
            odkaz = item.select_one("a")["href"]

            eid = "idnes_" + re.sub(r"\D", "", odkaz)

            offers.append({
                "portal": "iDNES",
                "eid": eid,
                "titulek": titulek,
                "cena": cena,
                "lokalita": lokalita,
                "patro": "",
                "vytah": False,
                "odkaz": odkaz,
            })
        except:
            continue

    return offers
