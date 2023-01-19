#!/bin/bash

echo "Enter filepath of makeexe folder:"
read fp
cd fp
pyinstaller --onefile decryptitgame.py
mv dist/decryptitgame .
rm -R dist build decryptitgame.spec
