import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.fromarray(np.zeros((150, 150), dtype=np.float32), mode= "F")

def lower(x1, y1, x2, y2):
    dy = 2 * (y2 - y1)
    dx = 2 * (x2 - x1)
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy 
    d = 2 * dy - dx    
    y = y1
    for x in range(x1, x2+1):
        img.putpixel((x, y), 1)
        if d >= 0:
            y += yi
            d -= dx
        d += dy
        
def higher(x1, y1, x2, y2):
    dy = 2 * (y2 - y1)
    dx = 2 * (x2 - x1)
    xi = 1   
    if dx < 0:
        xi = -1
        dx = -dx     
    d = 2 * dx - dy     
    x = x1
    for y in range(y1, y2+1):     
        img.putpixel((x, y), 1)  
        if d >= 0:
            x += xi
            d -= dy 
        d += dx

def bresenham(x1, y1, x2, y2):
    if abs(y2 - y1) < abs(x2 - x1):
        if x1 > x2:
            lower(x2, y2, x1, y1)
        else:
            lower(x1, y1, x2, y2)
    else:
        if y1 > y2:
            higher(x2, y2, x1, y1)
        else:
            higher(x1, y1, x2, y2)
            
bresenham(20, 30, 90, 60)

plt.imshow(np.array(img))
plt.show()