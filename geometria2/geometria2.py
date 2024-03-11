import customtkinter as ctk
import tkinter.filedialog as filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

def calc_przec_x(xa,ya,xb,yb,xc,yc,xd,yd):
    t=((xc-xa)*(yd-yc)-(yc-ya)*(xd-xc))/((xb-xa)*(yd-yc)-(yb-ya)*(xd-xc))
    return xa+t*(xb-xa)
def calc_przec_y(xa,ya,xb,yb,xc,yc,xd,yd):
    t=((xc-xa)*(yd-yc)-(yc-ya)*(xd-xc))/((xb-xa)*(yd-yc)-(yb-ya)*(xd-xc))
    return ya+t*(yb-ya)
root = ctk.CTk()
root.title("Przeciecie prostych")

canvas=plt.figure(figsize=(10,7))
canvas = FigureCanvasTkAgg(canvas, master=root)
canvas.get_tk_widget().grid(column=5,row=0,rowspan=15,columnspan=4)

toolbarFrame = ctk.CTkFrame(root)
toolbarFrame.grid(row=15,column=5,columnspan=4)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
toolbar.update()
toolbar.grid(row=15,column=5,columnspan=4)



XA_label = ctk.CTkLabel(root, text="XA:")
XA_label.grid(row=0, column=0)
XA_entry = ctk.CTkEntry(root)
XA_entry.grid(row=0, column=1)

YA_label = ctk.CTkLabel(root, text="YA:")
YA_label.grid(row=0, column=2)
YA_entry = ctk.CTkEntry(root)
YA_entry.grid(row=0, column=3)

XB_label = ctk.CTkLabel(root, text="XB:")
XB_label.grid(row=1, column=0)
XB_entry = ctk.CTkEntry(root)
XB_entry.grid(row=1, column=1)

YB_label = ctk.CTkLabel(root, text="YB:")
YB_label.grid(row=1, column=2)
YB_entry = ctk.CTkEntry(root)
YB_entry.grid(row=1, column=3)

XC_label = ctk.CTkLabel(root, text="XC:")
XC_label.grid(row=2, column=0)
XC_entry = ctk.CTkEntry(root)
XC_entry.grid(row=2, column=1)

YC_label = ctk.CTkLabel(root, text="YC:")
YC_label.grid(row=2, column=2)
YC_entry = ctk.CTkEntry(root)
YC_entry.grid(row=2, column=3)

XD_label = ctk.CTkLabel(root, text="XD:")
XD_label.grid(row=3, column=0)
XD_entry = ctk.CTkEntry(root)
XD_entry.grid(row=3, column=1)

YD_label = ctk.CTkLabel(root, text="YD:")
YD_label.grid(row=3, column=2)
YD_entry = ctk.CTkEntry(root)
YD_entry.grid(row=3, column=3)

p1=ctk.CTkLabel(root,text='  ')
p2=ctk.CTkLabel(root,text='  ')
p1.grid(row=5,column=1)
p2.grid(row=5,column=3)

xa=0
ya=0
xb=0
yb=0
xc=0
yc=0
xd=0
yd=0
def calculate():
    #clear the canvas
    canvas.figure.clear()
    global xa
    global ya
    global xb
    global yb
    global xc
    global yc
    global xd
    global yd
    xa = float(XA_entry.get()) 
    ya = float(YA_entry.get()) 
    xb = float(XB_entry.get()) 
    yb = float(YB_entry.get()) 
    xc = float(XC_entry.get()) 
    yc = float(YC_entry.get()) 
    xd = float(XD_entry.get()) 
    yd = float(YD_entry.get())
    
    #check if the lines intersect
    if((0<=((xc-xa)*(yd-yc)-(yc-ya)*(xd-xc))/((xb-xa)*(yd-yc)-(yb-ya)*(xd-xc))<=1)or
       (0<=((xc-xa)*(xb-xa)-(yc-ya)*(xb-xa))/((xb-xa)*(yd-yc)-(yb-ya)*(xd-xc))<=1)):
        XP = calc_przec_x(xa,ya,xb,yb,xc,yc,xd,yd)
        YP = calc_przec_y(xa,ya,xb,yb,xc,yc,xd,yd)
        p1.configure(text=XP)
        p2.configure(text=YP)
        
        # #add letters next to the points: A B C D and P on the plot
        plt.annotate('A', (xa, ya), fontsize=10)
        plt.annotate('B', (xb, yb), fontsize=10)
        plt.annotate('C', (xc, yc), fontsize=10)
        plt.annotate('D', (xd, yd), fontsize=10)
        plt.annotate('P', (XP, YP), fontsize=10)
    
        
        plt.plot([xa,xb],[ya,yb],color='blue',linewidth=3,label='line1')
        plt.plot([xc,xd],[yc,yd],color='green',linewidth=3,label='line2')
        plt.plot(xa,ya, 'ro', label='A')
        plt.plot(xb,yb, 'ro', label='B')
        plt.plot(xc,yc, 'ro', label='C')
        plt.plot(xd,yd, 'ro', label='D')
        plt.plot(XP, YP, color='black', marker='o', markersize=7, label='P')
        canvas.draw()
    
    else:
        #print "brak punktu przeciecia" if the lines do not intersect
        p1.configure(text="brak")
        p2.configure(text="brak")
        
        #draw the lines without the point of intersection
        plt.annotate('A', (xa, ya), fontsize=10)
        plt.annotate('B', (xb, yb), fontsize=10)
        plt.annotate('C', (xc, yc), fontsize=10)
        plt.annotate('D', (xd, yd), fontsize=10)
        
        plt.plot([xa,xb],[ya,yb],color='blue',linewidth=3,label='line1')
        plt.plot([xc,xd],[yc,yd],color='green',linewidth=3,label='line2')
        plt.plot(xa,ya, 'ro', label='A')
        plt.plot(xb,yb, 'ro', label='B')
        plt.plot(xc,yc, 'ro', label='C')
        plt.plot(xd,yd, 'ro', label='D')
        canvas.draw()

