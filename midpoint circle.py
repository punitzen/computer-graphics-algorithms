import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.fromarray(np.zeros((150, 150), dtype=np.float32), mode= "F")

def midPoint_Circle(x, y, ycenter, xcenter):
    p = 1.25 - y
    img.putpixel((x+xcenter, y+ycenter), 3)
    img.putpixel((-x+xcenter, y+ycenter), 3)
    img.putpixel((x+xcenter, -y+ycenter), 3)
    img.putpixel((-x+xcenter, -y+ycenter), 3)
    if x!=y:
            img.putpixel((y+xcenter, x+ycenter), 3)
            img.putpixel((-y+xcenter, x+ycenter), 3)
            img.putpixel((y+xcenter, -x+ycenter), 3)
            img.putpixel((-y+xcenter, -x+ycenter), 3)
    while(x<=y):
        x = x+1
        if(p >= 0):
            y -= 1
            p = p + 2*x - 2*y + 5
        else:
            p = p + 2*x + 3
        if(x>y):
            break
        img.putpixel((x+xcenter, y+ycenter), 3)
        img.putpixel((-x+xcenter, y+ycenter), 3)
        img.putpixel((x+xcenter, -y+ycenter), 3)
        img.putpixel((-x+xcenter, -y+ycenter), 3)

        if x!=y:
            img.putpixel((y+xcenter, x+ycenter), 3)
            img.putpixel((-y+xcenter, x+ycenter), 3)
            img.putpixel((y+xcenter, -x+ycenter), 3)
            img.putpixel((-y+xcenter, -x+ycenter), 3)


midPoint_Circle(0,50,70,70)
midPoint_Circle(0,10,50,90)
midPoint_Circle(0,10,90,90)
midPoint_Circle(0,20,70,50)

img = np.transpose(img)
plt.imshow(np.array(img))
plt.show()