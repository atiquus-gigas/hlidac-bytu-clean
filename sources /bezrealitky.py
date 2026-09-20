# sources/bezrealitky.py
from bs4 import BeautifulSoup
import re

def fetch(scraper):
    url = "https://www.bezrealitky.cz/vypis/nabidka-pronajem/byt/praha"
    html = scraper.get(url)
    soup = BeautifulSoup(html, "html.parser")

    offers = []

    items = soup.select("div.property")
    for item in items:
        try:
            titulek = item.select_one("h2").get_text(strip=True)
            cena = item.select_one(".price").get_text(strip=True)
            lokalita = item.select_one(".location").get_text(strip=True)
            odkaz = "https://www.bezrealitky.cz" + item.select_one("a")["href"]

            eid = "bezrealitky_" + re.sub(r"\D", "", odkaz)

            offers.append({
                "portal": "Bezrealitky",
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
