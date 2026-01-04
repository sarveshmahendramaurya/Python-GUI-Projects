from tkinter import *
from os import *


style='Segoe UI'
size=15

def print_this():
    global textvar
    textvar=Ntry2.get("1.0", "end")
    print(textvar)

def font_setting():
    global style
    global size
    style=font_style.get()
    size=font_size.get()
    Ntry2.config(font=(style, size))

root=Tk()
root.state('zoomed')

Frame1=Frame(root)
Frame1.pack(side=LEFT)

#settings
style_label=Label(Frame1,text="Font Style")
style_label.pack(side=TOP)
font_style=StringVar(value='Segoe UI')
fntstyl=Entry(Frame1,textvariable=font_style)
fntstyl.pack(side=TOP)

size_label=Label(Frame1,text="Font Size")
size_label.pack(side=TOP)
font_size=IntVar(value=15)
fntsz=Spinbox(Frame1,from_=1,to=150,textvariable=font_size)
fntsz.pack(side=TOP)

Frame2=Frame(root)
Frame2.pack(side=LEFT,fill=BOTH,expand=True)

Ntry2=Text(Frame2,font=(style ,size))
Ntry2.insert("1.0", "Hello students")
Ntry2.pack(fill=BOTH,expand=True)
    
tryButton=Button(Frame1,text="Set Font Setting", font=('Segoe UI',10),command=font_setting)
tryButton.pack(side=TOP)




