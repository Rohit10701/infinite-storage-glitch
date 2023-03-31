from PIL import Image
import cv2
import os
import math
def file_to_binary_string(file_path):
    with open(file_path, 'rb') as file:
        binary_code = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_code)
    return binary_string

def binary_string_to_file(binary_string, file_path):
    with open(file_path, 'wb') as file:
        bytes_list = [int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8)]
        bytes_arr = bytearray(bytes_list)
        file.write(bytes_arr)

#binary_str = 1000 1010 1111 0000 1111
def binary_to_image(binary_str):
    img_width = int(math.sqrt(len(binary_str)))+2
    img_height= int(math.sqrt(len(binary_str)))+1
    size = (img_width)* (img_height)
    index = 0
    num_images = (len(binary_str) // (size)) + 1
    for i in range(num_images):
        image = Image.new("RGB", (img_width, img_height), (255, 0, 0))
        for y in range(img_height): #0
            for x in range(img_width): #0
                if index < len(binary_str):
                    if binary_str[index] == "1":
                        image.putpixel((x, y), (0, 0, 0))
                    else:
                        image.putpixel((x, y), (255, 255, 255))
                else:
                    image.putpixel((x, y), (255, 0, 0))
                index+=1
        image.save(f"images/binary_image_{i}.png")

def remove_img(path):
    try:
        os.remove(path)
    except NameError:
        print("No image found")


#taking the input
file_path="test/test_paper.pdf"


#spliting thr name
fileName = file_path.split(".")
binary_string = file_to_binary_string(file_path)

print(len(binary_string))
#logging original binary
with open('binary/binary.txt', 'w') as f:
    f.write(binary_string)

#reading form log
with open('binary/binary.txt') as f:
    new_binary = f.read()


#converting binary to image
binary_to_image(new_binary)

#making video

image_folder = 'images'
video_name = fileName[0]+'.'+fileName[1]+'.mp4'

import glob

img_width = int(math.sqrt(len(binary_string)))+2
img_height= int(math.sqrt(len(binary_string)))+1
frameSize = (img_width,img_height)


out = cv2.VideoWriter(video_name,0, 1, frameSize)

for filename in glob.glob('images/*.png'):
    img = cv2.imread(filename)
    out.write(img)

out.release()

#deleting images
# binary_strings = []
# directory="images"
# onlyfiles = next(os.walk(directory))[2]
#
# number_of_images = len(onlyfiles)
# for i in range(len(onlyfiles)):
#     remove_img(f"images/binary_image_{i}.png")
