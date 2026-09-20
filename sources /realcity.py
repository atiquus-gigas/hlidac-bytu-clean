# sources/realcity.py
from bs4 import BeautifulSoup
import re

def fetch(scraper):
    url = "https://www.realcity.cz/nemovitosti/pronajem-bytu/praha"
    html = scraper.get(url)
    soup = BeautifulSoup(html, "html.parser")

    offers = []

    items = soup.select("div.property")
    for item in items:
        try:
            titulek = item.select_one("h2").get_text(strip=True)
            cena = item.select_one(".price").get_text(strip=True)
            lokalita = item.select_one(".location").get_text(strip=True)
            odkaz = item.select_one("a")["href"]

            eid = "realcity_" + re.sub(r"\D", "", odkaz)

            offers.append({
                "portal": "RealCity",
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
