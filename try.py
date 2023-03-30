from PIL import Image

import binascii

# read the file in binary mode
with open('pika.txt', 'rb') as file:
    binary_data = file.read()

# convert binary data to binary format
binary_string = binascii.b2a_base64(binary_data)

width=1920
height=1080
# create an image from binary data
image = Image.frombytes('RGB', (width, height), binary_data)

# save the image as a PNG file
image.save('image.png')