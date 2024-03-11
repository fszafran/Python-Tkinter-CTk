import customtkinter as ctk
import tkinter.filedialog as filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
from graham import *

root=ctk.CTk()
root.title('Otoczka')
canvas=plt.figure(figsize=(7,7))

plt.gca().set_aspect('equal', adjustable='box')
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)
canvas = FigureCanvasTkAgg(canvas, master=root)
canvas.get_tk_widget().grid(row=0, column=0,rowspan=15,columnspan=5)

points = []
box=[]
hull=[]
pts=[]
text=[]
cbox='blue'
wbox=2
dbox='solid'
current_style = None 
colors = {'zielony': 'green', 'niebieski': 'blue', 'żółty': 'yellow', 'czarny': 'black', 'fioletowy': 'purple','czerwony': 'red', 'brązowy': 'brown'}
dashes = {'stały': 'solid', 'kreskowany': 'dashed', 'kropka-kreska': 'dashdot', 'kropkowany': 'dotted'}
style ={'Okrąg': 'o', 'Trójkąt': '^', 'Kwadrat': 's', 'Gwiazda': '*', 'Romb': 'd', 'Plus': 'P', 'X': 'X'}

def load_points():
    global pts, points,text, hull
    points = []
    for p in pts:
        p.remove()
    pts=[]
    for tx in text:
        tx.remove()
    text=[]
    for h in hull:
        h.remove()
    hull=[]
    checkbox.deselect()
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if len(line.split()) < 2:
            continue
        x, y = line.split()
        points.append([float(y), float(x)])
    
            
    ax=canvas.figure.gca()
    pt=ax.scatter([p[0] for p in points], [p[1] for p in points], color='black')
    pts.append(pt)
    #draw_bbox(points)
    canvas.draw()

def draw_point():
    global points,pts, hull
    y=float(y_entry.get())
    x=float(x_entry.get())
    points.append([x,y])
    ax = canvas.figure.gca()
    color=hull[0].get_color()
    pt=ax.scatter(x,y,color='black')
    pts.append(pt)
    draw_bbox(points)
    if checkbox.get():
        t=plt.gca().text(x, y, str(points.index([x,y])+1), fontsize=12)
        text.append(t)
    if hull:
        for h in hull:
            h.remove()
        hull=[]
        ot = ot_graham(points.copy())
        h=ax.plot([p[0] for p in ot], [p[1] for p in ot], color=color,linewidth=2)
        hull.append(h[0])
    canvas.draw()
        
def draw_bbox(points):
    global box,cbox,wbox,dbox
    for b in box:
        b.remove()
    box=[]
    xmin = min(points, key=lambda point: point[1])[1]
    xmax = max(points, key=lambda point: point[1])[1]
    ymin = min(points, key=lambda point: point[0])[0]
    ymax = max(points, key=lambda point: point[0])[0]
    ax = canvas.figure.gca()
    b=ax.add_patch(Rectangle((ymin, xmin), ymax - ymin, xmax - xmin,facecolor='none',edgecolor=cbox, linewidth=wbox, linestyle=dbox))
    box.append(b)
    print('dodano')

def checkbox_box():
    global box, points 
    if checkbox_box.get():
        for b in box:
            b.remove()
        box = []
        draw_bbox(points)
    else:
        for b in box:
            b.remove()
        box=[]
    canvas.draw()


def draw_hull():
    global points, hull
    color=None
    width=None
    dash=None
    if hull:
        color=hull[0].get_color()
        width=hull[0].get_linewidth()
        dash=hull[0].get_linestyle()
    else:
        color='red'
        width=2
        dash='solid'
    for ax in hull:
        ax.remove()
    hull=[]
    ax=canvas.figure.gca()
    ot = ot_graham(points.copy())
    h=ax.plot([p[0] for p in ot], [p[1] for p in ot], color=color,linewidth=width,linestyle=dash)
    hull.append(h[0])
    canvas.draw()

def change_color_box(value):
    global box, cbox
    color=colors[value]
    box[0].set_edgecolor(color)
    cbox=color
    canvas.draw()

def change_style_box(value):
    global box, dbox
    dash=dashes[value]
    box[0].set_linestyle(dash)
    dbox=dash
    canvas.draw()

def change_width_box(value):
    global box, wbox
    box[0].set_linewidth(float(value))
    wbox=float(value)
    canvas.draw()


def change_color_points(value):
    global pts, points, current_style
    ax=canvas.figure.gca()
    size=pts[0].get_sizes()
    color=colors[value]
    for p in pts:
        p.remove()
    pts=[]
    if current_style is not None:
        pt=ax.scatter([p[0] for p in points], [p[1] for p in points], color=color, marker=current_style, s=size)
    else: 
        pt=ax.scatter([p[0] for p in points], [p[1] for p in points], color=color, s=size)
    pts.append(pt)
    canvas.draw()

def change_style_points(value):
    global pts, points, current_style
    ax=canvas.figure.gca()
    current_style = style[value] 
    color=pts[0].get_facecolor()
    size=pts[0].get_sizes()
    for p in pts:
        p.remove()
    pts=[]
    pt=ax.scatter([p[0] for p in points], [p[1] for p in points], color=color, marker=current_style, s=size)
    pts.append(pt)
    canvas.draw()

def change_width_points(value):
    global pts,points, current_style
    ax=canvas.figure.gca()
    size=float(value)
    color=pts[0].get_facecolor()
    for p in pts:
        p.remove()
    pts=[]
    pt=ax.scatter([p[0] for p in points], [p[1] for p in points], color=color,marker=current_style,s=size)
    pts.append(pt)
    canvas.draw()

