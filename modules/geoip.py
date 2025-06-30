import requests

def run():
    print("=== HackCrist GeoIP ===")
    ip = input("🌐 Ingresa IP objetivo: ")
    url = f"https://ipinfo.io/{ip}/json"
    try:
        r = requests.get(url)
        print(r.text)
    except:
        print("❌ Error al consultar API.")
