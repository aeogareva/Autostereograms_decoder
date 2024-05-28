from PIL import Image
n=1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
im = Image.open("/home/anyka/Project/d.png")
pix = im.load()
num_common_pixels = dict()
for period in range(85,150):
    matches=0
    for i in range(800):
        for j in range(400):
          if i+period>799:
             break
          else: 
             if pix[i,j]==pix[i+period,j]:
                matches+=1
    num_common_pixels[period]=matches

for period in range(85,150):
   if num_common_pixels[period]>n:
      n=num_common_pixels[period]
##h=max(u)
##s=get_key(u, h)
new_period=get_key(num_common_pixels, n)
print('Period:',new_period)  
width, height = im.size
img = im.crop((0, 0, new_period, height))
img.show()
img.save('period.png')
