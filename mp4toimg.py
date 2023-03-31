from PIL import Image
import cv2
import os

def image_to_binary(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    binary_str = ""
    for y in range(height-1):
        for x in range(width):
            r, g, b = pixels[x, y]
            if r<128 and g<128 and b<128 :
                binary_str += "1"
            elif r>128 and g>128 and b>128:
                binary_str += "0"
            else:
                continue
    return binary_str

def binary_string_to_file(binary_string, file_path):
    with open(file_path, 'wb') as file:
        bytes_list = [int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8)]
        bytes_arr = bytearray(bytes_list)
        file.write(bytes_arr)

def capture_frame(filePath):
    cam = cv2.VideoCapture(filePath)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')
    currentframe = 0
    while (True):
        ret, img = cam.read()
        if ret:
            name = './data/binary_image_' + str(currentframe) + '.png'
            print('Creating...' + name)
            cv2.imwrite(name, img)
            currentframe += 1
        # else:
            break
    cam.release()
    cv2.destroyAllWindows()
def remove_img(path):
    try:
        os.remove(path)
    except NameError:
        print("No image found")



filePath = "test/word.docx.mp4"
fileName = filePath.split('.')

capture_frame(filePath)

#convert image to binary
binary_strings = []
#counting number of files in directory
directory="data"
onlyfiles = next(os.walk(directory))[2] #directory is your directory path as string

number_of_images = len(onlyfiles)
for i in range(len(onlyfiles)):
    image_path = f"data/binary_image_{i}.png"
    binary_strings.append(image_to_binary(image_path))
    #remove_img(f"data/binary_image_{i}.png")
original_binary_str = "".join(binary_strings)

with open('binary/retrived-binary.txt', 'w') as f:
    f.write(original_binary_str)
#
with open('binary/retrived-binary.txt') as f:
    retrived_string = f.read()

binary_string_to_file(retrived_string, fileName[0]+'-copy.'+fileName[1])
