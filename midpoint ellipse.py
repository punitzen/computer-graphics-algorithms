import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.fromarray(np.zeros((150, 150), dtype=np.float32), mode= "F")

def ellipse(major,minor, xcenter, ycenter):
    x = 0
    y = minor
    p1 = minor**2 - (major**2 * minor) + (0.25 * major**2)
    dx = 2 * minor**2 * x
    dy = 2 * major**2 * y
    img.putpixel((x+xcenter, y+ycenter), 3)
    img.putpixel((-x+xcenter, y+ycenter), 3)
    img.putpixel((x+xcenter, -y+ycenter), 3)
    img.putpixel((-x+xcenter, -y+ycenter), 3)

    # Region 1
    while(dx < dy):
        x += 1
        if (p1 < 0):
            dx = 2 * minor**2 * x
            p1 = p1 + dx + minor**2
        else:
            y -= 1
            dx = 2 * minor**2 * x
            dy = 2 * major**2 * y
            p1 = p1 + dx -dy + minor**2
        img.putpixel((x+xcenter, y+ycenter), 3)
        img.putpixel((-x+xcenter, y+ycenter), 3)
        img.putpixel((x+xcenter, -y+ycenter), 3)
        img.putpixel((-x+xcenter, -y+ycenter), 3)

    # Region 2
    p2 = (minor * (x + 0.5))**2 + (major * (y-1))**2 - (major * minor)**2
    if(dx >= dy):
        while(y>=0):
            img.putpixel((x+xcenter, y+ycenter), 3)
            y -= 1
            if(p2>0):
                dy = 2 * major**2 * y
                p2 = p2 - dy + major**2
            else:
                x += 1
                dy = 2 * major**2 * y
                dx = 2 * minor**2 * x
                p2 = p2 + dx - dy + major**2
            img.putpixel((x+xcenter, y+ycenter), 3)
            img.putpixel((-x+xcenter, y+ycenter), 3)
            img.putpixel((x+xcenter, -y+ycenter), 3)
            img.putpixel((-x+xcenter, -y+ycenter), 3)

ellipse(40,50,70,70)
ellipse(5,15,50,90)
ellipse(5,15,90,90)
ellipse(10,20,70,50)

plt.imshow(np.array(img))
plt.show()