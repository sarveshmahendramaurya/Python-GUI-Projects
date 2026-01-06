import tkinter as tk
from tkinter import ttk

root=tk.Tk()
#--Frame1 Elements--#
frame1=tk.Frame(root)
frame1.pack(side=tk.LEFT)

Avatar1=tk.Canvas(frame1)
Avatar1.pack(side=tk.TOP)
p1_name=tk.StringVar(value="Enter your name")
player1=tk.Entry(frame1,textvariable=p1_name)
player1.pack(side=tk.TOP)
Button1=tk.Button(frame1,text='Confirm')
Button1.pack()
#Avatar1.create_image(image=image1)

#--Frame2 Elements --#
option=["O","X"]
frame2=tk.Frame(root)
frame2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
frame2a=tk.Frame(frame2)
frame2a.pack(side=tk.TOP)

#ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady
Ipadx=20
Ipady=20
Padx=5
Pady=5
style=ttk.Style()
style.configure("custom.Tcombobox",
                font=('Arial Black', 40, 'bold'))
frame2a1=tk.Frame(frame2a)
frame2a1.pack(side=tk.TOP)
a=ttk.Combobox(frame2a1,width=1,values=option,state="readonly")
a.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady,)
b=ttk.Combobox(frame2a1,width=1,values=option,state="readonly")
b.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
c=ttk.Combobox(frame2a1,width=1,values=option,state="readonly")
c.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)

frame2a2=tk.Frame(frame2a)
frame2a2.pack(side=tk.TOP)
d=ttk.Combobox(frame2a2,width=1,values=option,state="readonly")
d.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
e=ttk.Combobox(frame2a2,width=1,values=option,state="readonly")
e.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
f=ttk.Combobox(frame2a2,width=1,values=option,state="readonly")
f.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)

frame2a3=tk.Frame(frame2a)
frame2a3.pack(side=tk.TOP)
g=ttk.Combobox(frame2a3,width=1,values=option,state="readonly")
g.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
h=ttk.Combobox(frame2a3,width=1,values=option,state="readonly")
h.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
i=ttk.Combobox(frame2a3,width=1,values=option,state="readonly")
i.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)

frame3=tk.Frame(root)
frame3.pack(side=tk.LEFT)
Avatar2=tk.Canvas(frame3)
Avatar2.pack(side=tk.TOP)
p2_name=tk.StringVar(value="Enter your name")
player2=tk.Entry(frame3,textvariable=p2_name)
player2.pack(side=tk.TOP)
Button2=tk.Button(frame3,text='Confirm')
Button2.pack()




