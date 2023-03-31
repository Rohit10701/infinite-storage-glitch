# Importing library
import qrcode
# Data to be encoded
def file_to_binary_string(file_path):
    with open(file_path, 'rb') as file:
        binary_code = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_code)
    return binary_string

file_path="test/test_paper.pdf"
#spliting thr name
fileName = file_path.split(".")
binary_string = file_to_binary_string(file_path)

data = "1"+binary_string[:5000]

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')
