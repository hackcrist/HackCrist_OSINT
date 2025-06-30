import os

def run():
    os.system("clear")
    print("=== HackCrist PhoneInfoga ===")
    if not os.path.exists("tools/PhoneInfoga"):
        os.system("mkdir -p tools && cd tools && git clone https://github.com/sundowndev/phoneinfoga && cd phoneinfoga")
    number = input("📞 Ingresa número: ")
    os.system(f"cd tools/phoneinfoga && python3 phoneinfoga.py scan -n {number}")
