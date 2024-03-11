import customtkinter as ctk
from funkcje import *
import tkinter.filedialog as filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

# zmienne globalne,okno i canvas
root= ctk.CTk()
root.title('Punkt w Wielokącie')
canvas = plt.figure(figsize=(10,7))
#set the scaling of the x and y to the same value 
plt.gca().set_aspect('equal', adjustable='box')
canvas = FigureCanvasTkAgg(canvas, master=root)
canvas.get_tk_widget().grid(row=0, column=0,rowspan=15,columnspan=5)
pkt=0
polygon=[]
scat=[]
points_in=[]
points_out=[]
colors = {'zielony': 'green', 'niebieski': 'blue', 'żółty': 'yellow', 'czarny': 'black', 'fioletowy': 'purple'}
dashes = {'stały': 'solid', 'kreskowany': 'dashed', 'kropka-kreska': 'dashdot', 'kropkowany': 'dotted'}
style ={'Okrąg': 'o', 'Trójkąt': '^', 'Kwadrat': 's', 'Gwiazda': '*', 'Romb': 'd', 'Plus': 'P', 'X': 'X'}


#funkcje
def load_polygon():
    global polygon,pkt
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
    if filename != "":
        f = open(filename, 'r')
        polygon = []
        for line in f:
            if len(line.split()) < 2:
                continue
            x, y = line.split()
            polygon.append([float(y),float(x)])
        f.close()
        canvas.figure.gca().clear()
        draw_polygon(polygon,canvas)
        liczba_pkt_label2.configure(text='')
        pkt=0
        points_in.clear()
        points_out.clear()
        for sc in scat:
            sc.remove()
        scat.clear()

def draw_polygon(polygon, canvas):
    ax = canvas.figure.gca()
    polygon.append(polygon[0])
    xs, ys = zip(*polygon) 
    ax.clear()
    ax.plot(xs, ys) 
    canvas.draw()
 
def draw_point():
    global polygon, pkt,scat, points_in, points_out
    if not polygon:
        messagebox.showwarning("Uwaga", "Najpierw wprowadź wielokąt.")
        return
    x=float(x_entry.get())
    y=float(y_entry.get())
    ax = canvas.figure.gca()
    marker_size = ax.collections[1].get_sizes()[0]
    marker_style = ax.collections[1].get_paths()[0]
    #marker_color = ax.collections[1].get_facecolors()[0]
    if check_points(polygon,[y,x]):
        scatter=ax.scatter(y,x,color='black',marker=marker_style, s=marker_size)
        points_in.append([y,x])
        canvas.draw()
        messagebox.showinfo("Wynik sprawdzenia", "Punkt jest wewnątrz wielokąta.")
        pkt += 1
        scat.append(scatter)
        liczba_pkt_label2.configure(text=pkt)
    else:
        scatter=ax.scatter(y,x,color='black',marker=marker_style, s=marker_size)
        points_out.append([y,x])
        canvas.draw()
        scat.append(scatter)
        messagebox.showinfo("Wynik sprawdzenia", "Punkt jest poza wielokątem.")

def load_points():
    global polygon, pkt, scat, points_in, points_out
    points = []
    if not polygon:
        messagebox.showwarning("Uwaga", "Najpierw wprowadź wielokąt.")
        return
    if len(scat)>=0:
        for sc in scat:
            sc.remove()
        scat=[]
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if len(line.split()) < 2:
            continue
        x, y = line.split()
        if float(x)<bounding_box(polygon)[0] or float(x)>bounding_box(polygon)[2] or float(y)<bounding_box(polygon)[1] or float(y)>bounding_box(polygon)[3]:
            continue
        points.append([float(y), float(x)])
    pkt=0
    ax = canvas.figure.gca() 
    for i in range(0, len(points)):
        if check_points(polygon, points[i]):
            scatter = ax.scatter(points[i][0], points[i][1], color='green')
            scat.append(scatter)
            points_in.append(points[i])
            pkt += 1
            liczba_pkt_label2.configure(text=pkt)
        else:
            scatter = ax.scatter(points[i][0], points[i][1], color='red')
            scat.append(scatter)
            points_out.append(points[i])
    canvas.draw()

