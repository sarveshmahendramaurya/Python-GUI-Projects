from tkinter import *

global x_last,y_last
global brush_color
global brush_size
x_last,y_last=None,None
brush_color='black'
brush_size=3

#to take co-ordinates
def start(event):
    global x_last,y_last
    x_last,y_last=event.x,event.y

def focusout(event):
    global x_last,y_last
    x_last,y_last=None,None
    
def draw(event):
    global x_last, y_last # <--- THIS LINE IS THE FIX
    if x_last is not None and y_last is not None:
        canvas.create_line(
            x_last, y_last, event.x, event.y,
            fill=brush_color,
            width=brush_size,
            smooth=True,
            capstyle=ROUND
        )
    x_last, y_last = event.x, event.y

def lightblue1(event):
    global brush_color
    brush_color='lightblue'

def blue1(event):
    global brush_color
    brush_color='blue'

def lightgreen1(event):
    global brush_color
    brush_color='lightgreen'

def green1(event):
    global brush_color
    brush_color='green'

def yellow1(event):
    global brush_color
    brush_color='yellow'

def red1(event):
    global brush_color
    brush_color='red'

def orange1(event):
    global brush_color
    brush_color='orange'

def hotpink1(event):
    global brush_color
    brush_color='hotpink'

def earaser(event):
    global brush_color
    brush_color='white'
    
def delete(event):
    canvas.delete("all")
    
root=Tk()
root.state('zoomed')


Frame1=Frame(root)
clrs=Label(Frame1,text='Colors')
lightblue=Label(Frame1,text='__',bg='lightblue',fg='lightblue')
blue=Label(Frame1,text='__',bg='blue',fg='blue')
lightgreen=Label(Frame1,text='__',bg='lightgreen',fg='lightgreen')
green=Label(Frame1,text='__',bg='green',fg='green')
yellow=Label(Frame1,text='__',bg='yellow',fg='yellow')
orange=Label(Frame1,text='__',bg='orange',fg='orange')
red=Label(Frame1,text='__',bg='red',fg='red')
hotpink=Label(Frame1,text='__',bg='hotpink',fg='hotpink')


Frame2=Frame(root)
spin_val=IntVar(value=5)
spin=Spinbox(Frame2, from_=0, to=500, textvariable=spin_val)
def Brush_size():
    global brush_size
    brush_size=spin_val.get()
Set_size=Button(Frame2,text='Set Size', command=Brush_size)
text=StringVar()
Entry=Entry(Frame2,textvariable=text)
def hexcode():
    global brush_color
    brush_color=text.get()
clr_set=Button(Frame2,text='Set color', command=hexcode)
eraser=Label(Frame2,text='▰ Eraser',bg='white',fg='black')
clrll=Button(Frame2, text="Clear All", bg='white', fg='black')


Frame3=Frame(root)
canvas=Canvas(Frame3, bg='white')

#events
lightblue.bind('<Button-1>',lightblue1)
lightgreen.bind('<Button-1>',lightgreen1)
green.bind('<Button-1>',green1)
blue.bind('<Button-1>',blue1)
yellow.bind('<Button-1>',yellow1)
orange.bind('<Button-1>',orange1)
red.bind('<Button-1>',red1)
hotpink.bind('<Button-1>',hotpink1)
canvas.bind('<Double-Button-1>',start)
canvas.bind('<B1-Motion>',draw)
canvas.bind('<ButtonRelease-1>',focusout)
clrll.bind('<Button-1>',delete)
eraser.bind('<Button-1>',earaser)
#pack manages
Frame1.pack(side=LEFT)
ipadX=20
ipadY=20
padX=5
padY=5
clrs.pack(side=TOP,padx=20,pady=15)
lightblue.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
blue.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
lightgreen.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
green.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
yellow.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
orange.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
red.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)
hotpink.pack(side=TOP,ipadx=25,ipady=25,padx=padX,pady=padY)


Frame2.pack(side=LEFT)
Frame3.pack(side=LEFT,fill=BOTH, expand=True)

Entry.pack(side=TOP,pady=10)
clr_set.pack(side=TOP,pady=10)
spin.pack(side=TOP,pady=10)
Set_size.pack(side=TOP,pady=10)
eraser.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)

clrll.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)

canvas.pack(fill=BOTH, expand=True)
root.mainloop()











