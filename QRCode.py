import pyqrcode
from pyqrcode import QRCode

string = "https://www.linkedin.com/in/jangambheemeswarasastry/"

url = pyqrcode.create(string)

url.svg("qr.svg", scale=8)