def change_color_outline(value):
    global polygon
    ax = canvas.figure.gca()
    w = plt.gca().lines[0].get_linewidth()
    d = plt.gca().lines[0].get_linestyle()
    while len(ax.lines) > 0:
        ax.lines[0].remove()
    polygon.append(polygon[0])
    xs, ys = zip(*polygon)
    ax.plot(xs, ys, color=colors[value], linewidth=w, linestyle=d)
    polygon.pop()  
    canvas.draw()

def change_dash_outline(value):
    global polygon
    ax = canvas.figure.gca()
    c = plt.gca().lines[0].get_color()
    w = plt.gca().lines[0].get_linewidth()
    while len(ax.lines) > 0:
        ax.lines[0].remove()
    polygon.append(polygon[0])
    xs, ys = zip(*polygon)
    ax.plot(xs, ys, linestyle=dashes[value], color=c, linewidth=w)
    polygon.pop()  
    canvas.draw()

def change_width_outline(value):
    global polygon
    ax = canvas.figure.gca()
    c=plt.gca().lines[0].get_color()
    d=plt.gca().lines[0].get_linestyle()
    while len(ax.lines) > 0:
        ax.lines[0].remove()
    polygon.append(polygon[0])
    xs, ys = zip(*polygon)
    ax.plot(xs, ys, linewidth=int(value), color=c, linestyle=d)    
    polygon.pop()  
    canvas.draw()

def change_marker_points(value):
    global points_in,points_out,scat
    ax = canvas.figure.gca()
    if point_color_button.get() == 'Kolor punktów wewnątrz wielokąta':
        marker_color=colors['zielony']
    else:
        marker_color = ax.collections[1].get_facecolors()[0]
    marker_size = ax.collections[1].get_sizes()[0]
      
    for sc in scat:
        sc.remove()
    scat = [] 
    for i in range(0, len(points_in)):
        scatter = ax.scatter(points_in[i][0], points_in[i][1], color=marker_color,marker=style[value], s=marker_size)
        scat.append(scatter)
    for i in range(0, len(points_out)):
        scatter = ax.scatter(points_out[i][0], points_out[i][1], color='red',marker=style[value], s=marker_size)
        scat.append(scatter)
    canvas.draw()

def change_color_points(value):
    global points_in, points_out, scat
    ax = canvas.figure.gca()
    marker_style = ax.collections[1].get_paths()[0]
    marker_size = ax.collections[1].get_sizes()[0]
    for sc in scat:
        sc.remove()
    scat = [] 
    for i in range(0, len(points_in)):
        scatter = ax.scatter(points_in[i][0], points_in[i][1], color=colors[value],marker=marker_style, s=marker_size)
        scat.append(scatter)
    for i in range(0, len(points_out)):
        scatter = ax.scatter(points_out[i][0], points_out[i][1], color='red',marker=marker_style, s=marker_size)
        scat.append(scatter)
    canvas.draw()

def change_size_points(value):
    global points_in,points_out,scat
    ax = canvas.figure.gca()
    if point_color_button.get() == 'Kolor punktów wewnątrz wielokąta':
        marker_color=colors['zielony']
    else:
        marker_color = ax.collections[1].get_facecolors()[0]
    marker_style = ax.collections[1].get_paths()[0]
    for sc in scat:
        sc.remove()
    scat = []  
    for i in range(0, len(points_in)):
        scatter = ax.scatter(points_in[i][0], points_in[i][1], color=marker_color,marker=marker_style, s=int(value))
        scat.append(scatter)
    for i in range(0, len(points_out)):
        scatter = ax.scatter(points_out[i][0], points_out[i][1], color='red',marker=marker_style, s=int(value))
        scat.append(scatter)
    canvas.draw()

