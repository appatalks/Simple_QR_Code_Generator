import qrcode
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import datetime
import random

# Create a QApplication (needed for a QLabel)
app = QApplication([])

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Ask the user for the data to add to the QR code
data = input("Enter the data you want to add to the QR code: ")
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Get current date
now = datetime.datetime.now()

# Format the date to include it in the file name
date_string = now.strftime("%Y-%m-%d")

# Generate a random 5 digit string
random_string = str(random.randint(10000, 99999))

# Save the image to a file in the ~/Downloads/ directory with date and random string in the filename
img.save(os.path.expanduser(f"~/Downloads/qr_code_{date_string}_{random_string}.png"))

# Create a QLabel to display the image
label = QLabel()

# Get the full path of the file
full_path = os.path.expanduser(f"~/Downloads/qr_code_{date_string}_{random_string}.png")
label.setPixmap(QPixmap(full_path))

# Create a QWidget
widget = QWidget()

# Set the window title
widget.setWindowTitle(data)

# Create a layout
layout = QVBoxLayout()
layout.addWidget(label)
widget.setLayout(layout)

# Show the QWidget
widget.show()

# Run the QApplication
app.exec_()
