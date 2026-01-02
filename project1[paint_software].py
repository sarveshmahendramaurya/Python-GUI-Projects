from tkinter import *

global x_last,y_last
global brush_color
x_last,y_last=None,None
brush_color='black'
brush_size=3

#to take co-ordinates
def start(event):
    global x_last,y_last
    x_last,y_last=event.x,event.y

def draw(event):
    global x_last, y_last  # <--- THIS LINE IS THE FIX
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

def delete(event):
    canvas.delete("all")
    
root=Tk()
root.state('zoomed')
Frame1=Frame(root)
Frame2=Frame(root)
Frame3=Frame(root)

clrs=Label(Frame1,text='Colors')
lightblue=Label(Frame1,text='___',bg='lightblue',fg='lightblue')
blue=Label(Frame1,text='___',bg='blue',fg='blue')
lightgreen=Label(Frame1,text='___',bg='lightgreen',fg='lightgreen')
green=Label(Frame1,text='___',bg='green',fg='green')
yellow=Label(Frame1,text='___',bg='yellow',fg='yellow')
orange=Label(Frame1,text='___',bg='orange',fg='orange')
red=Label(Frame1,text='___',bg='red',fg='red')

eraser=Label(Frame2,text='Earaser',bg='white',fg='black')
clrll=Button(Frame2, text="Clear All", bg='white', fg='black')

canvas=Canvas(Frame3, bg='white')

#events
lightblue.bind('<Button-1>',lightblue1)
lightgreen.bind('<Button-1>',lightgreen1)
green.bind('<Button-1>',green1)
blue.bind('<Button-1>',blue1)
yellow.bind('<Button-1>',yellow1)
orange.bind('<Button-1>',orange1)
red.bind('<Button-1>',red1)
canvas.bind('<Double-Button-1>',start)
canvas.bind('<B1-Motion>',draw)
clrll.bind('<Button-1>',delete)
#pack manages
Frame1.pack(side=LEFT)
Frame2.pack(side=LEFT)
Frame3.pack(side=LEFT,fill=BOTH, expand=True)

clrs.pack(side=TOP,padx=20,pady=15)

ipadx=25
ipadx=25
padx=20
pady=15
lightblue.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
blue.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
lightgreen.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
green.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
yellow.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
orange.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
red.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)

eraser.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)
clrll.pack(side=TOP,ipadx=25,ipady=25,padx=20,pady=15)

canvas.pack(fill=BOTH, expand=True)












