import tkinter as tk
import os

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
    global content
    
    if(v.get()=="r"):
        with open(FileName.get(),'r') as f:
            content=f.read()
            Ntry2.insert('1.0',content)
    else:
        with open(FileName.get(),'w') as f:
            f.write(Ntry2.get("1.0","end"))
#---parent window---#
root=tk.Tk()
root.state('zoomed')

Frame1=tk.Frame(root)
Frame1.pack(side=tk.LEFT)

#---File settings---#
ex=0
ey=5
ix=5
iy=5
"""padx=ex,pady=ey.ipadx=ix,ipady=iy"""
tk.Label(
    Frame1,text="◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈"
    ).pack(side=tk.TOP)
tk.Label(
    Frame1,text="File Name"
    ).pack(side=tk.TOP)

FileName=tk.StringVar(value="Project2[Notebook_demo_text].txt")
tk.Entry(
    Frame1,textvariable=FileName
    ).pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)

v=tk.StringVar()

rb1=tk.Radiobutton(Frame1, text='Read' ,variable=v, value="r")
rb1.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)

rb2=tk.Radiobutton(Frame1, text='Write' ,variable=v, value="w")
rb2.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)

ConfirnButton=tk.Button(Frame1,text="Confirm",command=File_setting)
ConfirnButton.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)
#---Font settings---#
tk.Label(
    Frame1,text="________________________________"
    ).pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)

style_label=tk.Label(Frame1,text="Font Style")
style_label.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)
font_style=tk.StringVar(value='Segoe UI')
fntstyl=tk.Entry(Frame1,textvariable=font_style)
fntstyl.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)

size_label=tk.Label(Frame1,text="Font Size")
size_label.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)
font_size=tk.IntVar(value=15)
fntsz=tk.Spinbox(Frame1,from_=1,to=150,textvariable=font_size)
fntsz.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)

tryButton=tk.Button(Frame1,text="Set Font Setting", font=('Segoe UI',10),command=font_setting)
tryButton.pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)
tk.Label(
    Frame1,text="◈◇◈◇◈◇◈◇◈◇◈◇◈◇◈"
    ).pack(side=tk.TOP,padx=ex,pady=ey,ipadx=ix,ipady=iy)
#---canvas---#
Frame2=tk.Frame(root)
Frame2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
Ntry2=tk.Text(Frame2,font=(style ,size))
Ntry2.insert("1.0", "")
Ntry2.pack(fill=tk.BOTH,expand=True)

root.mainloop()




