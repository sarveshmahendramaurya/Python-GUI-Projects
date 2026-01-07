import tkinter as tk
from tkinter import ttk

def win():
    A=a.get()
    B=b.get()
    C=c.get()
    D=d.get()
    E=e.get()
    F=f.get()
    G=g.get()
    H=h.get()
    I=i.get()
    if A==B and B==C and C==A and A!="":
        a1= A
    elif D==E and E==F and F==D and D!="":
        a1= D
    elif G==H and H==I and I==G and H!="":
        a1= H
    elif A==D and D==G and G==A and A!="":
        a1=D
    elif B==E and E==H and H==B and H!="":
        a1= H
    elif C==F and F==I and I==C and C!="":
        a1=F
    elif A==E and E==I and A==I and A!="":
        a1= A
    elif C==E and E==G and G==C and C!="":
        a1= E
    if a1!="":
        if a1=="X":
            a1=p1_name.get()
        else:
            a1=p2_name.get()
        pass
    result=f"{a1} Won ! "
    Won=tk.Label(frame2,text=result,font=('Arial Black', 15))
    Won.pack(side=tk.TOP)

def changing_p1():
    p1_name=player1name.get()
    print(p1_name)
def changing_p2():
    p2_name=player2name.get()
    print(p2_name)
    
root=tk.Tk()

root.title("Tic Tac Toe")
#--Frame1 Elements--#
frame1=tk.Frame(root)
frame1.pack(side=tk.LEFT)

Avatar1=tk.Canvas(frame1)
Avatar1.pack(side=tk.TOP)
PlayerL=tk.Label(frame1,text="Enter your name")
PlayerL.pack(side=tk.TOP)
p1_name=tk.StringVar(value="Player X")
player1=tk.Entry(frame1,textvariable=p1_name)
player1name=p1_name
player1.pack(side=tk.TOP)
Button1=tk.Button(frame1,text='Confirm',command=changing_p1)
Button1.pack()

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
frame2a1=tk.Frame(frame2a)
frame2a1.pack(side=tk.TOP)
a=ttk.Combobox(frame2a1,width=1,font=('Arial',20),values=option,state="readonly")
a.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady,)
b=ttk.Combobox(frame2a1,width=1,font=('Arial',20),values=option,state="readonly")
b.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
c=ttk.Combobox(frame2a1,width=1,font=('Arial',20),values=option,state="readonly")
c.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)

frame2a2=tk.Frame(frame2a)
frame2a2.pack(side=tk.TOP)
d=ttk.Combobox(frame2a2,width=1,font=('Arial',20),values=option,state="readonly")
d.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
e=ttk.Combobox(frame2a2,width=1,font=('Arial',20),values=option,state="readonly")
e.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
f=ttk.Combobox(frame2a2,width=1,font=('Arial',20),values=option,state="readonly")
f.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)

frame2a3=tk.Frame(frame2a)
frame2a3.pack(side=tk.TOP)
g=ttk.Combobox(frame2a3,width=1,font=('Arial',20),values=option,state="readonly")
g.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
h=ttk.Combobox(frame2a3,width=1,font=('Arial',20),values=option,state="readonly")
h.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)
i=ttk.Combobox(frame2a3,width=1,font=('Arial',20),values=option,state="readonly")
i.pack(side=tk.LEFT,ipadx=Ipadx,ipady=Ipady,padx=Padx,pady=Pady)

okButton=tk.Button(frame2a,text="OK",command=win).pack(side=tk.TOP)
    
frame3=tk.Frame(root)
frame3.pack(side=tk.LEFT)
Avatar2=tk.Canvas(frame3)
Avatar2.pack(side=tk.TOP)
PlayerL=tk.Label(frame3,text="Enter your name")
PlayerL.pack(side=tk.TOP)
p2_name=tk.StringVar(value="Player O")
player2=tk.Entry(frame3,textvariable=p2_name)
player2name=p2_name
player2.pack(side=tk.TOP)
Button2=tk.Button(frame3,text='Confirm',command=changing_p2)
Button2.pack()
    
root.mainloop()