def exit():
    for after_id in root.tk.eval('after info').split(): 
        root.after_cancel(after_id) 
    root.quit()
    root.destroy()


#interfejs
add_point_label=ctk.CTkLabel(root, text='Współrzędne punktu:', font=('Arial', 15, 'bold'), width=20, height=2)
add_point_label.grid(row=0, column=5, columnspan=4, sticky='n',padx=10, pady=10)

x_label=ctk.CTkLabel(root, text='x: ', font=('Arial', 15, 'bold'), width=5, height=2)
x_label.grid(row=1, column=5,sticky='ne')

y_label=ctk.CTkLabel(root, text='y: ', font=('Arial', 15, 'bold'), width=5, height=2)
y_label.grid(row=1, column=7,sticky='ne')

liczba_pkt_label=ctk.CTkLabel(root, text='Liczba punktów wewnątrz wielokąta: ', font=('Arial', 15, 'bold'), width=30, height=2)
liczba_pkt_label.grid(row=4, column=5, columnspan=4, sticky='n',padx=10, pady=10)

liczba_pkt_label2=ctk.CTkLabel(root, text='', font=('Arial', 15, 'bold'), width=5, height=2)
liczba_pkt_label2.grid(row=5, column=5,sticky='n',columnspan=4,pady=1)

point = ctk.CTkButton(root, text='Sprawdź punkt', font=('Arial', 15, 'bold'), width=20, height=2,command=draw_point)
point.grid(row=2, column=5, columnspan=4, sticky='n',padx=10, pady=10)

x_entry=ctk.CTkEntry(root, font=('Arial', 15, 'bold'), width=180, height=2)
x_entry.grid(row=1, column=6,sticky='ne')

y_entry=ctk.CTkEntry(root, font=('Arial', 15, 'bold'), width=180, height=2)
y_entry.grid(row=1, column=8,sticky='ne')

load_polygon_button=ctk.CTkButton(root, text='Wczytaj wielokąt', font=('Arial', 15, 'bold'), width=20, height=2,command=load_polygon)
load_polygon_button.grid(row=3, column=5, columnspan=2, sticky='n',padx=10, pady=10)

load_points_button=ctk.CTkButton(root, text='Wczytaj punkty', font=('Arial', 15, 'bold'), width=20, height=2,command=load_points)
load_points_button.grid(row=3, column=7, columnspan=2, sticky='n',padx=10, pady=10)

color_button = ctk.CTkComboBox(root, width=230, height=20, values=list(colors.keys()), command=change_color_outline)
color_button.set('Kolor krawędzi wielokąta')
color_button.grid(row=6, column=5, columnspan=2)

dash_button = ctk.CTkComboBox(root, width=230, height=20, values=list(dashes.keys()), command=change_dash_outline)
dash_button.set('Styl krawędzi wielokąta')
dash_button.grid(row=7, column=5, columnspan=2)

width_button=ctk.CTkComboBox(root,width=230,height=20,values=['1','2','3','4','5'],command=change_width_outline)
width_button.set('Grubość krawędzi wielokąta')
width_button.grid(row=8,column=5,columnspan=2)

point_color_button=ctk.CTkComboBox(root,width=230,height=20,values=list(colors.keys()),command=change_color_points)
point_color_button.set('Kolor punktów wewnątrz wielokąta')
point_color_button.grid(row=6,column=7,columnspan=2)

change_marker_button = ctk.CTkComboBox(root,width=230,height=20,values=list(style.keys()),command=change_marker_points)
change_marker_button.set('Styl punktów')
change_marker_button.grid(row=7,column=7,columnspan=2)

change_size_button = ctk.CTkComboBox(root,width=230,height=20,values=['1','4','7','10','13','16','19','30','50'],command=change_size_points)
change_size_button.set('Rozmiar punktów')
change_size_button.grid(row=8,column=7,columnspan=2)

#loop 
root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()