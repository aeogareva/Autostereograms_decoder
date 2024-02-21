from PIL import Image
n=1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
im = Image.open("/home/anyka/Project/Horse.jpg")
pix = im.load()
u = dict()
for m in range(85,101):
    d=0
    for i in range(1024):
        for j in range(867):
          if i+m>1023:
             break
          else: 
             if pix[i,j]==pix[i+m,j]:
                d+=1
    u[m]=d

for m in range(85,101):
   if u[m]>n:
      n=u[m]
##h=max(u)
##s=get_key(u, h)
print('Period:',get_key(u, n))        
