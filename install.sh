#!/bin/bash
# HackCrist OSINT Toolkit Installer

clear
echo "🚀 Instalador HackCrist OSINT Toolkit"
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y
pip install requests pyqrcode pypng pyshorteners
echo "✅ Listo. Ejecuta: python3 toolkit.py"
