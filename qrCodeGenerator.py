import qrcode

data = 'Dont\'t forget to subscribe'

qr = qrcode.QRCode(version =1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img =qr.make_image(fill_color = 'red', back_color ='white')

img.save('C:/Users/gahmed/pictures/myqrcode.png')