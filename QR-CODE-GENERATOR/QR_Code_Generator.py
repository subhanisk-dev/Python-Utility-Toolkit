import qrcode
 
data = input("Enter the text/URL to convert into a QR code: ")
file_name = input("Enter output file name (example: myqr): ")+".png"

# version = size of the QR (1 to 40), box_size = pixels per box, border = margin
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)

qr.add_data(data)
qr.make(fit=True)
 
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)
 
print("QR code created successfully.")
print("Saved as :", file_name)