def change_color_ot(value):
    global hull
    color=colors[value]
    hull[0].set_color(color)
    canvas.draw()

def change_style_ot(value):
    global hull
    dash=dashes[value]
    hull[0].set_linestyle(dash)
    canvas.draw()

def change_width_ot(value):
    global hull
    hull[0].set_linewidth(float(value))
    canvas.draw()

def checkbox_nums():
    global points, pts, text
    ax=canvas.figure.gca()
    if checkbox.get():
        text=[]
        for i, point in enumerate(points):
            t = ax.text(point[0], point[1], str(i+1), fontsize=12)
            text.append(t)
    else:
        if text:
            for t in text:
                t.remove()
    canvas.draw()
def save():
    global points
    graham=ot_graham(points)
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if f is not None:
        for i,p in enumerate(graham):
            if i!=len(graham)-1:
                f.write(str(p[1]) + ' ' + str(p[0]) + '\n')
        f.close()



add_point_label=ctk.CTkLabel(root, text='Współrzędne punktu:', font=('Arial', 15, 'bold'), width=20, height=2)
add_point_label.grid(row=0, column=7, sticky='n',padx=10, pady=10)

x_label=ctk.CTkLabel(root, text='x: ', font=('Arial', 15, 'bold'), width=5, height=2)
x_label.grid(row=1, column=5,sticky='ne',padx=10)

y_label=ctk.CTkLabel(root, text='y: ', font=('Arial', 15, 'bold'), width=5, height=2)
y_label.grid(row=1, column=8,sticky='ne')

point = ctk.CTkButton(root, text='Dodaj punkt', font=('Arial', 15, 'bold'), width=150, height=2, command=draw_point)
point.grid(row=2, column=7, sticky='n',padx=10, pady=10)

y_entry=ctk.CTkEntry(root, font=('Arial', 15, 'bold'), width=150, height=2)
y_entry.grid(row=1, column=6,sticky='ne',padx=5)

x_entry=ctk.CTkEntry(root, font=('Arial', 15, 'bold'), width=150, height=2)
x_entry.grid(row=1, column=9,sticky='ne', padx=10)

load_points_button=ctk.CTkButton(root, text='Wczytaj punkty', font=('Arial', 15, 'bold'), width=80, height=2,command=load_points)
load_points_button.grid(row=3, column=8, columnspan=2, sticky='n',padx=10, pady=10)

otoczka_button=ctk.CTkButton(root, text='Oblicz otoczkę', font=('Arial', 15, 'bold'), width=80, height=2,command=draw_hull)
otoczka_button.grid(row=3, column=5, columnspan=2, sticky='n',padx=10, pady=10)

color_button_box = ctk.CTkComboBox(root, width=150, height=20, values=list(colors.keys()), command=change_color_box)
color_button_box.set('Kolor prostokąta')
color_button_box.grid(row=4, column=5, columnspan=2)

dash_button_box = ctk.CTkComboBox(root, width=150, height=20, values=list(dashes.keys()), command=change_style_box)
dash_button_box.set('Styl prostokąta')
dash_button_box.grid(row=4, column=7)

width_button_box=ctk.CTkComboBox(root,width=150,height=20,values=['1','2','3','4','5'],command=change_width_box)
width_button_box.set('Grubość prostokąta')
width_button_box.grid(row=4,column=8,columnspan=2)

color_button_points = ctk.CTkComboBox(root, width=150, height=20, values=list(colors.keys()), command=change_color_points)
color_button_points.set('Kolor punktów')
color_button_points.grid(row=5, column=5, columnspan=2)

dash_button_points = ctk.CTkComboBox(root, width=150, height=20, values=list(style.keys()), command=change_style_points)
dash_button_points.set('Styl punktów')
dash_button_points.grid(row=5, column=7)

width_button_points=ctk.CTkComboBox(root,width=150,height=20,values=['5','10','20','25','30','35','40','50'],command=change_width_points)
width_button_points.set('Rozmiar punktów')
width_button_points.grid(row=5,column=8, columnspan=2)

color_button_ot = ctk.CTkComboBox(root, width=150, height=20, values=list(colors.keys()), command=change_color_ot)
color_button_ot.set('Kolor otoczki')
color_button_ot.grid(row=6, column=5, columnspan=2)

dash_button_ot = ctk.CTkComboBox(root, width=150, height=20, values=list(dashes.keys()), command=change_style_ot)
dash_button_ot.set('Styl otoczki')
dash_button_ot.grid(row=6, column=7)

width_button_ot=ctk.CTkComboBox(root,width=150,height=20,values=['1','2','3','4','5'],command=change_width_ot)
width_button_ot.set('Grubość linii otoczki')
width_button_ot.grid(row=6,column=8, columnspan=2)

checkbox=ctk.CTkCheckBox(root,text='Pokaż numery punktów',command=checkbox_nums)
checkbox.grid(row=3, column=7)

save_button=ctk.CTkButton(root, text='Zapisz otoczkę', font=('Arial', 15, 'bold'), width=80, height=2,command=save,fg_color='darkgreen')
save_button.grid(row=7, column=7, sticky='n',padx=10, pady=10)

checkbox_box=ctk.CTkCheckBox(root,text='Pokaż prostokąt',command=checkbox_box)
checkbox_box.grid(row=7, column=9)


root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()