from PIL import Image
n=1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def consilience(widthx, heightx,widthy, heighty, width2, height2):
    u = dict()
    o = dict()
    for i in range(heightx, heighty):
        for j in range(widthx, widthy):
            uo=i%94
            jo=j%17
            u[i,j]=pix[i, j]
    for i in range(height):
        for j in range(width):
            ui=i%94
            uj=j%17
            x=u[ui,uj]
            y=pix[i,j]
            xr, xg, xb = x
            yr, yg, yb = y
            o[i,j]=(abs(xr-yr), abs(xg-yg), abs(xb-yb))
    return o
            

im = Image.open("/home/anyka/Project/Horse.jpg")
pix = im.load()
for m in range(5,95):
    d=0
    for i in range(1024):
        for j in range(867):
          if i+94>1023 or i+94+m>1023 or j+17>867 or j+17+m>867:
             break
          else: 
             if pix[i,j]==pix[i+m,j]:
                d+=1