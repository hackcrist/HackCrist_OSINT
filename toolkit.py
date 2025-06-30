#!/usr/bin/env python3
# HackCrist OSINT Toolkit

import os
import modules.sherlock as sherlock
import modules.nexfil as nexfil
import modules.geoip as geoip
import modules.phoneinfoga as phoneinfoga
import modules.qrcodegen as qrcodegen
import modules.shortener as shortener

def banner():
    return """
██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗ ██╗███████╗████████╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔═══██╗██╔══██╗██║██╔════╝╚══██╔══╝
██║  ██║███████║██║     █████╔╝ ██║   ██║██████╔╝██║███████╗   ██║   
██║  ██║██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ ██║╚════██║   ██║   
██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     ██║███████║   ██║   
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   
               HackCrist OSINT Toolkit
"""

def menu():
    os.system("clear")
    print(banner())
    print("""
[1] Sherlock
[2] Nexfil
[3] GeoIP
[4] PhoneInfoga
[5] QR Generator
[6] Shortener
[99] Salir
""")
    op = input("> ")
    if op == '1':
        sherlock.run()
    elif op == '2':
        nexfil.run()
    elif op == '3':
        geoip.run()
    elif op == '4':
        phoneinfoga.run()
    elif op == '5':
        qrcodegen.run()
    elif op == '6':
        shortener.run()
    elif op == '99':
        exit()
    else:
        print("Opción inválida")
    input("Pulsa enter para volver...")
    menu()

if __name__ == '__main__':
    menu()