calc_button = ctk.CTkButton(root,text='Oblicz',command= calculate,width=300)
calc_button.grid(row=4, column=1,columnspan=3)

index1 = 0 
index2=0

def change_color1():

    global index1
    colors = ['red', 'green', 'blue', 'yellow', 'black', 'purple']
    color = colors[index1]
    color1=colors[index1+1]
    # get the line objects from the plot
    line1 = plt.gca().lines[0]
    #get the point object from the plo
    a=plt.gca().lines[2]
    b=plt.gca().lines[3]
    # get the current width and style of line1
    w = line1.get_linewidth()
    d = line1.get_linestyle()

    line1.set_color(color)
    a.set_color(color1)
    b.set_color(color1)
    canvas.draw()
    # restore the original width and style of line1
    line1.set_linewidth(w)
    line1.set_linestyle(d)
    
    index1 = (index1 + 1) % 4
   
    
def change_color2():
    global index2
    colors = ['red', 'green', 'blue', 'yellow','black','purple']
    color = colors[index2]
    color1=colors[index2+1]
    # get the line objects from the plot
    line2 = plt.gca().lines[1]
    a=plt.gca().lines[4]
    b=plt.gca().lines[5]

    # get the current width and style of line1
    w = line2.get_linewidth()
    d = line2.get_linestyle()
    line2.set_color(color)
    a.set_color(color1)
    b.set_color(color1)
    # update the plot
    canvas.draw()
    # restore the original width and style of line1
    line2.set_linewidth(w)
    line2.set_linestyle(d)
    index2 = (index2 + 1) % 4




zmiana_kol_button1=ctk.CTkButton(root,text='Zmiana koloru linii 1',width = 140,command=change_color1)
zmiana_kol_button1.grid(row=16,column=5,padx=5,pady=5)

zmiana_kol_button2=ctk.CTkButton(root,text='Zmiana koloru linii 2',width = 140,command=change_color2)
zmiana_kol_button2.grid(row=17,column=5,padx=5,pady=5)

widths=['1','3', '5', '7', '9', '11']

def change_width1():
    index=grubosc1_button.get()
    szer_pattern = {'1':1,'3': 3, '5': 5, '7': 7, '9': 9, '11': 11}
    szer=szer_pattern[index]
    line1 = plt.gca().lines[0]
    a=plt.gca().lines[2]
    b=plt.gca().lines[3]
    length=len(plt.gca().get_lines())
    if(length>6):
        P=plt.gca().lines[6]
        P.set_markersize(szer+2)
    # get the current width and style of line1
    c = line1.get_color()
    d = line1.get_linestyle()
    line1.set_linewidth(szer)
    a.set_markersize(szer+2)
    b.set_markersize(szer+2)
    canvas.draw()
    # restore the original width and style of line1
    line1.set_color(c)
    line1.set_linestyle(d)
    #make points a and b match the color and width of the line
    


def change_width2():
    index=grubosc2_button.get()
    szer_pattern = {'1':1,'3': 3, '5': 5, '7': 7, '9': 9, '11': 11}
    szer=szer_pattern[index]
    line2 = plt.gca().lines[1]
    a=plt.gca().lines[4]
    b=plt.gca().lines[5]
    length=len(plt.gca().get_lines())
    if(length>6):
        P=plt.gca().lines[6]
        P.set_markersize(szer+2)
    # get the current width and style of line1
    c = line2.get_color()
    d = line2.get_linestyle()
    line2.set_linewidth(szer)
    a.set_markersize(szer+2)
    b.set_markersize(szer+2)
    canvas.draw()
    # restore the original width and style of line1
    line2.set_color(c)
    line2.set_linestyle(d)

grubosc1_button=ctk.CTkComboBox(root,width=200,height=20,values=widths,command= lambda value:  change_width1())
grubosc1_button.set('Wybierz grubość odcinka AB')
grubosc1_button.grid(row=16,column=6,padx=5,pady=5)

grubosc2_button=ctk.CTkComboBox(root,width=200,height=20,values=widths,command= lambda value: change_width2())
grubosc2_button.set('Wybierz grubość odcinka CD')
grubosc2_button.grid(row=17,column=6,padx=5,pady=5)


