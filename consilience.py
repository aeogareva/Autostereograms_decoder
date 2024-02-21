from PIL import Image
img = Image.open("/home/anyka/Project/Horse.jpg")
height0, width0 = img.size

m=94


im = img.crop((0, 0, 940, width0))
height, width = im.size
im.show()
pix = im.load()

u = dict()
for i in range(height-1,height-m-1,-1):
    for j in range(width):
            uo=i%m
            u[uo,j]=pix[i, j]
# print(list(u.keys()))
for i in range(height):
    for j in range(width):
            ui=i%m
            x=u[ui,j]
            y=pix[i,j]
            xr=x[0]
            xg=x[1]
            xb=x[2]
            yr=y[0]
            yg=y[1]
            yb=y[2]
            pix[i,j]=(abs(xr-yr), abs(xg-yg), abs(xb-yb))
# im.show()

          

##            x=pix[i,j]
            ##y=pix[i+87,j]
            ##xr=x[0]
            ##xg=x[1]
            ##xb=x[2]
            ##yr=y[0]
            ##yg=y[1]
            ##yb=y[2]
            ##print(abs((xr+xg+xb)/3-(yr+yg+yb)/3))
            
