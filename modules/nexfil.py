import os

def run():
    os.system("clear")
    print("=== HackCrist Nexfil ===")
    if not os.path.exists("tools/nexfil"):
        os.system("mkdir -p tools && cd tools && git clone https://github.com/thewhiteh4t/nexfil && cd nexfil && pip install -r requirements.txt")
    user = input("🔎 Ingresa nombre de usuario: ")
    os.system(f"cd tools/nexfil && python3 nexfil.py -u {user}")
