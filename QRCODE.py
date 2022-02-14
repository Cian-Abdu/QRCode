#Generate QR CODE

import pyqrcode
import png

site = "https://www.linkedin.com/in/hendel-naka/"

url = pyqrcode.create(site)

url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)

