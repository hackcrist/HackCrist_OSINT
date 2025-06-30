import os

def run():
    os.system("clear")
    print("=== HackCrist Sherlock ===")
    if not os.path.exists("tools/sherlock"):
        os.system("mkdir -p tools && cd tools && git clone https://github.com/sherlock-project/sherlock && cd sherlock && pip install -r requirements.txt")
    user = input("🔎 Ingresa nombre de usuario: ")
    os.system(f"cd tools/sherlock && python3 sherlock.py {user}")
