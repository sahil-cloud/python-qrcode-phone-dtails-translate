import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# data to display after scanning of the qrcode
data = "Hello,I am sahil \nwww.idhrudhr.tk"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color= 'white')
img.save('qrcode.png')