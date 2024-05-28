from PIL import Image

m=94



im = Image.open("/home/anyka/Project/Horse.jpg")
height, width = im.size
pix = im.load()



u = dict()
for i in range(m):
    for j in range(width):
            uo=i%m
            u[uo,j]=pix[i, j]
# print(list(u.keys()))
# im.close()

im2 = Image.open("/home/anyka/Project/Horse.jpg")
new_pix = im2.load()
for i in range(height):
    for j in range(width):
        if i // m < 1:
               ui=i%m
               x=u[ui,j]
               y=pix[i,j]
               xr=x[0]
               xg=x[1]
               xb=x[2]
               yr=y[0]
               yg=y[1]
               yb=y[2]
               new_pix[i,j]=(abs(xr-yr), abs(xg-yg), abs(xb-yb))
        else:
               ui=i-94
               x=pix[ui,j]
               y=pix[i,j]
               xr=x[0]
               xg=x[1]
               xb=x[2]
               yr=y[0]
               yg=y[1]
               yb=y[2]
               new_pix[i,j]=(abs(xr-yr), abs(xg-yg), abs(xb-yb))
             
im2.show()
im2.save('It.jpg')