import qrcode
qr = qrcode.QRCode()

qr.add_data("https://github.com/Alosii/product/blob/master/static/product1.json")
qr.make(fit = True)

img = qr.make_image()
img.save("gitqr.png")