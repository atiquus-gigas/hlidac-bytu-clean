# sources/realingo.py
import json

def fetch(scraper):
    url = "https://www.realingo.cz/api/v1/listings?city=praha&type=rent"
    raw = scraper.get(url)

    try:
        data = json.loads(raw)
    except:
        return []

    offers = []

    for item in data.get("listings", []):
        eid = f"realingo_{item.get('id')}"
        titulek = item.get("title", "")
        cena = item.get("price", "")
        lokalita = item.get("locality", "")
        odkaz = f"https://www.realingo.cz/detail/{item.get('id')}"

        offers.append({
            "portal": "Realingo",
            "eid": eid,
            "titulek": titulek,
            "cena": cena,
            "lokalita": lokalita,
            "patro": "",
            "vytah": False,
            "odkaz": odkaz,
        })

    return offers
