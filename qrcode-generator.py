# Program in Python3 to generate a QR Code and encode the user given data onto it.

import qrcode
from datetime import datetime

data = str(input("Enter data/link to be encoded to the QR code: "))

# Encoding the data using make() function of the qrcode library
img = qrcode.make(data)

# Logic for filename
now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S")
filename = "myQR_" + dt_string + ".png"

# Saving the QR Code as an image file
img.save(filename)
print("\n"+filename+" saved succesfully!")
