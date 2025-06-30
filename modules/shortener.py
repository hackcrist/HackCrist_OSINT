import pyshorteners

def run():
    print("=== HackCrist Shortener ===")
    url = input("Ingresa URL para acortar: ")
    s = pyshorteners.Shortener()
    short = s.tinyurl.short(url)
    print(f"🔗 Short: {short}")
