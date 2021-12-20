#!/bin/bash

# By SkylineIsBack

echo "Starting installation"
echo""
sudo apt install python-tk
sudo apt install python3-tk
sudo mv smaker.py /usr/bin/
sudo chmod +x /usr/bin/smaker.py
sudo mv shortcuticon.png /usr/share/icons/
cd /usr/share/applications/
sudo echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Shortcut Maker
Comment=Create shortcuts with ease
Exec=python3 /usr/bin/smaker.py
Icon=shortcuticon.png
Terminal=false" >> smaker.desktop
sudo chmod +x smaker.desktop
echo ""
echo "Installation successfull"