def change_style1():
    index=styl1_button.get()
    styl_pattern = {'solid': 'solid', 'dashed': 'dashed', 'dotted': 'dotted', 'dashdot': 'dashdot'}
    styl=styl_pattern[index]
    line1 = plt.gca().lines[0]
    # get the current width and style of line1
    c = line1.get_color()
    w = line1.get_linewidth()
    line1.set_linestyle(styl)
    canvas.draw()
    # restore the original width and style of line1
    line1.set_color(c)
    line1.set_linewidth(w)


def change_style2():
    index=styl2_button.get()
    styl_pattern = {'solid': 'solid', 'dashed': 'dashed', 'dotted': 'dotted', 'dashdot': 'dashdot'}
    styl=styl_pattern[index]
    line2 = plt.gca().lines[1]
    # get the current width and style of line1
    c = line2.get_color()
    w = line2.get_linewidth()
    line2.set_linestyle(styl)
    canvas.draw()
    # restore the original width and style of line1
    line2.set_color(c)
    line2.set_linewidth(w)


style=['solid','dashed','dotted','dashdot']

styl1_button=ctk.CTkComboBox(root,width=200,height=20,values=style,command= lambda value:  change_style1())
styl1_button.grid(row=16,column=7,padx=5,pady=5)
styl1_button.set('Wybierz styl odcinka AB')

styl2_button=ctk.CTkComboBox(root,width=200,height=20,values=style,command= lambda value: change_style2())
styl2_button.grid(row=17,column=7,padx=5,pady=5)
styl2_button.set('Wybierz styl odcinka CD')

def change_marker():
    index=A_button.get()
    marker_pattern = {'Okrąg': 'o', 'Trójkąt': '^', 'Kwadrat': 's', 'Gwiazda': '*', 'Romb': 'd', 'Plus': 'P', 'X': 'X'}
    marker=marker_pattern[index]
    a=plt.gca().lines[2]
    b=plt.gca().lines[3]
    c=plt.gca().lines[4]
    d=plt.gca().lines[5]
    # get the current width and style of line1
    a.set_marker(marker)
    b.set_marker(marker)
    c.set_marker(marker)
    d.set_marker(marker)
    canvas.draw()
    # restore the original width and style of line1

marker_pattern=['Okrąg','Trójkąt','Kwadrat','Gwiazda','Romb','Plus','X']
A_button=ctk.CTkComboBox(root,width=200,height=20,values=marker_pattern,command= lambda value:  change_marker())
A_button.grid(row=16,column=8,padx=5,pady=5,rowspan=2)
A_button.set('Wybierz styl punktów')
def load():
  filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
  if filename != "":
    f = open(filename, 'r')
    data = f.readline()
    f.close()
    
    coords = [float(x) for x in data.split()]
    XA_entry.delete(0, "end")
    XA_entry.insert(0, str(coords[0]))
    YA_entry.delete(0, "end")
    YA_entry.insert(0, str(coords[1]))
    XB_entry.delete(0, "end")
    XB_entry.insert(0, str(coords[2]))
    YB_entry.delete(0, "end")
    YB_entry.insert(0, str(coords[3]))
    XC_entry.delete(0, "end")
    XC_entry.insert(0, str(coords[4]))
    YC_entry.delete(0, "end")
    YC_entry.insert(0, str(coords[5]))
    XD_entry.delete(0, "end")
    XD_entry.insert(0, str(coords[6]))
    YD_entry.delete(0, "end")
    YD_entry.insert(0, str(coords[7]))
    calculate()



wczytaj_button = ctk.CTkButton(root,text='Wczytaj dane z pliku',width=200,command = load)
wczytaj_button.grid(row=6,column=0,padx=10,pady=10,columnspan=2)

def save():
  # get the current values of the entry widgets
  xa = XA_entry.get()
  ya = YA_entry.get()
  xb = XB_entry.get()
  yb = YB_entry.get()
  xc = XC_entry.get()
  yc = YC_entry.get()
  xd = XD_entry.get()
  yd = YD_entry.get()

  # open a file dialog and get a file object
  f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text files", "*.txt")])
  # check if the user did not cancel the dialog
  if f is not None:
    # write the values to the file separated by spaces
    f.write(f"XA:\t{xa}\tYA:\t{ya}\nXB:\t{xb}\tYB:\t{yb}\nXC:\t{xc}\tYC:\t{yc}\nXD:\t{xd}\tYD:\t{yd}\nXP:\t{p1.cget('text')}\tYP:\t{p2.cget('text')}\n")
    # close the file
    f.close()

zapis_button=ctk.CTkButton(root,text='Zapisz raport do pliku tekstowego', width=200,command=save)
zapis_button.grid(row=6, column=3,padx=10,pady=10,columnspan=2)


def exit():
    for after_id in root.tk.eval('after info').split(): # get all ids
        root.after_cancel(after_id) # cancel each task
    root.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", exit)

root.mainloop()



