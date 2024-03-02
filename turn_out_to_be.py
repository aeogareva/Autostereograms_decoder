import numpy as np
import os
import io
import requests
from PIL import Image, ImageDraw
n=1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def num_common_pixels(img, w, h, x1,y1,x2,y2,):
    pix=img.load()
    d=0
    im = img.crop((x1, y1, x1+h, y1+w))
    im2= img.crop((x2, y2, x2+h, y2+w))
    arr1=np.array(im)
    arr2=np.array(im2)
    G= (arr1 == arr2)
    G=np.all(G, axis=2)
    d=np.sum(G)
    return d

def best_shift(img, w,h,x,y,xstart, xend, y2):
    pix=img.load()
    max_d=0
    u=dict()
    for maybe_x in range(xstart, xend+1):
        d=num_common_pixels(img, w, h, x,y,maybe_x,y2,)
        if d>max_d:
            max_d=d
        u[maybe_x]=d
    x2=get_key(u, max_d)
    return x2
        
         
def visualise_shifts(img,w,h, matrix_of_shifts):
    pix=img.load()
    draw = ImageDraw.Draw(img)
    for j in range(len(matrix_of_shifts)):
        for i in range(len(matrix_of_shifts[j])):
            # print(i,j, i*h, j*w, img.size, len(matrix_of_shifts), len(matrix_of_shifts[i]))
            color=matrix_of_shifts[j][i]%little_width
            xy=[i*h, j*w, i*h+h, j*w+w]
            draw.rectangle(xy, fill=(color,color,color), outline=None, width=1)
            #        pix[i*h+e,j*w+p]=(color, color,color)
    # print(matrix_of_shifts)
    return img
    


#def consilience(widthx, heightx,widthy, heighty, width2, height2):
    #u = dict()
    #o = dict()
    #for i in range(heightx, heighty):
        #for j in range(widthx, widthy):
            ##uo=i%little_width
            ##jo=j%17
            ##u[i,j]=pix[i, j]
    ##for i in range(height):
        ##for j in range(width):
            ##ui=i%little_width
            ##uj=j%17
            ##x=u[ui,uj]
            ##y=pix[i,j]
            #xr, xg, xb = x
            ##yr, yg, yb = y
            #o[i,j]=(abs(xr-yr), abs(xg-yg), abs(xb-yb))
    #return o
            

img = Image.open("/home/anyka/Project/Horse.jpg")
height0, width0 = img.size

im = img.crop((0, 0, 940, width0))
pix = im.load()
width, height = im.size
little_height=17
little_width = 94
matrix_of_shifts=[[0] * (width//little_width) for _ in range(height//little_height)]
for i in range(0, width, little_width):
    for j in range(0, height, little_height):
        if i + little_width >= width or j + little_height >= height:
            break
        col = i // little_width 
        row = j // little_height
        # print(col, row, len(m), len(m[col]))
        matrix_of_shifts[row][col] = best_shift(im, little_height, little_width, i, j, i + little_width // 2, i + little_width, j)
resulting_image = visualise_shifts(im,little_height,little_width, matrix_of_shifts)
resulting_image.show()
resulting_image.save('image.png') #ww, visualise_shifts(im,little_height,little_width, m), quality=85)}
