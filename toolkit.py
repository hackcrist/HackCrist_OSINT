#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HackCrist OSINT Toolkit
# Basado en Doxxer-Toolkit de Euronymou5
# Adaptado y mantenido por HackCrist
# Licencia: MPL-2.0 + Apache 2.0

import os
import time

class Colores:
    red = "\033[31;1m"
    verde = "\033[92m"
    azul = "\033[94m"
    magenta = "\033[36m"
    amarillo = "\033[33m"

logo = Colores.red + '''
██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗ ██╗███████╗████████╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔═══██╗██╔══██╗██║██╔════╝╚══██╔══╝
██║  ██║███████║██║     █████╔╝ ██║   ██║██████╔╝██║███████╗   ██║   
██║  ██║██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ ██║╚════██║   ██║   
██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     ██║███████║   ██║   
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   
                   HackCrist OSINT Toolkit v2.6
'''

def menu():
    os.system("clear")
    print(logo)
    print(Colores.azul + '''
    [1] Sherlock / Nexfil
    [2] GeoIP
    [3] Phoneinfoga
    [4] Generar QR
    [5] Acortar Link
    [6] OSINT Links
    [99] Salir
    ''' )

    op = input('HackCrist > ')
    if op == '1':
        print('Aquí va el módulo Sherlock...')
    elif op == '2':
        print('Aquí va GeoIP...')
    elif op == '3':
        print('Aquí va Phoneinfoga...')
    elif op == '4':
        print('Aquí va QR...')
    elif op == '5':
        print('Aquí va Shorteners...')
    elif op == '6':
        print('Aquí van los links OSINT...')
    elif op == '99':
        exit()
    else:
        print('Opción inválida.')
        time.sleep(2)
        menu()

if __name__ == '__main__':
    menu()
