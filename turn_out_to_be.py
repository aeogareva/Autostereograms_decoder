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
        u[maybe_x]=d
    x2=get_key(u, max_d)
    return x2
        
         
def visualise_shifts(img,w,h, matrix_of_shifts):
    pix=img.load()
    for j in range(len(matrix_of_shifts)):
        for i in range(len(matrix_of_shifts[j])):
            print(i,j, i*h, j*w, img.size, len(matrix_of_shifts), len(matrix_of_shifts[i]))
            for e in range(h):
                for p in range(w):
                    color=matrix_of_shifts[j][i]%94
                    pix[i*h+e,j*w+p]=(color, color,color)
    print(matrix_of_shifts)
    return img
    


#def consilience(widthx, heightx,widthy, heighty, width2, height2):
    #u = dict()
    #o = dict()
    #for i in range(heightx, heighty):
        #for j in range(widthx, widthy):
            ##uo=i%94
            ##jo=j%17
            ##u[i,j]=pix[i, j]
    ##for i in range(height):
        ##for j in range(width):
            ##ui=i%94
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
height, width = im.size
m=[[0] * (height//94) for _ in range(width//17)]
for i in range(0, height, 94):
    for j in range(0,width, 17):
        if i+94>=height or j + 17 >= width:
            break
        print(i//94,j//17, len(m), len(m[i//94]))
        m[j//17][i//94]=best_shift(im,17,94,i,j,i+47, i+94, j)
visualise_shifts(im,17,94, m).show()