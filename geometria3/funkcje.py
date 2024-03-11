import numpy as np

def bounding_box(wielokat):
    x_min=wielokat[0][1]  
    x_max=wielokat[0][1]  
    y_min=wielokat[0][0]  
    y_max=wielokat[0][0]  
    for i in range(1,len(wielokat)):
        if x_min>wielokat[i][1]: 
            x_min=wielokat[i][1]  
        if x_max<wielokat[i][1]:  
            x_max=wielokat[i][1]  
        if y_min>wielokat[i][0]:  
            y_min=wielokat[i][0]  
        if y_max<wielokat[i][0]: 
            y_max=wielokat[i][0]  
    x_min-=20
    x_max+=20
    y_min-=20
    y_max+=20
    return [x_min,y_min,x_max,y_max]

def calc_angle(v1,v2,point):
    p1=np.array([v1[0]-point[0],v1[1]-point[1]])
    p2=np.array([v2[0]-point[0],v2[1]-point[1]])
    dot=np.dot(p1,p2)
    cross=np.cross(p1,p2) 
    angle=np.arctan2(cross,dot)
    return angle #rad
    
def check_points(polygon,point):
    asum=0
    for i in range(0,len(polygon)-1):
        asum+=calc_angle(polygon[i],polygon[i+1],point)
    if abs(asum - 2 * np.pi) < 1e-12:
        return True   
    elif abs(asum) < 1e-12:
        return False
    else:
        return True
