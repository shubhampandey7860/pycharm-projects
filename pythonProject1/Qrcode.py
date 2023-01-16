# Importing library
import qrcode

data = 'sp3336705-2@okaxis'
# create a instance of Qr
qr = qrcode.QRCode(version=2, box_size=10, border=5)
# Adding data to qr instance
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white', label='google')
img.save('UPI.png')
print(f'succesfully created qrcode')
