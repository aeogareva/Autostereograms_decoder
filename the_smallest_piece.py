import sys
import numpy as np
from PIL import Image
n=1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def num_common_pixels(img, w, h, x1,y1,x2,y2,):
    pix=img.load()
    d=0
    for i in range(h):
      for j in range(w):
         if pix[x1+i, y1+j]==pix[x2+i, y2+j]:
            d+=1
    return d

def best_shift(img, w,h, x,y, xstart, xend):
    pix=img.load()
    max_d=0
    u = dict()
    for maybe_x in range(xstart, xend + 1):
        d = num_common_pixels(img, w, h, x, y, maybe_x, y,)
        if d > max_d:
            imgarr = np(img)
            max_d = d
        u[maybe_x, y] = d
    x2=get_key(u, max_d)
    return u
        
         
def visualise_shifts(img, h, w, matrix_of_shifts):
    pix=img.load()
    width, height = img.size
    # print((0,17) in matrix_of_shifts)
    for (x0,y0) in matrix_of_shifts:
        #print(i,j, i*h, j*w, img.size, len(matrix_of_shifts), len(matrix_of_shifts[i]))
        for dx in range(w):
            for dy in range(h):
                color = matrix_of_shifts[(x0,y0)] % 255 # %little_width
                pix[min(x0 + dx, width-1), min(y0 + dy, height-1)]=(color, color, color)
    # print(matrix_of_shifts)
    return img

img = Image.open("/home/anyka/Project/Horse.jpg")
height0, width0 = img.size

im = img.crop((0, 0, 940, width0))
print(im.size)
# sys.exit(0)
processed_img = im.copy()
pix = im.load()
width, height = im.size
little_height = 17
little_width = 94
num_cols = width // little_width
num_rows = height // little_height
matrix_of_shifts = [[0] * num_cols for _ in range(num_rows)]
for start_x_pos in range(0, width, little_width):
    for start_y_pos in range(0, height, little_height):
        if start_x_pos+little_width>=width or start_y_pos + little_height >= height:
            break
        #print(i//little_width,j//little_height, len(m), len(m[i//little_width]))
        matrix_of_shifts = best_shift(im, little_height, little_width,
                     start_x_pos, start_y_pos,
                     start_x_pos + little_width // 2, start_x_pos + little_width)
        # print()
        processed_img = visualise_shifts(processed_img, little_height, little_width, matrix_of_shifts)
processed_img.show()