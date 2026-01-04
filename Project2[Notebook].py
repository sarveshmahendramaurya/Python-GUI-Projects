from tkinter import *
from os import *

global v
style='Segoe UI'
size=15
global f
#---functions---#
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

def File_setting():
    with open(FileName.get(),'r+') as f:
        if(v.get()=="r"):
            content=f.read()
            Ntry2.insert('1.0',content)
        else:
            f.write(content)
#---parent window---#
root=Tk()
root.state('zoomed')

Frame1=Frame(root)
Frame1.pack(side=LEFT)

#---File settings---#
Label(Frame1,text="File Name").pack(side=TOP)

FileName=StringVar()
Entry(Frame1,textvariable=FileName).pack(side=TOP)

v=StringVar()
rb1lbl=Label(Frame1,text='Read')
rb1lbl.pack()
rb1=Radiobutton(Frame1, text='Read' ,textvariable=v, value="r")
rb1.pack(side=TOP)

rb2lbl=Label(Frame1,text='write')
rb2lbl.pack()
rb2=Radiobutton(Frame1, text='Write' ,textvariable=v, value="w")
rb2.pack(side=TOP)

ConfirnButton=Button(Frame1,text="Confirm",command=File_setting)
ConfirnButton.pack(side=TOP)
#---Font settings---#
Label(Frame1,text="____________________________").pack(side=TOP)

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

tryButton=Button(Frame1,text="Set Font Setting", font=('Segoe UI',10),command=font_setting)
tryButton.pack(side=TOP)

#---canvas---#
Frame2=Frame(root)
Frame2.pack(side=LEFT,fill=BOTH,expand=True)
Ntry2=Text(Frame2,font=(style ,size))
Ntry2.insert("1.0", "Hello students")
Ntry2.pack(fill=BOTH,expand=True)






