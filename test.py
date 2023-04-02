from PIL import Image

img_width = 30
img_height = 30
size = img_width * img_height
index = 0
count = 1
image = Image.new("1", (img_width, img_height), color=0)
val = bin(count)[2:].zfill(10)
print(val)
pixels = image.load()
for u in range(len(val)):
    if val[u] == "1":
        print(pixels[u,0])
        for i in range(3):
            for j in range(3):
                image.putpixel((3*u + j, i), 0)

    else:
        for i in range(3):
            for j in range(3):
                image.putpixel((3*u + j, i), 1)

image.save(f"test.png")