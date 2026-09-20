# sources/bazos.py
from bs4 import BeautifulSoup
import re

def fetch(scraper):
    url = "https://reality.bazos.cz/pronajem/?hledat=praha"
    html = scraper.get(url)
    soup = BeautifulSoup(html, "html.parser")

    offers = []

    items = soup.select("div.inzeraty > div.inzerat")
    for item in items:
        try:
            titulek = item.select_one("h2").get_text(strip=True)
            cena = item.select_one(".inzeratcena").get_text(strip=True)
            lokalita = item.select_one(".inzerattext").get_text(strip=True)
            odkaz = item.select_one("a")["href"]

            eid = "bazos_" + re.sub(r"\D", "", odkaz)

            offers.append({
                "portal": "Bazos",
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
