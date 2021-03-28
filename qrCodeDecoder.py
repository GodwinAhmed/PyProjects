from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/gahmed/pictures/myqrcode.png')

result = decode(img)

print(result)