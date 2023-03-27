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


def binary_to_image(binary_str):
    img_width = 1920
    img_height = 1080
    size = img_width * img_height

    num_images = (len(binary_str) // (size)) + 1
    for i in range(num_images):
        image = Image.new("RGB", (img_width, img_height), (0, 255, 0))
        index=0
        for y in range(img_height):
            for x in range(img_width):
                if index < len(binary_str):
                    if binary_str[index] == "1":
                        image.putpixel((x, y), (0, 0, 0))

                    else:
                        image.putpixel((x, y), (255, 255, 255))
                else:
                    break
                index+=1
            index+=1
        print(len())
        binary_str=binary_str[index:]
        image.save(f"binary_image_{i}.png")


def image_to_binary(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    binary_str = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if (r, g, b) == (0, 0, 0):
                binary_str += "1"
            elif (r, g, b) == (255, 255, 255):
                binary_str += "0"

    return binary_str

file_path="test_paper.pdf"

fileName = file_path.split(".")
binary_string = file_to_binary_string(file_path)

#saving original binary
with open('binary.txt', 'w') as f:
    f.write(binary_string)

with open('binary.txt') as f:
    new_binary = f.read()
binary_to_image(new_binary)


binary_strings = []
for i in range(12):
    image_path = f"binary_image_{i}.png"
    binary_strings.append(image_to_binary(image_path))
original_binary_str = "".join(binary_strings)

if binary_strings==original_binary_str:
    print("True")

with open('retrived-binary.txt', 'w') as f:
    f.write(original_binary_str)
#
with open('retrived-binary.txt') as f:
    retrived_string = f.read()
binary_string_to_file(binary_string, 'try1.pdf')
