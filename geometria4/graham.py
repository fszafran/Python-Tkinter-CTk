import numpy as np
def calc_angle(p0,p1):
    delta_y=p1[0]-p0[0]  
    delta_x=p1[1]-p0[1]  
    angle=np.arctan2(delta_y,delta_x)
    return angle 

def distance (p0,p1):
    return np.sqrt((p1[1]-p0[1])**2+(p1[0]-p0[0])**2)

def det(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p1[0]) - (p2[0] - p1[0]) * (p3[1] - p1[1])

def ot_graham(data):
    mins=[]
    Po=[]
    mins.append(min(data,key=lambda item: item[1]))  
    for i in range(len(data)):
        if(data[i][1]==mins[0][1] and data[i][0]!=mins[0][0]):  
            mins.append(data[i])
    if(len(mins)>1):
        Po=max(mins,key=lambda item: item[0])  
    else:
        Po=mins[0]
    data.sort(key=lambda item: (calc_angle(Po,item), -distance(Po,item)))
    stack=[Po]
    for p in data:
        while len(stack) > 1 and det(stack[-2], stack[-1], p) <= 0: 
            stack.pop()
        stack.append(p)

    return stack + [stack[0]]

