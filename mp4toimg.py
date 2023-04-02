from PIL import Image
import os
import subprocess

def image_to_binary(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    binary_str = ""
    index=0
    for x in range(width//3):
        r,g,b=0,0,0
        for i in range(3):
            for j in range(3):
                r1,g1,b1 = pixels[3*x+j,i]
                r+=r1
                g+=g1
                b+=b1

        if r < 200 and g < 200 and b < 200:
            binary_str += "1"
        elif r > 200 and g > 200 and b > 200:
            binary_str += "0"
        else:
            continue
    for y in range(6,height,6):
        for x in range(0,width,6):
            index += 1
            r, g, b =pixels[x,y]
            if r<200 and g<200 and b<200:
                binary_str += "1"
            elif r>200 and g>200 and b>200:
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
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    print("here")
    # Path to output image frames
    output_frames = "data/binary_image_%d.png"

    # Command to extract frames using ffmpeg
    command = ["ffmpeg", "-i", filePath, "-vf", "fps=1", output_frames]

    # Execute the command using subprocess
    subprocess.call(command)


def remove_img(path):
    try:
        os.remove(path)
    except NameError:
        print("No image found")



filePath = "test/test_pdf.zip.17249216.mp4"
fileName = filePath.split('.')

capture_frame(filePath)

#convert image to binary
hm={}
#counting number of files in directory
directory="data"
onlyfiles = next(os.walk(directory))[2] #directory is your directory path as string
binary_from_image=""
number_of_images = len(onlyfiles)
for i in range(len(onlyfiles)):
    image_path = f"data/binary_image_{i+1}.png"
    binary_from_image=image_to_binary(image_path)
    if int(binary_from_image[:160],2) not in hm:
        hm[int(binary_from_image[:160],2)]=binary_from_image[160:]
    remove_img(f"data/binary_image_{i}.png")

sorted_keys = sorted(hm.keys())
sorted_dict = {key:hm[key] for key in sorted_keys}

original_binary_str=""
for k,v in sorted_dict.items():
    print(k)
    original_binary_str+=v
original_binary_str=original_binary_str[:int(fileName[2])]
with open('binary/retrived-binary.txt', 'w') as f:
    f.write(original_binary_str)
#
with open('binary/retrived-binary.txt') as f:
    retrived_string = f.read()

binary_string_to_file(retrived_string, fileName[0]+'-copy.'+fileName[1])
