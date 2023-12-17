import os
import time
import pyqrcode
import png 
from pyqrcode import QRCode

# String which represent the QR code
s = input("Enter the site you want to generate QR code for: ")

# Ask for the name of the file
filename = input("Enter the name of the file: ")

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file
url.svg(f'{filename}.svg', scale = 8)

# Create and save the png file
url.png(f'{filename}.png', scale = 6)

# Delete the svg file
os.remove(f'{filename}.svg')

time.sleep(1)

print("QR code generated successfully!")