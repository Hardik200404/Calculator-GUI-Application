import tkinter
from tkinter import *
from tkinter import messagebox

v=""
a=0
o=""
def one():
    global v
    v+="1"
    data.set(v)
def two():
    global v
    v+="2"
    data.set(v)
def three():
    global v
    v+="3"
    data.set(v)
def four():
    global v
    v+="4"
    data.set(v)
def five():
    global v
    v+="5"
    data.set(v)
def six():
    global v
    v+="6"
    data.set(v)
def seven():
    global v
    v+="7"
    data.set(v)
def eight():
    global v
    v+="8"
    data.set(v)
def nine():
    global v
    v+="9"
    data.set(v)
def zero():
    global v
    v+="0"
    data.set(v)

def plus():
   global a
   global v
   global o
   a=int(v)
   o="+"
   v+="+"
   data.set(v) 
def minus():
   global a
   global v
   global o
   a=int(v)
   o="-"
   v+="-"
   data.set(v)
def multiply():
   global a
   global v
   global o
   a=int(v)
   o="*"
   v+="*"
   data.set(v)
def divide():
   global a
   global v
   global o
   a=int(v)
   o="/"
   v+="/"
   data.set(v)
def c():
    global a
    global v
    global o
    v=""
    a=0
    o=""
    data.set(v)
def result():
    global a
    global v
    global o
    t=v
    if o=="+":
        b=int((t.split("+")[1]))
        s=a+b
        data.set(s)
        v=str(s)
    elif o=="-":
        b=int((t.split("-")[1]))
        s=a-b
        data.set(s)
        v=str(s)
    elif o=="*":
        b=int((t.split("*")[1]))
        s=a*b
        data.set(s)
        v=str(s)
    elif o=="/":
        b=int((t.split("/")[1]))
        if b==0:
            messagebox.showerror("Error","Division by '0' not allowed")
            a=""
            v=""
            data.set(v)
        else:
            s=int(a/b)
            data.set(s)
            v=str(s)


root=tkinter.Tk()
root.geometry('300x400+900+100')
root.wm_iconbitmap('cal.ico')
root.title('Calculator')
data=StringVar()
l=Label(
    root,
    text='label',
    anchor=SE,
    font=('verdana',20),
    textvariable=data)
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
    border=0,
    command=one)
b1.pack(side=LEFT,expand=True,fill ='both')
b2=Button(
    br1,
    text="2",
    font=('verdana',20),
    relief=GROOVE,
    border=0,
    command=two)
b2.pack(side=LEFT,expand=True,fill ='both')
b3=Button(
    br1,
    text="3",
    font=('verdana',20),
    relief=GROOVE,
    border=0,
    command=three)
b3.pack(side=LEFT,expand=True,fill ='both')
b4=Button(
    br1,
    text="+",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=plus)
b4.pack(side=LEFT,expand=True,fill ='both')


b5=Button(
    br2,
    text="4",
    font=('verdana',20),
    relief=GROOVE,
    border=0,
    command=four)
b5.pack(side=LEFT,expand=True,fill ='both')
b6=Button(
    br2,
    text="5",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=five)
b6.pack(side=LEFT,expand=True,fill ='both')
b7=Button(
    br2,
    text="6",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=six)
b7.pack(side=LEFT,expand=True,fill ='both')
b8=Button(
    br2,
    text="-",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=minus)
b8.pack(side=LEFT,expand=True,fill ='both')

b9=Button(
    br3,
    text="7",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=seven)
b9.pack(side=LEFT,expand=True,fill ='both')
b10=Button(
    br3,
    text="8",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=eight)
b10.pack(side=LEFT,expand=True,fill ='both')
b11=Button(
    br3,
    text="9",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=nine)
b11.pack(side=LEFT,expand=True,fill ='both')
b12=Button(
    br3,
    text="*",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=multiply)
b12.pack(side=LEFT,expand=True,fill ='both')


b13=Button(
    br4,
    text="C",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=c)
b13.pack(side=LEFT,expand=True,fill ='both')
b14=Button(
    br4,
    text="0",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=zero)
b14.pack(side=LEFT,expand=True,fill ='both')
b15=Button(
    br4,
    text="=",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=result)
b15.pack(side=LEFT,expand=True,fill ='both')
b16=Button(
    br4,
    text="/",
    font=('verdana',20),
    relief=GROOVE,
    border=0,command=divide)
b16.pack(side=LEFT,expand=True,fill ='both')


root.mainloop()