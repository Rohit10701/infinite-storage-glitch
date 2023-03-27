import time

from PIL import  ImageGrab

x =-1

while True:
    try:
        x+= 1
        ImageGrab().grab().save(f'images/binary_image_{x}.png')
    except:
        movie = "file"
        for _ in range(x):
            movie.save(f'images/binary_image_{x}.png')

movie.save()