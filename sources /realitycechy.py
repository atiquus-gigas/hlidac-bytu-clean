# sources/realitycechy.py
from bs4 import BeautifulSoup
import re

def fetch(scraper):
    url = "https://www.realitycechy.cz/pronajem-bytu/praha"
    html = scraper.get(url)
    soup = BeautifulSoup(html, "html.parser")

    offers = []

    items = soup.select("div.offer")
    for item in items:
        try:
            titulek = item.select_one("h2").get_text(strip=True)
            cena = item.select_one(".price").get_text(strip=True)
            lokalita = item.select_one(".location").get_text(strip=True)
            odkaz = item.select_one("a")["href"]

            eid = "realitycechy_" + re.sub(r"\D", "", odkaz)

            offers.append({
                "portal": "RealityČechy",
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
