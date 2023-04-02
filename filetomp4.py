import subprocess
import os
import glob
from PIL import Image

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
    img_width = 480
    img_height = 360
    size = img_width * img_height
    index = 0
    count = 0

    while index < len(binary_str):
        image = Image.new("1", (img_width, img_height), color=1)
        val = bin(count)[2:].zfill(160)
        for u in range(len(val)):
            if val[u] == "1":
                for i in range(3):
                    for j in range(3):
                        image.putpixel((3 * u + j, i), 0)

            else:
                for i in range(3):
                    for j in range(3):
                        image.putpixel((3 * u + j, i), 1)

        for y in range(6, img_height,6):
            for x in range(0, img_width,6):
                if index < len(binary_str):
                    if binary_str[index] == "1":
                        for i in range(3):
                            for j in range(3):
                                image.putpixel((x + j, y + i), 0)
                    else:
                        for i in range(3):
                            for j in range(3):
                                image.putpixel((x + j, y + i), 1)
                else:
                    for i in range(3):
                        for j in range(3):
                            image.putpixel((x + j, y + i), 0)
                index += 1

        image.save(f"images/binary_image_{count}.png")
        count += 1


def remove_img(path):
    try:
        os.remove(path)
    except NameError:
        print("No image found")


def images_to_video(video_filename):
    # Set input and output file paths relative to script directory
    input_path = "images/*.png"
    output_path =video_filename

    # Get a list of image files
    image_files = glob.glob(input_path)
    print(image_files)
    # Set video parameters
    fps = 30
    video_codec = "libx264"
    crf = 30

    # Run ffmpeg command to make video

    cmd = ["ffmpeg", "-y", "-framerate", str(fps), "-i" ,"images/binary_image_%d.png", "-codec:v", video_codec, "-r", str(crf),output_path]
    subprocess.call(cmd)

#taking the input
file_path="test/test_pdf.zip"


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
video_name = fileName[0]+'.'+fileName[1]+'.'+str(len(new_binary))+'.mp4'

images_to_video(video_name)

#deleting images
directory="images"
onlyfiles = next(os.walk(directory))[2]

number_of_images = len(onlyfiles)
for i in range(len(onlyfiles)):
    remove_img(f"images/binary_image_{i}.png")
