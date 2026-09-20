# sources/realitymix.py
from bs4 import BeautifulSoup
import re

def fetch(scraper):
    url = "https://www.realitymix.cz/vypis/pronajem-bytu/praha.html"
    html = scraper.get(url)
    soup = BeautifulSoup(html, "html.parser")

    offers = []

    items = soup.select("div.rm-property")
    for item in items:
        try:
            titulek = item.select_one("h2").get_text(strip=True)
            cena = item.select_one(".rm-price").get_text(strip=True)
            lokalita = item.select_one(".rm-location").get_text(strip=True)
            odkaz = item.select_one("a")["href"]

            eid = "realitymix_" + re.sub(r"\D", "", odkaz)

            offers.append({
                "portal": "RealityMix",
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
