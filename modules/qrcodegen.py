import pyqrcode

def run():
    print("=== HackCrist QR Generator ===")
    text = input("Texto o URL: ")
    name = input("Nombre archivo PNG: ")
    qr = pyqrcode.create(text)
    qr.png(f"{name}.png", scale=6)
    print(f"✅ QR guardado como {name}.png")
