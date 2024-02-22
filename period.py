from PIL import Image
n=1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
im = Image.open("/home/anyka/Project/Horse.jpg")
pix = im.load()
num_common_pixels = dict()
for period in range(85,101):
    matches=0
    for i in range(1024):
        for j in range(867):
          if i+period>1023:
             break
          else: 
             if pix[i,j]==pix[i+period,j]:
                matches+=1
    num_common_pixels[period]=matches

for period in range(85,101):
   if num_common_pixels[period]>n:
      n=num_common_pixels[period]
##h=max(u)
##s=get_key(u, h)
print('Period:',get_key(num_common_pixels, n))        
