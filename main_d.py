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
        
def num_common_pixels(im_array, little_height, little_width, x1,y1,x2,y2,):
    # pix=im_array.load()
    d=0
    arr = im_array[y1:y1+little_height , x1:x1+little_width]
    arr2= im_array[y2:y2+little_height , x2:x2+little_width]
    G= (arr == arr2)
    G=np.all(G, axis=2)
    d=np.sum(G)
    return d

def best_shift(im_array, little_height,little_width, x,y,xstart, xend, y2, height_padding):
    # pix=im_array.load()
    max_d=0
    u=dict()
    for maybe_x in range(xstart, xend+1):
        d=num_common_pixels(im_array, little_height+2*height_padding, little_width, x,y-height_padding,maybe_x,y2-height_padding)
        if d>max_d:
            max_d=d
        u[maybe_x]=d
    x2=get_key(u, max_d)
    return x2
        
         
def visualise_shifts(img,little_height,little_width, matrix_of_shifts):
    # pix=img.load()
    draw = ImageDraw.Draw(img)
    for j in range(len(matrix_of_shifts)):
        for i in range(len(matrix_of_shifts[j])):
            # print(i,j, i*little_width, j*little_height, img.size, len(matrix_of_shifts), len(matrix_of_shifts[i]))
            color=matrix_of_shifts[j][i]%little_width
            print(i*little_width, j*little_height, i*little_width+little_width, j*little_height+little_height, '__', color)
            xy=[i*little_width, j*little_height, i*little_width+little_width, j*little_height+little_height]
            draw.rectangle(xy, fill=(color,color,color), outline=None, width=1)
            #        pix[i*w+e,j*h+p]=(color, color,color)
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
            


img = Image.open("/home/anyka/Project/d.png")
height0, width0 = img.size
im = img.crop((100, 0, height0, width0))
pix = im.load()
width, height = im.size

im_array = np.array(im)

little_height=1
height_padding = 1
little_width = 140
matrix_of_shifts=[[0] * (width//little_width) for _ in range(height)]
for i in range(0, width, little_width):
    for j in range(height):
        if i + little_width >= width or j + little_height >= height:
            break
        col = i // little_width 
        row = j // little_height
        #print(col, row, little_height, little_width, i, j, i + little_width // 2, i + little_width, j,height_padding)
        matrix_of_shifts[row][col] = best_shift(im_array, little_height, little_width, i, j, i + little_width // 2, i + little_width, j,height_padding)
resulting_image = visualise_shifts(im, little_height, little_width, matrix_of_shifts)
#print(little_height, little_width, matrix_of_shifts)
resulting_image.show()
resulting_image.save('image.png') #ww, visualise_shifts(im,little_height,little_width, m), quality=85)}