# sources/sreality.py
import json

def fetch(scraper):
    url = (
        "https://www.sreality.cz/api/cs/v2/estates?"
        "category_main_cb=1&category_type_cb=1&per_page=50"
    )

    try:
        raw = scraper.get(url)
        data = json.loads(raw)
    except Exception as e:
        print("Sreality API error:", e)
        return []

    estates = data.get("_embedded", {}).get("estates", [])
    offers = []

    for est in estates:
        eid = f"sreality_{est.get('hash_id')}"
        titulek = est.get("name", "")
        cena = est.get("price", "")
        lokalita = est.get("locality", "")
        odkaz = f"https://www.sreality.cz/detail/{est.get('hash_id')}"

        # patro + výtah
        detail = est.get("_embedded", {}).get("detail", {})
        patro = detail.get("floor", "")
        vytah = detail.get("lift", False)

        offers.append({
            "portal": "Sreality",
            "eid": eid,
            "titulek": titulek,
            "cena": cena,
            "lokalita": lokalita,
            "patro": patro,
            "vytah": vytah,
            "odkaz": odkaz,
        })

    return offers
