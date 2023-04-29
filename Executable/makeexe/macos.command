#!/bin/bash

echo "Enter filepath of tomake:"
read fp
cd $fp
pyinstaller --onefile decrypt-it.py
mv dist/decrypt-it .
rm -R dist build decrypt-it.spec
