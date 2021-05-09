import numpy as np 
from PIL import Image 
import matplotlib.pyplot as plt 

img = Image.fromarray(np.zeros((100, 100), dtype=np.float32), mode= "F") 

def dda_line(xl, yl, x2, y2): 
    dx = x2 - xl 
    dy = y2 - yl  
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy) 
    x_inc = dx / steps 
    y_inc = dy / steps 
    for i in range(steps): 
        img.putpixel((round(xl), round(yl)), 1) 
        xl += x_inc 
        yl += y_inc 

dda_line(30, 10, 10, 40) 

plt.imshow(np.array(img)) 
plt.show() 