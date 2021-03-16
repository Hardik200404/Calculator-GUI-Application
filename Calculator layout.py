import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry('300x400+900+100')
root.wm_iconbitmap('cal.ico')
root.title('Calculator')
l=Label(
    root,
    text='label',
    anchor=SE,
    font=('verdana',20))
l.pack(expand=True,fill='both')
br1=Frame(root,bg='#000000')
br1.pack(expand=True,fill='both')
br2=Frame(root)
br2.pack(expand=True,fill='both')
br3=Frame(root)
br3.pack(expand=True,fill='both')
br4=Frame(root)
br4.pack(expand=True,fill='both')
b1=Button(
    br1,
    text="1",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b1.pack(side=LEFT,expand=True,fill ='both')
b2=Button(
    br1,
    text="2",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b2.pack(side=LEFT,expand=True,fill ='both')
b3=Button(
    br1,
    text="3",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b3.pack(side=LEFT,expand=True,fill ='both')
b4=Button(
    br1,
    text="+",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b4.pack(side=LEFT,expand=True,fill ='both')


b5=Button(
    br2,
    text="4",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b5.pack(side=LEFT,expand=True,fill ='both')
b6=Button(
    br2,
    text="5",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b6.pack(side=LEFT,expand=True,fill ='both')
b7=Button(
    br2,
    text="6",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b7.pack(side=LEFT,expand=True,fill ='both')
b8=Button(
    br2,
    text="-",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b8.pack(side=LEFT,expand=True,fill ='both')

b9=Button(
    br3,
    text="7",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b9.pack(side=LEFT,expand=True,fill ='both')
b10=Button(
    br3,
    text="8",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b10.pack(side=LEFT,expand=True,fill ='both')
b11=Button(
    br3,
    text="9",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b11.pack(side=LEFT,expand=True,fill ='both')
b12=Button(
    br3,
    text="x",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b12.pack(side=LEFT,expand=True,fill ='both')


b13=Button(
    br4,
    text="C",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b13.pack(side=LEFT,expand=True,fill ='both')
b14=Button(
    br4,
    text="0",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b14.pack(side=LEFT,expand=True,fill ='both')
b15=Button(
    br4,
    text="=",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b15.pack(side=LEFT,expand=True,fill ='both')
b16=Button(
    br4,
    text="/",
    font=('verdana',20),
    relief=GROOVE,
    border=0)
b16.pack(side=LEFT,expand=True,fill ='both')


root.mainloop()