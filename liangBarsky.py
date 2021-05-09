def liangBarsky(x1,y1,x2,y2,x_min,y_min,x_max,y_max):
    dx = x2-x1
    dy = y2-y1
    p1 = -dx
    p2 = dx
    p3 = -dy
    p4 = dy

    q1 = x1 - x_min
    q2 = x_max - x1
    q3 = y1 - y_min
    q4 = y_max - y1

    print("p1 =  %.2f, q1 =  %.2f"% (p1,q1))
    print("p2 =  %.2f, q2 =  %.2f"% (p2,q2))
    print("p3 =  %.2f, q3 =  %.2f"% (p3,q3))
    print("p4 =  %.2f, q4 =  %.2f"% (p4,q4))
    print("\n")

    t1 = q1/p1
    t2 = q2/p2
    t3 = q3/p3
    t4 = q4/p4

    print("t1 = %.2f"% t1)
    print("t2 = %.2f"% t2)
    print("t3 = %.2f"% t3)
    print("t4 = %.2f"% t4)
    print("\n")

    t_max = 0
    t_min = 1

    if(p1 == 0 or p2 == 0 or p3 == 0 or p4 == 0):
        print("line is parallel")
        print("\n")
    
    if(p1 != 0):
        if(p1 < 0):
            t_max = max(t_max,t1)
        elif(p1 > 0):
            t_min = min(t_min,t1)

    if(p2 != 0):
        if(p2 < 0):
            t_max = max(t_max,t2)
        elif(p2 > 0):
            t_min = min(t_min,t2)  

    if(p3 != 0):
        if(p3 < 0):
            t_max = max(t_max,t3)
        elif(p3 > 0):
            t_min = min(t_min,t3)   

    if(p4 != 0):
        if(p4 < 0):
            t_max = max(t_max,t4)
        elif(p4 > 0):
            t_min = min(t_min,t4)      
    
    if(t_max > t_min):
        print("Line is completely outside")
        print("\n")
    
    if(t_max < t_min):
        x_1 = x1 + (t_max * dx)
        y_1 = y1 + (t_max * dy)
        x_2 = x1 + (t_min * dx)
        y_2 = y1 + (t_min * dy)

    print("Line will be accepted from (%.2f, %.2f) to (%.2f, %.2f)"% (x_1,y_1,x_2,y_2))

print("Enter Clipping Region")
x_min = int(input("x_min: "))
y_min = int(input("y_min: "))
x_max = int(input("x_max: "))
y_max = int(input("y_max: "))
print("\n")

print("Enter Line Coord")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
print("\n")

liangBarsky(x1,y1,x2,y2,x_min,y_min,x_max,y_max)