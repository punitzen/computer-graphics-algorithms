from bresenham import bresenham
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.fromarray(np.zeros((200, 200), dtype=np.float32), mode= "F")

def line(x1,y1,x2,y2):
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    coords = bresenham(x1,y1,x2,y2)
    for coord in coords:
        img.putpixel(coord,1)

def translate(x1, y1, x2, y2, tx, ty):
    # Coordinate Matrix
    X  = np.array([[x1,y1,1],
                  [x2,y2,1]])
    
    # Translation Matrix
    T = np.array([[1,0,0],
                 [0,1,0],
                 [tx,ty,1]])
    
    result = np.matmul(X,T)

    print(result)
    line(result[0][0], result[0][1], result[1][0], result[1][1])

def rotation(x1, y1, x2, y2, theta):
    # Coordinate Matrix
    X  = np.array([[x1,y1,1],[x2,y2,1]])

    '''
    Translation matrices for rotation about origin
    '''
    T = np.array([[1,0,0],[0,1,0],[-x1,-y1,1]])

    Tinv = np.array([[1,0,0],[0,1,0],[x1,y1,1]])

    R = np.array([
        [np.cos(np.deg2rad(theta)), np.sin(np.deg2rad(theta)), 0],
        [np.sin(np.deg2rad(-theta)), np.cos(np.deg2rad(theta)), 0],
        [0, 0, 1]])
    
    result = np.matmul(X,T)
    result1 = np.matmul(result,R)
    result2 = np.matmul(result1,Tinv)

    print(result2)
    line(result2[0][0], result2[0][1], result2[1][0], result2[1][1])

def scaling(x1, y1, x2, y2, sx, sy):
    # Coordinate Matrix
    X  = np.array([[x1,y1,1],
                   [x2,y2,1]])

    # Scaling Matrix
    T = np.array([[sx,0,0],
                  [0,sy,0],
                  [0,0,1]])
    
    result = np.matmul(X,T)

    print(result)
    line(result[0][0], result[0][1], result[1][0], result[1][1])

def x_reflection(x1, y1, x2, y2):
    # Coordinate Matrix
    X  = np.array([[x1,y1,1],[x2,y2,1]])

    # Reflection about x-axis Matrix
    T = np.array([[1,0,0],
                  [0,-1,0],
                  [0,0,1]])
    
    result = np.matmul(X,T)

    print(result)
    line(result[0][0], result[0][1], result[1][0], result[1][1])

def y_reflection(x1, y1, x2, y2):
    # Coordinate Matrix
    X  = np.array([[x1,y1,1],[x2,y2,1]])

    # Reflection about x-axis Matrix
    T = np.array([[-1,0,0],
                  [0,1,0],
                  [0,0,1]])
    
    result = np.matmul(X,T)

    print(result)
    line(result[0][0], result[0][1], result[1][0], result[1][1])


# Call each functions separately

# Translation
line(20, 30, 100, 80)
translate(20, 30, 100, 80, 30, 40)

# Rotation
line(20, 30, 100, 80)
rotation(20, 30, 100, 80, -45)

# Scaling
line(25,25,25,175) 
line(25,175,175,175)
line(175,25,175,175)
line(25,25,175,25)

scaling(25,25,25,175,0.5,0.5) 
scaling(25,175,175,175,0.5,0.5)
scaling(175,25,175,175,0.5,0.5)
scaling(25,25,175,25,0.5,0.5)

# Reflection
line(100+20, 100+30, 100+90, 100+80)
x_reflection(100+20, 100+30, 100+90, 100+80)
y_reflection(100+20, 100+30, 100+90, 100+80)

plt.imshow(np.array(img))
plt.show()