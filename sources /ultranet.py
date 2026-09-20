# sources/ultranet.py
import json

def fetch(scraper):
    url = "https://www.ulovdomov.cz/api/advertisements?category=1&city=praha"
    raw = scraper.get(url)

    try:
        data = json.loads(raw)
    except:
        return []

    offers = []

    for item in data.get("items", []):
        eid = f"ulovdomov_{item.get('id')}"
        titulek = item.get("title", "")
        cena = item.get("price", "")
        lokalita = item.get("locality", "")
        odkaz = f"https://www.ulovdomov.cz/inzerat/{item.get('id')}"

        offers.append({
            "portal": "UlovDomov",
            "eid": eid,
            "titulek": titulek,
            "cena": cena,
            "lokalita": lokalita,
            "patro": "",
            "vytah": False,
            "odkaz": odkaz,
        })

    return offers
