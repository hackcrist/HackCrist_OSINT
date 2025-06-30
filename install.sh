#!/bin/bash
# HackCrist OSINT Toolkit — Instalador oficial
# Basado en Doxxer-Toolkit de Euronymou5 — MPL-2.0 + Apache 2.0
# Autor: HackCrist

clear
echo "======================================="
echo "  🚀 Instalador HackCrist OSINT Toolkit"
echo "======================================="

echo "[+] Actualizando paquetes..."
pkg update -y && pkg upgrade -y

echo "[+] Instalando dependencias..."
pkg install python -y
pkg install git -y
pkg install xdg-utils -y

echo "[+] Clonando repositorio..."
git clone https://github.com/hackcrist/OSINT-Toolkit.git
cd OSINT-Toolkit

echo "[+] Dando permisos..."
chmod +x toolkit.py

echo ""
echo "✅ Instalación lista. Ejecuta:"
echo "python3 toolkit.py"
