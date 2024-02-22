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

def best_shift(img, w,h,x,y,xstart, xend, y2):
    pix=img.load()
    max_d=0
    u=dict()
    for maybe_x in range(xstart, xend+1):
        d=num_common_pixels(img, w, h, x,y,maybe_x,y2,)
        if d>max_d:
            max_d=d
        u[maybe_x, y]=d
    x2=get_key(u, max_d)
    return u
        
         
def visualise_shifts(img,w,h, matrix_of_shifts):
    pix=img.load()
    width, height =img.size
    for j in matrix_of_shifts:
            #print(i,j, i*h, j*w, img.size, len(matrix_of_shifts), len(matrix_of_shifts[i]))
        for l in range(h):
            for i in range(w):
                    color=matrix_of_shifts[j]%255 # %94
                    pix[min(j[0]+l, width-1),min(j[1]+i, height-1)]=(color, color,color)
    print(matrix_of_shifts)
    return img

img = Image.open("/home/anyka/Project/Horse.jpg")
height0, width0 = img.size

im = img.crop((0, 0, 940, width0))
im2=im.copy()
pix = im.load()
width, height = im.size
little_height=17
m=[[0] * (width//94) for _ in range(height//little_height)]
for i in range(0, width, 94):
    for j in range(0,height, little_height):
        if i+94>=width or j + little_height >= height:
            break
        #print(i//94,j//little_height, len(m), len(m[i//94]))
        m=best_shift(im,little_height,94,i,j,i+47, i+94, j)
        print(m)
        im2=visualise_shifts(im2,little_height,94, m)
im2.show()