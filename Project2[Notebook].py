from tkinter import *
from os import *

global textvar
def print_this():
    global textvar
    textvar=Ntry2.get("1.0", "end")
    print(textvar)
    
root=Tk()
root.state('zoomed')

Frame1=Frame(root)
Frame1.pack(side=LEFT)

#settings
font_style=StringVar()
fntstyl=Entry(Frame1,textvariable=font_style)
fntstyl.pack(side=TOP)
font_size=IntVar(5)
fntsz=Entry(Frame1,textvariable=font_style)
fntsz.pack(side=TOP)

Label1=Label(Frame1,text='Set font size')
Label1.pack(side=TOP)

Frame2=Frame(root)
Frame2.pack(side=LEFT,fill=BOTH,expand=True)

Ntry2=Text(Frame2)
Ntry2.insert("1.0", "Hello students")
Ntry2.pack(fill=BOTH,expand=True)
    
tryButton=Button(Frame1,text="  ",command=print_this)
tryButton.pack(side=TOP)




